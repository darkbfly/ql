start cmd /k adb shell "su -c /data/local/tmp/frida-server"
frida -U -f com.hoge.android.jinhua -l ./okhttp3-1.js --no-pause
pause
