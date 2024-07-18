import datetime
import os
import time
import traceback

import keyboard
import win32con
import win32gui
import mytool

bPuase = False
def toggle_pause():
    global bPuase
    bPuase = not bPuase
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "循环" + ("暂停" if bPuase else "恢复"))


def 点击图片中心(path="", png="", timeout=3):
    import pyautogui
    time.sleep(1)
    if len(path) > 0:
        filename = os.path.dirname(os.path.abspath(__file__)) + f'\\{path}\\{png}'
    else:
        filename = os.path.dirname(os.path.abspath(__file__)) + f'\\{png}'
    if 寻找是否存在(path, png, timeout):
        print(f"找到{png}, 开始执行")
        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen(filename, confidence=0.8)))


def 淘宝拖动():
    import pyautogui
    png = 'taobao-do.png'
    filename = os.path.dirname(os.path.abspath(__file__)) + f'\\{png}'
    icount = 0
    while icount < 3:
        if 寻找是否存在(path='', png=png, timeout=1):
            print(f"找到{png}, 开始执行")
            点击图片中心(path='', png='do.png', timeout=1)
            start_x, start_y = pyautogui.center(pyautogui.locateOnScreen(filename, confidence=0.8))
            pyautogui.moveTo(start_x, start_y, duration=0.1)
            time.sleep(1)
            end_x = start_x + 500 + mytool.randomint(2)
            end_y = start_y + 20 + mytool.randomint(1)
            pyautogui.dragTo(end_x, end_y, duration=0.3)
        icount += 1
        time.sleep(1)
        if 寻找是否存在(path='', png='taobao-verify-error.png', timeout=1):
            点击图片中心(path='', png='taobao-verify-error.png', timeout=1)
            time.sleep(1)
            continue
        else:
            点击图片中心(path='', png='finish.png', timeout=1)
            break



def 寻找是否存在(path="", png="", timeout=3):
    import pyautogui
    try:
        while timeout > 0:
            if len(path) > 0:
                filename = os.path.dirname(os.path.abspath(__file__)) + f'\\{path}\\{png}'
            else:
                filename = os.path.dirname(os.path.abspath(__file__)) + f'\\{png}'
            if pyautogui.locateOnScreen(filename, confidence=0.8) is None:
                timeout -= 1
                time.sleep(1)
                continue
            else:
                return True
        return False
    except Exception:
        traceback.print_exc()
        return False


def find_windows_by_title(title):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and title in win32gui.GetWindowText(hwnd):
            hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds

def 保存图片():
    import pyautogui
    filename = os.path.dirname(os.path.abspath(__file__)) + f'\\{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.png'
    pyautogui.screenshot(filename)

def run_jd():
    print("开始查找京东窗口")
    for x in find_windows_by_title("京东"):
        # 设置窗口状态为最前
        win32gui.SetForegroundWindow(x)
        # 最大化
        win32gui.ShowWindow(x, win32con.SW_MAXIMIZE)
        time.sleep(1)
        if 寻找是否存在(path="", png="do.png"):
            print("找到 手工处理")
            if 寻找是否存在(path="", png="jd-verify.png"):
                print("需要验证")
                点击图片中心(path="", png="do.png")
                time.sleep(5)
                点击图片中心(path="", png="jd-verify.png")
                time.sleep(5)
                if 寻找是否存在(path="", png="jd-start-verify.png"):

                    保存图片()
                    点击图片中心(path="", png="finish.png")
        win32gui.ShowWindow(x, win32con.SW_MINIMIZE)


def run_taobao():
    print("开始查找淘宝窗口")
    for x in find_windows_by_title("淘宝"):
        time.sleep(1)
        if bPuase:
            continue
        try:
            # 设置窗口状态为最前
            win32gui.SetForegroundWindow(x)
            # 最大化
            win32gui.ShowWindow(x, win32con.SW_MAXIMIZE)
            if 寻找是否存在(path="", png="taobao-verify.png", timeout=1) or 寻找是否存在(path="", png="taobao-do.png",
                                                                                         timeout=1):
                print("找到 手工处理")
                淘宝拖动()
            # win32gui.ShowWindow(x, win32con.SW_MINIMIZE)
        except Exception:
            pass



if __name__ == '__main__':
    keyboard.add_hotkey('p', toggle_pause)
    while True:
        run_taobao()
