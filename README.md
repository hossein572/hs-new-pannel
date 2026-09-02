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

## ورود پیش‌فرض

- رمز: `123456`
- پورت: `8000`

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
