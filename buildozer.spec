[app]
title = Belote Score Counter
package.name = belotescore
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3==3.11.9,kivy
orientation = portrait
fullscreen = 0
android.accept_sdk_license = True
p4a.branch = v2024.01.21

# (list) Permissions
android.permissions =

[buildozer]
log_level = 2
warn_on_root = 0