[app]
title = Belote Score Counter
package.name = belotescore
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# 🔥 استخدام python3 فقط بدون رقم إصدار محدد
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.accept_sdk_license = True

# إعدادات Android المتوافقة
android.api = 33
android.minapi = 21
android.ndk = 25b

# تحسين الشاشة الكاملة
android.manifest.extra = <meta-data android:name="android.max_aspect" android:value="2.1" />

# صلاحيات التطبيق
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0