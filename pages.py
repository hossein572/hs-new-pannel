LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · HS Panel</title>
<meta name="description" content="HS Panel - مدیریت پروکسی چند پروتکله">
<meta name="theme-color" content="#0a0f0a">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230a0f0a'/%3E%3Cpath d='M8 16 L13 21 L24 10' stroke='%2300FF88' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css" media="print" onload="this.media='all'">
<style>
@font-face{font-family:'IRANSans';font-style:normal;font-weight:300;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Light.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:400;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:500;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Medium.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:600;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Bold.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:700;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Bold.woff2') format('woff2')}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --hs-bg:#0a0f0a;--hs-bg2:#0d1a0d;--hs-bg3:#122212;
  --hs-card:rgba(13,26,13,0.92);--hs-card-in:rgba(0,255,136,0.03);
  --hs-primary:#00FF88;--hs-primary2:#1DE9B6;--hs-primary-d:rgba(0,255,136,0.14);
  --hs-secondary:#FF077A;--hs-secondary2:#FF6B6B;--hs-secondary-d:rgba(255,7,122,0.14);
  --hs-text:#E8FFF0;--hs-dim:#7A9A82;--hs-mid:#A0C4A8;
  --hs-border:rgba(0,255,136,0.20);
  --hs-glow:rgba(0,255,136,0.40);
  --hs-glow-soft:rgba(0,255,136,0.18);
  --hs-purple:#00FF88;--hs-purple2:#1DE9B6;--hs-violet:#00CC6A;
  --hs-purple-d:rgba(0,255,136,0.12);--hs-violet-d:rgba(0,204,106,0.14);
  --hs-danger:#FB7185;
  --hs-success:#00FF88;--hs-success-d:rgba(0,255,136,0.12);
  --hs-warn:#FBBF24;--hs-warn-d:rgba(251,191,36,0.12);
}
[data-theme="light"]{
  --hs-bg:#F0F8F2;--hs-bg2:#E4F2E8;--hs-bg3:#D8ECDc;
  --hs-card:rgba(255,255,255,0.94);--hs-card-in:rgba(0,120,60,0.03);
  --hs-text:#0A1A0E;--hs-dim:#4A6A52;--hs-mid:#2A4A32;
  --hs-border:rgba(0,180,90,0.20);
  --hs-glow:rgba(0,200,100,0.20);--hs-glow-soft:rgba(0,200,100,0.12);
  --hs-purple:#00A85A;--hs-purple2:#008A48;--hs-violet:#00703A;
  --hs-purple-d:rgba(0,168,90,0.10);--hs-violet-d:rgba(0,140,74,0.10);
  --hs-success:#008A48;--hs-warn:#D97706;
  --hs-danger:#DC2626;
}
html,body{height:100%;overflow-x:hidden}
body{
  font-family:'IRANSans','Iran Sans',Tahoma,system-ui,sans-serif;background:var(--hs-bg);color:var(--hs-text);
  display:flex;align-items:center;justify-content:center;padding:20px;position:relative;
  transition:background .5s ease,color .5s ease;min-height:100vh}
.mono{font-family:'JetBrains Mono',ui-monospace,monospace}
.bg{position:fixed;inset:0;z-index:0;background:
  radial-gradient(ellipse 55% 44% at 16% 6%,var(--hs-glow-soft),transparent 70%),
  radial-gradient(ellipse 52% 40% at 90% 94%,var(--hs-primary-d),transparent 68%),
  var(--hs-bg);transition:background .5s ease}
.grid{position:fixed;inset:0;z-index:0;background-image:
  linear-gradient(rgba(0,255,136,0.05) 1px,transparent 1px),
  linear-gradient(90deg,rgba(0,255,136,0.05) 1px,transparent 1px);
  background-size:46px 46px;mask-image:radial-gradient(ellipse 64% 60% at 50% 44%,black 28%,transparent 88%);
  animation:gridpan 34s linear infinite}
@keyframes gridpan{from{background-position:0 0}to{background-position:92px 92px}}
.theme-switch{position:fixed;top:22px;left:22px;z-index:50}
.theme-btn{
  width:42px;height:42px;border-radius:12px;background:var(--hs-card);border:1px solid var(--hs-border);
  color:var(--hs-mid);display:flex;align-items:center;justify-content:center;font-size:18px;cursor:pointer;
  backdrop-filter:blur(16px);transition:all .25s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.theme-btn:hover{border-color:var(--hs-primary);color:var(--hs-primary2);transform:translateY(-2px);box-shadow:0 0 20px var(--hs-glow-soft)}
.theme-btn i{position:relative;z-index:1;transition:transform .45s cubic-bezier(.34,1.56,.64,1)}
.theme-btn.spin i{transform:rotate(300deg)}
.status-badge{position:fixed;top:22px;right:22px;z-index:50;display:flex;align-items:center;gap:7px;
  background:var(--hs-card);border:1px solid var(--hs-border);border-radius:999px;padding:8px 14px 8px 12px;
  backdrop-filter:blur(16px);animation:badgein .6s cubic-bezier(.16,1,.3,1) .3s backwards}
@keyframes badgein{from{opacity:0;transform:translateY(-10px)}to{opacity:1;transform:none}}
.status-dot{width:8px;height:8px;border-radius:50%;background:var(--hs-primary);position:relative;flex-shrink:0;box-shadow:0 0 10px var(--hs-glow)}
.status-dot::after{content:'';position:absolute;inset:-4px;border-radius:50%;background:var(--hs-primary);opacity:.4;animation:ping 1.8s cubic-bezier(0,0,.2,1) infinite}
@keyframes ping{0%{transform:scale(.6);opacity:.6}75%,100%{transform:scale(2.2);opacity:0}}
.status-badge span{font-size:10.5px;color:var(--hs-mid);letter-spacing:.03em}
.wrap{position:relative;z-index:10;width:100%;max-width:400px;animation:cardIn .65s cubic-bezier(.16,1,.3,1);perspective:900px}
@keyframes cardIn{from{opacity:0;transform:translateY(20px) scale(.975)}to{opacity:1;transform:none}}
.card{
  background:var(--hs-card);border:1px solid var(--hs-border);border-radius:22px;padding:40px 34px 32px;
  backdrop-filter:blur(30px);box-shadow:0 20px 60px -15px rgba(0,0,0,.5),0 0 60px -20px var(--hs-glow-soft),0 0 0 1px var(--hs-card-in) inset;
  position:relative;overflow:hidden;transition:transform .35s cubic-bezier(.16,1,.3,1),box-shadow .35s ease}
.card:hover{box-shadow:0 24px 70px -12px rgba(0,0,0,.55),0 0 80px -20px var(--hs-glow),0 0 0 1px var(--hs-card-in) inset}
.card::before{
  content:'';position:absolute;top:0;left:16px;right:16px;height:2px;
  background:linear-gradient(90deg,transparent,var(--hs-primary),transparent);opacity:.8;box-shadow:0 0 12px var(--hs-glow)}
.card::after{
  content:'';position:absolute;inset:-1px;border-radius:22px;padding:1px;z-index:-1;pointer-events:none;
  background:conic-gradient(from var(--ang,0deg),transparent 0%,var(--hs-primary) 8%,transparent 22%,transparent 100%);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;opacity:.5;animation:rotang 6s linear infinite}
@keyframes rotang{to{--ang:360deg}}
@property --ang{syntax:'<angle>';inherits:false;initial-value:0deg}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:30px}
.brand-img{
  width:48px;height:48px;border-radius:14px;overflow:hidden;border:1px solid var(--hs-border);
  flex-shrink:0;position:relative;box-shadow:0 0 0 4px var(--hs-card-in),0 0 30px var(--hs-glow-soft);
  animation:brandpulse 3s ease-in-out infinite}
@keyframes brandpulse{0%,100%{box-shadow:0 0 0 4px var(--hs-card-in),0 0 20px var(--hs-glow-soft)}50%{box-shadow:0 0 0 6px var(--hs-card-in),0 0 40px var(--hs-glow)}}
.brand-img svg{width:100%;height:100%;display:block}
.brand-name{font-size:16px;font-weight:800;color:var(--hs-text);letter-spacing:-.01em}
.brand-sub{font-size:10.5px;color:var(--hs-dim);margin-top:3px;letter-spacing:.02em}
.brand-sub .mono{color:var(--hs-primary);font-weight:600}
h1{font-size:22px;font-weight:800;color:var(--hs-text);margin-bottom:6px;letter-spacing:-.02em;animation:fadeup .5s cubic-bezier(.16,1,.3,1) .1s backwards}
.sub{font-size:12.5px;color:var(--hs-mid);margin-bottom:26px;line-height:1.7;animation:fadeup .5s cubic-bezier(.16,1,.3,1) .18s backwards}
@keyframes fadeup{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.field{margin-bottom:20px;animation:fadeup .5s cubic-bezier(.16,1,.3,1) .3s backwards}
.field label{display:block;font-size:10.5px;font-weight:700;color:var(--hs-mid);margin-bottom:9px;text-transform:uppercase;letter-spacing:.08em}
.inp-wrap{position:relative}
input[type=password],input[type=text],input[type=email]{
  width:100%;padding:16px 48px 16px 48px;border-radius:14px;border:2px solid var(--hs-border);
  background:rgba(0,0,0,.25);color:var(--hs-text);font-family:inherit;font-size:16px;outline:none;transition:.25s}
input.ltr{direction:ltr;text-align:left}
[data-theme="light"] input[type=password],[data-theme="light"] input[type=text],[data-theme="light"] input[type=email]{background:rgba(0,120,60,.04);color:var(--hs-text)}
input::placeholder{color:var(--hs-dim)}
input:focus{border-color:var(--hs-primary);background:rgba(0,255,136,.06);box-shadow:0 0 0 4px var(--hs-glow-soft)}
.ic-lock{position:absolute;right:16px;top:50%;transform:translateY(-50%);color:var(--hs-dim);font-size:19px;pointer-events:none;transition:.2s}
input:focus~.ic-lock{color:var(--hs-primary2)}
.ic-eye{
  position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--hs-dim);font-size:17px;
  cursor:pointer;padding:6px;transition:.2s;line-height:0}
.ic-eye:hover{color:var(--hs-primary2);transform:translateY(-50%) scale(1.15)}
.err{display:none;background:rgba(251,113,133,.08);border:1px solid rgba(251,113,133,.25);border-radius:11px;padding:11px 14px;margin-bottom:18px;font-size:12.5px;color:var(--hs-danger);align-items:center;gap:8px;animation:shake .35s}
.err.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.btn{
  width:100%;padding:14px;border-radius:13px;border:none;cursor:pointer;
  background:linear-gradient(135deg,var(--hs-primary),var(--hs-primary2),var(--hs-violet));
  background-size:200% 200%;color:#001a08;font-family:inherit;font-size:14.5px;font-weight:800;
  display:flex;align-items:center;justify-content:center;gap:9px;box-shadow:0 8px 28px -6px var(--hs-glow-soft),0 0 20px -4px var(--hs-glow);
  transition:all .22s;position:relative;overflow:hidden;margin-top:6px;
  animation:btngrad 4s ease infinite,fadeup .5s cubic-bezier(.16,1,.3,1) .36s backwards}
@keyframes btngrad{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.btn::before{content:'';position:absolute;inset:0;background:linear-gradient(120deg,transparent,rgba(255,255,255,.35),transparent);width:50%;transform:translateX(-160%)}
.btn:hover::before{animation:btnsheen 1s ease}
@keyframes btnsheen{to{transform:translateX(260%)}}
.btn:hover{transform:translateY(-2px);box-shadow:0 12px 36px -6px var(--hs-glow),0 0 30px -4px var(--hs-glow)}
.btn:active{transform:translateY(0) scale(.98)}
.btn:disabled{opacity:.55;cursor:not-allowed;transform:none;animation:btngrad 4s ease infinite}
.btn:focus-visible,input:focus-visible,.theme-btn:focus-visible{outline:2px solid var(--hs-primary);outline-offset:2px}
.footer{margin-top:24px;padding-top:20px;border-top:1px solid var(--hs-border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11.5px;color:var(--hs-dim);animation:fadeup .5s cubic-bezier(.16,1,.3,1) .42s backwards}
.footer a{color:var(--hs-primary);font-weight:700;text-decoration:none;display:flex;align-items:center;gap:5px;transition:.18s}
.footer a:hover{filter:brightness(1.15);transform:translateY(-1px)}
@keyframes spin{to{transform:rotate(360deg)}}
.tabs{display:flex;gap:6px;background:rgba(0,0,0,.15);border:1px solid var(--hs-border);border-radius:13px;padding:5px;margin-bottom:22px}
[data-theme="light"] .tabs{background:rgba(0,168,90,.06)}
.tab{flex:1;padding:10px 8px;border-radius:9px;border:none;background:transparent;color:var(--hs-dim);
  font-family:inherit;font-size:13.5px;font-weight:700;cursor:pointer;transition:.2s;display:flex;align-items:center;justify-content:center;gap:7px}
.tab i{font-size:15px}
.tab:hover{color:var(--hs-text)}
.tab.active{background:linear-gradient(135deg,var(--hs-primary),var(--hs-violet));color:#001a08;box-shadow:0 6px 18px -6px var(--hs-glow)}
.view{display:none}
.view.active{display:block;animation:fadeup .35s cubic-bezier(.16,1,.3,1)}
@media (max-width:480px){
  body{padding:14px}
  .wrap{max-width:100%}
  .card{padding:30px 20px 24px;border-radius:18px}
  .status-badge span{display:none}
  .status-badge{padding:9px;top:14px;right:14px}
  .theme-switch{top:14px;left:14px}
  h1{font-size:20px}
  .sub{font-size:12px}
  input[type=password],input[type=text],input[type=email]{font-size:16px;padding:13px 44px 13px 44px}
  .tab{font-size:12.5px;padding:9px 6px}
  .brand{margin-bottom:24px}
}
@media (max-width:360px){
  .card{padding:26px 16px 20px}
  .brand-name{font-size:14px}
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
              <stop offset="0" stop-color="#00FF88"/><stop offset="1" stop-color="#00CC6A"/>
            </linearGradient>
          </defs>
          <rect x="2" y="2" width="44" height="44" rx="12" fill="url(#lg1)"/>
          <path d="M12 25 L19 32 L36 14" stroke="#051A0B" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="38" cy="10" r="3" fill="#051A0B" opacity="0.4"/>
        </svg>
      </div>
      <div><div class="brand-name">HS Panel</div><div class="brand-sub">Proxy Manager <span class="mono">· v2.0</span></div></div>
    </div>
    <h1 id="page-title">ورود به پنل</h1>
    <p class="sub" id="sub-title">نام کاربری و رمز عبور خود را وارد کنید</p>
    <div class="err" id="err" role="alert"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="tabs" id="auth-tabs">
      <button class="tab active" id="tab-login" type="button" onclick="switchTab('login')"><i class="ti ti-login-2"></i> ورود</button>
      <button class="tab" id="tab-register" type="button" onclick="switchTab('register')"><i class="ti ti-user-plus"></i> ثبت‌نام</button>
    </div>
    <div class="view active" id="view-login">
      <form id="form-login" novalidate>
        <div class="field">
          <label for="li-user">نام کاربری</label>
          <div class="inp-wrap">
            <input type="text" id="li-user" class="ltr" placeholder="username" autocomplete="username" dir="ltr">
            <i class="ti ti-user ic-lock"></i>
          </div>
        </div>
        <div class="field">
          <label for="li-pass">رمز عبور</label>
          <div class="inp-wrap">
            <input type="password" id="li-pass" placeholder="رمز عبور" autocomplete="current-password">
            <i class="ti ti-lock ic-lock"></i>
            <span class="ic-eye" onclick="togglePw('li-pass',this)" title="نمایش رمز"><i class="ti ti-eye"></i></span>
          </div>
        </div>
        <button class="btn" type="submit" id="btn-login"><i class="ti ti-login-2"></i> ورود</button>
      </form>
    </div>
    <div class="view" id="view-register">
      <form id="form-register" novalidate>
        <div class="field">
          <label for="rg-user">نام کاربری</label>
          <div class="inp-wrap">
            <input type="text" id="rg-user" class="ltr" placeholder="username" autocomplete="username" dir="ltr">
            <i class="ti ti-user ic-lock"></i>
          </div>
        </div>
        <div class="field">
          <label for="rg-pw1">رمز عبور</label>
          <div class="inp-wrap">
            <input type="password" id="rg-pw1" placeholder="حداقل ۶ کاراکتر" autocomplete="new-password">
            <i class="ti ti-lock ic-lock"></i>
            <span class="ic-eye" onclick="togglePw('rg-pw1',this)" title="نمایش رمز"><i class="ti ti-eye"></i></span>
          </div>
        </div>
        <div class="field">
          <label for="rg-pw2">تکرار رمز عبور</label>
          <div class="inp-wrap">
            <input type="password" id="rg-pw2" placeholder="رمز را مجدداً وارد کنید" autocomplete="new-password">
            <i class="ti ti-lock ic-lock"></i>
            <span class="ic-eye" onclick="togglePw('rg-pw2',this)" title="نمایش رمز"><i class="ti ti-eye"></i></span>
          </div>
        </div>
        <button class="btn" type="submit" id="btn-register"><i class="ti ti-user-plus"></i> ثبت‌نام و ورود</button>
      </form>
      <div style="font-size:11.5px;color:var(--hs-dim);margin-top:14px;line-height:1.8;text-align:center">
        با ثبت‌نام، پنل مستقل مخصوص شما ساخته می‌شود
      </div>
    </div>
    <div class="footer"><a href="https://t.me/pinginoo-bot" target="_blank" rel="noopener"><i class="ti ti-brand-telegram"></i> پشتیبانی @pinginoo-bot</a></div>
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
const errEl = document.getElementById('err');
const errText = document.getElementById('err-text');
function showErr(msg){ errText.textContent = msg; errEl.style.display = 'flex'; errEl.classList.add('show'); }
function hideErr(){ errEl.style.display = 'none'; errEl.classList.remove('show'); }
function setHeader(t, s){ document.getElementById('page-title').textContent = t; document.getElementById('sub-title').textContent = s; }
function togglePw(id, el){
  const i = document.getElementById(id);
  const show = i.type === 'password';
  i.type = show ? 'text' : 'password';
  el.innerHTML = '<i class="ti ' + (show ? 'ti-eye-off' : 'ti-eye') + '"></i>';
}
const VIEW_HEADERS = {
  'login': ['ورود به پنل', 'نام کاربری و رمز عبور خود را وارد کنید'],
  'register': ['ثبت‌نام', 'یک حساب جدید بسازید — پنل مستقل خودتان می‌شود']
};
function switchTab(tab){
  document.getElementById('tab-login').classList.toggle('active', tab === 'login');
  document.getElementById('tab-register').classList.toggle('active', tab === 'register');
  document.getElementById('view-login').classList.toggle('active', tab === 'login');
  document.getElementById('view-register').classList.toggle('active', tab === 'register');
  hideErr();
  const h = VIEW_HEADERS[tab] || VIEW_HEADERS['login'];
  setHeader(h[0], h[1]);
}
function busy(btn, on, loadingHtml){
  if(on){ btn.disabled = true; btn.dataset.orig = btn.innerHTML; btn.innerHTML = loadingHtml; }
  else { btn.disabled = false; if(btn.dataset.orig) btn.innerHTML = btn.dataset.orig; }
}
async function api(path, body){
  const r = await fetch(path, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)});
  const d = await r.json().catch(() => ({}));
  if(!r.ok) throw new Error(d.detail || 'خطایی رخ داد');
  return d;
}
function validUsername(v){ return v && v.length >= 3 && v.length <= 32 && /^[a-zA-Z0-9_]+$/.test(v); }
document.getElementById('form-login').addEventListener('submit', async (e) => {
  e.preventDefault();
  const username = document.getElementById('li-user').value.trim().toLowerCase();
  const password = document.getElementById('li-pass').value;
  const btn = document.getElementById('btn-login');
  if(!username){ showErr('نام کاربری را وارد کنید'); return; }
  if(!password){ showErr('رمز عبور را وارد کنید'); return; }
  hideErr();
  busy(btn, true, '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...');
  try {
    await api('/api/auth/login', {username: username, password: password});
    window.location.href = '/dashboard';
  } catch(err){ showErr(err.message); busy(btn, false); }
});
document.getElementById('form-register').addEventListener('submit', async (e) => {
  e.preventDefault();
  const username = document.getElementById('rg-user').value.trim().toLowerCase();
  const pw1 = document.getElementById('rg-pw1').value;
  const pw2 = document.getElementById('rg-pw2').value;
  const btn = document.getElementById('btn-register');
  if(!validUsername(username)){ showErr('نام کاربری باید ۳ تا ۳۲ کاراکتر باشد (حروف انگلیسی، عدد یا _)'); return; }
  if(pw1.length < 6){ showErr('رمز عبور باید حداقل ۶ کاراکتر باشد'); return; }
  if(pw1 !== pw2){ showErr('رمزهای واردشده یکسان نیستند'); return; }
  hideErr();
  busy(btn, true, '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ثبت‌نام...');
  try {
    await api('/api/auth/register', {username: username, password: pw1});
    window.location.href = '/dashboard';
  } catch(err){ showErr(err.message); busy(btn, false); }
});
</script>
</body>
</html>
"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HS Panel · داشبورد</title>
<meta name="theme-color" content="#0a0f0a">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230a0f0a'/%3E%3Cpath d='M8 16 L13 21 L24 10' stroke='%2300FF88' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css" media="print" onload="this.media='all'">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js" async onerror="this.onerror=null;this.src='https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.js'"></script>
<style>
@font-face{font-family:'IRANSans';font-style:normal;font-weight:300;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Light.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:400;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:500;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Medium.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:600;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Bold.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:700;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Bold.woff2') format('woff2')}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --hs-bg:#080e08;--hs-bg2:#0c180c;--hs-bg3:#112411;
  --hs-card:rgba(12,24,12,0.75);--hs-card-solid:#0e1e0e;--hs-card-in:rgba(0,255,136,0.04);
  --hs-primary:#00FF88;--hs-primary2:#1DE9B6;--hs-primary-d:rgba(0,255,136,0.14);
  --hs-secondary:#FF077A;--hs-secondary2:#FF6B6B;--hs-secondary-d:rgba(255,7,122,0.14);
  --hs-text:#E8FFF0;--hs-dim:#70947A;--hs-mid:#98C0A2;
  --hs-border:rgba(0,255,136,0.18);--hs-border2:rgba(0,255,136,0.08);
  --hs-glow:rgba(0,255,136,0.35);--hs-glow-soft:rgba(0,255,136,0.15);
  --hs-purple:#00FF88;--hs-purple2:#1DE9B6;--hs-violet:#00CC6A;
  --hs-purple-d:rgba(0,255,136,0.10);--hs-violet-d:rgba(0,204,106,0.12);
  --hs-success:#00FF88;--hs-success-d:rgba(0,255,136,0.12);
  --hs-warn:#FBBF24;--hs-warn-d:rgba(251,191,36,0.12);
  --hs-danger:#FB7185;--hs-danger-d:rgba(251,113,133,0.12);
  --hs-info:#60A5FA;--hs-info-d:rgba(96,165,250,0.12);
  --hs-text2:#98C0A2;
  --hs-sidebar:248px;--hs-radius:14px;
}
[data-theme="light"]{
  --hs-bg:#EDF6F0;--hs-bg2:#DFEDE4;--hs-bg3:#D0E5D6;
  --hs-card:rgba(255,255,255,0.88);--hs-card-solid:#FFFFFF;--hs-card-in:rgba(0,130,65,0.04);
  --hs-primary:#00A85A;--hs-primary2:#00C070;--hs-primary-d:rgba(0,168,90,0.10);
  --hs-secondary:#E0077A;--hs-secondary2:#FF6B6B;--hs-secondary-d:rgba(224,7,122,0.10);
  --hs-text:#081A0C;--hs-dim:#4A6A52;--hs-mid:#2A4A34;
  --hs-border:rgba(0,168,90,0.20);--hs-border2:rgba(0,168,90,0.10);
  --hs-glow:rgba(0,180,95,0.20);--hs-glow-soft:rgba(0,180,95,0.10);
  --hs-purple:#00A85A;--hs-purple2:#008A48;--hs-violet:#00703A;
  --hs-purple-d:rgba(0,168,90,0.08);--hs-violet-d:rgba(0,140,74,0.08);
  --hs-success:#008A48;--hs-success-d:rgba(0,138,72,0.10);
  --hs-warn:#D97706;--hs-warn-d:rgba(217,119,6,0.10);
  --hs-danger:#DC2626;--hs-danger-d:rgba(220,38,38,0.10);
  --hs-info:#2563EB;--hs-info-d:rgba(37,99,235,0.10);
  --hs-text2:#4A6A52;
}
html,body{height:100%}
body{font-family:'IRANSans','Iran Sans',Tahoma,system-ui,sans-serif;background:var(--hs-bg);color:var(--hs-text);min-height:100vh;font-size:14px;line-height:1.5;transition:background .3s,color .3s}
.mono{font-family:'JetBrains Mono',ui-monospace,monospace}
a{color:inherit;text-decoration:none}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--hs-border);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:var(--hs-primary-d)}
.app{display:flex;min-height:100vh;position:relative}
.app-bg{position:fixed;inset:0;z-index:0;pointer-events:none;background:
  radial-gradient(ellipse 40% 30% at 10% 0%,var(--hs-glow-soft),transparent 60%),
  radial-gradient(ellipse 30% 25% at 95% 100%,var(--hs-primary-d),transparent 60%)}
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
.sb-logo-img{width:36px;height:36px;border-radius:10px;flex-shrink:0;overflow:hidden;box-shadow:0 0 20px var(--hs-glow-soft)}
.sb-logo-img svg{width:100%;height:100%;display:block}
.sb-logo-text{flex:1;min-width:0}
.sb-logo-name{font-size:14px;font-weight:800;color:var(--hs-text);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sb-logo-sub{font-size:9.5px;color:var(--hs-dim);font-weight:600;letter-spacing:.05em;margin-top:1px}
.sb-toggle{position:absolute;left:-13px;top:24px;width:26px;height:26px;border-radius:50%;background:var(--hs-card-solid);border:1px solid var(--hs-border);color:var(--hs-mid);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:14px;transition:.2s;z-index:101;box-shadow:0 4px 12px rgba(0,0,0,.18)}
.sb-toggle:hover{color:var(--hs-primary);border-color:var(--hs-primary);transform:scale(1.08);box-shadow:0 0 15px var(--hs-glow-soft)}
.sb-body{flex:1;overflow-y:auto;padding:14px 10px 16px;scrollbar-width:thin}
.sb-section-label{font-size:9.5px;font-weight:700;color:var(--hs-dim);text-transform:uppercase;letter-spacing:.12em;padding:14px 12px 6px}
.sb-nav-item{display:flex;align-items:center;gap:11px;padding:10px 12px;border-radius:10px;color:var(--hs-dim);
  font-size:13px;font-weight:500;cursor:pointer;transition:all .2s cubic-bezier(.4,0,.2,1);
  position:relative;margin-bottom:2px;white-space:nowrap;overflow:hidden}
.sb-nav-item i{font-size:17px;width:20px;text-align:center;flex-shrink:0;transition:transform .2s}
.sb-nav-item:hover{background:var(--hs-primary-d);color:var(--hs-text)}
.sb-nav-item:hover i{transform:scale(1.08)}
.sb-nav-item.active{background:linear-gradient(135deg,var(--hs-violet-d),var(--hs-primary-d));
  color:var(--hs-text);font-weight:600;box-shadow:inset 0 0 0 1px var(--hs-border),0 0 20px -8px var(--hs-glow)}
.sb-nav-item.active::before{content:'';position:absolute;right:0;top:50%;transform:translateY(-50%);width:3px;height:18px;background:linear-gradient(180deg,var(--hs-primary),var(--hs-violet));border-radius:3px 0 0 3px;box-shadow:0 0 10px var(--hs-primary)}
.sb-nav-item.active i{color:var(--hs-primary2)}
.sb-badge{margin-right:auto;background:var(--hs-violet-d);color:var(--hs-primary);font-size:9.5px;padding:2px 7px;border-radius:10px;font-weight:700;min-width:18px;text-align:center}
.sb-foot{padding:12px 12px 14px;border-top:1px solid var(--hs-border2)}
.sb-foot-info{display:flex;align-items:center;gap:9px;padding:8px 4px;font-size:11px;color:var(--hs-dim)}
.sb-foot-info .dot{width:6px;height:6px;border-radius:50%;background:var(--hs-success);box-shadow:0 0 8px var(--hs-success-d);animation:pulse-dot 2s infinite}
@keyframes pulse-dot{0%,100%{opacity:1;box-shadow:0 0 8px var(--hs-glow)}50%{opacity:.5;box-shadow:0 0 2px var(--hs-glow)}}
.sb-foot-info b{color:var(--hs-text);font-weight:600}
.main{margin-right:var(--hs-sidebar);flex:1;display:flex;flex-direction:column;min-width:0;position:relative;z-index:1;transition:margin .3s}
.sidebar.collapsed~.main{margin-right:72px}
.topbar{height:64px;background:var(--hs-card);backdrop-filter:blur(20px);border-bottom:1px solid var(--hs-border2);
  display:flex;align-items:center;padding:0 26px;gap:18px;position:sticky;top:0;z-index:50}
.tb-search{flex:1;max-width:420px;position:relative}
.tb-search input{width:100%;padding:9px 14px 9px 38px;border-radius:10px;border:1px solid var(--hs-border2);
  background:rgba(0,0,0,.15);color:var(--hs-text);font-family:inherit;font-size:13px;outline:none;transition:.2s}
[data-theme="light"] .tb-search input{background:rgba(0,130,65,.04)}
.tb-search input:focus{border-color:var(--hs-primary);box-shadow:0 0 0 3px var(--hs-glow-soft)}
.tb-search input::placeholder{color:var(--hs-dim)}
.tb-search i{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--hs-dim);font-size:16px;pointer-events:none}
.tb-actions{margin-right:auto;display:flex;align-items:center;gap:8px}
.tb-btn{width:38px;height:38px;border-radius:10px;background:transparent;border:1px solid transparent;
  color:var(--hs-mid);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:17px;transition:.2s;position:relative}
.tb-btn:hover{background:var(--hs-primary-d);color:var(--hs-text);border-color:var(--hs-border2)}
.tb-btn.logout:hover{color:var(--hs-danger);border-color:rgba(251,113,133,.35);background:rgba(251,113,133,.08)}
.tb-btn .dot-ind{position:absolute;top:8px;right:8px;width:7px;height:7px;border-radius:50%;background:var(--hs-danger);box-shadow:0 0 0 2px var(--hs-bg)}
.tb-user{display:flex;align-items:center;gap:9px;padding:6px 10px 6px 6px;border-radius:10px;
  background:rgba(0,0,0,.15);border:1px solid var(--hs-border2);cursor:pointer;transition:.2s}
[data-theme="light"] .tb-user{background:rgba(0,130,65,.05)}
.tb-user:hover{background:var(--hs-primary-d);border-color:var(--hs-primary)}
.tb-avatar{width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,var(--hs-primary),var(--hs-violet));
  display:flex;align-items:center;justify-content:center;color:#001a08;font-size:13px;font-weight:800}
.tb-user-name{font-size:12.5px;font-weight:600;color:var(--hs-text)}
.content{padding:24px 26px 60px;flex:1}
.page{display:none;animation:pageIn .35s cubic-bezier(.16,1,.3,1)}
.page.active{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.page-head{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:14px}
.page-title{font-size:22px;font-weight:800;color:var(--hs-text);letter-spacing:-.02em;display:flex;align-items:center;gap:10px}
.page-title i{color:var(--hs-primary);font-size:24px;text-shadow:0 0 15px var(--hs-glow-soft)}
.page-sub{font-size:12.5px;color:var(--hs-dim);margin-top:4px}
.page-actions{display:flex;gap:8px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12.5px;font-weight:600;border-radius:10px;padding:9px 16px;cursor:pointer;
  display:inline-flex;align-items:center;gap:7px;border:1px solid transparent;transition:all .2s cubic-bezier(.4,0,.2,1);white-space:nowrap}
.btn i{font-size:14px}
.btn:disabled{opacity:.5;cursor:not-allowed}
.btn-primary{background:linear-gradient(135deg,var(--hs-primary),var(--hs-violet));color:#001a08;font-weight:700;
  box-shadow:0 6px 18px -4px var(--hs-glow-soft),0 0 15px -4px var(--hs-glow)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 10px 24px -4px var(--hs-glow),0 0 20px -4px var(--hs-glow)}
.btn-primary:active{transform:translateY(0) scale(.98)}
.btn-outline{background:transparent;border:1px solid var(--hs-border);color:var(--hs-text)}
.btn-outline:hover{background:var(--hs-primary-d);border-color:var(--hs-primary)}
.btn-ghost{background:var(--hs-primary-d);color:var(--hs-primary2)}
.btn-ghost:hover{background:var(--hs-violet-d)}
.btn-danger{background:var(--hs-danger-d);color:var(--hs-danger);border-color:rgba(251,113,133,.2)}
.btn-danger:hover{background:rgba(251,113,133,.2)}
.btn-sm{padding:6px 11px;font-size:11.5px;border-radius:8px}
.btn-sm i{font-size:12px}
.btn-icon{width:34px;height:34px;padding:0;justify-content:center;border-radius:9px}
.card{background:var(--hs-card-solid);border:1px solid var(--hs-border2);border-radius:var(--hs-radius);
  padding:20px 22px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--hs-border)}
.card-title{font-size:13.5px;font-weight:700;color:var(--hs-text);margin-bottom:14px;display:flex;align-items:center;gap:8px}
.card-title i{font-size:17px;color:var(--hs-primary);text-shadow:0 0 10px var(--hs-glow-soft)}
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.stat-card{background:var(--hs-card-solid);border:1px solid var(--hs-border2);border-radius:var(--hs-radius);
  padding:18px 20px;position:relative;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);cursor:default}
.stat-card::before{content:'';position:absolute;top:0;right:0;left:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--hs-primary),transparent);opacity:0;transition:opacity .25s;box-shadow:0 0 10px var(--hs-glow)}
.stat-card:hover{border-color:var(--hs-border);transform:translateY(-3px);box-shadow:0 14px 32px -10px rgba(0,0,0,.25),0 0 30px -12px var(--hs-glow-soft)}
.stat-card:hover::before{opacity:1}
.stat-icon{width:40px;height:40px;border-radius:11px;background:var(--hs-primary-d);color:var(--hs-primary);
  display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;box-shadow:0 0 15px var(--hs-glow-soft)}
.stat-icon.green{background:var(--hs-success-d);color:var(--hs-success)}
.stat-icon.amber{background:var(--hs-warn-d);color:var(--hs-warn)}
.stat-icon.purple{background:var(--hs-violet-d);color:var(--hs-primary2)}
.stat-icon.blue{background:var(--hs-info-d);color:var(--hs-info)}
.stat-label{font-size:11px;color:var(--hs-dim);font-weight:600;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.stat-value{font-size:24px;font-weight:800;color:var(--hs-text);letter-spacing:-.02em;line-height:1}
.stat-value .unit{font-size:13px;font-weight:500;color:var(--hs-dim);margin-right:4px}
.stat-trend{font-size:10.5px;color:var(--hs-success);font-weight:600;margin-top:8px;display:flex;align-items:center;gap:3px}
.stat-trend.down{color:var(--hs-danger)}
.chart-card{background:var(--hs-card-solid);border:1px solid var(--hs-border2);border-radius:var(--hs-radius);
  padding:22px;margin-bottom:18px;position:relative;overflow:hidden}
.chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;flex-wrap:wrap;gap:10px}
.chart-title{font-size:14px;font-weight:700;color:var(--hs-text);display:flex;align-items:center;gap:8px}
.chart-title i{color:var(--hs-primary);font-size:18px;text-shadow:0 0 10px var(--hs-glow-soft)}
.chart-body{position:relative;height:280px}
.tbl-wrap{background:var(--hs-card-solid);border:1px solid var(--hs-border2);border-radius:var(--hs-radius);overflow:hidden}
.tbl-head{padding:16px 20px;border-bottom:1px solid var(--hs-border2);display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
.tbl-title{font-size:13.5px;font-weight:700;color:var(--hs-text);display:flex;align-items:center;gap:8px}
.tbl-title i{color:var(--hs-primary);font-size:17px}
.tbl-scroll{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:12.5px}
thead{background:rgba(0,0,0,.12)}
[data-theme="light"] thead{background:rgba(0,130,65,.04)}
th{padding:11px 16px;text-align:right;font-size:10.5px;font-weight:700;color:var(--hs-dim);
  text-transform:uppercase;letter-spacing:.06em;white-space:nowrap}
td{padding:13px 16px;border-top:1px solid var(--hs-border2);color:var(--hs-text);white-space:nowrap}
tbody tr{transition:background .15s}
tbody tr:hover{background:var(--hs-primary-d)}
.cell-label{font-weight:600;color:var(--hs-text)}
.cell-mono{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--hs-mid)}
.cell-muted{color:var(--hs-dim);font-size:11.5px}
.ping-badge{display:inline-flex;align-items:center;gap:4px;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;padding:3px 8px;border-radius:6px;
  background:rgba(0,255,136,.08);color:var(--hs-primary);border:1px solid rgba(0,255,136,.18);min-width:56px;justify-content:center}
.ping-badge.warn{background:rgba(251,191,36,.08);color:var(--hs-warn);border-color:rgba(251,191,36,.2)}
.ping-badge.bad{background:rgba(251,113,133,.08);color:var(--hs-danger);border-color:rgba(251,113,133,.2)}
.ping-badge.testing{background:rgba(96,165,250,.08);color:var(--hs-info);border-color:rgba(96,165,250,.2)}
.badge{font-size:10px;font-weight:700;padding:4px 9px;border-radius:8px;display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.badge-green{background:var(--hs-success-d);color:var(--hs-success)}
.badge-red{background:var(--hs-danger-d);color:var(--hs-danger)}
.badge-amber{background:var(--hs-warn-d);color:var(--hs-warn)}
.badge-purple{background:var(--hs-violet-d);color:var(--hs-primary2)}
.badge-blue{background:var(--hs-info-d);color:var(--hs-info)}
.badge-dot::before{content:'';width:5px;height:5px;border-radius:50%;background:currentColor}
.empty{padding:60px 20px;text-align:center;color:var(--hs-dim)}
.empty i{font-size:48px;color:var(--hs-primary-d);margin-bottom:14px;display:block}
.empty-title{font-size:15px;font-weight:600;color:var(--hs-text);margin-bottom:6px}
.empty-sub{font-size:12.5px;color:var(--hs-dim);margin-bottom:18px}
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
.toast.success{border-color:rgba(0,255,136,.35)}.toast.success .toast-icon{color:var(--hs-success)}
.toast.error{border-color:rgba(251,113,133,.35)}.toast.error .toast-icon{color:var(--hs-danger)}
.toast.info .toast-icon{color:var(--hs-info)}
.toast.warn .toast-icon{color:var(--hs-warn)}
@keyframes toastIn{from{opacity:0;transform:translateX(-20px)}to{opacity:1;transform:none}}
@keyframes toastOut{to{opacity:0;transform:translateX(-20px)}}
.modal-bg{position:fixed;inset:0;background:rgba(0,0,0,.65);backdrop-filter:blur(8px);
  z-index:200;display:none;align-items:center;justify-content:center;padding:20px;animation:bgIn .25s ease}
.modal-bg.open{display:flex}
@keyframes bgIn{from{opacity:0}to{opacity:1}}
.modal{background:var(--hs-card-solid);border:1px solid var(--hs-border);border-radius:18px;
  width:100%;max-width:560px;max-height:90vh;overflow:hidden;display:flex;flex-direction:column;
  animation:modalIn .3s cubic-bezier(.16,1,.3,1);box-shadow:0 30px 80px -20px rgba(0,0,0,.6),0 0 60px -20px var(--hs-glow-soft)}
@keyframes modalIn{from{opacity:0;transform:translateY(20px) scale(.97)}to{opacity:1;transform:none}}
.modal-head{padding:20px 24px 16px;border-bottom:1px solid var(--hs-border2);display:flex;align-items:flex-start;gap:14px;position:relative}
.modal-icon{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,var(--hs-primary),var(--hs-violet));
  display:flex;align-items:center;justify-content:center;color:#001a08;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px -4px var(--hs-glow-soft)}
.modal-title{font-size:15px;font-weight:800;color:var(--hs-text);letter-spacing:-.01em}
.modal-sub{font-size:11.5px;color:var(--hs-dim);margin-top:3px}
.modal-close{position:absolute;left:16px;top:16px;width:30px;height:30px;border-radius:8px;background:transparent;
  border:1px solid transparent;color:var(--hs-dim);cursor:pointer;font-size:17px;display:flex;align-items:center;justify-content:center;transition:.2s}
.modal-close:hover{background:var(--hs-primary-d);color:var(--hs-text);border-color:var(--hs-border2)}
.modal-body{padding:20px 24px;overflow-y:auto;flex:1}
.modal-foot{padding:14px 24px;border-top:1px solid var(--hs-border2);display:flex;gap:8px;justify-content:flex-end}
.field{margin-bottom:14px}
.field label{display:block;font-size:11px;font-weight:700;color:var(--hs-mid);margin-bottom:7px;
  text-transform:uppercase;letter-spacing:.05em}
.field input,.field select,.field textarea{width:100%;padding:10px 13px;border-radius:9px;border:1px solid var(--hs-border2);
  background:rgba(0,0,0,.15);color:var(--hs-text);font-family:inherit;font-size:12.5px;outline:none;transition:.2s}
[data-theme="light"] .field input,[data-theme="light"] .field select,[data-theme="light"] .field textarea{background:rgba(0,130,65,.04)}
.field input:focus,.field select:focus,.field textarea:focus{border-color:var(--hs-primary);
  box-shadow:0 0 0 3px var(--hs-glow-soft);background:rgba(0,255,136,.05)}
.field input::placeholder,.field textarea::placeholder{color:var(--hs-dim)}
.field select option{background:var(--hs-card-solid);color:var(--hs-text)}
.server-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.server-card{background:var(--hs-card-solid);border:1px solid var(--hs-border2);border-radius:var(--hs-radius);
  padding:18px;cursor:pointer;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.server-card:hover{border-color:var(--hs-primary);transform:translateY(-3px);box-shadow:0 12px 30px -10px rgba(0,0,0,.3),0 0 30px -10px var(--hs-glow-soft)}
.server-card.protected{border-color:rgba(0,255,136,.35)}
.server-card.protected::after{content:'\F08DB';font-family:'tabler-icons';position:absolute;top:10px;left:10px;color:var(--hs-primary);font-size:14px;opacity:.6}
.server-card-header{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.server-icon{width:44px;height:44px;border-radius:12px;background:var(--hs-primary-d);color:var(--hs-primary);
  display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 0 15px var(--hs-glow-soft)}
.server-name{font-size:14px;font-weight:700;color:var(--hs-text);flex:1;min-width:0}
.server-meta{font-size:10.5px;color:var(--hs-dim);margin-top:2px}
.server-stats{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;padding-top:12px;border-top:1px solid var(--hs-border2)}
.server-stat{text-align:center}
.server-stat-val{font-size:16px;font-weight:800;color:var(--hs-text);font-family:'JetBrains Mono',monospace}
.server-stat-lbl{font-size:9.5px;color:var(--hs-dim);margin-top:2px}
.vps-config-item{background:rgba(0,0,0,.12);border:1px solid var(--hs-border2);border-radius:10px;padding:12px;margin-bottom:8px;display:flex;align-items:center;gap:10px;transition:.2s}
.vps-config-item:hover{border-color:var(--hs-border)}
.vps-config-info{flex:1;min-width:0}
.vps-config-name{font-size:12.5px;font-weight:600;color:var(--hs-text)}
.vps-config-details{font-size:10.5px;color:var(--hs-dim);margin-top:2px;font-family:'JetBrains Mono',monospace}
.vps-config-actions{display:flex;gap:4px;flex-shrink:0}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:56px;background:var(--hs-card-solid);
  border-bottom:1px solid var(--hs-border2);z-index:99;align-items:center;justify-content:space-between;padding:0 14px;backdrop-filter:blur(20px)}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-top svg{width:28px;height:28px;border-radius:8px}
.mob-top .t{font-size:13px;font-weight:700;color:var(--hs-text)}
.mob-btn{width:36px;height:36px;border-radius:9px;background:transparent;border:1px solid var(--hs-border2);
  color:var(--hs-mid);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:18px;transition:.2s}
.mob-btn:hover{background:var(--hs-primary-d);color:var(--hs-text)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:98;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.tg-badge{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;background:var(--hs-info-d);border:1px solid rgba(96,165,250,.25);border-radius:10px;color:var(--hs-info);font-size:12px;font-weight:600;font-family:'JetBrains Mono',monospace}
.socks-status{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px;margin-bottom:16px}
.socks-stat{background:rgba(0,0,0,.12);border:1px solid var(--hs-border2);border-radius:10px;padding:12px;text-align:center}
.socks-stat-val{font-size:18px;font-weight:800;color:var(--hs-primary);font-family:'JetBrains Mono',monospace}
.socks-stat-lbl{font-size:10px;color:var(--hs-dim);margin-top:4px}
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
  .server-grid{grid-template-columns:1fr}
}
@media(max-width:480px){.stats-grid{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){*{animation-duration:.001s!important;animation-iteration-count:1!important}}
</style>
</head>
<body>
<div class="app-bg"></div>
<div class="app">
  <div class="mob-top">
    <div class="ml">
      <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
        <defs><linearGradient id="ml" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00FF88"/><stop offset="1" stop-color="#00CC6A"/></linearGradient></defs>
        <rect x="2" y="2" width="28" height="28" rx="7" fill="url(#ml)"/>
        <path d="M9 16 L13 20 L22 10" stroke="#051A0B" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <span class="t">HS Panel</span>
    </div>
    <div style="display:flex;gap:6px">
      <button class="mob-btn" onclick="toggleTheme()" title="تم"><i class="ti" id="mob-theme-ic"></i></button>
      <button class="mob-btn" onclick="toggleSidebar()" title="منو"><i class="ti ti-menu-2"></i></button>
    </div>
  </div>
  <div class="overlay" id="overlay" onclick="closeSidebar()"></div>
  <aside class="sidebar" id="sidebar">
    <div class="sb-head">
      <button class="sb-toggle" onclick="toggleCollapse()" title="جمع کردن"><i class="ti ti-chevron-right" id="collapse-ic"></i></button>
      <div class="sb-logo">
        <div class="sb-logo-img">
          <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
            <defs><linearGradient id="sb1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00FF88"/><stop offset="1" stop-color="#00CC6A"/></linearGradient></defs>
            <rect x="2" y="2" width="28" height="28" rx="7" fill="url(#sb1)"/>
            <path d="M9 16 L13 20 L22 10" stroke="#051A0B" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="sb-logo-text">
          <div class="sb-logo-name">HS Panel</div>
          <div class="sb-logo-sub">v2.0</div>
        </div>
      </div>
    </div>
    <nav class="sb-body">
      <div class="sb-section-label">اصلی</div>
      <a class="sb-nav-item active" data-page="dashboard" onclick="nav('dashboard')"><i class="ti ti-layout-dashboard"></i><span class="sb-text">داشبورد</span></a>
      <a class="sb-nav-item" data-page="links" onclick="nav('links')"><i class="ti ti-link"></i><span class="sb-text">کانفیگ‌ها</span><span class="sb-badge" id="bdg-links">0</span></a>
      <a class="sb-nav-item" data-page="connections" onclick="nav('connections')"><i class="ti ti-activity"></i><span class="sb-text">اتصالات</span></a>
      <div class="sb-section-label">سرویس‌ها</div>
      <a class="sb-nav-item" data-page="gaming" onclick="nav('gaming')"><i class="ti ti-server-cog"></i><span class="sb-text">گیمینگ / VPS</span><span class="sb-badge" id="bdg-vps" style="display:none">0</span></a>
      <a class="sb-nav-item" data-page="socks" onclick="nav('socks')"><i class="ti ti-shield-lock"></i><span class="sb-text">SOCKS5</span><span class="sb-badge" id="bdg-socks" style="display:none">0</span></a>
      <div class="sb-section-label">ابزارها</div>
      <a class="sb-nav-item" data-page="nodes" onclick="nav('nodes')"><i class="ti ti-server-2"></i><span class="sb-text">نودها</span></a>
      <a class="sb-nav-item" data-page="telegram" onclick="nav('telegram')"><i class="ti ti-brand-telegram"></i><span class="sb-text">ربات تلگرام</span></a>
      <div class="sb-section-label">سیستم</div>
      <a class="sb-nav-item" data-page="settings" onclick="nav('settings')"><i class="ti ti-settings"></i><span class="sb-text">تنظیمات</span></a>
      <a class="sb-nav-item" data-page="update" onclick="nav('update')"><i class="ti ti-cloud-download"></i><span class="sb-text">بروزرسانی</span></a>
    </nav>
    <div class="sb-foot">
      <div class="sb-foot-info"><span class="dot"></span><span><b>سیستم فعال</b> · <span class="mono" id="uptime-mini">00:00:00</span></span></div>
    </div>
  </aside>
  <main class="main">
    <header class="topbar">
      <div class="tb-search">
        <i class="ti ti-search"></i>
        <input type="text" placeholder="جستجو...">
      </div>
      <div class="tb-actions">
        <button class="tb-btn" onclick="toggleTheme()" title="تغییر تم"><i class="ti" id="top-theme-ic"></i></button>
        <button class="tb-btn logout" onclick="logout()" title="خروج از حساب"><i class="ti ti-logout"></i></button>
        <button class="tb-btn" title="اعلان‌ها" onclick="showToast('اعلان جدیدی نیست','info')"><i class="ti ti-bell"></i><span class="dot-ind"></span></button>
        <div class="tb-user" onclick="logout()" title="خروج">
          <div class="tb-avatar">A</div>
          <span class="tb-user-name" id="tb-user-name">مدیر</span>
        </div>
      </div>
    </header>
    <div class="content">
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
              <button class="btn btn-ghost btn-sm" onclick="testAllLinks()" style="color:var(--hs-success);border-color:rgba(0,255,136,.25);background:rgba(0,255,136,.06)"><i class="ti ti-bolt"></i> تست همه</button>
              <button class="btn btn-ghost btn-sm" onclick="showCloudflareIPs()" style="color:var(--hs-primary2);border-color:rgba(0,200,110,.25);background:rgba(0,200,110,.06)"><i class="ti ti-world"></i> IP Static</button>
              <input type="text" id="links-search" placeholder="جستجو..." style="padding:7px 12px;border-radius:8px;border:1px solid var(--hs-border2);background:rgba(0,0,0,.15);color:var(--hs-text);font-family:inherit;font-size:12px;outline:none" oninput="filterLinks(this.value)">
            </div>
          </div>
          <div class="tbl-scroll">
            <table id="links-tbl">
              <thead><tr><th>نام</th><th>پروتکل</th><th>ترافیک</th><th>سهمیه</th><th>کشور/IP</th><th>وضعیت</th><th>پینگ</th><th>زمان</th><th>عملیات</th></tr></thead>
              <tbody><tr><td colspan="9" class="empty">در حال بارگذاری...</td></tr></tbody>
            </table>
          </div>
        </div>
      </div>
      
            <div class="page" id="page-connections">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-activity"></i> اتصالات فعال</h1><div class="page-sub">مانیتورینگ لحظه‌ای اتصالات به کانفیگ‌های شما</div></div>
          <div class="page-actions">
            <label style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--hs-mid);cursor:pointer"><input type="checkbox" id="conn-auto" checked onchange="toggleConnAuto()" style="accent-color:var(--hs-primary)"> به‌روزرسانی خودکار (۵ ثانیه)</label>
            <button class="btn btn-outline btn-sm" onclick="loadConnections()"><i class="ti ti-refresh"></i> بروزرسانی</button>
          </div>
        </div>
        <div class="stats-grid" style="grid-template-columns:repeat(3,1fr)">
          <div class="stat-card"><div class="stat-icon"><i class="ti ti-world"></i></div><div class="stat-label">آی‌پی متصل</div><div class="stat-value" id="stc-ips">0</div><div class="stat-trend">لحظه‌ای</div></div>
          <div class="stat-card"><div class="stat-icon green"><i class="ti ti-plug-connected"></i></div><div class="stat-label">اتصال فعال</div><div class="stat-value" id="stc-ses">0</div><div class="stat-trend">لحظه‌ای</div></div>
          <div class="stat-card"><div class="stat-icon amber"><i class="ti ti-arrows-exchange"></i></div><div class="stat-label">ترافیک اتصالات</div><div class="stat-value" id="stc-bytes">0 B</div><div class="stat-trend">مجموع</div></div>
        </div>
        <div class="tbl-wrap">
          <div class="tbl-head">
            <div class="tbl-title"><i class="ti ti-list"></i> لیست اتصالات</div>
          </div>
          <div class="tbl-scroll">
            <table id="conn-tbl">
              <thead><tr><th>IP</th><th>کانفیگ</th><th>پروتکل</th><th>اتصال</th><th>ترافیک</th><th>اولین اتصال</th><th>آخرین فعالیت</th></tr></thead>
              <tbody><tr><td colspan="7" class="empty">در حال بارگذاری...</td></tr></tbody>
            </table>
          </div>
        </div>
      </div>
            <div class="page" id="page-gaming">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-server-cog"></i> گیمینگ / VPS</h1><div class="page-sub">ثبت سرورهای VPS و ساخت کانفیگ‌های Xray-SOCKS برای هر سرور — سرورها دائمی ذخیره می‌شوند و با خروج از پنل پاک نمی‌شوند</div></div>
          <div class="page-actions">
            <button class="btn btn-outline btn-sm" onclick="loadVpsServers()"><i class="ti ti-refresh"></i> بروزرسانی</button>
            <button class="btn btn-primary btn-sm" onclick="openAddVpsModal()"><i class="ti ti-plus"></i> ثبت سرور جدید</button>
          </div>
        </div>
        <div id="vps-servers-list" class="server-grid"></div>
        <div id="vps-detail" style="display:none;margin-top:18px">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px">
            <button class="btn btn-outline btn-sm" onclick="backToVpsList()"><i class="ti ti-arrow-right"></i> بازگشت</button>
            <h2 id="vps-detail-title" style="font-size:18px;font-weight:800;color:var(--hs-text)"></h2>
          </div>
          <div class="card" style="margin-bottom:14px">
            <div class="card-title"><i class="ti ti-info-circle"></i> اطلاعات سرور</div>
            <div id="vps-detail-info" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;font-size:12.5px"></div>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px">
            <h3 style="font-size:14px;font-weight:700;color:var(--hs-text)">کانفیگ‌های این سرور <span style="font-size:11px;color:var(--hs-dim);font-weight:400">— JSON را کپی کنید و روی سرور با Xray اجرا کنید</span></h3>
            <button class="btn btn-primary btn-sm" onclick="openGenCfgModal('vps')"><i class="ti ti-plus"></i> کانفیگ جدید</button>
          </div>
          <div class="tbl-wrap">
            <div class="tbl-scroll">
              <table id="vps-cfg-tbl">
                <thead><tr><th>نام</th><th>کانفیگ مبنا</th><th>SOCKS</th><th>ترافیک</th><th>سهمیه</th><th>وضعیت</th><th>پینگ</th><th>زمان</th><th>عملیات</th></tr></thead>
                <tbody id="vps-cfg-tbody"><tr><td colspan="9" class="empty">در حال بارگذاری...</td></tr></tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
            <div class="page" id="page-socks">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-shield-lock"></i> SOCKS5</h1><div class="page-sub">ساخت کانفیگ Xray با پورت SOCKS5 که از روی یکی از کانفیگ‌های VLESS شما تونل می‌زند — JSON را کپی و روی سرور خود اجرا کنید</div></div>
          <div class="page-actions">
            <button class="btn btn-outline btn-sm" onclick="loadSocksList()"><i class="ti ti-refresh"></i> بروزرسانی</button>
            <button class="btn btn-primary btn-sm" onclick="openGenCfgModal('socks')"><i class="ti ti-plus"></i> کانفیگ SOCKS جدید</button>
          </div>
        </div>
        <div class="tbl-wrap">
          <div class="tbl-head">
            <div class="tbl-title"><i class="ti ti-list"></i> کانفیگ‌های SOCKS5</div>
          </div>
          <div class="tbl-scroll">
            <table id="socks-tbl">
              <thead><tr><th>نام</th><th>کانفیگ مبنا</th><th>SOCKS</th><th>ترافیک</th><th>سهمیه</th><th>وضعیت</th><th>پینگ</th><th>زمان</th><th>عملیات</th></tr></thead>
              <tbody id="socks-tbody"><tr><td colspan="9" class="empty">در حال بارگذاری...</td></tr></tbody>
            </table>
          </div>
        </div>
      </div>
      
      <div class="page" id="page-nodes">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-server-2"></i> نودها</h1><div class="page-sub">مدیریت نودهای متصل</div></div>
        </div>
        <div class="card"><div class="empty"><i class="ti ti-server"></i><div class="empty-title">نودها</div><div class="empty-sub">این بخش در حال توسعه است</div></div></div>
      </div>
      <div class="page" id="page-telegram">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-brand-telegram"></i> ربات تلگرام</h1><div class="page-sub">تنظیمات ربات و پشتیبانی</div></div>
        </div>
        <div class="card" style="max-width:520px">
          <div class="card-title"><i class="ti ti-brand-telegram"></i> ربات پشتیبانی</div>
          <div style="text-align:center;padding:20px 0">
            <div style="width:72px;height:72px;border-radius:20px;background:linear-gradient(135deg,var(--hs-primary),var(--hs-violet));display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:34px;color:#001a08;box-shadow:0 10px 30px -8px var(--hs-glow)"><i class="ti ti-brand-telegram"></i></div>
            <div style="font-size:15px;font-weight:700;color:var(--hs-text);margin-bottom:6px">@pinginoo-bot</div>
            <div style="font-size:12px;color:var(--hs-dim);margin-bottom:20px;line-height:1.8">ربات رسمی پینگینو برای اطلاع‌رسانی وضعیت سرور، پشتیبانی و دریافت کانفیگ</div>
            <a href="https://t.me/pinginoo-bot" target="_blank" rel="noopener" class="btn btn-primary" style="width:auto;display:inline-flex"><i class="ti ti-brand-telegram"></i> ورود به ربات</a>
          </div>
        </div>
      </div>
      
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
        <div class="card" style="max-width:520px;margin-top:14px" id="account-card">
          <div class="card-title"><i class="ti ti-user-circle"></i> حساب کاربری</div>
          <div style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(0,0,0,.12);border:1px solid var(--hs-border2);border-radius:12px">
            <div class="tb-avatar" id="acct-avatar" style="width:40px;height:40px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:15px;background:linear-gradient(135deg,var(--hs-primary),var(--hs-violet));color:#001a08">؟</div>
            <div style="flex:1;min-width:0">
              <div style="font-size:13.5px;font-weight:700;direction:ltr;text-align:right" id="acct-username">—</div>
              <div style="font-size:11px;color:var(--hs-dim);margin-top:3px" id="acct-role">در حال بارگذاری...</div>
            </div>
            <span class="badge badge-green badge-dot" style="display:none" id="acct-badge">پنل شما</span>
          </div>
          <div style="font-size:11px;color:var(--hs-dim);margin-top:12px;line-height:1.9">
            پنل هر کاربر کاملاً مستقل است؛ کانفیگ‌ها، سرورهای VPS و کانفیگ‌های SOCKS فقط برای همان حساب ثبت‌شده قابل مشاهده و ویرایش هستند.
          </div>
        </div>
      </div>
      <div class="page" id="page-update">
        <div class="page-head">
          <div><h1 class="page-title"><i class="ti ti-cloud-download"></i> بروزرسانی</h1><div class="page-sub">بررسی و نصب نسخه جدید</div></div>
        </div>
        <div class="card" id="update-card"><div class="empty"><i class="ti ti-cloud-check"></i><div class="empty-title">بروزرسانی</div><div class="empty-sub">برای بررسی نسخه جدید روی دکمه زیر بزنید</div></div>
          <div style="display:flex;gap:8px;justify-content:center;margin-top:10px"><button class="btn btn-primary" onclick="checkVersion()"><i class="ti ti-refresh"></i> بررسی نسخه</button></div>
        </div>
      </div>
    </div>
  </main>
</div>
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
          <select id="cl-ipver"><option value="ipv4">IPv4</option><option value="ipv6">IPv6</option></select>
        </div>
        <div class="field"><label>پورت (fallback)</label>
          <select id="cl-port">
            <option value="443">443 (HTTPS)</option>
            <option value="8443">8443</option>
            <option value="2053">2053 (Cloudflare)</option>
            <option value="2083">2083</option>
            <option value="2087">2087</option>
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
            <option value="US">🇺🇸 US</option><option value="DE">🇩🇪 DE</option><option value="FR">🇫🇷 FR</option>
            <option value="GB">🇬🇧 GB</option><option value="NL">🇳🇱 NL</option><option value="TR">🇹🇷 TR</option>
            <option value="JP">🇯🇵 JP</option><option value="SG">🇸🇬 SG</option>
          </select>
        </div>
        <div class="field"><label>IP Static</label>
          <select id="el-static-ip"><option value="">خودکار</option></select>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>IP Version</label><select id="el-ipver"><option value="ipv4">IPv4</option><option value="ipv6">IPv6</option></select></div>
        <div class="field"><label>پورت</label>
          <select id="el-port"><option value="443">443</option><option value="8443">8443</option><option value="2053">2053</option><option value="2083">2083</option></select>
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
<div class="modal-bg" id="modal-gen-cfg">
  <div class="modal">
    <div class="modal-head">
      <div class="modal-icon"><i class="ti ti-file-plus"></i></div>
      <div><div class="modal-title" id="gcfg-title">کانفیگ جدید</div><div class="modal-sub" id="gcfg-sub">از روی کانفیگ VLESS، کانفیگ Xray با پورت SOCKS5 ساخته می‌شود</div></div>
      <button class="modal-close" onclick="closeModal('modal-gen-cfg')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <input type="hidden" id="gc-kind">
      <input type="hidden" id="gc-cid">
      <div class="field"><label>نام کانفیگ</label><input type="text" id="gc-name" placeholder="مثلاً: کاربر 1"></div>
      <div class="field"><label>کانفیگ مبنا (خروجی VLESS)</label>
        <select id="gc-base"><option value="">در حال بارگذاری...</option></select>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>پورت SOCKS</label><input type="number" id="gc-port" value="10808" class="ltr" dir="ltr"></div>
        <div class="field"><label>آدرس Listen</label>
          <select id="gc-listen"><option value="127.0.0.1">127.0.0.1 (محلی)</option><option value="0.0.0.0">0.0.0.0 (عمومی)</option></select>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 80px;gap:10px">
        <div class="field"><label>سهمیه ترافیک</label><input type="number" id="gc-val" min="0" placeholder="0 = نامحدود"></div>
        <div class="field"><label>واحد</label><select id="gc-unit"><option>GB</option><option>MB</option></select></div>
      </div>
      <div class="field"><label>مدت اعتبار (روز)</label><input type="number" id="gc-exp" min="0" placeholder="0 = نامحدود / خالی = بدون تغییر"></div>
      <div class="field"><label>یادداشت</label><textarea id="gc-note" rows="2" placeholder="اختیاری"></textarea></div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-gen-cfg')">انصراف</button>
      <button class="btn btn-primary" onclick="saveGenCfg()"><i class="ti ti-check"></i> ذخیره</button>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-add-vps">
  <div class="modal">
    <div class="modal-head">
      <div class="modal-icon"><i class="ti ti-server-plus"></i></div>
      <div><div class="modal-title">ثبت سرور VPS جدید</div><div class="modal-sub">اطلاعات سرور خود را وارد کنید</div></div>
      <button class="modal-close" onclick="closeModal('modal-add-vps')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="field"><label>نام سرور</label><input type="text" id="vps-name" placeholder="مثلاً: سرور آلمان"></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>IP / Hostname</label><input type="text" id="vps-host" class="ltr" placeholder="1.2.3.4" dir="ltr"></div>
        <div class="field"><label>پورت SSH</label><input type="number" id="vps-port" value="22" class="ltr" dir="ltr"></div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>نام کاربری</label><input type="text" id="vps-user" class="ltr" value="root" dir="ltr"></div>
        <div class="field"><label>رمز عبور / کلید</label><input type="password" id="vps-pass" dir="ltr"></div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
        <div class="field"><label>کشور</label>
          <select id="vps-country">
            <option value="DE">🇩🇪 آلمان</option><option value="US">🇺🇸 آمریکا</option><option value="FR">🇫🇷 فرانسه</option>
            <option value="GB">🇬🇧 انگلیس</option><option value="NL">🇳🇱 هلند</option><option value="TR">🇹🇷 ترکیه</option>
            <option value="AE">🇦🇪 امارات</option><option value="JP">🇯🇵 ژاپن</option><option value="SG">🇸🇬 سنگاپور</option>
            <option value="other">🌐 سایر</option>
          </select>
        </div>
        <div class="field"><label>نوع سرور</label>
          <select id="vps-type">
            <option value="kvm">KVM</option><option value="openvz">OpenVZ</option><option value="dedicated">Dedicated</option><option value="cloud">Cloud</option>
          </select>
        </div>
      </div>
      <div class="field"><label>یادداشت</label><textarea id="vps-note" rows="2" placeholder="اختیاری"></textarea></div>
      <div style="font-size:11px;color:var(--hs-dim);line-height:1.8;padding:10px;background:rgba(0,255,136,.05);border:1px solid var(--hs-border2);border-radius:8px">
        <i class="ti ti-info-circle" style="color:var(--hs-primary);margin-left:6px"></i>
        سرورها پس از ثبت در پنل شما ذخیره می‌شوند و با خروج از پنل حذف نمی‌شوند.
      </div>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-add-vps')">انصراف</button>
      <button class="btn btn-primary" onclick="saveVpsServer()"><i class="ti ti-check"></i> ثبت سرور</button>
    </div>
  </div>
</div><div class="modal-bg" id="modal-xray-view">
  <div class="modal" style="max-width:720px">
    <div class="modal-head">
      <div class="modal-icon"><i class="ti ti-code"></i></div>
      <div><div class="modal-title" id="xv-title">کانفیگ Xray</div><div class="modal-sub">این JSON را کپی کرده و روی سرور با Xray اجرا کنید</div></div>
      <button class="modal-close" onclick="closeModal('modal-xray-view')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <pre id="xv-json" style="direction:ltr;text-align:left;font-family:'JetBrains Mono',monospace;font-size:11.5px;line-height:1.6;background:rgba(0,0,0,.25);border:1px solid var(--hs-border2);border-radius:10px;padding:14px;max-height:52vh;overflow:auto;white-space:pre;color:var(--hs-primary)"></pre>
    </div>
    <div class="modal-foot">
      <button class="btn btn-outline" onclick="closeModal('modal-xray-view')">بستن</button>
      <button class="btn btn-primary" id="xv-copy"><i class="ti ti-copy"></i> کپی JSON</button>
    </div>
  </div>
</div>

<div class="toast-host" id="toast-host"></div>
<script>
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
let linkPingCache = {};
try{ linkPingCache = JSON.parse(localStorage.getItem('hs-ping-cache') || '{}'); }catch(e){ linkPingCache = {}; }
function savePingCache(){ try{ localStorage.setItem('hs-ping-cache', JSON.stringify(linkPingCache)); }catch(e){} }
function nav(page){
  document.querySelectorAll('.sb-nav-item').forEach(n => n.classList.toggle('active', n.dataset.page === page));
  document.querySelectorAll('.page').forEach(p => p.classList.toggle('active', p.id === 'page-' + page));
  closeSidebar();
  window.scrollTo({top:0,behavior:'smooth'});
  if(page === 'gaming'){ loadVpsServers(); }
  if(page === 'socks'){ loadSocksList(); }
  if(page === 'connections'){ loadConnections(); startConnTimer(); }
}
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
function openModal(id){
  document.getElementById(id).classList.add('open');
  if(id === 'modal-create-link'){ populateStaticIPSelect(); }
}
function closeModal(id){ document.getElementById(id).classList.remove('open'); }
document.querySelectorAll('.modal-bg').forEach(m => m.addEventListener('click', e => { if(e.target === m) m.classList.remove('open'); }));
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
async function logout(){
  try{ await fetch('/api/logout', {method:'POST'}); }catch(e){}
  window.location.href = '/login';
}
const _rawFetch = window.fetch.bind(window);
window.fetch = async function(url, opts){
  const r = await _rawFetch(url, opts);
  if(r.status === 401 && typeof url === 'string' && url.startsWith('/') && !url.startsWith('/api/login')){
    window.location.href = '/login';
    throw new Error('unauthorized');
  }
  return r;
};
async function authFetch(url, opts){
  const r = await fetch(url, opts);
  if(r.status === 401){ window.location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}
async function loadStats(){
  try{
    const r = await authFetch('/stats');
    if(!r.ok) throw new Error();
    const d = await r.json();
    document.getElementById('st-links').textContent = d.links_count || 0;
    document.getElementById('st-active-links').textContent = d.active_links || 0;
    document.getElementById('st-conn').textContent = d.active_connections || 0;
    document.getElementById('st-bytes').textContent = d.total_traffic_mb || 0;
    document.getElementById('st-uptime').textContent = d.uptime || '00:00:00';
    document.getElementById('uptime-mini').textContent = d.uptime || '00:00:00';
    document.getElementById('bdg-links').textContent = d.links_count || 0;
    const ss = document.getElementById('system-status');
    ss.innerHTML = '<div style="display:flex;align-items:center;gap:10px;padding:8px 0"><span class="badge badge-green badge-dot">آنلاین</span><span style="font-size:12px;color:var(--hs-dim)">سیستم فعال است</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid var(--hs-border2);font-size:12px"><span style="color:var(--hs-dim)">کانفیگ‌های منقضی</span><span style="font-weight:600">' + (d.expired_links||0) + '</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid var(--hs-border2);font-size:12px"><span style="color:var(--hs-dim)">سرورهای VPS</span><span style="font-weight:600">' + (d.vps_count||0) + '</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid var(--hs-border2);font-size:12px"><span style="color:var(--hs-dim)">کانفیگ‌های SOCKS</span><span style="font-weight:600">' + (d.socks_count||0) + '</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid var(--hs-border2);font-size:12px"><span style="color:var(--hs-dim)">کل درخواست‌ها</span><span style="font-weight:600">' + (d.total_requests||0) + '</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid var(--hs-border2);font-size:12px"><span style="color:var(--hs-dim)">ربات تلگرام</span><span class="tg-badge" style="font-size:10px;padding:3px 8px">@pinginoo-bot</span></div>';
  }catch(e){ showToast('خطا در بارگذاری آمار','error'); }
}
async function loadActivity(){
  try{
    const r = await authFetch('/api/activity');
    if(!r.ok) throw new Error();
    const d = await r.json();
    const logs = d.logs || [];
    const feed = document.getElementById('activity-feed');
    if(!logs.length){ feed.innerHTML = '<div class="empty" style="padding:30px 10px"><i class="ti ti-history"></i><div>فعالیتی ثبت نشده</div></div>'; return; }
    feed.innerHTML = logs.slice(-12).reverse().map(l => {
      const ic = l.level==='err' ? 'ti-alert-circle' : l.level==='warn' ? 'ti-alert-triangle' : l.level==='ok' ? 'ti-circle-check' : 'ti-info-circle';
      const cl = l.level==='err' ? 'danger' : l.level==='warn' ? 'warn' : l.level==='ok' ? 'success' : 'info';
      return '<div style="display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:9px;background:rgba(0,0,0,.12)"><i class="ti ' + ic + '" style="color:var(--hs-' + cl + ');font-size:15px;flex-shrink:0"></i><div style="flex:1;min-width:0;font-size:12px;color:var(--hs-text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + (l.message||'') + '</div><div style="font-size:10.5px;color:var(--hs-dim);white-space:nowrap">' + (l.time||'').substring(11,16) + '</div></div>';
    }).join('');
  }catch(e){}
}
function pingBadgeHtml(uid){
  const cached = linkPingCache[uid];
  if(cached != null){
    let cls = '';
    if(cached > 200) cls = 'bad';
    else if(cached > 100) cls = 'warn';
    return '<span class="ping-badge ' + cls + '" id="ping-' + uid + '">' + cached + 'ms</span>';
  }
  return '<span class="ping-badge testing" id="ping-' + uid + '" style="cursor:pointer" onclick="runPingTest(\'' + uid + '\')"><i class="ti ti-bolt" style="font-size:12px"></i></span>';
}
function updatePingDisplay(uid, ms){
  linkPingCache[uid] = ms;
  savePingCache();
  const el = document.getElementById('ping-' + uid);
  if(!el) return;
  let cls = '';
  if(ms > 200) cls = 'bad';
  else if(ms > 100) cls = 'warn';
  el.className = 'ping-badge ' + cls;
  el.textContent = ms + 'ms';
  el.style.cursor = 'pointer';
  el.onclick = () => runPingTest(uid);
}
async function loadLinks(){
  try{
    const r = await authFetch('/api/links');
    if(!r.ok) throw new Error();
    const d = await r.json();
    const rows = document.querySelector('#links-tbl tbody');
    const links = d.links || [];
    document.getElementById('bdg-links').textContent = links.length;
    if(!links.length){ rows.innerHTML = '<tr><td colspan="9"><div class="empty"><i class="ti ti-link-off"></i><div class="empty-title">کانفیگی نیست</div><div class="empty-sub">اولین کانفیگ خود را بسازید</div></div></td></tr>'; return; }
    rows.innerHTML = links.map(l => {
      const used = (l.used_bytes||0);
      const lim = (l.limit_bytes||0);
      const pct = lim > 0 ? Math.min(100, (used/lim*100)) : 0;
      const subLine = l.static_ip || (l.uuid ? l.uuid.substring(0,8) : '—');
      return '<tr data-label="' + (l.label||'').toLowerCase() + '"><td><div class="cell-label">' + (l.label||'—') + '</div><div class="cell-mono">' + subLine + '</div></td>' +
        '<td><span class="badge badge-purple">' + (l.protocol||'') + '</span></td>' +
        '<td><div class="cell-mono">' + fmtBytes(used) + '</div>' + (lim>0 ? '<div style="height:3px;background:var(--hs-border2);border-radius:2px;margin-top:4px;overflow:hidden"><div style="height:100%;width:' + pct + '%;background:linear-gradient(90deg,var(--hs-primary),var(--hs-violet))"></div></div>' : '') + '</td>' +
        '<td><span class="cell-mono">' + (lim>0 ? fmtBytes(lim) : '∞') + '</span></td>' +
        '<td><div style="font-size:11px"><div>' + (l.country && l.country!=='auto' ? l.country : '🌐 Auto') + ' · :' + (l.port||443) + '</div>' + (l.static_ip ? '<div style="color:var(--hs-primary);font-family:monospace">' + l.static_ip + '</div>' : '<div style="color:var(--hs-dim);font-size:10px">' + (l.ip_version==='ipv6' ? 'IPv6' : 'IPv4') + '</div>') + '</div></td>' +
        '<td>' + (l.expired ? '<span class="badge badge-red badge-dot">منقضی</span>' : l.active===false ? '<span class="badge badge-amber badge-dot">غیرفعال</span>' : '<span class="badge badge-green badge-dot">فعال</span>') + '</td>' +
        '<td>' + pingBadgeHtml(l.uuid) + '</td>' +
        '<td><div class="cell-mono" style="font-size:11px">' + (l.expires_at ? formatExpiry(l.expires_at) : '<span style="color:var(--hs-dim)">∞</span>') + '</div></td>' +
        '<td><div style="display:flex;gap:4px"><button class="btn btn-ghost btn-sm" onclick="copyLink(\'' + l.uuid + '\')" title="کپی"><i class="ti ti-copy"></i></button><button class="btn btn-ghost btn-sm" onclick="editLink(\'' + l.uuid + '\')" title="ویرایش"><i class="ti ti-edit"></i></button><button class="btn btn-ghost btn-sm" onclick="toggleLink(\'' + l.uuid + '\',' + (l.active!==false) + ')" title="تغییر وضعیت"><i class="ti ti-power"></i></button><button class="btn btn-danger btn-sm" onclick="deleteLink(\'' + l.uuid + '\')" title="حذف"><i class="ti ti-trash"></i></button></div></td></tr>';
    }).join('');
    links.forEach(l => { pingTestHandlers[l.uuid] = () => testLink(l.uuid, true); });
  }catch(e){ showToast('خطا در بارگذاری کانفیگ‌ها','error'); }
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
function formatExpiry(iso){
  try{
    const dt = new Date(iso);
    const now = new Date();
    const diff = dt - now;
    if(diff < 0) return '<span style="color:var(--hs-danger)">منقضی</span>';
    const d = Math.floor(diff / 86400000);
    const h = Math.floor((diff % 86400000) / 3600000);
    const col = d < 3 ? 'var(--hs-warn)' : 'var(--hs-text)';
    return '<span style="color:' + col + '">' + d + ' روز ' + h + 'س</span>';
  }catch(e){ return '—'; }
}
async function createLink(){
  const country = document.getElementById('cl-country').value || 'auto';
  let staticIp = document.getElementById('cl-static-ip').value || '';
  if(!staticIp && country !== 'auto'){
    try{ const r = await fetch('/api/cloudflare-ips/speedtest?country=' + country); const d = await r.json(); if(d.fastest) staticIp = d.fastest; }catch(e){}
  }else if(!staticIp){
    try{ const r = await fetch('/api/cloudflare-ips/speedtest'); const d = await r.json(); if(d.fastest) staticIp = d.fastest; }catch(e){}
  }
  const body = {
    label: document.getElementById('cl-label').value || 'لینک جدید',
    protocol: document.getElementById('cl-proto').value,
    limit_value: parseFloat(document.getElementById('cl-val').value) || 0,
    limit_unit: document.getElementById('cl-unit').value,
    expires_days: parseInt(document.getElementById('cl-exp').value) || 0,
    note: document.getElementById('cl-note').value || '',
    country: country, static_ip: staticIp,
    ip_version: document.getElementById('cl-ipver').value || 'ipv4',
    port: parseInt(document.getElementById('cl-port').value) || 443,
  };
  try{
    const r = await fetch('/api/links', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)});
    if(!r.ok){ const e = await r.json().catch(()=>({})); throw new Error(e.detail || 'خطا'); }
    closeModal('modal-create-link');
    showToast('کانفیگ با موفقیت ساخته شد','success');
    loadLinks(); loadStats();
  }catch(e){ showToast(e.message,'error'); }
}
async function copyLink(uid){
  try{
    const r = await fetch('/api/links');
    const d = await r.json();
    const l = (d.links||[]).find(x => x.uuid === uid);
    if(l && l.vless_link){ navigator.clipboard.writeText(l.vless_link); showToast('لینک کپی شد','success'); }
  }catch(e){ showToast('خطا در کپی','error'); }
}
async function testAllLinks(){
  showToast('⏳ در حال تست همه کانفیگ‌ها...','info',2000);
  try{
    const r = await fetch('/api/links');
    const d = await r.json();
    const links = d.links || [];
    if(!links.length){ showToast('کانفیگی نیست','warn'); return; }
    let ok=0, fail=0;
    links.forEach(l => {
      const el = document.getElementById('ping-' + l.uuid);
      if(el){ el.className = 'ping-badge testing'; el.innerHTML = '<i class="ti ti-loader" style="font-size:11px;animation:spin 1s linear infinite"></i>'; }
    });
    for(const l of links){
      try{
        const tr = await fetch('/api/links/' + l.uuid + '/test');
        const td = await tr.json();
        if(tr.ok && td.total_ms != null){ updatePingDisplay(l.uuid, td.total_ms); ok++; }
        else{ fail++; updatePingDisplay(l.uuid, 999); }
      }catch(e){ fail++; updatePingDisplay(l.uuid, 999); }
    }
    showToast('✅ ' + ok + ' کانفیگ تست شد · ' + (fail ? '❌ ' + fail + ' مشکل دارد' : ''),'info',5000);
  }catch(e){ showToast('خطا','error'); }
}
async function testLink(uid, fromPing){
  const el = document.getElementById('ping-' + uid);
  if(el){ el.className = 'ping-badge testing'; el.innerHTML = '<i class="ti ti-loader" style="font-size:11px;animation:spin 1s linear infinite"></i>'; }
  try{
    const r = await fetch('/api/links/' + uid + '/test');
    const d = await r.json();
    if(d.ok && d.total_ms != null){
      updatePingDisplay(uid, d.total_ms);
      if(!fromPing) showToast('پینگ: ' + d.total_ms + 'ms','success',2000);
    }else{
      updatePingDisplay(uid, 999);
      if(!fromPing) showToast('خطا در اتصال','error',3000);
    }
  }catch(e){
    updatePingDisplay(uid, 999);
    if(!fromPing) showToast('خطا در تست','error');
  }
}
async function showCloudflareIPs(){
  showToast('در حال بارگذاری IP ها...','info',1000);
  try{
    const r = await fetch('/api/cloudflare-ips');
    const d = await r.json();
    populateStaticIPSelect(d);
    let html = '<div style="text-align:right;direction:rtl;min-width:320px;max-height:400px;overflow-y:auto">';
    html += '<div style="font-weight:600;margin-bottom:8px;color:var(--hs-primary)"><i class="ti ti-world"></i> IP های Static</div>';
    const byCountry = d.by_country || {};
    Object.keys(byCountry).forEach(code => {
      const grp = byCountry[code];
      html += '<div style="margin-top:8px;padding:4px 8px;background:rgba(0,255,136,.10);border-radius:6px;font-weight:700;color:var(--hs-primary2);font-size:12px;display:inline-block">' + grp.name + '</div>';
      html += '<div style="display:grid;grid-template-columns:1fr 1fr;gap:5px;font-family:monospace;font-size:11px;margin-top:4px">';
      grp.ips.forEach(item => {
        html += '<div style="padding:6px 8px;background:rgba(0,255,136,.06);border:1px solid rgba(0,255,136,.15);border-radius:6px;cursor:pointer" onclick="navigator.clipboard.writeText(\'' + item.ip + '\');showToast(\'کپی شد: ' + item.ip + '\',\'success\',1500)"><div style="color:var(--hs-primary2);font-weight:600">' + item.ip + '</div><div style="font-size:9px;color:var(--hs-dim);margin-top:1px">' + item.city + '</div></div>';
      });
      html += '</div>';
    });
    html += '</div>';
    showToast(html, 'info', 25000);
  }catch(e){ showToast('خطا: ' + e.message,'error'); }
}
async function populateStaticIPSelect(preloaded){
  try{
    const d = preloaded || await (await fetch('/api/cloudflare-ips')).json();
    const sel = document.getElementById('cl-static-ip');
    if(!sel) return;
    const selCountry = document.getElementById('cl-country');
    const currentCountry = selCountry ? selCountry.value : 'auto';
    sel.innerHTML = '<option value="">⚡ خودکار</option>';
    d.ips.forEach(item => {
      if(currentCountry === 'auto' || item.country === currentCountry){
        const opt = document.createElement('option');
        opt.value = item.ip; opt.textContent = item.ip + ' (' + item.city + ')';
        sel.appendChild(opt);
      }
    });
  }catch(e){}
}
let _editIPCache = null;
async function populateEditStaticIP(){
  try{
    if(!_editIPCache) _editIPCache = await (await fetch('/api/cloudflare-ips')).json();
    const d = _editIPCache;
    const sel = document.getElementById('el-static-ip');
    if(!sel) return;
    const currentRegion = document.getElementById('el-country') ? document.getElementById('el-country').value : 'auto';
    const currentVal = sel.dataset.current || '';
    sel.innerHTML = '<option value="">خودکار</option>';
    d.ips.forEach(item => {
      if(currentRegion === 'auto' || item.country === currentRegion){
        const opt = document.createElement('option');
        opt.value = item.ip; opt.textContent = item.ip + ' (' + item.city + ')';
        if(item.ip === currentVal) opt.selected = true;
        sel.appendChild(opt);
      }
    });
  }catch(e){}
}
async function editLink(uid){
  try{
    const r = await fetch('/api/links');
    const d = await r.json();
    const l = (d.links||[]).find(x => x.uuid === uid);
    if(!l){ showToast('کانفیگ پیدا نشد','error'); return; }
    document.getElementById('el-uid').value = uid;
    document.getElementById('el-label').value = l.label || '';
    document.getElementById('el-country').value = l.country || 'auto';
    document.getElementById('el-ipver').value = l.ip_version || 'ipv4';
    document.getElementById('el-port').value = l.port || 443;
    const lb = l.limit_bytes || 0;
    if(lb > 0){
      if(lb >= 1024*1024*1024){ document.getElementById('el-val').value = (lb/1024/1024/1024).toFixed(2); document.getElementById('el-unit').value = 'GB'; }
      else{ document.getElementById('el-val').value = (lb/1024/1024).toFixed(2); document.getElementById('el-unit').value = 'MB'; }
    }else{ document.getElementById('el-val').value = 0; document.getElementById('el-unit').value = 'GB'; }
    document.getElementById('el-exp').value = '';
    document.getElementById('el-exp-orig').value = l.expires_at || '';
    document.getElementById('el-note').value = l.note || '';
    document.getElementById('el-static-ip').dataset.current = l.static_ip || '';
    await populateEditStaticIP();
    openModal('modal-edit-link');
  }catch(e){ showToast('خطا: ' + e.message,'error'); }
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
  if(expVal !== '' && expVal !== null) body.expires_days = parseInt(expVal) || 0;
  try{
    const r = await fetch('/api/links/' + uid, {method:'PATCH', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)});
    if(!r.ok){ const e = await r.json().catch(()=>({})); throw new Error(e.detail || 'خطا'); }
    closeModal('modal-edit-link');
    showToast('کانفیگ ویرایش شد','success');
    loadLinks(); loadStats();
  }catch(e){ showToast(e.message,'error'); }
}
async function toggleLink(uid, currentActive){
  try{
    await fetch('/api/links/' + uid, {method:'PATCH', headers:{'Content-Type':'application/json'}, body: JSON.stringify({active: !currentActive})});
    showToast('وضعیت تغییر کرد','success');
    loadLinks();
  }catch(e){ showToast('خطا','error'); }
}
async function deleteLink(uid){
  if(!confirm('حذف شود؟')) return;
  try{
    await fetch('/api/links/' + uid, {method:'DELETE'});
    delete linkPingCache[uid];
    showToast('حذف شد','success');
    loadLinks(); loadStats();
  }catch(e){ showToast('خطا','error'); }
}
async function changePw(){
  const cur = document.getElementById('set-cur-pw').value;
  const nw = document.getElementById('set-new-pw').value;
  if(!cur || !nw){ showToast('همه فیلدها را پر کنید','warn'); return; }
  if(nw.length < 6){ showToast('رمز جدید حداقل ۶ کاراکتر','warn'); return; }
  try{
    const r = await fetch('/api/change-password', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({current_password: cur, new_password: nw})});
    if(!r.ok){ const e = await r.json().catch(()=>({})); throw new Error(e.detail || 'خطا'); }
    showToast('رمز تغییر کرد','success');
    document.getElementById('set-cur-pw').value = '';
    document.getElementById('set-new-pw').value = '';
  }catch(e){ showToast(e.message,'error'); }
}
let pingTestHandlers = {};
function runPingTest(key){ const h = pingTestHandlers[key]; if(h) h(); }
let vpsServers = [];
let currentVpsServerId = null;
let vpsCfgsCache = {};
let socksConfigs = [];
async function loadVpsServers(){
  try{
    const r = await authFetch('/api/vps');
    if(!r.ok) throw new Error();
    const d = await r.json();
    vpsServers = d.servers || [];
  }catch(e){ vpsServers = []; }
  const bdg = document.getElementById('bdg-vps');
  if(bdg){ bdg.textContent = vpsServers.length; bdg.style.display = vpsServers.length ? '' : 'none'; }
  renderVpsServers();
}
function renderVpsServers(){
  currentVpsServerId = null;
  document.getElementById('vps-detail').style.display = 'none';
  const list = document.getElementById('vps-servers-list');
  if(!list) return;
  if(!vpsServers.length){
    list.innerHTML = '<div class="card" style="grid-column:1/-1"><div class="empty"><i class="ti ti-server"></i><div class="empty-title">هنوز سروری ثبت نشده</div><div class="empty-sub">اولین سرور VPS خود را ثبت کنید — سرورها دائمی هستند و با خروج از پنل پاک نمی‌شوند</div></div></div>';
    return;
  }
  list.innerHTML = vpsServers.map(s => {
    const cc = s.configs_count || 0;
    return '<div class="server-card protected" onclick="openVpsServer(\'' + s.id + '\')">' +
      '<div style="position:absolute;top:10px;left:10px"><button class="btn btn-danger btn-icon btn-sm" onclick="event.stopPropagation();deleteVpsServer(\'' + s.id + '\',\'' + esc(s.name) + '\')" title="حذف سرور"><i class="ti ti-trash"></i></button></div>' +
      '<div class="server-card-header">' +
      '<div class="server-icon"><i class="ti ti-server"></i></div>' +
      '<div style="flex:1;min-width:0"><div class="server-name">' + esc(s.name) + '</div><div class="server-meta mono" style="direction:ltr;text-align:left">' + esc(s.host) + ':' + (s.port||22) + '</div></div>' +
      '<span class="badge badge-green badge-dot" style="flex-shrink:0"><i class="ti ti-lock" style="font-size:10px"></i> دائمی</span>' +
      '</div>' +
      '<div class="server-stats">' +
      '<div class="server-stat"><div class="server-stat-val">' + cc + '</div><div class="server-stat-lbl">کانفیگ</div></div>' +
      '<div class="server-stat"><div class="server-stat-val">' + (s.active_configs||0) + '</div><div class="server-stat-lbl">فعال</div></div>' +
      '<div class="server-stat"><div class="server-stat-val" style="font-size:13px">' + esc(s.country||'—') + '</div><div class="server-stat-lbl">کشور</div></div>' +
      '</div></div>';
  }).join('');
}
async function backToVpsList(){ await loadVpsServers(); }
async function openVpsServer(sid){
  currentVpsServerId = sid;
  try{
    const r = await authFetch('/api/vps/' + sid);
    if(!r.ok) throw new Error();
    const s = await r.json();
    vpsCfgsCache[sid] = s.configs || [];
    document.getElementById('vps-servers-list').innerHTML = '';
    document.getElementById('vps-detail').style.display = 'block';
    document.getElementById('vps-detail-title').textContent = s.name;
    document.getElementById('vps-detail-info').innerHTML =
      '<div><div style="font-size:10px;color:var(--hs-dim);text-transform:uppercase">IP / Host</div><div class="mono" style="font-size:13px;margin-top:4px;direction:ltr;text-align:left">' + esc(s.host) + '</div></div>' +
      '<div><div style="font-size:10px;color:var(--hs-dim);text-transform:uppercase">پورت SSH</div><div class="mono" style="font-size:13px;margin-top:4px">' + (s.port||22) + '</div></div>' +
      '<div><div style="font-size:10px;color:var(--hs-dim);text-transform:uppercase">کاربر</div><div class="mono" style="font-size:13px;margin-top:4px;direction:ltr;text-align:left">' + esc(s.user||'root') + '</div></div>' +
      '<div><div style="font-size:10px;color:var(--hs-dim);text-transform:uppercase">کشور</div><div style="font-size:13px;margin-top:4px">' + esc(s.country||'—') + '</div></div>' +
      '<div><div style="font-size:10px;color:var(--hs-dim);text-transform:uppercase">نوع</div><div style="font-size:13px;margin-top:4px">' + esc(s.type||'kvm') + '</div></div>' +
      '<div><div style="font-size:10px;color:var(--hs-dim);text-transform:uppercase">وضعیت</div><div style="font-size:13px;margin-top:4px"><span class="badge badge-green badge-dot"><i class="ti ti-lock" style="font-size:9px"></i> ذخیره دائمی</span></div></div>' +
      (s.note ? '<div style="grid-column:1/-1"><div style="font-size:10px;color:var(--hs-dim);text-transform:uppercase">یادداشت</div><div style="font-size:12px;margin-top:4px;color:var(--hs-mid)">' + esc(s.note) + '</div></div>' : '');
    renderVpsCfgTable();
    window.scrollTo({top:0,behavior:'smooth'});
  }catch(e){ showToast('خطا در بارگذاری سرور','error'); }
}
function renderVpsCfgTable(){
  const tb = document.getElementById('vps-cfg-tbody');
  if(!tb) return;
  const cfgs = (currentVpsServerId && vpsCfgsCache[currentVpsServerId]) || [];
  cfgs.forEach(c => { pingTestHandlers['vps:' + currentVpsServerId + ':' + c.id] = () => testGenPing(currentVpsServerId, c.id); });
  if(!cfgs.length){ tb.innerHTML = '<tr><td colspan="9"><div class="empty"><i class="ti ti-file-plus"></i><div class="empty-title">کانفیگی نیست</div><div class="empty-sub">اولین کانفیگ این سرور را بسازید</div></div></td></tr>'; return; }
  tb.innerHTML = cfgs.map(c => genCfgRowHtml('vps', c)).join('');
}
function openAddVpsModal(){
  ['vps-name','vps-host','vps-pass','vps-note'].forEach(id => { const el = document.getElementById(id); if(el) el.value = ''; });
  openModal('modal-add-vps');
}
async function saveVpsServer(){
  const name = document.getElementById('vps-name').value.trim();
  const host = document.getElementById('vps-host').value.trim();
  if(!name || !host){ showToast('نام و IP را وارد کنید','warn'); return; }
  const body = {
    name: name, host: host,
    port: parseInt(document.getElementById('vps-port').value) || 22,
    user: document.getElementById('vps-user').value || 'root',
    password: document.getElementById('vps-pass').value,
    country: document.getElementById('vps-country').value,
    type: document.getElementById('vps-type').value,
    note: document.getElementById('vps-note').value,
  };
  try{
    const r = await fetch('/api/vps', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)});
    if(!r.ok){ const e = await r.json().catch(()=>({})); throw new Error(e.detail || 'خطا'); }
    closeModal('modal-add-vps');
    showToast('سرور «' + name + '» ثبت شد و دائمی شد','success');
    await loadVpsServers();
  }catch(e){ showToast(e.message,'error'); }
}
async function deleteVpsServer(sid, name){
  if(!confirm('سرور «' + name + '» و همه کانفیگ‌هایش حذف شود؟')) return;
  try{
    await fetch('/api/vps/' + sid, {method:'DELETE'});
    showToast('سرور حذف شد','success');
    await loadVpsServers();
  }catch(e){ showToast('خطا در حذف','error'); }
}
function genCfgRowHtml(kind, c){
  const sid = kind === 'vps' ? currentVpsServerId : null;
  const pk = kind === 'vps' ? 'vps:' + sid + ':' + c.id : 'sk:' + c.id;
  const used = c.used_bytes||0, lim = c.limit_bytes||0;
  const pct = lim > 0 ? Math.min(100, used/lim*100) : 0;
  const status = c.expired ? '<span class="badge badge-red badge-dot">منقضی</span>' : (c.active===false ? '<span class="badge badge-amber badge-dot">غیرفعال</span>' : '<span class="badge badge-green badge-dot">فعال</span>');
  const sidArg = sid ? "'" + sid + "'" : 'null';
  const cidArg = "'" + c.id + "'";
  const act = (fn, icon, title) => '<button class="btn btn-ghost btn-sm" onclick="' + fn + '(' + sidArg + ',' + cidArg + ')" title="' + title + '"><i class="ti ' + icon + '"></i></button>';
  const actions = act('viewGenCfg','ti-code','مشاهده JSON') + act('copyGenCfg','ti-copy','کپی JSON') + act('editGenCfg','ti-edit','ویرایش') +
    '<button class="btn btn-ghost btn-sm" onclick="toggleGenCfg(' + sidArg + ',' + cidArg + ',' + (c.active!==false) + ')" title="تغییر وضعیت"><i class="ti ti-power"></i></button>' +
    '<button class="btn btn-danger btn-sm" onclick="deleteGenCfg(' + sidArg + ',' + cidArg + ')" title="حذف"><i class="ti ti-trash"></i></button>';
  return '<tr>' +
    '<td><div class="cell-label">' + esc(c.name) + '</div>' + (c.note ? '<div class="cell-muted">' + esc(c.note) + '</div>' : '') + '</td>' +
    '<td><div style="font-size:11.5px">' + esc(c.base_label || '—') + '</div><span class="badge badge-purple" style="margin-top:3px">' + esc(c.base_protocol || '') + '</span></td>' +
    '<td><span class="cell-mono" style="display:inline-block;direction:ltr">' + esc(c.listen||'127.0.0.1') + ':' + (c.socks_port||10808) + '</span></td>' +
    '<td><div class="cell-mono">' + fmtBytes(used) + '</div>' + (lim>0 ? '<div style="height:3px;background:var(--hs-border2);border-radius:2px;margin-top:4px;overflow:hidden"><div style="height:100%;width:' + pct + '%;background:linear-gradient(90deg,var(--hs-primary),var(--hs-violet))"></div></div>' : '') + '</td>' +
    '<td><span class="cell-mono">' + (lim>0 ? fmtBytes(lim) : '∞') + '</span></td>' +
    '<td>' + status + '</td>' +
    '<td>' + pingBadgeHtml(pk) + '</td>' +
    '<td><div class="cell-mono" style="font-size:11px">' + (c.expires_at ? formatExpiry(c.expires_at) : '<span style="color:var(--hs-dim)">∞</span>') + '</div></td>' +
    '<td><div style="display:flex;gap:4px">' + actions + '</div></td></tr>';
}
function findGenCfg(kind, cid){
  if(kind === 'vps'){
    const cfgs = (currentVpsServerId && vpsCfgsCache[currentVpsServerId]) || [];
    return cfgs.find(x => x.id === cid);
  }
  return socksConfigs.find(x => x.id === cid);
}
async function populateBaseSelect(){
  const sel = document.getElementById('gc-base');
  if(!sel) return;
  try{
    const r = await fetch('/api/links');
    const d = await r.json();
    const okProto = ['vless-ws','xhttp-packet-up','xhttp-stream-up','trojan-ws','trojan-xhttp-packet-up','trojan-xhttp-stream-up','shadowsocks'];
    const links = (d.links||[]).filter(l => okProto.includes(l.protocol));
    const prev = sel.value;
    sel.innerHTML = links.length
      ? links.map(l => '<option value="' + l.uuid + '">' + esc(l.label) + ' · ' + esc(l.protocol) + '</option>').join('')
      : '<option value="">اول از بخش کانفیگ‌ها یک کانفیگ بسازید</option>';
    if(prev) sel.value = prev;
  }catch(e){ sel.innerHTML = '<option value="">خطا در بارگذاری</option>'; }
}
function openGenCfgModal(kind, cid){
  if(kind === 'vps' && !currentVpsServerId){ showToast('ابتدا سرور را انتخاب کنید','error'); return; }
  document.getElementById('gc-kind').value = kind;
  document.getElementById('gc-cid').value = cid || '';
  const title = document.getElementById('gcfg-title');
  const sub = document.getElementById('gcfg-sub');
  if(cid){
    const c = findGenCfg(kind, cid);
    title.textContent = 'ویرایش کانفیگ';
    sub.textContent = kind === 'vps' ? 'ویرایش کانفیگ سرور VPS' : 'ویرایش کانفیگ SOCKS5';
    document.getElementById('gc-name').value = c ? c.name : '';
    document.getElementById('gc-port').value = c ? (c.socks_port||10808) : 10808;
    document.getElementById('gc-listen').value = c ? (c.listen||'127.0.0.1') : '127.0.0.1';
    const lb = c ? (c.limit_bytes||0) : 0;
    if(lb > 0){
      if(lb >= 1024*1024*1024){ document.getElementById('gc-val').value = (lb/1024/1024/1024).toFixed(2); document.getElementById('gc-unit').value = 'GB'; }
      else{ document.getElementById('gc-val').value = (lb/1024/1024).toFixed(2); document.getElementById('gc-unit').value = 'MB'; }
    }else{ document.getElementById('gc-val').value = 0; document.getElementById('gc-unit').value = 'GB'; }
    document.getElementById('gc-exp').value = '';
    document.getElementById('gc-note').value = c ? (c.note||'') : '';
    populateBaseSelect().then(() => { if(c && c.vless_uuid) document.getElementById('gc-base').value = c.vless_uuid; });
  }else{
    title.textContent = kind === 'vps' ? 'کانفیگ VPS جدید' : 'کانفیگ SOCKS جدید';
    sub.textContent = 'از روی کانفیگ VLESS، کانفیگ Xray با پورت SOCKS5 ساخته می‌شود';
    document.getElementById('gc-name').value = '';
    document.getElementById('gc-port').value = 10808;
    document.getElementById('gc-listen').value = '127.0.0.1';
    document.getElementById('gc-val').value = 0;
    document.getElementById('gc-unit').value = 'GB';
    document.getElementById('gc-exp').value = '';
    document.getElementById('gc-note').value = '';
    populateBaseSelect();
  }
  openModal('modal-gen-cfg');
}
async function saveGenCfg(){
  const kind = document.getElementById('gc-kind').value;
  const cid = document.getElementById('gc-cid').value;
  const name = document.getElementById('gc-name').value.trim();
  const base = document.getElementById('gc-base').value;
  if(!name){ showToast('نام کانفیگ را وارد کنید','warn'); return; }
  if(!base){ showToast('کانفیگ مبنا (VLESS) را انتخاب کنید','warn'); return; }
  const body = {
    name: name,
    vless_uuid: base,
    socks_port: parseInt(document.getElementById('gc-port').value) || 10808,
    listen: document.getElementById('gc-listen').value,
    limit_value: parseFloat(document.getElementById('gc-val').value) || 0,
    limit_unit: document.getElementById('gc-unit').value,
    note: document.getElementById('gc-note').value,
  };
  const expVal = document.getElementById('gc-exp').value;
  if(expVal !== '' && expVal !== null) body.expires_days = parseInt(expVal) || 0;
  try{
    let url, method;
    if(kind === 'vps'){
      if(!currentVpsServerId){ showToast('ابتدا سرور را انتخاب کنید','error'); return; }
      url = '/api/vps/' + currentVpsServerId + '/configs' + (cid ? '/' + cid : '');
      method = cid ? 'PATCH' : 'POST';
    }else{
      url = '/api/socks' + (cid ? '/' + cid : '');
      method = cid ? 'PATCH' : 'POST';
    }
    const r = await fetch(url, {method, headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)});
    if(!r.ok){ const e = await r.json().catch(()=>({})); throw new Error(e.detail || 'خطا'); }
    closeModal('modal-gen-cfg');
    showToast(cid ? 'کانفیگ ویرایش شد' : 'کانفیگ ساخته شد','success');
    if(kind === 'vps') await openVpsServer(currentVpsServerId); else await loadSocksList();
  }catch(e){ showToast(e.message,'error'); }
}
async function toggleGenCfg(sid, cid, active){
  try{
    const url = sid ? '/api/vps/' + sid + '/configs/' + cid : '/api/socks/' + cid;
    await fetch(url, {method:'PATCH', headers:{'Content-Type':'application/json'}, body: JSON.stringify({active: !active})});
    showToast(!active ? 'کانفیگ فعال شد' : 'کانفیگ غیرفعال شد','success');
    if(sid) await openVpsServer(sid); else await loadSocksList();
  }catch(e){ showToast('خطا','error'); }
}
async function deleteGenCfg(sid, cid){
  if(!confirm('حذف شود؟')) return;
  try{
    const url = sid ? '/api/vps/' + sid + '/configs/' + cid : '/api/socks/' + cid;
    await fetch(url, {method:'DELETE'});
    delete linkPingCache[sid ? 'vps:' + sid + ':' + cid : 'sk:' + cid];
    savePingCache();
    showToast('حذف شد','success');
    if(sid) await openVpsServer(sid); else await loadSocksList();
  }catch(e){ showToast('خطا','error'); }
}
function copyGenCfg(sid, cid){
  const c = findGenCfg(sid ? 'vps' : 'socks', cid);
  if(!c || !c.xray_json){ showToast('کانفیگ پیدا نشد','error'); return; }
  navigator.clipboard.writeText(c.xray_json);
  showToast('JSON کانفیگ کپی شد','success');
}
function viewGenCfg(sid, cid){
  const c = findGenCfg(sid ? 'vps' : 'socks', cid);
  if(!c || !c.xray_json){ showToast('کانفیگ پیدا نشد','error'); return; }
  document.getElementById('xv-title').textContent = c.name;
  document.getElementById('xv-json').textContent = c.xray_json;
  document.getElementById('xv-copy').onclick = () => { navigator.clipboard.writeText(c.xray_json); showToast('کپی شد','success'); };
  openModal('modal-xray-view');
}
async function testGenPing(sid, cid){
  const pk = sid ? 'vps:' + sid + ':' + cid : 'sk:' + cid;
  const el = document.getElementById('ping-' + pk);
  if(el){ el.className = 'ping-badge testing'; el.innerHTML = '<i class="ti ti-loader" style="font-size:11px;animation:spin 1s linear infinite"></i>'; }
  try{
    const url = sid ? '/api/vps/' + sid + '/configs/' + cid + '/test' : '/api/socks/' + cid + '/test';
    const r = await fetch(url, {method:'POST'});
    const d = await r.json().catch(()=>({}));
    if(r.ok && d.ok && d.total_ms != null){ updatePingDisplay(pk, d.total_ms); }
    else{ updatePingDisplay(pk, 999); }
  }catch(e){ updatePingDisplay(pk, 999); }
}
async function loadSocksList(){
  try{
    const r = await authFetch('/api/socks');
    if(!r.ok) throw new Error();
    const d = await r.json();
    socksConfigs = d.socks || [];
  }catch(e){ socksConfigs = []; }
  const bdg = document.getElementById('bdg-socks');
  if(bdg){ bdg.textContent = socksConfigs.length; bdg.style.display = socksConfigs.length ? '' : 'none'; }
  renderSocksTable();
}
function renderSocksTable(){
  const tb = document.getElementById('socks-tbody');
  if(!tb) return;
  socksConfigs.forEach(c => { pingTestHandlers['sk:' + c.id] = () => testGenPing(null, c.id); });
  if(!socksConfigs.length){ tb.innerHTML = '<tr><td colspan="9"><div class="empty"><i class="ti ti-shield-lock"></i><div class="empty-title">کانفیگ SOCKS نیست</div><div class="empty-sub">از روی یک کانفیگ VLESS، کانفیگ Xray با پورت SOCKS5 بسازید</div></div></td></tr>'; return; }
  tb.innerHTML = socksConfigs.map(c => genCfgRowHtml('socks', c)).join('');
}
let connTimer = null;
let connAuto = true;
function connTimeFmt(iso){
  if(!iso) return '—';
  try{
    const d = new Date(iso);
    if(isNaN(d)) return iso;
    return d.toLocaleTimeString('en-GB', {hour:'2-digit', minute:'2-digit', second:'2-digit'});
  }catch(e){ return iso; }
}
async function loadConnections(){
  try{
    const r = await authFetch('/api/connections');
    const d = await r.json();
    const conns = d.connections || [];
    const ips = document.getElementById('stc-ips');
    if(ips) ips.textContent = d.count || 0;
    const ses = document.getElementById('stc-ses');
    if(ses) ses.textContent = d.raw_count || 0;
    const by = document.getElementById('stc-bytes');
    if(by) by.textContent = fmtBytes(conns.reduce((a,c) => a + (c.bytes||0), 0));
    const tb = document.querySelector('#conn-tbl tbody');
    if(!tb) return;
    if(!conns.length){
      tb.innerHTML = '<tr><td colspan="7"><div class="empty"><i class="ti ti-pulse"></i><div class="empty-title">اتصال فعالی نیست</div><div class="empty-sub">وقتی کاربری به کانفیگ‌های شما وصل شود، اینجا نمایش داده می‌شود</div></div></td></tr>';
      return;
    }
    tb.innerHTML = conns.map(c =>
      '<tr>' +
      '<td><div class="cell-mono" style="direction:ltr;text-align:right">' + esc(c.ip) + '</div></td>' +
      '<td><div class="cell-label">' + esc(c.label) + '</div></td>' +
      '<td>' + (c.transports||[]).map(t => '<span class="badge badge-purple">' + esc(t) + '</span>').join(' ') + '</td>' +
      '<td><span class="cell-mono">' + (c.sessions||0) + '</span></td>' +
      '<td><div class="cell-mono">' + esc(c.bytes_fmt||'0 B') + '</div></td>' +
      '<td><div class="cell-muted">' + connTimeFmt(c.connected_at) + '</div></td>' +
      '<td><div class="cell-muted">' + connTimeFmt(c.last_connected_at) + '</div></td>' +
      '</tr>'
    ).join('');
  }catch(e){}
}
function startConnTimer(){
  if(connTimer) return;
  connTimer = setInterval(() => {
    const pg = document.getElementById('page-connections');
    if(pg && pg.classList.contains('active') && connAuto){ loadConnections(); }
  }, 5000);
}
function toggleConnAuto(){
  connAuto = !connAuto;
  const cb = document.getElementById('conn-auto');
  if(cb) cb.checked = connAuto;
}

let trafficChart = null;
function renderChart(hourly){
  const ctx = document.getElementById('trafficChart');
  if(!ctx) return;
  const labels = [], data = [];
  const now = new Date();
  for(let i=23; i>=0; i--){
    const h = new Date(now.getTime() - i*3600*1000);
    labels.push(h.getHours().toString().padStart(2,'0') + ':00');
    const key = h.getHours().toString().padStart(2,'0') + ':00';
    data.push((hourly && hourly[key]) ? (hourly[key]/1024/1024) : 0);
  }
  if(typeof Chart === 'undefined'){
    if(!renderChart._retries) renderChart._retries = 0;
    if(renderChart._retries++ < 20) setTimeout(() => renderChart(hourly), 1500);
    return;
  }
  const grad = ctx.getContext('2d').createLinearGradient(0,0,0,280);
  grad.addColorStop(0, 'rgba(0,255,136,0.45)');
  grad.addColorStop(1, 'rgba(0,255,136,0)');
  if(trafficChart) trafficChart.destroy();
  trafficChart = new Chart(ctx, {
    type: 'line',
    data: { labels, datasets: [{
      label: 'ترافیک (MB)', data, borderColor: '#00FF88', backgroundColor: grad,
      borderWidth: 2, fill: true, tension: 0.4, pointRadius: 0, pointHoverRadius: 5,
      pointBackgroundColor: '#00FF88', pointBorderColor: '#000', pointBorderWidth: 2
    }]},
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend:{display:false}, tooltip:{
        backgroundColor:'#0e1e0e', titleColor:'#E8FFF0', bodyColor:'#98C0A2',
        borderColor:'rgba(0,255,136,.3)', borderWidth:1, padding:10, displayColors:false, rtl:true, textDirection:'rtl',
        callbacks:{label:ctx => ctx.parsed.y.toFixed(2)+' MB'}
      }},
      scales:{
        x:{grid:{color:'rgba(0,255,136,.04)'}, ticks:{color:'#70947A', font:{size:10}}},
        y:{grid:{color:'rgba(0,255,136,.04)'}, ticks:{color:'#70947A', font:{size:10}, callback:v => v.toFixed(0)+'M'}}
      }
    }
  });
}
function esc(x){ return String(x ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
async function checkVersion(){
  const card = document.getElementById('update-card');
  if(!card) return;
  card.innerHTML = '<div class="empty"><i class="ti ti-loader"></i><div class="empty-sub">در حال بررسی...</div></div>';
  try{
    const r = await fetch('/api/version');
    if(!r.ok) throw new Error();
    const d = await r.json();
    const cur = (d.current && d.current.version) || '-';
    const lat = (d.latest && d.latest.version) || '-';
    const notes = (d.latest && (d.latest.notes||d.latest.description)) || '';
    card.innerHTML =
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--hs-border2);font-size:13px"><span style="color:var(--hs-dim)">نسخه فعلی</span><span style="font-weight:600;font-family:monospace">' + esc(cur) + '</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--hs-border2);font-size:13px"><span style="color:var(--hs-dim)">آخرین نسخه</span><span style="font-weight:600;font-family:monospace">' + esc(lat) + '</span></div>' +
      (notes ? '<div style="padding:10px 0;font-size:12px;color:var(--hs-dim);white-space:pre-wrap">' + esc(notes) + '</div>' : '') +
      '<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">' +
      '<button class="btn btn-outline" onclick="checkVersion()"><i class="ti ti-refresh"></i> بررسی مجدد</button>' +
      (d.update_available ? '<button class="btn btn-primary" onclick="startUpdate()"><i class="ti ti-cloud-download"></i> نصب نسخه ' + esc(lat) + '</button>' : '<span class="badge badge-green badge-dot" style="align-self:center">به‌روز هستید</span>') +
      '</div><div id="update-log" style="margin-top:10px;font-size:11px;font-family:monospace;color:var(--hs-dim);white-space:pre-wrap"></div>';
  }catch(e){
    card.innerHTML = '<div class="empty"><i class="ti ti-alert-triangle"></i><div class="empty-title">خطا</div><div class="empty-sub">دریافت اطلاعات ممکن نشد</div></div><div style="display:flex;justify-content:center;margin-top:10px"><button class="btn btn-outline" onclick="checkVersion()"><i class="ti ti-refresh"></i> تلاش مجدد</button></div>';
  }
}
async function startUpdate(){
  if(!confirm('نسخه جدید نصب شود؟')) return;
  try{
    const r = await fetch('/api/update', {method:'POST'});
    const d = await r.json().catch(()=>({}));
    if(!r.ok) throw new Error(d.detail||'خطا');
    showToast('بروزرسانی شروع شد','success');
    pollUpdateLog();
  }catch(e){ showToast(e.message||'خطا','error'); }
}
async function pollUpdateLog(){
  const el = document.getElementById('update-log');
  if(!el) return;
  try{
    const r = await fetch('/api/update-log');
    const d = await r.json();
    el.textContent = (d.logs||[]).map(l => l.msg).join('\n');
    el.scrollTop = el.scrollHeight;
    if(d.running) setTimeout(pollUpdateLog, 2000);
    else setTimeout(checkVersion, 4000);
  }catch(e){ setTimeout(pollUpdateLog, 3000); }
}
async function initAccountCard(){
  try{
    const me = await (await fetch('/api/me')).json();
    const un = document.getElementById('tb-user-name');
    if(un && me.username) un.textContent = me.username;
    const uname = document.getElementById('acct-username');
    const role = document.getElementById('acct-role');
    const avatar = document.getElementById('acct-avatar');
    const badge = document.getElementById('acct-badge');
    if(uname && me.username) uname.textContent = me.username;
    if(avatar) avatar.textContent = (me.username||'?').slice(0,1).toUpperCase();
    if(role) role.textContent = me.is_admin ? 'مدیر سیستم' : 'کاربر عادی';
    if(badge) badge.style.display = 'inline-flex';
  }catch(e){}
}
async function refreshAll(){ await Promise.all([loadStats(), loadActivity(), loadLinks()]); }
async function init(){
  try{ await refreshAll(); }catch(e){}
  try{ loadVpsServers(); }catch(e){}
  try{ loadSocksList(); }catch(e){}
  try{ await initAccountCard(); }catch(e){}
  try{ const r = await authFetch('/stats'); const d = await r.json(); renderChart(d.hourly||{}); }catch(e){ renderChart({}); }
  startConnTimer();
  setInterval(loadStats, 30000);
}
init().catch(e => console.error('init failed', e));
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
<meta name="theme-color" content="#0a0f0a">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230a0f0a'/%3E%3Cpath d='M8 16 L13 21 L24 10' stroke='%2300FF88' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<style>
@font-face{font-family:'IRANSans';font-style:normal;font-weight:400;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:500;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Medium.woff2') format('woff2')}
@font-face{font-family:'IRANSans';font-style:normal;font-weight:700;font-display:swap;src:url('https://cdn.jsdelivr.net/npm/iransans@1.0.0/woff2/IRANSansWeb_Bold.woff2') format('woff2')}
</style>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css" media="print" onload="this.media='all'">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--hs-bg:#080e08;--hs-card:rgba(12,24,12,0.85);--hs-primary:#00FF88;--hs-text:#E8FFF0;--hs-dim:#70947A;--hs-mid:#98C0A2;--hs-border:rgba(0,255,136,0.20);--hs-secondary:#FF077A}
body{font-family:'IRANSans','Iran Sans',Tahoma,sans-serif;background:var(--hs-bg);color:var(--hs-text);min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px;position:relative;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 50% 40% at 20% 10%,rgba(0,255,136,.18),transparent 70%),radial-gradient(ellipse 50% 40% at 80% 90%,rgba(0,204,106,.15),transparent 70%);pointer-events:none}
.card{background:var(--hs-card);backdrop-filter:blur(30px);border:1px solid var(--hs-border);border-radius:20px;padding:32px;max-width:520px;width:100%;position:relative;z-index:1;box-shadow:0 20px 60px -15px rgba(0,0,0,.5),0 0 40px -15px rgba(0,255,136,.2)}
.brand{display:flex;align-items:center;gap:12px;margin-bottom:22px}
.brand svg{width:42px;height:42px;border-radius:11px}
.brand-name{font-size:16px;font-weight:800}
.brand-sub{font-size:11px;color:var(--hs-dim);margin-top:2px}
h1{font-size:20px;font-weight:800;margin-bottom:6px}
.sub{font-size:13px;color:var(--hs-mid);margin-bottom:22px;line-height:1.7}
.links{display:flex;flex-direction:column;gap:10px}
.link-item{background:rgba(0,0,0,.15);border:1px solid var(--hs-border);border-radius:11px;padding:14px;display:flex;align-items:center;gap:12px;transition:.2s;cursor:pointer}
.link-item:hover{border-color:var(--hs-primary);background:rgba(0,255,136,.06);box-shadow:0 0 20px -8px rgba(0,255,136,.3)}
.link-info{flex:1;min-width:0}
.link-name{font-size:13.5px;font-weight:600}
.link-meta{font-size:11px;color:var(--hs-dim);margin-top:2px;font-family:'JetBrains Mono',monospace}
.copy-btn{width:32px;height:32px;border-radius:8px;background:rgba(0,255,136,.12);border:1px solid var(--hs-border);color:var(--hs-primary);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s;flex-shrink:0}
.copy-btn:hover{background:var(--hs-primary);color:#001a08}
.empty{padding:40px 20px;text-align:center;color:var(--hs-dim)}
.empty i{font-size:42px;display:block;margin-bottom:12px;color:var(--hs-primary);opacity:.4}
</style>
</head>
<body>
<div class="card">
  <div class="brand">
    <svg viewBox="0 0 32 32"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00FF88"/><stop offset="1" stop-color="#00CC6A"/></linearGradient></defs><rect x="2" y="2" width="28" height="28" rx="7" fill="url(#g)"/><path d="M9 16 L13 20 L22 10" stroke="#051A0B" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <div><div class="brand-name">HS Panel</div><div class="brand-sub">اشتراک عمومی</div></div>
  </div>
  <h1>گروه اشتراک</h1>
  <p class="sub" id="sub-name">در حال بارگذاری...</p>
  <div class="links" id="links-list"><div class="empty"><i class="ti ti-loader"></i> در حال بارگذاری...</div></div>
</div>
<script>
async function load(){
  try{
    const r = await fetch('/api/public/sub/""" + uuid_key + """');
    if(!r.ok) throw new Error();
    const d = await r.json();
    if(d.locked){ document.getElementById('sub-name').textContent = 'این گروه رمز دارد'; return; }
    document.getElementById('sub-name').textContent = d.name || 'گروه';
    const el = document.getElementById('links-list');
    if(!d.links||!d.links.length){ el.innerHTML='<div class="empty"><i class="ti ti-link-off"></i> کانفیگی موجود نیست</div>'; return; }
    el.innerHTML = d.links.map(l =>
      '<div class="link-item" onclick="copyText(\\''+l.vless_link+'\\')"><div class="link-info"><div class="link-name">'+(l.label||'—')+'</div><div class="link-meta">'+(l.protocol||'')+'</div></div><button class="copy-btn"><i class="ti ti-copy"></i></button></div>'
    ).join('');
  }catch(e){ document.getElementById('sub-name').textContent = 'خطا در بارگذاری'; }
}
function copyText(t){ navigator.clipboard.writeText(t); }
load();
</script>
</body>
</html>"""
