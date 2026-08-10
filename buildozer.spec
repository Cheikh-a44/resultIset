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
- name: Build APK with Buildozer
        run: |
          yes | buildozer -v android debug

# (list) Permissions
android.permissions = 

[buildozer]
log_level = 2
warn_on_root = 1
