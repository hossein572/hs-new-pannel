# HS Panel

یک سیستم مدیریت پروکسی چند پروتکله با پشتیبانی از:

- **VLESS** (WebSocket, XHTTP)
- **Trojan** (WebSocket, XHTTP)
- **MTProto** (تلگرام)
- **Shadowsocks**

## ویژگی‌ها

- 🎛️ داشبورد وب ریسپانسیو
- 🔐 احراز هویت با رمز عبور
- 📊 مانیتورینگ ترافیک و اتصالات
- 🌐 ساخت خودکار لینک‌های اشتراک
- 📦 بکاپ و ریستور
- 🔄 آپدیت خودکار

## نصب

```bash
pip install -r requirements.txt
python main.py
```

## ورود

- ثبت‌نام با ایمیل (کد تأیید واقعی به ایمیل ارسال می‌شود)
- ورود با ایمیل + رمز عبور، یا ورود با کد یکبارمصرف ایمیل
- اولین کاربر ثبت‌نام‌شده = مدیر
- پورت پیش‌فرض: `8000`

## تنظیم SMTP (ارسال کد تأیید)

کد تأیید به‌صورت واقعی ایمیل می‌شود. دو راه برای تنظیم:

۱. از داشبورد (توسط مدیر): تنظیمات ← تنظیمات ایمیل (SMTP) + دکمه «ارسال ایمیل تست»
۲. با Environment Variable:

```bash
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=you@gmail.com
SMTP_PASS=xxxx-xxxx-xxxx-xxxx   # App Password جیمیل
SMTP_FROM=you@gmail.com
```

> نکته: مقادیر Environment بر تنظیمات داشبورد اولویت دارند.

## تست محلی (Local Dev)

```bash
# ترمینال ۱: SMTP تستی (کدها را در ترمینال چاپ می‌کند)
python dev_smtp.py

# ترمینال ۲: پنل با ری‌لود خودکار
SMTP_HOST=127.0.0.1 SMTP_PORT=1025 SMTP_USER=test SMTP_PASS=test SMTP_FROM=test@local \
PORT=8000 DATA_DIR=./data RELOAD=1 python main.py
```

با `RELOAD=1`، با هر تغییر فایل `.py` سرور خودکار ری‌استارت می‌شود.

## ساختار پروژه

```
HS/
├── main.py              # فایل اصلی سرور
├── central.py           # ارتباط با سرویس مرکزی
├── pages.py             # رابط کاربری وب
├── botgeneratedomin.py  # ساخت دامنه
├── bottokentcpproxy.py  # مدیریت TCP Proxy
├── zeussocks5.py       # پروکسی Zeus
├── protocol/           # پروتکل‌های پروکسی
│   ├── vless/
│   ├── trojan/
│   ├── mtproto/
│   └── shadowsocks/
└── requirements.txt     # وابستگی‌ها
```

## لایسنس

MIT License
