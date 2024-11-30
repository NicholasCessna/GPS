[app]
# (str) Title of your application
title = GPSApp

# (str) Package name
package.name = gpsapp

# (str) Package domain (e.g., org.test)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Application requirements
# Ensure all necessary modules are included
requirements = python3,kivy,requests,geocoder,plyer

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait, or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions required by the app
# Ensure the app has access to the internet and fine location
android.permissions = INTERNET,ACCESS_FINE_LOCATION

# (int) Target Android API, should be as high as possible
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
# android.ndk = 23b

# (bool) Enable AndroidX support
# android.enable_androidx requires android.api >= 28
android.enable_androidx = True

# (list) Gradle dependencies to add
# android.gradle_dependencies =

# (list) Add Java compile options
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add
# android.add_gradle_repositories =

# (list) Packaging options to add
# android.add_packaging_options =

# (list) Java classes to add as activities to the manifest
# android.add_activities =

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
# icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
# icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Features (adds uses-feature tags to manifest)
# android.features = android.hardware.usb.host

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra XML to write directly inside the <manifest> element of AndroidManifest.xml
# android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra XML to write directly inside the <manifest><application> tag of AndroidManifest.xml
# android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) Full name including package path of the Java class that implements Python Service
# android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
# android.whitelist =

# (str) Path to a custom whitelist file
# android.whitelist_src =

# (str) Path to a custom blacklist file
# android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access their classes
# android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a directory containing the files)
# android.add_src =

# (list) Android AAR archives to add
# android.add_aars =

# (list) Put these files or directories in the apk assets directory
# android.add_assets =

# (list) Put these files or directories in the apk res directory
# android.add_resources =

# (bool) If True, then skip trying to update the Android SDK
# android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
# android.accept_sdk_license = False

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
# android.ant_path =

# (str) Python-for-Android git clone directory (if empty, it will be automatically cloned from GitHub)
# p4a.source_dir = /p4a

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes =

# (str) Filename to the hook for p4a
# p4a.hook =

# (list) Python-for-Android whitelist
# android.p4a_whitelist =

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e., .apk, .ipa) storage
# bin_dir = ./bin

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

# (list) List of services to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) Author of the application
# author = Your Name

# (str) License of the application
# license = MIT

# (str) Description of the application
# description = Short description of your app

# (str) URL of the application's website
# url = http://example.com

# (str) Email of the author
# author.email = your.email@example.com

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
# garden_requirements = mapview

# (str) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB, #AARRGGBB, or color names (e.g
::contentReference[oaicite:0]{index=0}
 
