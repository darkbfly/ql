import subprocess
import pyautogui
from mytool import *

微信路径 = "D:\Program Files (x86)\Tencent\WeChat\WeChat.exe"


def 打开微信():
    subprocess.run(微信路径)
    点击图片中心("pc-asm", "1.png")
    if 寻找是否存在("pc-asm", "2.png") is False:
        raise Exception("未找到搜一搜图片")
    else:
        点击图片中心("pc-asm", "search.png")
        输入中文('统一快乐星球')
        点击图片中心("pc-asm", "3.png")
        点击图片中心("pc-asm", "4.png", 5)

    点击图片中心("pc-asm", "skip.png", 5)
    点击图片中心("pc-asm", "close2.png", 5)
    if 寻找是否存在("pc-asm", "5.png", 10) is False:
        raise Exception("未找到阿萨姆入口")
    else:
        点击图片中心("pc-asm", "5.png")
        点击图片中心("pc-asm", "6.png", 10)

    time.sleep(1)
    print("开始执行签到任务")
    for i in list(pyautogui.locateAllOnScreen(os.path.dirname(os.path.abspath(__file__)) + "\\pc-asm\\sign.png")):
        print(i)
        pyautogui.click(pyautogui.center(i))
        time.sleep(1)
    print("开始执行其他任务")
    for i in list(pyautogui.locateAllOnScreen(os.path.dirname(os.path.abspath(__file__)) + "\\pc-asm\\finish.png")):
        print(i)
        pyautogui.click(pyautogui.center(i))
        点击图片中心("pc-asm", "close.png")
        time.sleep(1)
    pyautogui.hotkey("alt", "f4")
    pass


if __name__ == '__main__':
    打开微信()
