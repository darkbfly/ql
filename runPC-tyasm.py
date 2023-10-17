import os
import subprocess
import time
import pyautogui
import pyperclip
from mytool import *

微信路径 = "D:\Program Files (x86)\Tencent\WeChat\WeChat.exe"



def 打开微信():
    subprocess.run(微信路径)
    点击图片中心("pc-asm", "1.png")
    if 寻找是否存在("pc-asm", "2.png") is False:
        raise Exception("未找到搜一搜图片")
    else:
        输入中文('统一快乐星球')
        点击图片中心("pc-asm", "3.png")
        点击图片中心("pc-asm", "4.png", 5)
    if 寻找是否存在("pc-asm", "5.png", 10) is False:
        raise Exception("未找到阿萨姆入口")
    else:
        点击图片中心("pc-asm", "5.png")
        点击图片中心("pc-asm", "6.png", 10)
    if 寻找是否存在("pc-asm", "signed.png") is False:
        点击图片中心("pc-asm", "sign.png", 7)

    点击图片中心("pc-asm", "finish.png", 10)




if __name__ == '__main__':
    打开微信()
