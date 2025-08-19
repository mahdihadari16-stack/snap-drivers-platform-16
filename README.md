# SnappDrivers

## معرفی پروژه

SnappDrivers اپلیکیشنی برای جمع‌آوری، تحلیل و نمایش داده‌های مربوط به رانندگان اسنپ است. هدف اصلی این ابزار:
- پیاده‌سازی یک داشبورد کامل و کاربرپسند  
- ارائه‌ی گزارش‌های عملکردی به صورت نمودار  
- ذخیره و مدیریت خودکار لاگ‌ها و تراکنش‌های رانندگان  

این پروژه به زبان Dart/Flutter و با تمرکز بر بومی‌سازی فارسی توسعه یافته و برای اجرا روی اندروید و iOS آماده است.

---

## ویژگی‌ها

- ورود و ثبت‌نام راننده با شماره تلفن  
- نمایش آمار روزانه، هفتگی و ماهانه  
- نمودارهای خطی، میله‌ای و دایره‌ای برای تحلیل سفرها  
- امکان صادرات گزارش به CSV  
- ذخیره خودکار لاگ‌ها در فضای محلی (SQLite)  
- پشتیبانی کامل از زبان فارسی  
- امکان تنظیم بازه زمانی دلخواه  

---

## معماری کلی

1. Presentation Layer  
   - ویجت‌های Flutter  
   - مدیریت وضعیت با Provider  
2. Business Logic Layer  
   - سرویس‌های تحلیل  
   - لاجیک تبدیل داده  
3. Data Layer  
   - Repository برای دسترسی به SQLite  
   - مدل‌های داده (Models)  
4. API Client  
   - ارتباط با سرور Snapp (در صورت نیاز)  
   - مدیریت درخواست‌ها و خطاها  

---

## پیش‌نیازها

- Flutter SDK نسخه ۲.۵ به بالا  
- Android Studio یا VS Code  
- اکانت Snapp برای تست API (اختیاری)  

---

## نصب و راه‌اندازی

```bash
# گام ۱: کلون کردن مخزن
git clone https://github.com/YourUsername/SnappDrivers.git

# گام ۲: ورود به پوشه پروژه
cd SnappDrivers

# گام ۳: نصب بسته‌ها
flutter pub get

# گام ۴: اجرای برنامه
flutter run

پیکربندی

تمام تنظیمات را در فایل lib/config/config.dart می‌توانید تغییر دهید:

class AppConfig {
  static const apiBaseUrl = "https://api.snapp.com";
  static const defaultLocale = Locale('fa');
  static const dbName = "snapp_drivers.db";
}

بومی‌سازی (Localization)

فایل‌های ترجمه در مسیر assets/lang/ قرار دارند.

برای اضافه کردن زبان جدید:

یک فایل JSON جدید با کلیدهای مشابه ایجاد کنید.

در pubspec.yaml زیر بخش flutter اضافه کنید:

assets:
  - assets/lang/fa.json
  - assets/lang/en.json

در main.dart زبان را تنظیم کنید:

runApp(
  MaterialApp(
    locale: AppConfig.defaultLocale,
    supportedLocales: [Locale('fa'), Locale('en')],
    localizationsDelegates: [/* ... */],
  ),
);

مشارکت

هرگونه مشارکت و گزارش باگ خوش‌آمد است:

Issue جدید باز کنید

شاخه (branch) جدید بر اساس شماره Issue بسازید

Pull Request بدهید با توضیح تغییرات

قبل از مرج، لطفاً تست‌های واحد را پاس کنید:

flutter test

ساختار دایرکتوری

SnappDrivers/
├── lib/
│   ├── config/
│   ├── models/
│   ├── services/
│   ├── ui/
│   └── main.dart
├── assets/
│   └── lang/
├── test/
├── pubspec.yaml
└── README.md

مجوز

این پروژه تحت مجوز MIT منتشر شده است.لطفاً برای جزئیات بیشتر به فایل LICENSE مراجعه کنید.


## راهنمای افزودن README.md به مخزن با GitHop

۱. اپلیکیشن GitHop را روی دستگاه اندرویدی خود باز کنید.  
۲. وارد مخزن SnappDrivers شوید (Repository → SnappDrivers).  
۳. در منوی پایین صفحه، روی دکمه‌ی **Add file** بزنید.  
۴. گزینه‌ی **Create new file** را انتخاب کنید.  
۵. در فیلد فایل‌نام، بنویسید `README.md`.  
۶. در بخش محتوا، کل متن بالا را پیست (Paste) کنید.  
۷. اسکرول کنید و در بخش Commit message بنویسید:

Add complete README for SnappDrivers

۸. دکمه‌ی **Commit** را بزنید تا تغییرات محلی ذخیره شود.  
۹. سپس روی **Push** کلیک کنید تا فایل به مخزن GitHub منتقل شود.  

با این روش، فایل README.md شما در شاخه اصلی (main یا master) قرار می‌گیرد و بلافاصله در صفحه‌ی GitHub پروژه نمایش داده می‌شود.