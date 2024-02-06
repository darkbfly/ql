start cmd /k adb shell "su -c /data/local/tmp/frida-server"
frida -U -f com.xx.tanwo -l ./sslkeyfilelog.js --no-pause
pause
