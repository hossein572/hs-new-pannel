# dev_smtp.py — SMTP تستی برای تست محلی پنل
# ایمیل واقعی نمی‌فرستد؛ کد تأیید را در همین ترمینال چاپ می‌کند.
#
# اجرا (یک ترمینال جدا):
#   python dev_smtp.py
#
# بعد پنل را با این SMTP اجرا کن:
#   PowerShell:
#     $env:SMTP_HOST="127.0.0.1"; $env:SMTP_PORT="1025"
#     $env:SMTP_USER="test"; $env:SMTP_PASS="test"; $env:SMTP_FROM="test@local"
#     $env:PORT=8000; $env:DATA_DIR=".\data"; $env:RELOAD="1"; python main.py
#   bash:
#     SMTP_HOST=127.0.0.1 SMTP_PORT=1025 SMTP_USER=test SMTP_PASS=test SMTP_FROM=test@local \
#     PORT=8000 DATA_DIR=./data RELOAD=1 python3 main.py

import asyncio
import email
import json
import re
import sys
from email import policy
from pathlib import Path

sys.stdout.reconfigure(errors="replace")

OUT = Path(__file__).parent / "smtp_received.jsonl"
HOST, PORT = "127.0.0.1", 1025


def show(data: str):
    try:
        msg = email.message_from_string(data, policy=policy.default)
        print("\n==================== EMAIL ====================", flush=True)
        print(f"To: {msg['to']} | Subject: {msg['subject']}", flush=True)
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_content()
                print(body, flush=True)
                m = re.search(r"(\d{6})", body)
                if m:
                    print(f">>> CODE: {m.group(1)} <<<", flush=True)
        print("=================================================\n", flush=True)
    except Exception as e:  # noqa: BLE001
        print(f"(parse error: {e})", flush=True)


async def handle(reader, writer):
    def send(m):
        writer.write((m + "\r\n").encode())
        return writer.drain()

    async def line():
        return (await reader.readline()).decode("utf-8", "replace").strip()

    await send("220 dev-smtp ready")
    rc, dl, dm, au = [], [], False, 0
    while True:
        ln = await line()
        if not ln and reader.at_eof():
            break
        if dm:
            if ln == ".":
                dm = False
                full = "\n".join(dl)
                with OUT.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({"to": rc, "data": full}, ensure_ascii=False) + "\n")
                show(full)
                rc, dl = [], []
                await send("250 OK queued")
            else:
                dl.append(ln)
            continue
        up = ln.upper()
        if up.startswith(("EHLO", "HELO")):
            await send("250-dev")
            await send("250 AUTH LOGIN")
        elif up.startswith("AUTH LOGIN"):
            init = len(ln.split()) > 2  # AUTH LOGIN <b64-user> یک‌خطی
            await send("334 UGFzc3dvcmQ6" if init else "334 VXNlcm5hbWU6")
            au = 2 if init else 1
        elif au == 1:
            await send("334 UGFzc3dvcmQ6")
            au = 2
        elif au == 2:
            await send("235 OK")
            au = 0
        elif up.startswith("MAIL FROM"):
            await send("250 OK")
        elif up.startswith("RCPT TO"):
            rc.append(ln)
            await send("250 OK")
        elif up == "DATA":
            dm = True
            await send("354 End with .")
        elif up == "RSET":
            rc, dl, dm = [], [], False
            await send("250 OK")
        elif up == "QUIT":
            await send("221 bye")
            break
        else:
            await send("250 OK")
    writer.close()
    try:
        await writer.wait_closed()
    except Exception:  # noqa: BLE001
        pass


async def main():
    OUT.write_text("", encoding="utf-8")
    srv = await asyncio.start_server(handle, HOST, PORT)
    print(f"DEV SMTP on {HOST}:{PORT} — mailha inja chap mishan", flush=True)
    print("(Ctrl+C baraye khamush kardan)", flush=True)
    async with srv:
        await srv.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
