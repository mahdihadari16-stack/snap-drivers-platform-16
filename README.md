# 🚗 SappDriver - اپلیکیشن راننده هوشمند

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Android%20%7C%20iOS-green.svg)
![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)
![Build Status](https://img.shields.io/badge/build-passing-success.svg)

## 📋 فهرست مطالب

- [درباره پروژه](#درباره-پروژه)
- [ویژگی‌های کلیدی](#ویژگی‌های-کلیدی)
- [فناوری‌های استفاده‌شده](#فناوری‌های-استفاده‌شده)
- [نصب و راه‌اندازی](#نصب-و-راه‌اندازی)
- [مستندات API](#مستندات-api)
- [معماری پروژه](#معماری-پروژه)
- [راهنمای مشارکت](#راهنمای-مشارکت)
- [عیب‌یابی](#عیب‌یابی)
- [لایسنس](#لایسنس)
- [تماس با ما](#تماس-با-ما)

## 🎯 درباره پروژه

**SappDriver** یک اپلیکیشن پیشرفته و هوشمند برای رانندگان است که با هدف بهبود تجربه کاری و افزایش بهره‌وری طراحی شده است. این اپلیکیشن قابلیت‌های مدرن و کاربردی را ارائه می‌دهد تا رانندگان بتوانند به‌صورت بهینه خدمات خود را ارائه دهند.

### 🎨 چشم‌انداز پروژه
ایجاد پلتفرمی جامع و کاربرپسند که نیازهای مختلف رانندگان حرفه‌ای را پاسخ دهد و تجربه کاری آن‌ها را متحول کند.

## ✨ ویژگی‌های کلیدی

### 🗺️ ردیابی مکان و ناوبری
- **ردیابی دقیق موقعیت جغرافیایی** با استفاده از GPS پیشرفته
- **مسیریابی هوشمند** با در نظر گیری ترافیک real-time
- **نقشه‌های تعاملی** با رابط کاربری بهینه‌شده

### 💳 سیستم پرداخت پیشرفته
- **پرداخت آنلاین ایمن** با رمزنگاری پیشرفته
- **پشتیبانی از درگاه‌های مختلف** پرداخت داخلی و خارجی
- **مدیریت مالی هوشمند** و گزارش‌گیری دقیق

### 📱 رابط کاربری مدرن
- **طراحی Material Design** با تجربه کاربری بهینه
- **پشتیبانی از حالت تاریک/روشن**
- **واکنش‌گرایی کامل** برای انواع دستگاه‌ها

### 🔔 سیستم اعلانات پیشرفته
- **اعلانات Push** در real-time
- **اعلانات محلی** برای یادآوری‌های مهم
- **تنظیمات شخصی‌سازی** اعلانات

### 📊 آنالیتیکس و گزارش‌گیری
- **داشبورد تحلیلی** با نمودارهای تعاملی
- **گزارش‌های دوره‌ای** عملکرد
- **تحلیل الگوهای حرکتی** و بهینه‌سازی

## 🛠️ فناوری‌های استفاده‌شده

### Backend
```
- Node.js / Express.js
- MongoDB / PostgreSQL
- JWT Authentication
- Redis Caching
- Socket.IO (Real-time Communication)
```

### Mobile Development
```
- React Native / Flutter
- Native Modules (Android/iOS)
- Google Maps SDK
- Firebase Services
```

### DevOps & Tools
```
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- AWS / Google Cloud Platform
- Nginx (Load Balancer)
```

### Monitoring & Analytics
```
- Google Analytics
- Sentry (Error Tracking)
- PM2 (Process Management)
```

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها
```bash
- Node.js (v16+)
- npm یا yarn
- MongoDB (v4.4+)
- Redis Server
- Android Studio / Xcode (برای توسعه موبایل)
```

### مراحل نصب

#### 1️⃣ کلون کردن پروژه
```bash
git clone https://github.com/mahdihadari16-stack/SappDriver-.git
cd SappDriver-
```

#### 2️⃣ نصب وابستگی‌ها
```bash
# Backend dependencies
cd backend
npm install

# Frontend dependencies  
cd ../frontend
npm install

# Mobile app dependencies
cd ../mobile
npm install
```

#### 3️⃣ تنظیمات Environment Variables
```bash
# ایجاد فایل .env در پوشه backend
cp .env.example .env

# ویرایش متغیرهای محیطی
nano .env
```

#### 4️⃣ راه‌اندازی دیتابیس
```bash
# اجرای MongoDB
mongod

# اجرای Redis
redis-server

# Migration دیتابیس
npm run db:migrate
```

#### 5️⃣ اجرای پروژه
```bash
# Backend Server
npm run dev

# Frontend (در ترمینال جدید)
cd ../frontend
npm start

# Mobile App (در ترمینال جدید)
cd ../mobile
npx react-native run-android
# یا
npx react-native run-ios
```

## 📚 مستندات API

### Base URL
```
Production: https://api.sappdriver.com/v1
Development: http://localhost:3000/api/v1
```

### Authentication
تمامی API endpoints نیاز به JWT Token دارند:
```http
Authorization: Bearer <your_jwt_token>
```

### اصلی‌ترین Endpoints

#### 🔐 Authentication
```http
POST /auth/login          # ورود کاربر
POST /auth/register       # ثبت نام
POST /auth/refresh        # تمدید توکن
POST /auth/logout         # خروج
```

#### 👤 User Management  
```http
GET  /users/profile       # مشاهده پروفایل
PUT  /users/profile       # ویرایش پروفایل
POST /users/avatar        # آپلود تصویر پروفایل
```

#### 🚗 Driver Operations
```http
GET  /driver/trips        # لیست سفرها
POST /driver/status       # تغییر وضعیت آنلاین/آفلاین
PUT  /driver/location     # بروزرسانی موقعیت
```

#### 💰 Payment
```http
GET  /payments/history    # تاریخچه پرداخت‌ها
POST /payments/request    # درخواست پرداخت
GET  /payments/balance    # موجودی حساب
```

مستندات کامل API در [**🔗 API Documentation**](./docs/api-documentation.md) موجود است.

## 🏗️ معماری پروژه

```
SappDriver/
├── 📱 mobile/                 # اپلیکیشن موبایل
│   ├── src/
│   │   ├── components/       # کامپوننت‌های قابل استفاده مجدد
│   │   ├── screens/         # صفحات اپلیکیشن
│   │   ├── services/        # API calls و logic
│   │   ├── utils/           # توابع کمکی
│   │   └── navigation/      # تنظیمات Navigation
│   └── android/ios/         # فایل‌های Native
│
├── 🖥️ backend/               # سرور Backend
│   ├── src/
│   │   ├── controllers/     # منطق کنترلرها
│   │   ├── models/          # مدل‌های دیتابیس
│   │   ├── routes/          # تعریف مسیرها
│   │   ├── middleware/      # Middleware functions
│   │   ├── services/        # Business logic
│   │   └── utils/           # توابع کمکی
│   └── tests/               # تست‌های واحد
│
├── 🌐 web-dashboard/         # داشبورد وب
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── services/
│   └── public/
│
├── 📋 docs/                  # مستندات پروژه
├── 🐳 docker/                # فایل‌های Docker
├── 🧪 tests/                 # تست‌های integration
└── 📊 scripts/               # اسکریپت‌های automation
```

### الگوهای معماری استفاده‌شده:
- **🏛️ MVC Pattern** در backend
- **🔄 Redux/Context API** برای state management
- **🧩 Component-Based Architecture** در frontend
- **📡 RESTful API Design** برای communication
- **🔐 JWT-Based Authentication** برای امنیت

## 🤝 راهنمای مشارکت

ما از مشارکت شما در بهبود **SappDriver** استقبال می‌کنیم! 

### مراحل مشارکت:

#### 1️⃣ Fork کردن پروژه
```bash
# Fork repository از GitHub
git clone https://github.com/YOUR_USERNAME/SappDriver-.git
```

#### 2️⃣ ایجاد Branch جدید
```bash
git checkout -b feature/amazing-feature
```

#### 3️⃣ Commit کردن تغییرات
```bash
git commit -m "Add: ویژگی جدید فوق‌العاده"
```

#### 4️⃣ Push و ایجاد Pull Request
```bash
git push origin feature/amazing-feature
```

### 📝 قوانین Commit
لطفاً از conventional commits استفاده کنید:
```
feat: اضافه کردن ویژگی جدید
fix: رفع باگ
docs: بروزرسانی مستندات  
style: تغییرات فرمت کد
refactor: بازنویسی کد
test: اضافه کردن تست
chore: تغییرات ابزارها و کانفیگ
```

### 🧪 اجرای تست‌ها
```bash
# تست‌های backend
cd backend && npm test

# تست‌های mobile
cd mobile && npm test

# تست‌های integration
npm run test:e2e
```

## 🔧 عیب‌یابی

### مشکلات رایج و راه‌حل‌ها:

#### ❌ خطای اتصال به دیتابیس
```bash
# بررسی وضعیت MongoDB
systemctl status mongod

# راه‌اندازی مجدد
sudo systemctl restart mongod
```

#### ❌ مشکل در build اپلیکیشن موبایل
```bash
# پاک کردن cache
cd mobile
npx react-native start --reset-cache

# rebuild کامل
cd android && ./gradlew clean
cd .. && npx react-native run-android
```

#### ❌ خطای JWT Token
```bash
# بررسی تاریخ انقضا توکن
# تنظیم صحیح SECRET_KEY در .env
```

### 🆘 درخواست کمک
اگر با مشکلی مواجه شدید:
1. ابتدا [**Issues**](https://github.com/mahdihadari16-stack/SappDriver-/issues) را بررسی کنید
2. Issue جدید با template مناسب ایجاد کنید
3. Log های مربوطه را ضمیمه کنید

## 📈 نقشه راه توسعه

### ✅ ویژگی‌های کامل‌شده (v1.0)
- [x] سیستم احراز هویت
- [x] ردیابی موقعیت جغرافیایی  
- [x] پرداخت آنلاین
- [x] اعلانات Push
- [x] داشبورد تحلیلی

### 🚧 در حال توسعه (v1.1)
- [ ] پشتیبانی از چند زبان
- [ ] سیستم امتیازدهی رانندگان
- [ ] چت آنلاین با مسافران
- [ ] پیش‌بینی ترافیک با AI

### 🔮 ویژگی‌های آینده (v2.0)
- [ ] تشخیص صدا و دستورات گفتاری
- [ ] واقعیت افزوده برای ناوبری
- [ ] اتصال به خودروهای هوشمند
- [ ] تحلیل رفتار رانندگی

## 📄 لایسنس

این پروژه تحت لایسنس **MIT** منتشر شده است. برای جزئیات بیشتر فایل [LICENSE](./LICENSE) را مطالعه کنید.

```
MIT License

Copyright (c) 2024 Mahdi Hadari

مجوز استفاده، تغییر و توزیع این نرم‌افزار برای اهداف تجاری و غیرتجاری آزاد است.
```

## 📞 تماس با ما

### 👨‍💻 توسعه‌دهنده اصلی
**Mahdi Hadari**
- 📧 Email: mahdihadari16@gmail.com
- 💼 LinkedIn: [Mahdi Hadari](https://linkedin.com/in/mahdihadari)
- 🐙 GitHub: [@mahdihadari16-stack](https://github.com/mahdihadari16-stack)

### 🤝 حمایت و پشتیبانی
- 📋 **Issues**: [GitHub Issues](https://github.com/mahdihadari16-stack/SappDriver-/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/mahdihadari16-stack/SappDriver-/discussions)
- 📧 **Email**: support@sappdriver.com

### 🌟 حمایت از پروژه
اگر این پروژه برایتان مفید بود:
- ⭐ **Star** کنید در GitHub
- 🍴 **Fork** کنید برای مشارکت
- 🐛 **Bug** ها را گزارش دهید
- 💡 **ایده** های جدید پیشنهاد دهید

---

<div align="center">

**🚗 ساخته شده با ❤️ برای جامعه رانندگان ایران**

[![GitHub Stars](https://img.shields.io/github/stars/mahdihadari16-stack/SappDriver-?style=social)](https://github.com/mahdihadari16-stack/SappDriver-)
[![GitHub Forks](https://img.shields.io/github/forks/mahdihadari16-stack/SappDriver-?style=social)](https://github.com/mahdihadari16-stack/SappDriver-)
[![GitHub Issues](https://img.shields.io/github/issues/mahdihadari16-stack/SappDriver-)](https://github.com/mahdihadari16-stack/SappDriver-/issues)

</div>
