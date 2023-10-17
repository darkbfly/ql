import os
import random
import re
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import pyautogui
import pyperclip


def getlistCk(ckname):
    if os.getenv(ckname) is None:
        return None
    # 字符串用回车或@符号分开为list
    return re.split(r'\n|@', os.getenv(ckname))


# 获取北京时间 带时区
def gettime():
    return datetime.now(tz=ZoneInfo('Asia/Shanghai'))

def getSecTimestamp():
    return int(time.time())
def getMSecTimestamp():
    return int(time.time() * 1000)


# 随机休眠几秒 随机数为float
def sleep(x, y):
    time.sleep(random.uniform(x, y))



def 输入中文(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


def 点击图片中心(path, png, timeout=1):
    if 寻找是否存在(png, timeout):
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(os.getcwd() + f'\\{path}\\{png}', confidence=0.8)))


def 寻找是否存在(path, png, timeout=2):
    while timeout > 0:
        if pyautogui.locateOnScreen(os.getcwd() + f'\\{path}\\{png}', confidence=0.8) is None:
            timeout -= 1
            time.sleep(1)
            continue
        else:
            return True
    return False

if __name__ == '__main__':
    print(getMSecTimestamp())