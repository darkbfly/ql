import asyncio
import os
import subprocess

import pyperclip
from pywebio import start_server, config
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

from updateCookie_Util import *

电话号码列表 = []


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
    USERID = value.split('USERID=')[1].split(";")[0]
    for i in searchEnvs(name=ckname):
        USERID2 = i['value'].split('USERID=')[1].split(";")[0]
        if USERID2 == USERID:
            put_text(f'已经存在 {i["id"]} {USERID}')
            deleteEnv(i['id'])
    if postEnv(ckname, value, info['remark']):
        put_text('更新成功')
    else:
        put_text('更新失败')
    time.sleep(5)
    go_app('饿了么ck更新', new_window=False)
    pass


def 京东登录(x):
    pyperclip.copy("")
    cmd = 'python.exe JDLogin.py --account ' + x
    st = subprocess.STARTUPINFO()
    st.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    st.wShowWindow = subprocess.SW_HIDE
    p = subprocess.Popen(cmd,
                         bufsize=1,
                         creationflags=subprocess.CREATE_NEW_CONSOLE,
                         startupinfo=st)
    p.wait()
    put_text(f'运行结束 {x}返回{pyperclip.paste()}')
    if len(pyperclip.paste()) != 0:
        return pyperclip.paste()
    else:
        return None


@config(title='京东ck更新')
def 京东ck更新():
    ckname = 'JD_COOKIE'
    for x in 电话号码列表:
        put_text(f'开始更新{x}')
        value = 京东登录(x)
        if 'pt_pin=' in value:
            USERID = value.split('pt_pin=')[1].split(";")
            for i in searchEnvs(name=ckname):
                USERID2 = i['value'].split('pt_pin=')[1].split(";")
                if USERID2 == USERID:
                    put_text(f'已经存在 {i["id"]} {USERID}')
                    deleteEnv(i['id'])
            if postEnv(ckname, value, x):
                put_text(x + ' 更新成功')
            else:
                put_text(x + '更新失败')
        else:
            continue

    # time.sleep(5)
    # go_app('京东ck更新', new_window=False)


if __name__ == '__main__':
    with open('config.json', 'r') as f:
        config = json.load(f)
        电话号码列表 = config['phoneList']

    os.environ['PYWEBIO_THEME'] = 'dark'
    隐藏cmd对话框()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start_server(
        [
            饿了么ck更新,
            京东ck更新
        ],
        port=28989
    )
