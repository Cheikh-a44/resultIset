[app]
title = Belote Score Counter
package.name = belotescore
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.manifest.extra = <meta-data android:name="android.max_aspect" android:value="2.1" />
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0