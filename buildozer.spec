[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (leave empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Adding all necessary requirements including Kivy, Plyer for Android APIs, and requests/geocoder
requirements = python3,kivy,plyer,requests,geocoder

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions needed by the application
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

# (int) Target Android API level. Set this to 33 for Android 13
android.api = 32

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 32

# Add or update the following line
android.ndk_path = ~/android-sdk/ndk/android-ndk-r25b

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use (minimum API your app will support)
android.ndk_api = 21

# (bool) Enable AndroidX support. Required for newer Android APIs.
android.enable_androidx = True

# (list) The Android architectures to build for (ARM architectures are commonly used)
android.archs = arm64-v8a, armeabi-v7a

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
android.apptheme = "@android:style/Theme.NoTitleBar"

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (list) Gradle dependencies to add (using androidx to enable modern Android features)
android.gradle_dependencies = androidx.legacy:legacy-support-v4:1.0.0

# (bool) Enable or disable backup (useful for restoring app data)
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk or aar)
android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar)
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
