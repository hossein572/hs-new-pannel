









import asyncio
import secrets
import socket
import time
import traceback
from datetime import datetime, timezone
from protocol.trojan.trojan import parse_trojan_header, find_uuid_by_trojan_hash

from fastapi import Request, HTTPException
from starlette.requests import ClientDisconnect
from fastapi.responses import StreamingResponse

from main import (
    LINKS,
    LINKS_LOCK,
    stats,
    hourly_traffic,
    connections,
    error_logs,
    logger,
    is_link_allowed,
    save_state,
)
from protocol.vless.vless import parse_vless_header, check_and_use


XHTTP_BUF = 1024 * 1024
DOWNLINK_QUEUE_MAX = 512
SESSION_IDLE_TIMEOUT = 30
SESSION_IDLE_TIMEOUT_ACTIVE = 90
REAPER_INTERVAL = 10
TCP_CONNECT_TIMEOUT = 10.0


SOCK_BUF_SIZE = 4 * 1024 * 1024





FLOW_MIN_HW = 256 * 1024
FLOW_MAX_HW = 32 * 1024 * 1024
FLOW_START_HW = 2 * 1024 * 1024

FLOW_FAST_DRAIN_MS = 12.0




FLOW_SLOW_DRAIN_MS = 40.0



QUOTA_MIN_BATCH = 32 * 1024
QUOTA_MAX_BATCH = 4 * 1024 * 1024
QUOTA_START_BATCH = 256 * 1024
QUOTA_CHECK_INTERVAL = 0.25

PACKET_UP_HIGH_WATER = 2 * 1024 * 1024

xhttp_sessions: dict = {}
XHTTP_LOCK = asyncio.Lock()

FINGERPRINTS = {
    "chrome": {
        "content-type": "application/grpc",
        "cache-control": "no-cache, no-store",
        "x-accel-buffering": "no",
        "server": "cloudflare",
    },
    "plain": {
        "content-type": "application/octet-stream",
        "cache-control": "no-store",
        "x-accel-buffering": "no",
    },
}
DEFAULT_FINGERPRINT = "chrome"


def _resp_headers(fp: str) -> dict:
    return dict(FINGERPRINTS.get(fp, FINGERPRINTS[DEFAULT_FINGERPRINT]))


def _tune_socket(writer: asyncio.StreamWriter):

    sock = writer.transport.get_extra_info("socket")
    if not sock:
        return
    try:
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCK_BUF_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCK_BUF_SIZE)
        if hasattr(socket, "TCP_QUICKACK"):
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 1)
    except OSError as e:
        logger.warning(f"XHTTP _tune_socket failed: {e}")


class _QuotaGate:

    __slots__ = ("uuid", "pending", "last_check", "ok", "batch_bytes", "rate_ewma")

    def __init__(self, uuid: str):
        self.uuid = uuid
        self.pending = 0
        self.last_check = time.monotonic()
        self.ok = True
        self.batch_bytes = QUOTA_START_BATCH
        self.rate_ewma = 0.0

    async def add(self, nbytes: int) -> bool:
        if not self.ok:
            return False
        self.pending += nbytes
        now = time.monotonic()
        elapsed = now - self.last_check
        if self.pending >= self.batch_bytes or elapsed >= QUOTA_CHECK_INTERVAL:
            flush, self.pending = self.pending, 0
            if elapsed > 0:
                inst_rate = flush / elapsed
                self.rate_ewma = inst_rate if self.rate_ewma == 0 else (0.7 * self.rate_ewma + 0.3 * inst_rate)
                target = int(self.rate_ewma * QUOTA_CHECK_INTERVAL)
                self.batch_bytes = max(QUOTA_MIN_BATCH, min(QUOTA_MAX_BATCH, target or QUOTA_MIN_BATCH))
            self.last_check = now
            try:
                self.ok = await check_and_use(self.uuid, flush)
            except Exception as exc:
                logger.error(f"XHTTP _QuotaGate.add check_and_use failed uuid={self.uuid[:8]}: {type(exc).__name__}: {exc}")
                self.ok = False
            return self.ok
        return True

    async def flush(self) -> bool:
        if self.pending:
            flush, self.pending = self.pending, 0
            try:
                self.ok = self.ok and await check_and_use(self.uuid, flush)
            except Exception as exc:
                logger.error(f"XHTTP _QuotaGate.flush check_and_use failed uuid={self.uuid[:8]}: {type(exc).__name__}: {exc}")
                self.ok = False
        return self.ok


class _AdaptiveFlow:

    __slots__ = ("high_water", "last_drain_ms")

    def __init__(self):
        self.high_water = FLOW_START_HW
        self.last_drain_ms = 0.0

    def should_drain(self, buf_size: int) -> bool:
        return buf_size > self.high_water

    async def drain(self, writer: asyncio.StreamWriter):
        t0 = time.monotonic()
        await writer.drain()
        elapsed_ms = (time.monotonic() - t0) * 1000
        self.last_drain_ms = elapsed_ms
        if elapsed_ms < FLOW_FAST_DRAIN_MS:
            self.high_water = min(FLOW_MAX_HW, int(self.high_water * 2.0) + 65536)
        elif elapsed_ms > FLOW_SLOW_DRAIN_MS:
            self.high_water = max(FLOW_MIN_HW, self.high_water // 2)


def _req_client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "نامشخص"


async def _open_tcp_from_header(first_chunk: bytes, is_trojan: bool = False):
    if is_trojan:
        pw_hash, command, address, port, payload = await parse_trojan_header(first_chunk)
        resolved_uuid = await find_uuid_by_trojan_hash(pw_hash)
        if resolved_uuid is None:
            raise ValueError("trojan auth failed")
    else:
        command, address, port, payload = await parse_vless_header(first_chunk)

    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(address, port), timeout=TCP_CONNECT_TIMEOUT
        )
    except asyncio.TimeoutError:
        logger.error(f"XHTTP TCP connect TIMEOUT -> {address}:{port} (>{TCP_CONNECT_TIMEOUT}s)")
        raise
    except OSError as exc:
        logger.error(f"XHTTP TCP connect FAILED -> {address}:{port}: {type(exc).__name__}: {exc}")
        raise

    _tune_socket(writer)
    if payload:
        writer.write(payload)
        await writer.drain()
    return reader, writer, address, port


async def _check_link(uuid: str):
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not is_link_allowed(link):
        raise HTTPException(status_code=403, detail="not authorized")


async def _get_or_create_session(uuid: str, mode: str, session_id: str, ip: str = "نامشخص") -> dict:

    async with XHTTP_LOCK:
        sess = xhttp_sessions.get(session_id)
        if sess is not None:
            sess["last_seen"] = time.time()
            return sess
        conn_id = secrets.token_urlsafe(6)
        connections[conn_id] = {
            "uuid": uuid,
            "ip": ip,
            "connected_at": datetime.now(timezone.utc).isoformat(),
            "bytes": 0,
            "transport": f"xhttp-{mode}",
        }
        sess = {
            "uuid": uuid, "mode": mode, "writer": None,
            "downlink_task": None, "uplink_task": None,
            "down_q": asyncio.Queue(maxsize=DOWNLINK_QUEUE_MAX),
            "last_seen": time.time(),
            "conn_id": conn_id, "tcp_open": False, "closed": False,
            "seq_buf": {}, "next_seq": 0,
            "gate": None,
            "flow": None,
        }
        xhttp_sessions[session_id] = sess
        logger.info(f"new XHTTP[{mode}] session [{session_id[:8]}] uuid={uuid[:8]} ip={ip}")
        return sess


async def _teardown(session_id: str, reason: str = ""):
    async with XHTTP_LOCK:
        sess = xhttp_sessions.pop(session_id, None)
    if not sess:
        return
    sess["closed"] = True
    for t in ("uplink_task", "downlink_task"):
        task = sess.get(t)
        if task:
            task.cancel()
            try:
                await task
            except (asyncio.CancelledError, Exception):
                pass
    writer = sess.get("writer")
    if writer:
        try:
            writer.close()
            await writer.wait_closed()
        except Exception:
            pass
    connections.pop(sess.get("conn_id"), None)
    dq = sess.get("down_q")
    if dq:
        try:
            dq.put_nowait(None)
        except Exception:
            pass
    suffix = f" reason={reason}" if reason else ""
    logger.info(f"closed XHTTP[{sess.get('mode')}] [{session_id[:8]}] total={len(xhttp_sessions)}{suffix}")


async def _reaper():
    while True:
        await asyncio.sleep(REAPER_INTERVAL)
        now = time.time()
        async with XHTTP_LOCK:
            stale = []
            for sid, s in xhttp_sessions.items():
                idle = now - s["last_seen"]
                if s.get("tcp_open"):
                    if idle > SESSION_IDLE_TIMEOUT_ACTIVE:
                        stale.append(sid)
                else:
                    if idle > SESSION_IDLE_TIMEOUT:
                        stale.append(sid)
        for sid in stale:
            await _teardown(sid, reason="idle-timeout")


_reaper_started = False


def ensure_reaper():
    global _reaper_started
    if not _reaper_started:
        asyncio.create_task(_reaper())
        _reaper_started = True


async def _pump_tcp_to_queue(session_id: str, uuid: str, reader: asyncio.StreamReader, down_q: asyncio.Queue, vless_prefix: bool = True, conn_id: str = ""):
    gate = _QuotaGate(uuid)
    close_reason = "remote-eof"
    first = True

    cached_conn = connections.get(conn_id) if conn_id else None
    try:
        while True:
            try:
                data = await reader.read(XHTTP_BUF)
            except (ConnectionResetError, OSError) as exc:
                close_reason = f"tcp-read-error: {type(exc).__name__}: {exc}"
                logger.warning(f"XHTTP[{session_id[:8]}] downlink read error: {close_reason}")
                break
            if not data:
                break
            if not await gate.add(len(data)):
                close_reason = "quota-exceeded"
                logger.warning(f"XHTTP[{session_id[:8]}] downlink quota exceeded, closing")
                break

            if cached_conn is not None:
                cached_conn["bytes"] += len(data)
            if vless_prefix and first:
                await down_q.put(b"\x00\x00" + data)
                first = False
            else:
                await down_q.put(data)
    except asyncio.CancelledError:
        close_reason = "cancelled"
    except Exception as exc:
        tb = traceback.format_exc()
        close_reason = f"unexpected: {type(exc).__name__}: {exc}"
        logger.error(f"XHTTP[{session_id[:8]}] downlink pump crashed: {type(exc).__name__}: {exc}\n{tb}")
    finally:
        await gate.flush()


        await _teardown(session_id, reason=close_reason)


async def _open_tcp_for_session(session_id: str, uuid: str, sess: dict, first_chunk: bytes):
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    proto = (link.get("protocol", "") or "") if link else ""
    is_trojan = proto.startswith("trojan")


    vless_prefix = not is_trojan
    try:
        reader, writer, address, port = await _open_tcp_from_header(first_chunk, is_trojan=is_trojan)
    except Exception as exc:
        tb = traceback.format_exc()
        logger.error(f"XHTTP[{sess['mode']}] [{session_id[:8]}] connect/parse FAILED: {type(exc).__name__}: {exc}\n{tb}")
        error_logs.append({"error": f"xhttp connect failed: {type(exc).__name__}: {exc}", "time": datetime.now().isoformat()})
        raise
    logger.info(f"connect XHTTP[{sess['mode']}] [{session_id[:8]}] -> {address}:{port}")
    sess["writer"] = writer
    sess["tcp_open"] = True
    sess["downlink_task"] = asyncio.create_task(
        _pump_tcp_to_queue(session_id, uuid, reader, sess["down_q"], vless_prefix=vless_prefix, conn_id=sess["conn_id"])
    )
    asyncio.create_task(save_state())


def _downstream_gen(sess: dict):
    async def gen():
        try:
            while True:
                chunk = await sess["down_q"].get()
                if chunk is None:
                    break
                sess["last_seen"] = time.time()
                yield chunk
        finally:
            pass
    return gen()
