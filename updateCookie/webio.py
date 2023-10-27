import asyncio
import ctypes
import os, re
import subprocess
import time

import pyperclip
from playwright.sync_api import sync_playwright
from pywebio import start_server, config
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

from updateCookie_Util import *

电话号码列表 = [
    '13055789923',
    '13107644225',
    '13107631307',
    '13255991819'
]


def 隐藏cmd对话框():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)


@config(title='饿了么ck更新')
def 饿了么ck更新():
    ckname = 'elmck'
    info = input_group('',
                       [
                           input('cookies值', name='val', required=True),
                           input('备注[一般写电话号码]', name='remark', datalist=电话号码列表, required=True),
                       ]
                       )
    value = info['val']
    USERID = re.search(r"USERID=(\d+);", value)
    if USERID:
        USERID = USERID.group(1)
    for i in searchEnvs(name=ckname):
        USERID2 = re.search(r"USERID=(\d+);", i['value'])
        if USERID2:
            USERID2 = USERID2.group(1)
        if USERID2 == USERID:
            deleteEnv(i['id'])
    if postEnv(ckname, value, info['remark']):
        put_text('更新成功')
    else:
        put_text('更新失败')
    time.sleep(5)
    go_app('饿了么ck更新', new_window=False)
    pass


def 京东登录(x):
    cmd = 'C:\\Python310\\python.exe JDLogin.py --account ' + x
    st = subprocess.STARTUPINFO()
    st.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    st.wShowWindow = subprocess.SW_HIDE
    p = subprocess.Popen(cmd,
                         bufsize=1,
                         creationflags=subprocess.CREATE_NEW_CONSOLE,
                         startupinfo=st)
    p.wait()
    put_text(f'运行结束 {x} {pyperclip.paste()}')
    if len(pyperclip.paste()) != 0:
        return pyperclip.paste()
    pass


@config(title='京东ck更新')
def 京东ck更新():
    ckname = 'JD_COOKIE'
    for x in 电话号码列表:
        value = 京东登录(x)
        USERID = re.search(r"pt_pin=(\d+);", value)
        if USERID:
            USERID = USERID.group(1)
        for i in searchEnvs(name=ckname):
            USERID2 = re.search(r"pt_pin=(\d+);", i['value'])
            if USERID2:
                USERID2 = USERID2.group(1)
            if USERID2 == USERID:
                deleteEnv(i['id'])
        if postEnv(ckname, value, x):
            put_text(x + ' 更新成功')
        else:
            put_text(x + '更新失败')

    time.sleep(5)
    go_app('京东ck更新', new_window=False)


if __name__ == '__main__':
    os.environ['PYWEBIO_THEME'] = 'dark'
    隐藏cmd对话框()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start_server(
        [
            饿了么ck更新,
            京东ck更新
        ],
        port=8989,
        debug=True,
    )
