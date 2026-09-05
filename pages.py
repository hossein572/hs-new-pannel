# pages.py - HS Panel v1.0
# Includes: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · HS Panel</title>
<meta name="description" content="HS Panel - مدیریت پروکسی چند پروتکله">
<meta name="theme-color" content="#0C0A14">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230C0A14'/%3E%3Cpath d='M8 16 L13 21 L24 10' stroke='%239B7CFF' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --hs-bg:#0C0A14;--hs-bg2:#13101E;--hs-bg3:#1A1626;
  --hs-card:rgba(22,18,34,0.88);--hs-card-in:rgba(255,255,255,0.03);
  --hs-purple:#9B7CFF;--hs-purple2:#B794FF;--hs-purple-d:rgba(155,124,255,0.14);
  --hs-violet:#7C5CE7;--hs-violet-d:rgba(124,92,231,0.20);
  --hs-text:#F2EEFF;--hs-dim:#8B85A8;--hs-mid:#A9A3C8;
  --hs-border:rgba(155,124,255,0.18);
  --hs-glow:rgba(155,124,255,0.30);
  --hs-glow-soft:rgba(124,92,231,0.22);
  --hs-danger:#FB7185;
}
[data-theme="light"]{
  --hs-bg:#F5F3FA;--hs-bg2:#EDE9F5;--hs-bg3:#E6E1F0;
  --hs-card:rgba(255,255,255,0.92);--hs-card-in:rgba(124,92,231,0.04);
  --hs-purple:#6D3FF5;--hs-purple2:#8B6AFF;--hs-purple-d:rgba(109,63,245,0.10);
  --hs-violet:#5A38D0;--hs-violet-d:rgba(90,56,208,0.14);
  --hs-text:#14111C;--hs-dim:#6B6880;--hs-mid:#4A4760;
  --hs-border:rgba(109,63,245,0.16);
  --hs-glow:rgba(109,63,245,0.22);--hs-glow-soft:rgba(90,56,208,0.16);
}
html,body{height:100%;overflow-x:hidden}
body{
  font-family:'Inter',system-ui,sans-serif;background:var(--hs-bg);color:var(--hs-text);
  display:flex;align-items:center;justify-content:center;padding:20px;position:relative;
  transition:background .5s ease,color .5s ease;min-height:100vh}
.mono{font-family:'JetBrains Mono',ui-monospace,monospace}

.bg{position:fixed;inset:0;z-index:0;background:
  radial-gradient(ellipse 55% 44% at 16% 6%,var(--hs-glow-soft),transparent 70%),
  radial-gradient(ellipse 52% 40% at 90% 94%,var(--hs-violet-d),transparent 68%),
  var(--hs-bg);transition:background .5s ease}
.grid{position:fixed;inset:0;z-index:0;background-image:
  linear-gradient(rgba(155,124,255,0.045) 1px,transparent 1px),
  linear-gradient(90deg,rgba(155,124,255,0.045) 1px,transparent 1px);
  background-size:46px 46px;mask-image:radial-gradient(ellipse 64% 60% at 50% 44%,black 28%,transparent 88%);
  animation:gridpan 34s linear infinite}
@keyframes gridpan{from{background-position:0 0}to{background-position:92px 92px}}

.theme-switch{position:fixed;top:22px;left:22px;z-index:50}
.theme-btn{
  width:42px;height:42px;border-radius:12px;background:var(--hs-card);border:1px solid var(--hs-border);
  color:var(--hs-mid);display:flex;align-items:center;justify-content:center;font-size:18px;cursor:pointer;
  backdrop-filter:blur(16px);transition:all .25s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.theme-btn:hover{border-color:var(--hs-purple);color:var(--hs-purple2);transform:translateY(-2px)}
.theme-btn i{position:relative;z-index:1;transition:transform .45s cubic-bezier(.34,1.56,.64,1)}
.theme-btn.spin i{transform:rotate(300deg)}

.status-badge{position:fixed;top:22px;right:22px;z-index:50;display:flex;align-items:center;gap:7px;
  background:var(--hs-card);border:1px solid var(--hs-border);border-radius:999px;padding:8px 14px 8px 12px;
  backdrop-filter:blur(16px);animation:badgein .6s cubic-bezier(.16,1,.3,1) .3s backwards}
@keyframes badgein{from{opacity:0;transform:translateY(-10px)}to{opacity:1;transform:none}}
.status-dot{width:7px;height:7px;border-radius:50%;background:var(--hs-purple);position:relative;flex-shrink:0}
.status-dot::after{content:'';position:absolute;inset:-4px;border-radius:50%;background:var(--hs-purple);opacity:.4;animation:ping 1.8s cubic-bezier(0,0,.2,1) infinite}
@keyframes ping{0%{transform:scale(.6);opacity:.5}75%,100%{transform:scale(2.1);opacity:0}}
.status-badge span{font-size:10.5px;color:var(--hs-mid);letter-spacing:.03em}

.wrap{position:relative;z-index:10;width:100%;max-width:400px;animation:cardIn .65s cubic-bezier(.16,1,.3,1);perspective:900px}
@keyframes cardIn{from{opacity:0;transform:translateY(20px) scale(.975)}to{opacity:1;transform:none}}
.card{
  background:var(--hs-card);border:1px solid var(--hs-border);border-radius:22px;padding:40px 34px 32px;
  backdrop-filter:blur(30px);box-shadow:0 30px 80px -20px rgba(0,0,0,.55),0 0 0 1px var(--hs-card-in) inset;
  position:relative;overflow:hidden;transition:transform .35s cubic-bezier(.16,1,.3,1),box-shadow .35s ease}
.card:hover{box-shadow:0 34px 90px -18px rgba(0,0,0,.6),0 0 0 1px var(--hs-card-in) inset,0 0 40px -6px var(--hs-glow-soft)}
.card::before{
  content:'';position:absolute;top:0;left:16px;right:16px;height:1px;
  background:linear-gradient(90deg,transparent,var(--hs-purple),transparent);opacity:.7}
.card::after{
  content:'';position:absolute;inset:-1px;border-radius:22px;padding:1px;z-index:-1;pointer-events:none;
  background:conic-gradient(from var(--ang,0deg),transparent 0%,var(--hs-purple) 8%,transparent 22%,transparent 100%);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;opacity:.45;animation:rotang 6s linear infinite}
@keyframes rotang{to{--ang:360deg}}
@property --ang{syntax:'<angle>';inherits:false;initial-value:0deg}

.brand{display:flex;align-items:center;gap:14px;margin-bottom:30px}
.brand-img{
  width:48px;height:48px;border-radius:14px;overflow:hidden;border:1px solid var(--hs-border);
  flex-shrink:0;position:relative;box-shadow:0 0 0 4px var(--hs-card-in),0 0 24px var(--hs-violet-d);
  animation:brandpulse 3.4s ease-in-out infinite}
@keyframes brandpulse{0%,100%{box-shadow:0 0 0 4px var(--hs-card-in)}50%{box-shadow:0 0 0 6px var(--hs-glow-soft)}}
.brand-img svg{width:100%;height:100%;display:block}
.brand-name{font-size:16px;font-weight:800;color:var(--hs-text);letter-spacing:-.01em}
.brand-sub{font-size:10.5px;color:var(--hs-dim);margin-top:3px;letter-spacing:.02em}
.brand-sub .mono{color:var(--hs-purple);font-weight:600}

h1{font-size:22px;font-weight:800;color:var(--hs-text);margin-bottom:6px;letter-spacing:-.02em;animation:fadeup .5s cubic-bezier(.16,1,.3,1) .1s backwards}
.sub{font-size:12.5px;color:var(--hs-mid);margin-bottom:26px;line-height:1.7;animation:fadeup .5s cubic-bezier(.16,1,.3,1) .18s backwards}
@keyframes fadeup{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

.hint{
  display:flex;align-items:center;gap:10px;background:var(--hs-card-in);border:1px dashed var(--hs-border);
  border-radius:12px;padding:10px 14px;margin-bottom:24px;animation:fadeup .5s cubic-bezier(.16,1,.3,1) .24s backwards}
.hint i{color:var(--hs-dim);font-size:15px}
.hint-label{font-size:11px;color:var(--hs-dim);flex:1}
.hint-val{
  font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:600;color:var(--hs-purple);
  background:var(--hs-violet-d);border:1px solid rgba(124,92,231,0.3);padding:4px 11px;border-radius:7px;
  cursor:pointer;transition:.18s;letter-spacing:.06em}
.hint-val:hover{filter:brightness(1.15);transform:translateY(-1px) scale(1.04)}
.hint-val:active{transform:translateY(0) scale(.96)}

.field{margin-bottom:20px;animation:fadeup .5s cubic-bezier(.16,1,.3,1) .3s backwards}
.field label{display:block;font-size:10.5px;font-weight:700;color:var(--hs-mid);margin-bottom:9px;text-transform:uppercase;letter-spacing:.08em}
.inp-wrap{position:relative}
input[type=password],input[type=text]{
  width:100%;padding:14px 46px 14px 46px;border-radius:13px;border:1px solid var(--hs-border);
  background:rgba(0,0,0,.22);color:var(--hs-text);font-family:inherit;font-size:14.5px;outline:none;transition:.2s}
[data-theme="light"] input[type=password],[data-theme="light"] input[type=text]{background:rgba(109,63,245,.04)}
input::placeholder{color:var(--hs-dim)}
input:focus{border-color:var(--hs-purple);background:rgba(124,92,231,.07);box-shadow:0 0 0 4px var(--hs-glow-soft)}
.ic-lock{position:absolute;right:16px;top:50%;transform:translateY(-50%);color:var(--hs-dim);font-size:17px;pointer-events:none;transition:.2s}
input:focus~.ic-lock{color:var(--hs-purple2);animation:wiggle .4s ease}
@keyframes wiggle{0%,100%{transform:translateY(-50%) rotate(0)}25%{transform:translateY(-50%) rotate(-12deg)}75%{transform:translateY(-50%) rotate(12deg)}}
.ic-eye{
  position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--hs-dim);font-size:17px;
  cursor:pointer;padding:6px;transition:.2s;line-height:0}
.ic-eye:hover{color:var(--hs-purple2);transform:translateY(-50%) scale(1.15)}

.err{display:none;background:rgba(251,113,133,.08);border:1px solid rgba(251,113,133,.25);border-radius:11px;padding:11px 14px;margin-bottom:18px;font-size:12.5px;color:var(--hs-danger);align-items:center;gap:8px;animation:shake .35s}
.err.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}

.btn{
  width:100%;padding:14px;border-radius:13px;border:none;cursor:pointer;
  background:linear-gradient(135deg,var(--hs-purple),var(--hs-purple2),var(--hs-violet));
  background-size:200% 200%;color:#fff;font-family:inherit;font-size:14.5px;font-weight:700;
  display:flex;align-items:center;justify-content:center;gap:9px;box-shadow:0 10px 28px -6px var(--hs-violet-d);
  transition:all .22s;position:relative;overflow:hidden;margin-top:6px;
  animation:btngrad 4s ease infinite,fadeup .5s cubic-bezier(.16,1,.3,1) .36s backwards}
@keyframes btngrad{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.btn::before{content:'';position:absolute;inset:0;background:linear-gradient(120deg,transparent,rgba(255,255,255,.22),transparent);width:50%;transform:translateX(-160%)}
.btn:hover::before{animation:btnsheen 1s ease}
@keyframes btnsheen{to{transform:translateX(260%)}}
.btn:hover{transform:translateY(-2px);box-shadow:0 14px 34px -6px var(--hs-violet-d)}
.btn:active{transform:translateY(0) scale(.98)}
.btn:disabled{opacity:.55;cursor:not-allowed;transform:none;animation:btngrad 4s ease infinite}
.btn:focus-visible,input:focus-visible,.theme-btn:focus-visible,.hint-val:focus-visible{outline:2px solid var(--hs-purple);outline-offset:2px}

.footer{margin-top:24px;padding-top:20px;border-top:1px solid var(--hs-border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11.5px;color:var(--hs-dim);animation:fadeup .5s cubic-bezier(.16,1,.3,1) .42s backwards}
.footer a{color:var(--hs-purple);font-weight:700;text-decoration:none;display:flex;align-items:center;gap:5px;transition:.18s}
.footer a:hover{filter:brightness(1.25);transform:translateY(-1px)}

@keyframes spin{to{transform:rotate(360deg)}}

@media (max-width:420px){
  .card{padding:32px 22px 26px;border-radius:18px}
  .status-badge span{display:none}
  .status-badge{padding:9px}
}
@media (prefers-reduced-motion:reduce){
  *{animation-duration:.001s !important;animation-iteration-count:1 !important}
}
</style>
</head>
<body>
<div class="bg"></div>
<div class="grid"></div>

<div class="theme-switch">
  <button class="theme-btn" id="theme-btn" onclick="toggleTheme()" title="تغییر تم" aria-label="تغییر تم">
    <i class="ti ti-sun" id="theme-icon"></i>
  </button>
</div>
<div class="status-badge"><span class="status-dot"></span><span class="mono">HS PANEL ONLINE</span></div>

<div class="wrap" id="wrap">
  <div class="card" id="card">
    <div class="brand">
      <div class="brand-img">
        <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="lg1" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stop-color="#9B7CFF"/><stop offset="1" stop-color="#7C5CE7"/>
            </linearGradient>
          </defs>
          <rect x="2" y="2" width="44" height="44" rx="12" fill="url(#lg1)"/>
          <path d="M12 25 L19 32 L36 14" stroke="#0C0A14" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="38" cy="10" r="3" fill="#0C0A14" opacity="0.5"/>
        </svg>
      </div>
      <div><div class="brand-name">HS Panel</div><div class="brand-sub">Proxy Manager <span class="mono">· v1.0</span></div></div>
    </div>
    <h1>ورود به پنل</h1>
    <p class="sub">رمز عبور را برای دسترسی به داشبورد مدیریت وارد کنید</p>

    <div class="err" id="err" role="alert"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>

    <div class="hint">
      <i class="ti ti-info-circle"></i>
      <span class="hint-label">رمز پیش‌فرض سیستم</span>
      <span class="hint-val" tabindex="0" role="button" onclick="fillDefault()" onkeydown="if(event.key==='Enter')fillDefault()">123456</span>
    </div>

    <form id="form" novalidate>
      <div class="field">
        <label for="pw">رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required autocomplete="current-password">
          <i class="ti ti-lock ic-lock"></i>
          <i class="ti ti-eye ic-eye" id="eye-toggle" onclick="togglePw()" role="button" tabindex="0" aria-label="نمایش رمز عبور"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
    </form>

    <div class="footer"><a href="https://t.me/" target="_blank" rel="noopener"><i class="ti ti-brand-telegram"></i> پشتیبانی</a></div>
  </div>
</div>

<script>
let isDark = localStorage.getItem('hs-panel-theme') !== 'light';
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
  document.getElementById('theme-icon').className = 'ti ' + (dark ? 'ti-sun' : 'ti-moon');
}
function toggleTheme(){
  isDark = !isDark;
  localStorage.setItem('hs-panel-theme', isDark ? 'dark' : 'light');
  const btn = document.getElementById('theme-btn');
  btn.classList.add('spin');
  setTimeout(()=>btn.classList.remove('spin'), 420);
  applyTheme(isDark);
}
applyTheme(isDark);

function fillDefault(){
  const pw = document.getElementById('pw');
  pw.value = '123456';
  pw.focus();
}
function togglePw(){
  const pw = document.getElementById('pw');
  const eye = document.getElementById('eye-toggle');
  const show = pw.type === 'password';
  pw.type = show ? 'text' : 'password';
  eye.className = 'ti ' + (show ? 'ti-eye-off' : 'ti-eye') + ' ic-eye';
}

const form = document.getElementById('form');
const btn = document.getElementById('btn');
const errEl = document.getElementById('err');
const errText = document.getElementById('err-text');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const pw = document.getElementById('pw').value;
  if(!pw){ errText.textContent = 'رمز عبور را وارد کنید'; errEl.classList.add('show'); return; }
  btn.disabled = true;
  btn.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  errEl.classList.remove('show');
  try {
    const r = await fetch('/api/login', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({password: pw})
    });
    if(!r.ok){ const d = await r.json().catch(()=>({})); throw new Error(d.detail || 'خطا در ورود'); }
    window.location.href = '/dashboard';
  } catch(err){
    errText.textContent = err.message;
    errEl.classList.add('show');
    btn.innerHTML = '<i class="ti ti-login-2"></i> ورود به داشبورد';
    btn.disabled = false;
  }
});
</script>
</body>
</html>
"""

# HS Panel Dashboard - Multi-page SPA with sidebar navigation
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HS Panel · داشبورد</title>
<meta name="theme-color" content="#0C0A14">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230C0A14'/%3E%3Cpath d='M8 16 L13 21 L24 10' stroke='%239B7CFF' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --hs-bg:#0C0A14;--hs-bg2:#13101E;--hs-bg3:#1A1626;
  --hs-card:rgba(22,18,34,0.7);--hs-card-solid:#161222;--hs-card-in:rgba(255,255,255,0.03);
  --hs-purple:#9B7CFF;--hs-purple2:#B794FF;--hs-purple-d:rgba(155,124,255,0.14);
  --hs-violet:#7C5CE7;--hs-violet-d:rgba(124,92,231,0.20);
  --hs-text:#F2EEFF;--hs-dim:#8B85A8;--hs-mid:#A9A3C8;
  --hs-border:rgba(155,124,255,0.18);--hs-border2:rgba(155,124,255,0.08);
  --hs-glow:rgba(155,124,255,0.30);--hs-glow-soft:rgba(124,92,231,0.22);
  --hs-success:#34D399;--hs-success-d:rgba(52,211,153,0.12);
  --hs-warn:#FBBF24;--hs-warn-d:rgba(251,191,36,0.12);
  --hs-danger:#FB7185;--hs-danger-d:rgba(251,113,133,0.12);
  --hs-info:#60A5FA;--hs-info-d:rgba(96,165,250,0.12);
  --hs-sidebar:248px;--hs-radius:14px;
}
[data-theme="light"]{
  --hs-bg:#F5F3FA;--hs-bg2:#EDE9F5;--hs-bg3:#E6E1F0;
  --hs-card:rgba(255,255,255,0.85);--hs-card-solid:#FFFFFF;--hs-card-in:rgba(124,92,231,0.04);
  --hs-purple:#6D3FF5;--hs-purple2:#8B6AFF;--hs-purple-d:rgba(109,63,245,0.10);
  --hs-violet:#5A38D0;--hs-violet-d:rgba(90,56,208,0.14);
  --hs-text:#14111C;--hs-dim:#6B6880;--hs-mid:#4A4760;
  --hs-border:rgba(109,63,245,0.16);--hs-border2:rgba(109,63,245,0.08);
  --hs-glow:rgba(109,63,245,0.22);--hs-glow-soft:rgba(90,56,208,0.16);
}
html,body{height:100%}
body{font-family:'Inter',system-ui,sans-serif;background:var(--hs-bg);color:var(--hs-text);min-height:100vh;font-size:14px;line-height:1.5;transition:background .3s,color .3s}
.mono{font-family:'JetBrains Mono',ui-monospace,monospace}
a{color:inherit;text-decoration:none}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--hs-border);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:var(--hs-purple-d)}

/* ── LAYOUT ───────────────────────────────────────────── */
.app{display:flex;min-height:100vh;position:relative}
.app-bg{position:fixed;inset:0;z-index:0;pointer-events:none;background:
  radial-gradient(ellipse 40% 30% at 10% 0%,var(--hs-violet-d),transparent 60%),
  radial-gradient(ellipse 30% 25% at 95% 100%,var(--hs-glow-soft),transparent 60%)}

/* ── SIDEBAR ───────────────────────────────────────────── */
.sidebar{width:var(--hs-sidebar);background:var(--hs-card-solid);border-left:1px solid var(--hs-border2);
  display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:100;
  transition:transform .3s cubic-bezier(.4,0,.2,1),width .3s}
.sidebar.collapsed{width:72px}
.sidebar.collapsed .sb-text,.sidebar.collapsed .sb-section-label,.sidebar.collapsed .sb-foot-info{display:none}
.sidebar.collapsed .sb-nav-item{justify-content:center;padding:11px}
.sidebar.collapsed .sb-logo-text{display:none}
.sidebar.collapsed .sb-logo{justify-content:center}

.sb-head{padding:18px 16px 14px;border-bottom:1px solid var(--hs-border2);display:flex;align-items:center;gap:11px;position:relative}
.sb-logo{display:flex;align-items:center;gap:11px;flex:1;min-width:0}
.sb-logo-img{width:36px;height:36px;border-radius:10px;flex-shrink:0;overflow:hidden;box-shadow:0 0 18px var(--hs-violet-d)}
.sb-logo-img svg{width:100%;height:100%;display:block}
.sb-logo-text{flex:1;min-width:0}
.sb-logo-name{font-size:14px;font-weight:800;color:var(--hs-text);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sb-logo-sub{font-size:9.5px;color:var(--hs-dim);font-weight:600;letter-spacing:.05em;margin-top:1px}
.sb-toggle{position:absolute;left:-13px;top:24px;width:26px;height:26px;border-radius:50%;background:var(--hs-card-solid);border:1px solid var(--hs-border);color:var(--hs-mid);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:14px;transition:.2s;z-index:101;box-shadow:0 4px 12px rgba(0,0,0,.18)}
.sb-toggle:hover{color:var(--hs-purple);border-color:var(--hs-purple);transform:scale(1.08)}

.sb-body{flex:1;overflow-y:auto;padding:14px 10px 16px;scrollbar-width:thin}
.sb-section-label{font-size:9.5px;font-weight:700;color:var(--hs-dim);text-transform:uppercase;letter-spacing:.12em;padding:14px 12px 6px}
.sb-nav-item{display:flex;align-items:center;gap:11px;padding:10px 12px;border-radius:10px;color:var(--hs-dim);
  font-size:13px;font-weight:500;cursor:pointer;transition:all .2s cubic-bezier(.4,0,.2,1);
  position:relative;margin-bottom:2px;white-space:nowrap;overflow:hidden}
.sb-nav-item i{font-size:17px;width:20px;text-align:center;flex-shrink:0;transition:transform .2s}
.sb-nav-item:hover{background:var(--hs-purple-d);color:var(--hs-text)}
.sb-nav-item:hover i{transform:scale(1.08)}
.sb-nav-item.active{background:linear-gradient(135deg,var(--hs-violet-d),var(--hs-purple-d));
  color:var(--hs-text);font-weight:600;box-shadow:inset 0 0 0 1px var(--hs-border),0 0 24px -8px var(--hs-glow)}
.sb-nav-item.active::before{content:'';position:absolute;right:0;top:50%;transform:translateY(-50%);width:3px;height:18px;background:linear-gradient(180deg,var(--hs-purple),var(--hs-violet));border-radius:3px 0 0 3px;box-shadow:0 0 12px var(--hs-purple)}
.sb-nav-item.active i{color:var(--hs-purple2)}
.sb-badge{margin-right:auto;background:var(--hs-violet-d);color:var(--hs-purple);font-size:9.5px;padding:2px 7px;border-radius:10px;font-weight:700;min-width:18px;text-align:center}

.sb-foot{padding:12px 12px 14px;border-top:1px solid var(--hs-border2)}
.sb-foot-info{display:flex;align-items:center;gap:9px;padding:8px 4px;font-size:11px;color:var(--hs-dim)}
.sb-foot-info .dot{width:6px;height:6px;border-radius:50%;background:var(--hs-success);box-shadow:0 0 8px var(--hs-success-d);animation:pulse-dot 2s infinite}
@keyframes pulse-dot{0%,100%{opacity:1}50%{opacity:.4}}
.sb-foot-info b{color:var(--hs-text);font-weight:600}

/* ── MAIN AREA ─────────────────────────────────────────── */
.main{margin-right:var(--hs-sidebar);flex:1;display:flex;flex-direction:column;min-width:0;position:relative;z-index:1;transition:margin .3s}
.sidebar.collapsed~.main{margin-right:72px}

/* ── TOPBAR ───────────────────────────────────────────── */
.topbar{height:64px;background:var(--hs-card);backdrop-filter:blur(20px);border-bottom:1px solid var(--hs-border2);
  display:flex;align-items:center;padding:0 26px;gap:18px;position:sticky;top:0;z-index:50}
.tb-search{flex:1;max-width:420px;position:relative}
.tb-search input{width:100%;padding:9px 14px 9px 38px;border-radius:10px;border:1px solid var(--hs-border2);
  background:rgba(0,0,0,.18);color:var(--hs-text);font-family:inherit;font-size:13px;outline:none;transition:.2s}
[data-theme="light"] .tb-search input{background:rgba(109,63,245,.04)}
.tb-search input:focus{border-color:var(--hs-purple);box-shadow:0 0 0 3px var(--hs-glow-soft)}
.tb-search input::placeholder{color:var(--hs-dim)}
.tb-search i{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--hs-dim);font-size:16px;pointer-events:none}
.tb-actions{margin-right:auto;display:flex;align-items:center;gap:8px}
.tb-btn{width:38px;height:38px;border-radius:10px;background:transparent;border:1px solid transparent;
  color:var(--hs-mid);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:17px;transition:.2s;position:relative}
.tb-btn:hover{background:var(--hs-purple-d);color:var(--hs-text);border-color:var(--hs-border2)}
.tb-btn .dot-ind{position:absolute;top:8px;right:8px;width:7px;height:7px;border-radius:50%;background:var(--hs-danger);box-shadow:0 0 0 2px var(--hs-bg)}
.tb-user{display:flex;align-items:center;gap:9px;padding:6px 10px 6px 6px;border-radius:10px;
  background:rgba(0,0,0,.18);border:1px solid var(--hs-border2);cursor:pointer;transition:.2s}
[data-theme="light"] .tb-user{background:rgba(109,63,245,.05)}
.tb-user:hover{background:var(--hs-purple-d);border-color:var(--hs-purple)}
.tb-avatar{width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,var(--hs-purple),var(--hs-violet));
  display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;font-weight:700}
.tb-user-name{font-size:12.5px;font-weight:600;color:var(--hs-text)}

/* ── PAGE CONTENT ─────────────────────────────────────── */
.content{padding:24px 26px 60px;flex:1}
.page{display:none;animation:pageIn .35s cubic-bezier(.16,1,.3,1)}
.page.active{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.page-head{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:14px}
.page-title{font-size:22px;font-weight:800;color:var(--hs-text);letter-spacing:-.02em;display:flex;align-items:center;gap:10px}
.page-title i{color:var(--hs-purple);font-size:24px}
.page-sub{font-size:12.5px;color:var(--hs-dim);margin-top:4px}
.page-actions{display:flex;gap:8px;flex-wrap:wrap}

/* ── BUTTONS ──────────────────────────────────────────── */
.btn{font-family:inherit;font-size:12.5px;font-weight:600;border-radius:10px;padding:9px 16px;cursor:pointer;
  display:inline-flex;align-items:center;gap:7px;border:1px solid transparent;transition:all .2s cubic-bezier(.4,0,.2,1);white-space:nowrap}
.btn i{font-size:14px}
.btn:disabled{opacity:.5;cursor:not-allowed}
.btn-primary{background:linear-gradient(135deg,var(--hs-purple),var(--hs-violet));color:#fff;
  box-shadow:0 6px 18px -4px var(--hs-violet-d)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 10px 24px -4px var(--hs-violet-d)}
.btn-primary:active{transform:translateY(0) scale(.98)}
.btn-outline{background:transparent;border:1px solid var(--hs-border);color:var(--hs-text)}
.btn-outline:hover{background:var(--hs-purple-d);border-color:var(--hs-purple)}
.btn-ghost{background:var(--hs-purple-d);color:var(--hs-purple2)}
.btn-ghost:hover{background:var(--hs-violet-d)}
.btn-danger{background:var(--hs-danger-d);color:var(--hs-danger);border-color:rgba(251,113,133,.2)}
.btn-danger:hover{background:rgba(251,113,133,.2)}
.btn-sm{padding:6px 11px;font-size:11.5px;border-radius:8px}
.btn-sm i{font-size:12px}
.btn-icon{width:34px;height:34px;padding:0;justify-content:center;border-radius:9px}

/* ── CARDS ────────────────────────────────────────────── */
.card{background:var(--hs-card-solid);border:1px solid var(--hs-border2);border-radius:var(--hs-radius);
  padding:20px 22px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--hs-border)}
.card-title{font-size:13.5px;font-weight:700;color:var(--hs-text);margin-bottom:14px;display:flex;align-items:center;gap:8px}
.card-title i{font-size:17px;color:var(--hs-purple)}

/* ── STATS GRID ──────────────────────────────────────── */
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.stat-card{background:var(--hs-card-solid);border:1px solid var(--hs-border2);border-radius:var(--hs-radius);
  padding:18px 20px;position:relative;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);cursor:default}
.stat-card::before{content:'';position:absolute;top:0;right:0;left:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--hs-purple),transparent);opacity:0;transition:opacity .25s}
.stat-card:hover{border-color:var(--hs-border);transform:translateY(-3px);box-shadow:0 14px 32px -10px rgba(0,0,0,.25)}
.stat-card:hover::before{opacity:1}
.stat-icon{width:40px;height:40px;border-radius:11px;background:var(--hs-purple-d);color:var(--hs-purple);
  display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px}
.stat-icon.green{background:var(--hs-success-d);color:var(--hs-success)}
.stat-icon.amber{background:var(--hs-warn-d);color:var(--hs-warn)}
.stat-icon.purple{background:var(--hs-violet-d);color:var(--hs-purple2)}
.stat-icon.blue{background:var(--hs-info-d);color:var(--hs-info)}
.stat-label{font-size:11px;color:var(--hs-dim);font-weight:600;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.stat-value{font-size:24px;font-weight:800;color:var(--hs-text);letter-spacing:-.02em;line-height:1}
.stat-value .unit{font-size:13px;font-weight:500;color:var(--hs-dim);margin-right:4px}
.stat-trend{font-size:10.5px;color:var(--hs-success);font-weight:600;margin-top:8px;display:flex;align-items:center;gap:3px}
.stat-trend.down{color:var(--hs-danger)}

/* ── CHART CARD ──────────────────────────────────────── */
.chart-card{background:var(--hs-card-solid);border:1px solid var(--hs-border2);border-radius:var(--hs-radius);
  padding:22px;margin-bottom:18px;position:relative;overflow:hidden}
.chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;flex-wrap:wrap;gap:10px}
.chart-title{font-size:14px;font-weight:700;color:var(--hs-text);display:flex;align-items:center;gap:8px}
.chart-title i{color:var(--hs-purple);font-size:18px}
.chart-body{position:relative;height:280px}

/* ── TABLES ───────────────────────────────────────────── */
.tbl-wrap{background:var(--hs-card-solid);border:1px solid var(--hs-border2);border-radius:var(--hs-radius);overflow:hidden}
.tbl-head{padding:16px 20px;border-bottom:1px solid var(--hs-border2);display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
.tbl-title{font-size:13.5px;font-weight:700;color:var(--hs-text);display:flex;align-items:center;gap:8px}
.tbl-title i{color:var(--hs-purple);font-size:17px}
.tbl-scroll{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:12.5px}
thead{background:rgba(0,0,0,.16)}
[data-theme="light"] thead{background:rgba(109,63,245,.04)}
th{padding:11px 16px;text-align:right;font-size:10.5px;font-weight:700;color:var(--hs-dim);
  text-transform:uppercase;letter-spacing:.06em;white-space:nowrap}
td{padding:13px 16px;border-top:1px solid var(--hs-border2);color:var(--hs-text);white-space:nowrap}
tbody tr{transition:background .15s}
tbody tr:hover{background:var(--hs-purple-d)}
.cell-label{font-weight:600;color:var(--hs-text)}
.cell-mono{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--hs-mid)}
.cell-muted{color:var(--hs-dim);font-size:11.5px}

/* ── BADGES ───────────────────────────────────────────── */
.badge{font-size:10px;font-weight:700;padding:4px 9px;border-radius:8px;display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.badge-green{background:var(--hs-success-d);color:var(--hs-success)}
.badge-red{background:var(--hs-danger-d);color:var(--hs-danger)}
.badge-amber{background:var(--hs-warn-d);color:var(--hs-warn)}
.badge-purple{background:var(--hs-violet-d);color:var(--hs-purple2)}
.badge-blue{background:var(--hs-info-d);color:var(--hs-info)}
.badge-dot::before{content:'';width:5px;height:5px;border-radius:50%;background:currentColor}

/* ── EMPTY STATE ──────────────────────────────────────── */
.empty{padding:60px 20px;text-align:center;color:var(--hs-dim)}
.empty i{font-size:48px;color:var(--hs-purple-d);margin-bottom:14px;display:block}
.empty-title{font-size:15px;font-weight:600;color:var(--hs-text);margin-bottom:6px}
.empty-sub{font-size:12.5px;color:var(--hs-dim);margin-bottom:18px}

/* ── TOAST ────────────────────────────────────────────── */
.toast-host{position:fixed;top:78px;left:24px;z-index:9999;display:flex;flex-direction:column;gap:8px;pointer-events:none}
.toast{background:var(--hs-card-solid);border:1px solid var(--hs-border);border-radius:11px;padding:11px 14px 11px 13px;
  display:flex;align-items:center;gap:11px;font-size:12.5px;color:var(--hs-text);min-width:240px;max-width:360px;
  box-shadow:0 14px 32px -8px rgba(0,0,0,.3);pointer-events:auto;animation:toastIn .35s cubic-bezier(.16,1,.3,1);backdrop-filter:blur(20px)}
.toast.exit{animation:toastOut .25s ease forwards}
.toast-icon{font-size:20px;flex-shrink:0}
.toast-msg{flex:1;line-height:1.45}
.toast-close{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);border-radius:7px;color:var(--hs-mid);
  cursor:pointer;font-size:14px;width:26px;height:26px;display:flex;align-items:center;justify-content:center;
  transition:.2s;flex-shrink:0;padding:0}
.toast-close:hover{background:rgba(255,255,255,.14);color:var(--hs-text)}
.toast.success{border-color:rgba(52,211,153,.35)}.toast.success .toast-icon{color:var(--hs-success)}
.toast.error{border-color:rgba(251,113,133,.35)}.toast.error .toast-icon{color:var(--hs-danger)}
.toast.info .toast-icon{color:var(--hs-info)}
.toast.warn .toast-icon{color:var(--hs-warn)}
@keyframes toastIn{from{opacity:0;transform:translateX(-20px)}to{opacity:1;transform:none}}
@keyframes toastOut{to{opacity:0;transform:translateX(-20px)}}

/* ── MODAL ────────────────────────────────────────────── */
.modal-bg{position:fixed;inset:0;background:rgba(0,0,0,.65);backdrop-filter:blur(8px);
  z-index:200;display:none;align-items:center;justify-content:center;padding:20px;animation:bgIn .25s ease}
.modal-bg.open{display:flex}
@keyframes bgIn{from{opacity:0}to{opacity:1}}
.modal{background:var(--hs-card-solid);border:1px solid var(--hs-border);border-radius:18px;
  width:100%;max-width:520px;max-height:90vh;overflow:hidden;display:flex;flex-direction:column;
  animation:modalIn .3s cubic-bezier(.16,1,.3,1);box-shadow:0 30px 80px -20px rgba(0,0,0,.6)}
@keyframes modalIn{from{opacity:0;transform:translateY(20px) scale(.97)}to{opacity:1;transform:none}}
.modal-head{padding:20px 24px 16px;border-bottom:1px solid var(--hs-border2);display:flex;align-items:flex-start;gap:14px;position:relative}
.modal-icon{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,var(--hs-purple),var(--hs-violet));
  display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px -4px var(--hs-violet-d)}
.modal-title{font-size:15px;font-weight:800;color:var(--hs-text);letter-spacing:-.01em}
.modal-sub{font-size:11.5px;color:var(--hs-dim);margin-top:3px}
.modal-close{position:absolute;left:16px;top:16px;width:30px;height:30px;border-radius:8px;background:transparent;
  border:1px solid transparent;color:var(--hs-dim);cursor:pointer;font-size:17px;display:flex;align-items:center;justify-content:center;transition:.2s}
.modal-close:hover{background:var(--hs-purple-d);color:var(--hs-text);border-color:var(--hs-border2)}
.modal-body{padding:20px 24px;overflow-y:auto;flex:1}
.modal-foot{padding:14px 24px;border-top:1px solid var(--hs-border2);display:flex;gap:8px;justify-content:flex-end}

/* ── FORM ─────────────────────────────────────────────── */
.field{margin-bottom:14px}
.field label{display:block;font-size:11px;font-weight:700;color:var(--hs-mid);margin-bottom:7px;
  text-transform:uppercase;letter-spacing:.05em}
.field input,.field select,.field textarea{width:100%;padding:10px 13px;border-radius:9px;border:1px solid var(--hs-border2);
  background:rgba(0,0,0,.18);color:var(--hs-text);font-family:inherit;font-size:12.5px;outline:none;transition:.2s}
[data-theme="light"] .field input,[data-theme="light"] .field select,[data-theme="light"] .field textarea{background:rgba(109,63,245,.04)}
.field input:focus,.field select:focus,.field textarea:focus{border-color:var(--hs-purple);
  box-shadow:0 0 0 3px var(--hs-glow-soft);background:rgba(0,0,0,.22)}
.field input::placeholder,.field textarea::placeholder{color:var(--hs-dim)}
.field select option{background:var(--hs-card-solid);color:var(--hs-text)}

/* ── MOBILE ───────────────────────────────────────────── */
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:56px;background:var(--hs-card-solid);
  border-bottom:1px solid var(--hs-border2);z-index:99;align-items:center;justify-content:space-between;padding:0 14px;backdrop-filter:blur(20px)}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-top img,.mob-top svg{width:28px;height:28px;border-radius:8px}
.mob-top .t{font-size:13px;font-weight:700;color:var(--hs-text)}
.mob-btn{width:36px;height:36px;border-radius:9px;background:transparent;border:1px solid var(--hs-border2);
  color:var(--hs-mid);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:18px;transition:.2s}
.mob-btn:hover{background:var(--hs-purple-d);color:var(--hs-text)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:98;backdrop-filter:blur(3px)}
.overlay.show{display:block}

@media(max-width:1100px){.stats-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:768px){
  .sidebar{transform:translateX(100%);width:280px;z-index:200}
  .sidebar.open{transform:translateX(0)}
  .main{margin-right:0!important}
  .sb-toggle{display:none}
  .mob-top{display:flex}
  .content{padding:80px 16px 60px}
  .topbar{padding:0 14px;gap:10px}
  .tb-search{display:none}
  .page-title{font-size:18px}
  .stats-grid{grid-template-columns:1fr 1fr}
  .chart-body{height:220px}
}
@media(max-width:480px){.stats-grid{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){*{animation-duration:.001s!important;animation-iteration-count:1!important}}
</style>
</head>
<body>
<div class="app-bg"></div>
<div class="app">

  <!-- Mobile top bar -->
  <div class="mob-top">
    <div class="ml">
      <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
        <defs><linearGradient id="ml" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9B7CFF"/><stop offset="1" stop-color="#7C5CE7"/></linearGradient></defs>
        <rect x="2" y="2" width="28" height="28" rx="7" fill="url(#ml)"/>
        <path d="M9 16 L13 20 L22 10" stroke="#0C0A14" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <span class="t">HS Panel</span>
    </div>
    <div style="display:flex;gap:6px">
      <button class="mob-btn" onclick="toggleTheme()" title="تم"><i class="ti" id="mob-theme-ic"></i></button>
      <button class="mob-btn" onclick="toggleSidebar()" title="منو"><i class="ti ti-menu-2"></i></button>
    </div>
  </div>
  <div class="overlay" id="overlay" onclick="closeSidebar()"></div>

  <!-- Sidebar -->
  <aside class="sidebar" id="sidebar">
    <div class="sb-head">
      <button class="sb-toggle" onclick="toggleCollapse()" title="جمع کردن"><i class="ti ti-chevron-right" id="collapse-ic"></i></button>
      <div class="sb-logo">
        <div class="sb-logo-img">
          <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
            <defs><linearGradient id="sb1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9B7CFF"/><stop offset="1" stop-color="#7C5CE7"/></linearGradient></defs>
            <rect x="2" y="2" width="28" height="28" rx="7" fill="url(#sb1)"/>
            <path d="M9 16 L13 20 L22 10" stroke="#0C0A14" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="sb-logo-text">
          <div class="sb-logo-name">HS Panel</div>
          <div class="sb-logo-sub">v1.0</div>
        </div>
      </div>
    </div>

    <nav class="sb-body">
      <div class="sb-section-label">اصلی</div>
      <a class="sb-nav-item active" data-page="dashboard" onclick="nav('dashboard')"><i class="ti ti-layout-dashboard"></i><span class="sb-text">داشبورد</span></a>
      <a class="sb-nav-item" data-page="links" onclick="nav('links')"><i class="ti ti-link"></i><span class="sb-text">کانفیگ‌ها</span><span class="sb-badge" id="bdg-links">0</span></a>
      <a class="sb-nav-item" data-page="subs" onclick="nav('subs')"><i class="ti ti-folder"></i><span class="sb-text">گروه‌ها</span><span class="sb-badge" id="bdg-subs">0</span></a>
      <a class="sb-nav-item" data-page="connections" onclick="nav('connections')"><i class="ti ti-activity"></i><span class="sb-text">اتصالات</span></a>

      <div class="sb-section-label">ابزارها</div>
      <a class="sb-nav-item" data-page="gaming" onclick="nav('gaming')"><i class="ti ti-device-gamepad-2"></i><span class="sb-text">کانفیگ گیمینگ</span><span class="sb-badge" style="background:var(--hs-violet-d);color:var(--hs-purple2)">جدید</span></a>
      <a class="sb-nav-item" data-page="nodes" onclick="nav('nodes')"><i class="ti ti-server-2"></i><span class="sb-text">نودها</span></a>
      <a class="sb-nav-item" data-page="telegram" onclick="nav('telegram')"><i class="ti ti-brand-telegram"></i><span class="sb-text">ربات تلگرام</span></a>
      <a class="sb-nav-item" data-page="backups" onclick="nav('backups')"><i class="ti ti-database"></i><span class="sb-text">بکاپ / ریستور</span></a>

      <div class="sb-section-label">سیستم</div>
      <a class="sb-nav-item" data-page="settings" onclick="nav('settings')"><i class="ti ti-settings"></i><span class="sb-text">تنظیمات</span></a>
      <a class="sb-nav-item" data-page="update" onclick="nav('update')"><i class="ti ti-cloud-download"></i><span class="sb-text">بروزرسانی</span></a>
    </nav>

    <div class="sb-foot">
      <div class="sb-foot-info"><span class="dot"></span><span><b>سیستم فعال</b> · <span class="mono" id="uptime-mini">00:00:00</span></span></div>
    </div>
  </aside>

  <!-- Main -->
  <main class="main">
    <!-- Topbar -->
    <header class="topbar">
      <div class="tb-search">
        <i class="ti ti-search"></i>
        <input type="text" placeholder="جستجو...">
      </div>
      <div class="tb-actions">
        <button class="tb-btn" onclick="toggleTheme()" title="تغییر تم"><i class="ti" id="top-theme-ic"></i></button>
        <button class="tb-btn" title="اعلان‌ها" onclick="showToast('اعلان جدیدی نیست','info')"><i class="ti ti-bell"></i><span class="dot-ind"></span></button>
        <div class="tb-user" onclick="logout()" title="خروج">
          <div class="tb-avatar">A</div>
          <span class="tb-user-name">مدیر</span>
        </div>
      </div>
    </header>

    <div class="content">
      <!-- DASHBOARD PAGE -->
      <div class="page active" id="page-dashboard">
        <div class="page-head">
          <div>
            <h1 class="page-title"><i class="ti ti-layout-dashboard"></i> داشبورد</h1>
            <div class="page-sub">نمای کلی از وضعیت سیستم و آمار لحظه‌ای</div>
          </div>
          <div class="page-actions">
            <button class="btn btn-outline btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> بروزرسانی</button>
            <button class="btn btn-primary btn-sm" onclick="openModal('modal-create-link')"><i class="ti ti-plus"></i> کانفیگ جدید</button>
          </div>
        </div>

        <div class="stats-grid">
          <div class="stat-card"><div class="stat-icon"><i class="ti ti-link"></i></div><div class="stat-label">کل کانفیگ‌ها</div><div class="stat-value" id="st-links">0</div><div class="stat-trend"><i class="ti ti-arrow-up"></i> <span id="st-active-links">0</span> فعال</div></div>
          <div class="stat-card"><div class="stat-icon green"><i class="ti ti-activity"></i></div><div class="stat-label">اتصالات فعال</div><div class="stat-value" id="st-conn">0</div><div class="stat-trend">لحظه‌ای</div></div>
          <div class="stat-card"><div class="stat-icon purple"><i class="ti ti-database"></i></div><div class="stat-label">ترافیک مصرفی</div><div class="stat-value"><span id="st-bytes">0</span> <span class="unit">MB</span></div><div class="stat-trend">مجموع</div></div>
          <div class="stat-card"><div class="stat-icon amber"><i class="ti ti-clock"></i></div><div class="stat-label">آپتایم</div><div class="stat-value mono" id="st-uptime">00:00:00</div><div class="stat-trend" id="st-start">—</div></div>
        </div>

        <div class="chart-card">
          <div class="chart-head">
            <div class="chart-title"><i class="ti ti-chart-area"></i> نمودار ترافیک ۲۴ ساعت گذشته</div>
          </div>
          <div class="chart-body"><canvas id="trafficChart"></canvas></div>
        </div>

        <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:14px">
          <div class="card">
            <div class="card-title"><i class="ti ti-bolt"></i> آخرین فعالیت‌ها</div>
            <div id="activity-feed" style="display:flex;flex-direction:column;gap:8px">
              <div class="empty" style="padding:30px 10px"><i class="ti ti-loader"></i> <div>در حال بارگذاری...</div></div>
            </div>
          </div>
          <div class="card">
            <div class="card-title"><i class="ti ti-server"></i> وضعیت سیستم</div>
            <div id="system-status" style="display:flex;flex-direction:column;gap:10px">
              <div class="empty" style="padding:30px 10px"><i class="ti ti-loader"></i> <div>در حال بارگذاری...</div></div>
            </div>
          </div>
        </div>
      </div>

      <!-- LINKS PAGE -->
      <div class="page" id="page-links">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-link"></i> کانفیگ‌ها</h1><div class="page-sub">مدیریت کانفیگ‌های پروکسی</div></div>
          <div class="page-actions">
            <button class="btn btn-outline btn-sm" onclick="loadLinks()"><i class="ti ti-refresh"></i> بروزرسانی</button>
            <button class="btn btn-primary btn-sm" onclick="openModal('modal-create-link')"><i class="ti ti-plus"></i> کانفیگ جدید</button>
          </div>
        </div>
        <div class="tbl-wrap">
          <div class="tbl-head">
            <div class="tbl-title"><i class="ti ti-list"></i> لیست کانفیگ‌ها</div>
            <div style="display:flex;gap:8px;align-items:center">
              <button class="btn btn-ghost btn-sm" onclick="testAllLinks()" style="color:var(--hs-success);border-color:rgba(52,211,153,.25);background:rgba(52,211,153,.06)" title="تست سریع همه کانفیگ‌ها"><i class="ti ti-bolt"></i> تست همه</button>
              <button class="btn btn-ghost btn-sm" onclick="showCloudflareIPs()" style="color:var(--hs-purple2);border-color:rgba(139,92,246,.25);background:rgba(139,92,246,.06)" title="IP های Static"><i class="ti ti-world"></i> IP Static</button>
              <input type="text" placeholder="جستجو..." style="padding:7px 12px;border-radius:8px;border:1px solid var(--hs-border2);background:rgba(0,0,0,.18);color:var(--hs-text);font-family:inherit;font-size:12px;outline:none" oninput="filterLinks(this.value)">
            </div>
          </div>
          <div class="tbl-scroll">
            <table id="links-tbl">
              <thead><tr><th>نام</th><th>پروتکل</th><th>ترافیک</th><th>سهمیه</th><th>کشور/IP</th><th>وضعیت</th><th>زمان</th><th>عملیات</th></tr></thead>
              <tbody><tr><td colspan="8" class="empty">در حال بارگذاری...</td></tr></tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- SUBS PAGE -->
      <div class="page" id="page-subs">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-folder"></i> گروه‌های اشتراک</h1><div class="page-sub">گروه‌بندی و اشتراک‌گذاری کانفیگ‌ها</div></div>
          <div class="page-actions"><button class="btn btn-primary btn-sm" onclick="showToast('به‌زودی','info')"><i class="ti ti-plus"></i> گروه جدید</button></div>
        </div>
        <div class="card"><div class="empty"><i class="ti ti-folder-open"></i><div class="empty-title">گروه‌ها</div><div class="empty-sub">این بخش در حال توسعه است</div></div></div>
      </div>

      <!-- CONNECTIONS PAGE -->
      <div class="page" id="page-connections">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-activity"></i> اتصالات فعال</h1><div class="page-sub">مانیتورینگ لحظه‌ای اتصالات</div></div>
        </div>
        <div class="card"><div class="empty"><i class="ti ti-pulse"></i><div class="empty-title">اتصالات</div><div class="empty-sub">در حال اتصال...</div></div></div>
      </div>

      <!-- GAMING PAGE (NEW FEATURE) -->
      <div class="page" id="page-gaming">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-device-gamepad-2"></i> کانفیگ گیمینگ</h1><div class="page-sub">پروفایل‌ها و پریست‌های بهینه برای بازی</div></div>
          <div class="page-actions"><button class="btn btn-primary btn-sm" onclick="openModal('modal-gaming')"><i class="ti ti-plus"></i> پروفایل جدید</button></div>
        </div>
        <div class="card" id="gaming-list"><div class="empty"><i class="ti ti-device-gamepad"></i><div class="empty-title">هنوز پروفایلی ندارید</div><div class="empty-sub">اولین پروفایل گیمینگ خود را بسازید</div><button class="btn btn-primary btn-sm" onclick="openModal('modal-gaming')"><i class="ti ti-plus"></i> ساخت پروفایل</button></div></div>
      </div>

      <!-- NODES PAGE -->
      <div class="page" id="page-nodes">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-server-2"></i> نودها</h1><div class="page-sub">مدیریت نودهای متصل</div></div>
        </div>
        <div class="card"><div class="empty"><i class="ti ti-server"></i><div class="empty-title">نودها</div><div class="empty-sub">این بخش در حال توسعه است</div></div></div>
      </div>

      <!-- TELEGRAM PAGE -->
      <div class="page" id="page-telegram">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-brand-telegram"></i> ربات تلگرام</h1><div class="page-sub">تنظیمات ربات و کانال</div></div>
        </div>
        <div class="card"><div class="empty"><i class="ti ti-brand-telegram"></i><div class="empty-title">ربات تلگرام</div><div class="empty-sub">این بخش در حال توسعه است</div></div></div>
      </div>

      <!-- BACKUPS PAGE -->
      <div class="page" id="page-backups">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-database"></i> بکاپ / ریستور</h1><div class="page-sub">پشتیبان‌گیری و بازیابی</div></div>
        </div>
        <div class="card"><div class="empty"><i class="ti ti-database"></i><div class="empty-title">بکاپ</div><div class="empty-sub">این بخش در حال توسعه است</div></div></div>
      </div>

      <!-- SETTINGS PAGE -->
      <div class="page" id="page-settings">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-settings"></i> تنظیمات</h1><div class="page-sub">تنظیمات کلی سیستم</div></div>
        </div>
        <div class="card" style="max-width:520px">
          <div class="card-title"><i class="ti ti-key"></i> تغییر رمز عبور</div>
          <div class="field"><label>رمز فعلی</label><input type="password" id="set-cur-pw"></div>
          <div class="field"><label>رمز جدید</label><input type="password" id="set-new-pw"></div>
          <button class="btn btn-primary" onclick="changePw()"><i class="ti ti-check"></i> ذخیره رمز جدید</button>
        </div>
      </div>

      <!-- UPDATE PAGE -->
      <div class="page" id="page-update">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-cloud-download"></i> بروزرسانی</h1><div class="page-sub">بررسی و نصب نسخه جدید</div></div>
        </div>
        <div class="card"><div class="empty"><i class="ti ti-cloud-check"></i><div class="empty-title">بروزرسانی</div><div class="empty-sub">در حال بارگذاری اطلاعات نسخه...</div></div></div>
      </div>
    </div>
  </main>
</div>

<!-- CREATE LINK MODAL -->
<div class="modal-bg" id="modal-create-link">
  <div class="modal">
    <div class="modal-head">
      <div class="modal-icon"><i class="ti ti-link-plus"></i></div>
      <div><div class="modal-title">ساخت کانفیگ جدید</div><div class="modal-sub">یک کانفیگ پروکسی با تنظیمات سفارشی بسازید</div></div>
      <button class="modal-close" onclick="closeModal('modal-create-link')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="field"><label>نام کانفیگ</label><input type="text" id="cl-label" placeholder="مثلاً: کاربر علی"></div>
      <div class="field"><label>پروتکل پایه</label>
        <select id="cl-proto">
          <option value="vless-ws">VLESS · WebSocket</option>
          <option value="trojan-ws">Trojan · WebSocket</option>
          <option value="xhttp-packet-up">VLESS · XHTTP packet-up</option>
          <option value="xhttp-stream-up">VLESS · XHTTP stream-up</option>
          <option value="shadowsocks">Shadowsocks</option>
          <option value="mtproto">MTProto (Telegram)</option>
        </select>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>کشور</label>
          <select id="cl-country" onchange="populateStaticIPSelect()">
            <option value="auto">🌐 خودکار (سریع‌ترین)</option>
            <option value="US">🇺🇸 United States</option>
            <option value="DE">🇩🇪 Germany</option>
            <option value="FR">🇫🇷 France</option>
            <option value="GB">🇬🇧 United Kingdom</option>
            <option value="NL">🇳🇱 Netherlands</option>
            <option value="IT">🇮🇹 Italy</option>
            <option value="ES">🇪🇸 Spain</option>
            <option value="SE">🇸🇪 Sweden</option>
            <option value="FI">🇫🇮 Finland</option>
            <option value="PL">🇵🇱 Poland</option>
            <option value="CH">🇨🇭 Switzerland</option>
            <option value="AT">🇦🇹 Austria</option>
            <option value="TR">🇹🇷 Turkey</option>
            <option value="AE">🇦🇪 UAE</option>
            <option value="JP">🇯🇵 Japan</option>
            <option value="SG">🇸🇬 Singapore</option>
            <option value="KR">🇰🇷 South Korea</option>
            <option value="HK">🇭🇰 Hong Kong</option>
          </select>
        </div>
        <div class="field"><label>IP Static</label>
          <select id="cl-static-ip">
            <option value="">⚡ خودکار (سریع‌ترین)</option>
          </select>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>IP Version</label>
          <select id="cl-ipver">
            <option value="ipv4">IPv4</option>
            <option value="ipv6">IPv6</option>
          </select>
        </div>
        <div class="field"><label>پورت (fallback)</label>
          <select id="cl-port">
            <option value="443">443 (HTTPS)</option>
            <option value="8443">8443 (alt HTTPS)</option>
            <option value="2053">2053 (Cloudflare)</option>
            <option value="2083">2083 (Cloudflare)</option>
            <option value="2087">2087 (Cloudflare)</option>
          </select>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 80px;gap:10px">
        <div class="field"><label>سهمیه ترافیک</label><input type="number" id="cl-val" min="0" placeholder="0 = نامحدود"></div>
        <div class="field"><label>واحد</label><select id="cl-unit"><option>GB</option><option selected>MB</option></select></div>
      </div>
      <div class="field"><label>مدت اعتبار (روز)</label><input type="number" id="cl-exp" min="0" placeholder="0 = نامحدود"></div>
      <div class="field"><label>یادداشت</label><textarea id="cl-note" rows="2" placeholder="اختیاری"></textarea></div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-create-link')">انصراف</button>
      <button class="btn btn-primary" onclick="createLink()"><i class="ti ti-check"></i> ساخت کانفیگ</button>
    </div>
  </div>
</div>

<!-- EDIT LINK MODAL -->
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <div class="modal-head">
      <div class="modal-icon"><i class="ti ti-edit"></i></div>
      <div><div class="modal-title">ویرایش کانفیگ</div><div class="modal-sub">تغییر حجم، زمان، کشور یا IP</div></div>
      <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <input type="hidden" id="el-uid">
      <div class="field"><label>نام کانفیگ</label><input type="text" id="el-label" placeholder="نام"></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>کشور</label>
          <select id="el-country" onchange="populateEditStaticIP()">
            <option value="auto">🌐 خودکار</option>
            <option value="US">🇺🇸 United States</option>
            <option value="DE">🇩🇪 Germany</option>
            <option value="FR">🇫🇷 France</option>
            <option value="GB">🇬🇧 United Kingdom</option>
            <option value="NL">🇳🇱 Netherlands</option>
            <option value="IT">🇮🇹 Italy</option>
            <option value="ES">🇪🇸 Spain</option>
            <option value="SE">🇸🇪 Sweden</option>
            <option value="FI">🇫🇮 Finland</option>
            <option value="PL">🇵🇱 Poland</option>
            <option value="CH">🇨🇭 Switzerland</option>
            <option value="AT">🇦🇹 Austria</option>
            <option value="TR">🇹🇷 Turkey</option>
            <option value="AE">🇦🇪 UAE</option>
            <option value="JP">🇯🇵 Japan</option>
            <option value="SG">🇸🇬 Singapore</option>
            <option value="KR">🇰🇷 South Korea</option>
            <option value="HK">🇭🇰 Hong Kong</option>
          </select>
        </div>
        <div class="field"><label>IP Static</label>
          <select id="el-static-ip">
            <option value="">⚡ خودکار (سریع‌ترین)</option>
          </select>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>IP Version</label>
          <select id="el-ipver">
            <option value="ipv4">IPv4</option>
            <option value="ipv6">IPv6</option>
          </select>
        </div>
        <div class="field"><label>پورت</label>
          <select id="el-port">
            <option value="443">443</option>
            <option value="8443">8443</option>
            <option value="2053">2053</option>
            <option value="2083">2083</option>
            <option value="2087">2087</option>
          </select>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 80px;gap:10px">
        <div class="field"><label>سهمیه ترافیک</label><input type="number" id="el-val" min="0" placeholder="0 = نامحدود"></div>
        <div class="field"><label>واحد</label><select id="el-unit"><option>GB</option><option>MB</option></select></div>
      </div>
      <div class="field"><label>تمدید مدت اعتبار (روز از الان)</label><input type="number" id="el-exp" min="0" placeholder="0 = نامحدود / خالی = بدون تغییر"><input type="hidden" id="el-exp-orig"></div>
      <div class="field"><label>یادداشت</label><textarea id="el-note" rows="2"></textarea></div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-primary" onclick="saveEdit()"><i class="ti ti-check"></i> ذخیره</button>
    </div>
  </div>
</div>

<!-- GAMING MODAL -->
<div class="modal-bg" id="modal-gaming">
  <div class="modal">
    <div class="modal-head">
      <div class="modal-icon" style="background:linear-gradient(135deg,#9B7CFF,#5A38D0)"><i class="ti ti-device-gamepad-2"></i></div>
      <div><div class="modal-title">پروفایل گیمینگ جدید</div><div class="modal-sub">پریست اختصاصی برای بازی</div></div>
      <button class="modal-close" onclick="closeModal('modal-gaming')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="field"><label>نام پروفایل</label><input type="text" id="gp-name" placeholder="مثلاً: Valorant Low Ping"></div>
      <div class="field"><label>بازی هدف</label>
        <select id="gp-game">
          <option>Valorant</option><option>CS2</option><option>PUBG</option><option>Fortnite</option>
          <option>Apex Legends</option><option>Overwatch 2</option><option>Call of Duty</option><option>Other</option>
        </select>
      </div>
      <div class="field"><label>پریست عملکرد</label>
        <select id="gp-preset">
          <option>Competitive (Ultra Low Ping)</option>
          <option>Balanced</option>
          <option>Streaming</option>
          <option>Casual</option>
        </select>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>اولویت شبکه</label><select id="gp-net"><option>UDP</option><option>TCP</option><option>Both</option></select></div>
        <div class="field"><label>MTU</label><input type="number" id="gp-mtu" value="1420"></div>
      </div>
      <div class="field"><label>توضیحات</label><textarea id="gp-desc" rows="2" placeholder="اختیاری"></textarea></div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-gaming')">انصراف</button>
      <button class="btn btn-primary" onclick="saveGamingProfile()"><i class="ti ti-check"></i> ذخیره</button>
    </div>
  </div>
</div>

<div class="toast-host" id="toast-host"></div>

<script>
/* ════ THEME ════ */
let isDark = localStorage.getItem('hs-panel-theme') !== 'light';
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
  const ic = dark ? 'ti-sun' : 'ti-moon';
  const e1 = document.getElementById('top-theme-ic'); if(e1) e1.className = 'ti ' + ic;
  const e2 = document.getElementById('mob-theme-ic'); if(e2) e2.className = 'ti ' + ic;
}
function toggleTheme(){
  isDark = !isDark;
  localStorage.setItem('hs-panel-theme', isDark ? 'dark' : 'light');
  applyTheme(isDark);
}
applyTheme(isDark);

/* ════ NAVIGATION ════ */
function nav(page){
  document.querySelectorAll('.sb-nav-item').forEach(n => n.classList.toggle('active', n.dataset.page === page));
  document.querySelectorAll('.page').forEach(p => p.classList.toggle('active', p.id === 'page-' + page));
  closeSidebar();
  window.scrollTo({top:0,behavior:'smooth'});
}

/* ════ SIDEBAR ════ */
let sidebarCollapsed = localStorage.getItem('hs-sb-collapsed') === '1';
function applySidebarState(){
  const sb = document.getElementById('sidebar');
  sb.classList.toggle('collapsed', sidebarCollapsed);
  const ic = document.getElementById('collapse-ic');
  if(ic) ic.style.transform = sidebarCollapsed ? 'rotate(180deg)' : 'rotate(0deg)';
}
function toggleCollapse(){
  sidebarCollapsed = !sidebarCollapsed;
  localStorage.setItem('hs-sb-collapsed', sidebarCollapsed ? '1' : '0');
  applySidebarState();
}
applySidebarState();
function toggleSidebar(){ document.getElementById('sidebar').classList.toggle('open'); document.getElementById('overlay').classList.toggle('show'); }
function closeSidebar(){ document.getElementById('sidebar').classList.remove('open'); document.getElementById('overlay').classList.remove('show'); }

/* ════ MODAL ════ */
function openModal(id){
  document.getElementById(id).classList.add('open');
  // اگه modal ساخت کانفیگه، لیست IP Static رو پر کن
  if (id === 'modal-create-link') {
    populateStaticIPSelect();
  }
}
function closeModal(id){ document.getElementById(id).classList.remove('open'); }
document.querySelectorAll('.modal-bg').forEach(m => m.addEventListener('click', e => { if(e.target === m) m.classList.remove('open'); }));

/* ════ TOAST ════ */
function showToast(msg, type='info', duration=3500){
  const h = document.getElementById('toast-host');
  const t = document.createElement('div');
  t.className = 'toast ' + type;
  const ic = {success:'ti-circle-check-filled',error:'ti-circle-x-filled',warn:'ti-alert-triangle-filled',info:'ti-info-circle-filled'}[type] || 'ti-info-circle-filled';
  t.innerHTML = '<i class="ti ' + ic + ' toast-icon"></i><span class="toast-msg">' + msg + '</span><button class="toast-close" aria-label="بستن"><i class="ti ti-x"></i></button>';
  const closeBtn = t.querySelector('.toast-close');
  const close = () => { t.classList.add('exit'); setTimeout(() => t.remove(), 250); };
  closeBtn.onclick = close;
  h.appendChild(t);
  setTimeout(close, duration);
}

/* ════ LOGOUT ════ */
async function logout(){
  try { await fetch('/api/logout', {method:'POST'}); } catch(e){}
  window.location.href = '/login';
}

/* ════ DATA LOADING ════ */
async function loadStats(){
  try {
    const r = await fetch('/stats');
    if(!r.ok) throw new Error();
    const d = await r.json();
    document.getElementById('st-links').textContent = d.links_count || 0;
    document.getElementById('st-active-links').textContent = d.active_links || 0;
    document.getElementById('st-conn').textContent = d.active_connections || 0;
    document.getElementById('st-bytes').textContent = d.total_traffic_mb || 0;
    document.getElementById('st-uptime').textContent = d.uptime || '00:00:00';
    document.getElementById('uptime-mini').textContent = d.uptime || '00:00:00';
    document.getElementById('bdg-links').textContent = d.links_count || 0;
    document.getElementById('bdg-subs').textContent = d.subs_count || 0;
    // System status
    const ss = document.getElementById('system-status');
    ss.innerHTML = '<div style="display:flex;align-items:center;gap:10px;padding:8px 0"><span class="badge badge-green badge-dot">آنلاین</span><span style="font-size:12px;color:var(--hs-dim)">سیستم فعال است</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid var(--hs-border2);font-size:12px"><span style="color:var(--hs-dim)">کانفیگ‌های منقضی</span><span style="font-weight:600">' + (d.expired_links||0) + '</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid var(--hs-border2);font-size:12px"><span style="color:var(--hs-dim)">گروه‌ها</span><span style="font-weight:600">' + (d.subs_count||0) + '</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid var(--hs-border2);font-size:12px"><span style="color:var(--hs-dim)">کل درخواست‌ها</span><span style="font-weight:600">' + (d.total_requests||0) + '</span></div>';
  } catch(e){ showToast('خطا در بارگذاری آمار','error'); }
}

async function loadActivity(){
  try {
    const r = await fetch('/api/activity');
    if(!r.ok) throw new Error();
    const d = await r.json();
    const logs = d.logs || [];
    const feed = document.getElementById('activity-feed');
    if(!logs.length){ feed.innerHTML = '<div class="empty" style="padding:30px 10px"><i class="ti ti-history"></i><div>فعالیتی ثبت نشده</div></div>'; return; }
    feed.innerHTML = logs.slice(-12).reverse().map(l => {
      const ic = l.level==='err' ? 'ti-alert-circle' : l.level==='warn' ? 'ti-alert-triangle' : l.level==='ok' ? 'ti-circle-check' : 'ti-info-circle';
      const cl = l.level==='err' ? 'red' : l.level==='warn' ? 'amber' : l.level==='ok' ? 'green' : 'blue';
      return '<div style="display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:9px;background:rgba(0,0,0,.12)"><i class="ti ' + ic + '" style="color:var(--hs-' + (cl==='red'?'danger':cl==='amber'?'warn':cl==='green'?'success':'info') + ');font-size:15px;flex-shrink:0"></i><div style="flex:1;min-width:0;font-size:12px;color:var(--hs-text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + (l.message||'') + '</div><div style="font-size:10.5px;color:var(--hs-dim);white-space:nowrap">' + (l.time||'').substring(11,16) + '</div></div>';
    }).join('');
  } catch(e){}
}

async function loadLinks(){
  try {
    const r = await fetch('/api/links');
    if(!r.ok) throw new Error();
    const d = await r.json();
    const rows = document.querySelector('#links-tbl tbody');
    const links = d.links || [];
    if(!links.length){ rows.innerHTML = '<tr><td colspan="8"><div class="empty"><i class="ti ti-link-off"></i><div class="empty-title">کانفیگی نیست</div><div class="empty-sub">اولین کانفیگ خود را بسازید</div></div></td></tr>'; return; }
    rows.innerHTML = links.map(l => {
      const used = (l.used_bytes||0);
      const lim = (l.limit_bytes||0);
      const pct = lim > 0 ? Math.min(100, (used/lim*100)) : 0;
      // زیر کانفیگ فقط IP یا UUID کوتاه نشون بده - نه ایمیل/فول اینفو
      const subLine = l.static_ip || (l.uuid ? l.uuid.substring(0,8) : '—');
      return '<tr data-label="' + (l.label||'').toLowerCase() + '"><td><div class="cell-label">' + (l.label||'—') + '</div><div class="cell-mono">' + subLine + '</div></td>' +
        '<td><span class="badge badge-purple">' + (l.protocol||'') + '</span></td>' +
        '<td><div class="cell-mono">' + fmtBytes(used) + '</div>' + (lim>0 ? '<div style="height:3px;background:var(--hs-border2);border-radius:2px;margin-top:4px;overflow:hidden"><div style="height:100%;width:' + pct + '%;background:linear-gradient(90deg,var(--hs-purple),var(--hs-violet))"></div></div>' : '') + '</td>' +
        '<td><span class="cell-mono">' + (lim>0 ? fmtBytes(lim) : '∞') + '</span></td>' +
        '<td><div style="font-size:11px"><div>' + (l.country && l.country!=='auto' ? l.country : '🌐 Auto') + ' · :' + (l.port||443) + '</div>' + (l.static_ip ? '<div style="color:var(--hs-purple);font-family:monospace">' + l.static_ip + '</div>' : '<div style="color:var(--hs-dim);font-size:10px">' + (l.ip_version==='ipv6' ? 'IPv6' : 'IPv4') + '</div>') + '</div></td>' +
        '<td>' + (l.expired ? '<span class="badge badge-red badge-dot">منقضی</span>' : l.active===false ? '<span class="badge badge-amber badge-dot">غیرفعال</span>' : '<span class="badge badge-green badge-dot">فعال</span>') + '</td>' +
        '<td><div class="cell-mono" style="font-size:11px">' + (l.expires_at ? (function(){try{const dt=new Date(l.expires_at);const now=new Date();const diff=dt-now;if(diff<0)return '<span style="color:var(--hs-danger)">منقضی</span>';const d=Math.floor(diff/86400000),h=Math.floor((diff%86400000)/3600000);return '<span style="color:'+(d<3?'var(--hs-warn)':'var(--hs-text)')+'">' + d + ' روز ' + h + 'س</span>';}catch(e){return '—';}})() : '<span style="color:var(--hs-dim)">∞</span>') + '</div></td>' +
        '<td><div style="display:flex;gap:4px"><button class="btn btn-ghost btn-sm" onclick="copyLink(\'' + l.uuid + '\')" title="کپی"><i class="ti ti-copy"></i></button><button class="btn btn-ghost btn-sm" onclick="testLink(\'' + l.uuid + '\')" title="تست/پینگ"><i class="ti ti-bolt"></i></button><button class="btn btn-ghost btn-sm" onclick="editLink(\'' + l.uuid + '\')" title="ویرایش"><i class="ti ti-edit"></i></button><button class="btn btn-ghost btn-sm" onclick="toggleLink(\'' + l.uuid + '\',' + (l.active!==false) + ')" title="تغییر وضعیت"><i class="ti ti-power"></i></button><button class="btn btn-danger btn-sm" onclick="deleteLink(\'' + l.uuid + '\')" title="حذف"><i class="ti ti-trash"></i></button></div></td></tr>';
    }).join('');
  } catch(e){ showToast('خطا در بارگذاری کانفیگ‌ها','error'); }
}

function filterLinks(q){
  q = q.toLowerCase();
  document.querySelectorAll('#links-tbl tbody tr').forEach(r => {
    const label = r.dataset.label || '';
    r.style.display = label.includes(q) ? '' : 'none';
  });
}

function fmtBytes(b){
  if(!b) return '0 B';
  if(b < 1024) return b + ' B';
  if(b < 1024*1024) return (b/1024).toFixed(1) + ' KB';
  if(b < 1024*1024*1024) return (b/1024/1024).toFixed(2) + ' MB';
  return (b/1024/1024/1024).toFixed(2) + ' GB';
}

async function createLink(){
  const country = document.getElementById('cl-country').value || 'auto';
  let staticIp = document.getElementById('cl-static-ip').value || '';
  // اگه کاربر چیزی انتخاب نکرده، خودمون سریع‌ترین رو پیدا کنیم
  if (!staticIp && country !== 'auto') {
    try {
      const r = await fetch('/api/cloudflare-ips/speedtest?country=' + country);
      const d = await r.json();
      if (d.fastest) staticIp = d.fastest;
    } catch(e){}
  } else if (!staticIp) {
    // auto: همه رو تست کن
    try {
      const r = await fetch('/api/cloudflare-ips/speedtest');
      const d = await r.json();
      if (d.fastest) staticIp = d.fastest;
    } catch(e){}
  }
  const body = {
    label: document.getElementById('cl-label').value || 'لینک جدید',
    protocol: document.getElementById('cl-proto').value,
    limit_value: parseFloat(document.getElementById('cl-val').value) || 0,
    limit_unit: document.getElementById('cl-unit').value,
    expires_days: parseInt(document.getElementById('cl-exp').value) || 0,
    note: document.getElementById('cl-note').value || '',
    country: country,
    static_ip: staticIp,
    ip_version: document.getElementById('cl-ipver').value || 'ipv4',
    port: parseInt(document.getElementById('cl-port').value) || 443,
  };
  try {
    const r = await fetch('/api/links', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)});
    if(!r.ok){ const e = await r.json().catch(()=>({})); throw new Error(e.detail || 'خطا'); }
    closeModal('modal-create-link');
    showToast('کانفیگ با موفقیت ساخته شد' + (staticIp ? ' · IP: ' + staticIp : ''),'success');
    loadLinks();
    loadStats();
  } catch(e){ showToast(e.message,'error'); }
}

async function copyLink(uid){
  try {
    const r = await fetch('/api/links');
    const d = await r.json();
    const l = (d.links||[]).find(x => x.uuid === uid);
    if(l && l.vless_link){ navigator.clipboard.writeText(l.vless_link); showToast('لینک کپی شد','success'); }
  } catch(e){ showToast('خطا در کپی','error'); }
}

async function testAllLinks(){
  showToast('⏳ در حال تست همه کانفیگ‌ها...','info',2000);
  try {
    const r = await fetch('/api/links');
    const d = await r.json();
    const links = d.links || [];
    if(!links.length){ showToast('کانفیگی نیست','warn'); return; }
    let ok=0, fail=0;
    for(const l of links){
      try {
        const tr = await fetch('/api/links/' + l.uuid + '/test');
        if(tr.ok) ok++; else fail++;
      } catch(e){ fail++; }
    }
    showToast('✅ ' + ok + ' کانفیگ آنلاین · ❌ ' + fail + ' مشکل دارد','info',6000);
  } catch(e){ showToast('خطا','error'); }
}

async function testLink(uid){
  const btn = event.target.closest('button');
  const orig = btn.innerHTML;
  btn.innerHTML = '<i class="ti ti-loader"></i>';
  btn.disabled = true;
  try {
    const r = await fetch('/api/links/' + uid + '/test');
    const d = await r.json();
    let html = '<div style="text-align:right;direction:rtl;min-width:280px">';
    html += '<div style="font-weight:600;margin-bottom:8px;color:var(--hs-purple)">🔍 تست کانفیگ</div>';
    html += '<div style="font-size:12px;color:var(--hs-text2);margin-bottom:10px">' + (d.label||'—') + ' · ' + (d.protocol||'') + '</div>';
    if (!d.tests || !d.tests.length){
      html += '<div style="color:#f55">❌ ' + (d.error || 'خطای ناشناخته') + '</div>';
    } else {
      d.tests.forEach(t => {
        const icon = t.ok ? '✅' : '❌';
        const ms = t.ms != null ? ' <span style="color:var(--hs-text2);font-size:11px">(' + t.ms + 'ms)</span>' : '';
        html += '<div style="padding:4px 0;border-bottom:1px solid var(--hs-border)">' + icon + ' <b>' + t.name + '</b>' + ms;
        if (t.detail) html += '<div style="font-size:11px;color:var(--hs-text2);margin-right:20px">' + t.detail + '</div>';
        if (t.error) html += '<div style="font-size:11px;color:#f55;margin-right:20px">' + t.error + '</div>';
        html += '</div>';
      });
      if (d.total_ms != null){
        html += '<div style="margin-top:8px;padding-top:8px;border-top:1px solid var(--hs-border);font-weight:600">⏱ کل: ' + d.total_ms + 'ms</div>';
      }
    }
    html += '</div>';
    const ok = d.ok;
    showToast(html, ok ? 'success' : 'error', 8000);
  } catch(e){
    showToast('خطا در تست: ' + e.message, 'error');
  } finally {
    btn.innerHTML = orig;
    btn.disabled = false;
  }
}

async function showCloudflareIPs(){
  const btn = event.target.closest('button');
  const orig = btn.innerHTML;
  btn.innerHTML = '<i class="ti ti-loader"></i>';
  btn.disabled = true;
  try {
    const r = await fetch('/api/cloudflare-ips');
    const d = await r.json();
    // پر کردن dropdown داخل modal
    populateStaticIPSelect(d);
    let html = '<div style="text-align:right;direction:rtl;min-width:360px;max-height:400px;overflow-y:auto">';
    html += '<div style="font-weight:600;margin-bottom:6px;color:var(--hs-purple);display:flex;align-items:center;gap:8px"><i class="ti ti-world"></i> IP های Static (Cloudflare)</div>';
    html += '<div style="font-size:11px;color:var(--hs-text2);margin-bottom:10px">Host: ' + d.host + '<br>اگه DNS فیلتره، این IP ها رو مستقیم تو کانفیگ بذار. SNI = host.</div>';
    // گروه‌بندی بر اساس کشور
    const byCountry = d.by_country || {};
    Object.keys(byCountry).forEach(code => {
      const grp = byCountry[code];
      html += '<div style="margin-top:10px;padding:5px 9px;background:rgba(139,92,246,.12);border-radius:6px;font-weight:700;color:var(--hs-purple2);font-size:12px;display:inline-block">' + grp.name + '</div>';
      html += '<div style="display:grid;grid-template-columns:1fr 1fr;gap:5px;font-family:monospace;font-size:11px;margin-top:6px">';
      grp.ips.forEach(item => {
        html += '<div style="padding:7px 9px;background:rgba(124,92,231,.08);border:1px solid rgba(124,92,231,.15);border-radius:7px;cursor:pointer;transition:.2s" title="کلیک برای کپی" onclick="navigator.clipboard.writeText(\'' + item.ip + '\');showToast(\'کپی شد: ' + item.ip + ' (' + item.city + ')\',\'success\',2000)"><div style="color:var(--hs-purple2);font-weight:600">' + item.ip + '</div><div style="font-size:9.5px;color:var(--hs-text2);margin-top:2px">' + item.city + '</div></div>';
      });
      html += '</div>';
    });
    html += '</div>';
    showToast(html, 'info', 30000);
  } catch(e){
    showToast('خطا: ' + e.message, 'error');
  } finally {
    btn.innerHTML = orig;
    btn.disabled = false;
  }
}

async function populateStaticIPSelect(){
  try {
    const r = await fetch('/api/cloudflare-ips');
    const d = await r.json();
    const sel = document.getElementById('cl-static-ip');
    if (!sel) return;
    const selCountry = document.getElementById('cl-country');
    const currentCountry = selCountry ? selCountry.value : 'auto';
    sel.innerHTML = '<option value="">⚡ خودکار (تست سریع‌ترین)</option>';
    d.ips.forEach(item => {
      if (currentCountry === 'auto' || item.country === currentCountry) {
        const opt = document.createElement('option');
        opt.value = item.ip;
        opt.textContent = item.ip + ' (' + item.city + ')';
        sel.appendChild(opt);
      }
    });
  } catch(e){}
}

let _editIPCache = null;
async function populateEditStaticIP(){
  try {
    if (!_editIPCache) {
      const r = await fetch('/api/cloudflare-ips');
      _editIPCache = await r.json();
    }
    const d = _editIPCache;
    const sel = document.getElementById('el-static-ip');
    if (!sel) return;
    const selCountry = document.getElementById('el-country');
    const currentRegion = selCountry ? selCountry.value : 'auto';
    const currentVal = sel.dataset.current || '';
    sel.innerHTML = '<option value="">خودکار (پیش‌فرض)</option>';
    d.ips.forEach(item => {
      if (currentRegion === 'auto' || item.country === currentRegion) {
        const opt = document.createElement('option');
        opt.value = item.ip;
        opt.textContent = item.ip + ' (' + item.city + ')';
        if (item.ip === currentVal) opt.selected = true;
        sel.appendChild(opt);
      }
    });
  } catch(e){}
}

async function editLink(uid){
  try {
    const r = await fetch('/api/links');
    const d = await r.json();
    const l = (d.links||[]).find(x => x.uuid === uid);
    if (!l) { showToast('کانفیگ پیدا نشد','error'); return; }
    document.getElementById('el-uid').value = uid;
    document.getElementById('el-label').value = l.label || '';
    document.getElementById('el-country').value = l.country || 'auto';
    document.getElementById('el-ipver').value = l.ip_version || 'ipv4';
    document.getElementById('el-port').value = l.port || 443;
    // اگه limit_bytes > 0، به GB یا MB تبدیل کن
    const lb = l.limit_bytes || 0;
    if (lb > 0) {
      if (lb >= 1024*1024*1024) {
        document.getElementById('el-val').value = (lb / 1024 / 1024 / 1024).toFixed(2);
        document.getElementById('el-unit').value = 'GB';
      } else {
        document.getElementById('el-val').value = (lb / 1024 / 1024).toFixed(2);
        document.getElementById('el-unit').value = 'MB';
      }
    } else {
      document.getElementById('el-val').value = 0;
      document.getElementById('el-unit').value = 'GB';
    }
    document.getElementById('el-exp').value = '';
    document.getElementById('el-exp-orig').value = l.expires_at || '';
    document.getElementById('el-note').value = l.note || '';
    const elStatic = document.getElementById('el-static-ip');
    elStatic.dataset.current = l.static_ip || '';
    await populateEditStaticIP();
    openModal('modal-edit-link');
  } catch(e){ showToast('خطا: ' + e.message,'error'); }
}

async function saveEdit(){
  const uid = document.getElementById('el-uid').value;
  const expVal = document.getElementById('el-exp').value;
  const body = {
    label: document.getElementById('el-label').value,
    country: document.getElementById('el-country').value,
    static_ip: document.getElementById('el-static-ip').value,
    ip_version: document.getElementById('el-ipver').value,
    port: parseInt(document.getElementById('el-port').value) || 443,
    limit_value: parseFloat(document.getElementById('el-val').value) || 0,
    limit_unit: document.getElementById('el-unit').value,
    note: document.getElementById('el-note').value,
  };
  if (expVal !== '' && expVal !== null) {
    body.expires_days = parseInt(expVal) || 0;
  }
  try {
    const r = await fetch('/api/links/' + uid, {method:'PATCH', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)});
    if (!r.ok){ const e = await r.json().catch(()=>({})); throw new Error(e.detail || 'خطا'); }
    closeModal('modal-edit-link');
    showToast('کانفیگ با موفقیت ویرایش شد','success');
    loadLinks();
    loadStats();
  } catch(e){ showToast(e.message,'error'); }
}

async function toggleLink(uid, currentActive){
  try {
    const r = await fetch('/api/links/' + uid, {method:'PATCH', headers:{'Content-Type':'application/json'}, body: JSON.stringify({active: !currentActive})});
    if(!r.ok) throw new Error();
    showToast('وضعیت تغییر کرد','success');
    loadLinks();
  } catch(e){ showToast('خطا','error'); }
}

async function deleteLink(uid){
  if(!confirm('حذف شود؟')) return;
  try {
    const r = await fetch('/api/links/' + uid, {method:'DELETE'});
    if(!r.ok) throw new Error();
    showToast('حذف شد','success');
    loadLinks();
    loadStats();
  } catch(e){ showToast('خطا','error'); }
}

async function changePw(){
  const cur = document.getElementById('set-cur-pw').value;
  const nw = document.getElementById('set-new-pw').value;
  if(!cur || !nw){ showToast('همه فیلدها را پر کنید','warn'); return; }
  if(nw.length < 4){ showToast('رمز جدید حداقل ۴ کاراکتر','warn'); return; }
  try {
    const r = await fetch('/api/change-password', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({current_password: cur, new_password: nw})});
    if(!r.ok){ const e = await r.json().catch(()=>({})); throw new Error(e.detail || 'خطا'); }
    showToast('رمز تغییر کرد','success');
    document.getElementById('set-cur-pw').value = '';
    document.getElementById('set-new-pw').value = '';
  } catch(e){ showToast(e.message,'error'); }
}

/* ════ GAMING CONFIG (NEW FEATURE) ════ */
let gamingProfiles = [];
function loadGamingProfiles(){
  try {
    gamingProfiles = JSON.parse(localStorage.getItem('hs-gaming') || '[]');
  } catch(e){ gamingProfiles = []; }
  renderGaming();
}
function saveGamingProfiles(){
  localStorage.setItem('hs-gaming', JSON.stringify(gamingProfiles));
}
function renderGaming(){
  const el = document.getElementById('gaming-list');
  if(!gamingProfiles.length){
    el.innerHTML = '<div class="empty"><i class="ti ti-device-gamepad"></i><div class="empty-title">هنوز پروفایلی ندارید</div><div class="empty-sub">اولین پروفایل گیمینگ خود را بسازید</div><button class="btn btn-primary btn-sm" onclick="openModal(\'modal-gaming\')"><i class="ti ti-plus"></i> ساخت پروفایل</button></div>';
    return;
  }
  el.innerHTML = '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px">' + gamingProfiles.map((p,i) =>
    '<div style="background:rgba(0,0,0,.16);border:1px solid var(--hs-border2);border-radius:12px;padding:14px;transition:.2s" onmouseover="this.style.borderColor=\'var(--hs-purple)\'" onmouseout="this.style.borderColor=\'var(--hs-border2)\'">' +
    '<div style="display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:10px"><div style="flex:1;min-width:0"><div style="font-size:13.5px;font-weight:700;color:var(--hs-text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + (p.name||'') + '</div><div style="font-size:11px;color:var(--hs-dim);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + (p.game||'') + '</div></div><button onclick="deleteGaming(' + i + ')" style="background:rgba(251,113,133,.12);border:1px solid rgba(251,113,133,.2);color:var(--hs-danger);width:28px;height:28px;border-radius:7px;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0;transition:.2s" onmouseover="this.style.background=\'rgba(251,113,133,.22)\'" onmouseout="this.style.background=\'rgba(251,113,133,.12)\'"><i class="ti ti-trash"></i></button></div>' +
    '<div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:10px">' +
    '<span class="badge badge-purple">' + (p.preset||'') + '</span>' +
    '<span class="badge badge-blue">' + (p.net||'') + '</span>' +
    '<span class="badge badge-amber mono">MTU ' + (p.mtu||1420) + '</span>' +
    '</div>' +
    (p.desc ? '<div style="font-size:11.5px;color:var(--hs-dim);margin-top:10px;line-height:1.6">' + p.desc + '</div>' : '') +
    '</div>'
  ).join('') + '</div>';
}
function saveGamingProfile(){
  const p = {
    name: document.getElementById('gp-name').value || 'بدون نام',
    game: document.getElementById('gp-game').value,
    preset: document.getElementById('gp-preset').value,
    net: document.getElementById('gp-net').value,
    mtu: parseInt(document.getElementById('gp-mtu').value) || 1420,
    desc: document.getElementById('gp-desc').value,
    created_at: new Date().toISOString(),
  };
  gamingProfiles.push(p);
  saveGamingProfiles();
  renderGaming();
  closeModal('modal-gaming');
  showToast('پروفایل گیمینگ ذخیره شد','success');
  ['gp-name','gp-desc'].forEach(id => document.getElementById(id).value = '');
}
function deleteGaming(i){
  if(!confirm('حذف شود؟')) return;
  gamingProfiles.splice(i,1);
  saveGamingProfiles();
  renderGaming();
  showToast('حذف شد','success');
}

/* ════ CHART ════ */
let trafficChart = null;
function renderChart(hourly){
  const ctx = document.getElementById('trafficChart');
  if(!ctx) return;
  const labels = [];
  const data = [];
  const now = new Date();
  for(let i=23; i>=0; i--){
    const h = new Date(now.getTime() - i*3600*1000);
    const key = h.getHours().toString().padStart(2,'0') + ':00';
    labels.push(key);
    data.push((hourly && hourly[key]) ? (hourly[key]/1024/1024) : 0);
  }
  const grad = ctx.getContext('2d').createLinearGradient(0,0,0,280);
  grad.addColorStop(0, 'rgba(155,124,255,0.5)');
  grad.addColorStop(1, 'rgba(155,124,255,0)');
  if(trafficChart) trafficChart.destroy();
  trafficChart = new Chart(ctx, {
    type: 'line',
    data: { labels, datasets: [{
      label: 'ترافیک (MB)',
      data, borderColor: '#9B7CFF', backgroundColor: grad,
      borderWidth: 2, fill: true, tension: 0.4, pointRadius: 0, pointHoverRadius: 5,
      pointBackgroundColor: '#9B7CFF', pointBorderColor: '#fff', pointBorderWidth: 2
    }]},
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: {display:false}, tooltip: {
        backgroundColor: '#161222', titleColor: '#F2EEFF', bodyColor: '#A9A3C8',
        borderColor: 'rgba(155,124,255,0.3)', borderWidth: 1, padding: 10,
        displayColors: false, rtl: true, textDirection: 'rtl',
        callbacks: { label: ctx => ctx.parsed.y.toFixed(2) + ' MB' }
      }},
      scales: {
        x: { grid: {color: 'rgba(155,124,255,0.05)'}, ticks: {color: '#8B85A8', font: {size: 10}}},
        y: { grid: {color: 'rgba(155,124,255,0.05)'}, ticks: {color: '#8B85A8', font: {size: 10}, callback: v => v.toFixed(0) + 'M'}}
      }
    }
  });
}

/* ════ INIT ════ */
async function refreshAll(){
  await Promise.all([loadStats(), loadActivity(), loadLinks()]);
}
async function init(){
  await refreshAll();
  loadGamingProfiles();
  // Get hourly data from stats
  try {
    const r = await fetch('/stats');
    const d = await r.json();
    renderChart(d.hourly || {});
  } catch(e){ renderChart({}); }
  // Auto refresh every 30s
  setInterval(loadStats, 30000);
}
init();
</script>
</body>
</html>
"""


def get_public_page_html(uuid_key: str) -> str:
    return """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HS Panel · اشتراک عمومی</title>
<meta name="theme-color" content="#0C0A14">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230C0A14'/%3E%3Cpath d='M8 16 L13 21 L24 10' stroke='%239B7CFF' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--hs-bg:#0C0A14;--hs-card:rgba(22,18,34,0.7);--hs-purple:#9B7CFF;--hs-text:#F2EEFF;--hs-dim:#8B85A8;--hs-mid:#A9A3C8;--hs-border:rgba(155,124,255,0.18);--hs-violet:#7C5CE7}
body{font-family:'Inter',sans-serif;background:var(--hs-bg);color:var(--hs-text);min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px;position:relative;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 50% 40% at 20% 10%,rgba(124,92,231,.18),transparent 70%),radial-gradient(ellipse 50% 40% at 80% 90%,rgba(155,124,255,.18),transparent 70%);pointer-events:none}
.card{background:var(--hs-card);backdrop-filter:blur(30px);border:1px solid var(--hs-border);border-radius:20px;padding:32px;max-width:520px;width:100%;position:relative;z-index:1;box-shadow:0 30px 80px -20px rgba(0,0,0,.5)}
.brand{display:flex;align-items:center;gap:12px;margin-bottom:22px}
.brand img,.brand svg{width:42px;height:42px;border-radius:11px}
.brand-name{font-size:16px;font-weight:800}
.brand-sub{font-size:11px;color:var(--hs-dim);margin-top:2px}
h1{font-size:20px;font-weight:800;margin-bottom:6px}
.sub{font-size:13px;color:var(--hs-mid);margin-bottom:22px;line-height:1.7}
.links{display:flex;flex-direction:column;gap:10px}
.link-item{background:rgba(0,0,0,.18);border:1px solid var(--hs-border);border-radius:11px;padding:14px;display:flex;align-items:center;gap:12px;transition:.2s;cursor:pointer}
.link-item:hover{border-color:var(--hs-purple);background:rgba(124,92,231,.08)}
.link-info{flex:1;min-width:0}
.link-name{font-size:13.5px;font-weight:600}
.link-meta{font-size:11px;color:var(--hs-dim);margin-top:2px;font-family:'JetBrains Mono',monospace}
.copy-btn{width:32px;height:32px;border-radius:8px;background:rgba(124,92,231,.14);border:1px solid var(--hs-border);color:var(--hs-purple);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s;flex-shrink:0}
.copy-btn:hover{background:var(--hs-purple);color:#fff}
.empty{padding:40px 20px;text-align:center;color:var(--hs-dim)}
.empty i{font-size:42px;display:block;margin-bottom:12px;color:var(--hs-purple);opacity:.4}
</style>
</head>
<body>
<div class="card">
  <div class="brand">
    <svg viewBox="0 0 32 32"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9B7CFF"/><stop offset="1" stop-color="#7C5CE7"/></linearGradient></defs><rect x="2" y="2" width="28" height="28" rx="7" fill="url(#g)"/><path d="M9 16 L13 20 L22 10" stroke="#0C0A14" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <div><div class="brand-name">HS Panel</div><div class="brand-sub">اشتراک عمومی</div></div>
  </div>
  <h1>گروه اشتراک</h1>
  <p class="sub" id="sub-name">در حال بارگذاری...</p>
  <div class="links" id="links-list"><div class="empty"><i class="ti ti-loader"></i> در حال بارگذاری...</div></div>
</div>
<script>
async function load(){
  try {
    const r = await fetch('/api/public/sub/""" + uuid_key + """');
    if(!r.ok) throw new Error();
    const d = await r.json();
    if(d.locked){ document.getElementById('sub-name').textContent = 'این گروه رمز دارد'; return; }
    document.getElementById('sub-name').textContent = d.name || 'گروه';
    const el = document.getElementById('links-list');
    if(!d.links || !d.links.length){ el.innerHTML = '<div class="empty"><i class="ti ti-link-off"></i> کانفیگی موجود نیست</div>'; return; }
    el.innerHTML = d.links.map(l =>
      '<div class="link-item" onclick="copyText(\\''+l.vless_link+'\\')"><div class="link-info"><div class="link-name">'+(l.label||'—')+'</div><div class="link-meta">'+(l.protocol||'')+' · '+(l.used_bytes||0)+' / '+(l.limit_bytes||'∞')+' bytes</div></div><button class="copy-btn"><i class="ti ti-copy"></i></button></div>'
    ).join('');
  } catch(e){ document.getElementById('sub-name').textContent = 'خطا در بارگذاری'; }
}
function copyText(t){ navigator.clipboard.writeText(t); }
load();
</script>
</body>
</html>"""

