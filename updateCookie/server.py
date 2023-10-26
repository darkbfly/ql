import ctypes
import json
import os
import pprint
import time

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from listDialog import runDialog

app = FastAPI()
目前电话 = ''

def updateFile(file_path, name, value):
    global 目前电话
    文件路径 = os.path.dirname(os.path.abspath(__file__)) + "\\" + 目前电话 + '-' + file_path
    if not os.path.exists(文件路径):
        # 文件不存在,创建文件并写入内容
        with open(文件路径, 'w') as f:
            content = {'name': name, 'value': value, 'remark': 目前电话}
            json.dump(content, f)

    else:
        # 文件已存在,判断内容是否相同
        with open(文件路径, 'r') as f:
            content = json.load(f)

        if content['value'] != value:
            content['value'] = value
            content['remark'] = 目前电话
            # 内容不同,修改内容
            with open(文件路径, 'w') as f:
                f.write(json.dumps(content, ensure_ascii=False))


class Request(BaseModel):
    url: str
    method: str
    host: str
    path: str
    body: str
    headers: dict
    queries: dict
    context: dict


@app.post("/xapi.weimob.com")
def 统一快乐星球(data: Request):
    updateFile("xapi.weimob.com.txt", 'tyklxq_cookies', data.headers['X-WX-Token'])
    return data.headers['X-WX-Token']

@app.post("/ucode-openapi.aax6.cn")
def 甄爱粉俱乐部(data: Request):
    updateFile("ucode-openapi.aax6.cn.txt", 'zaf_auth', data.headers['Authorization'])
    return data.headers['Authorization']

@app.post("/m.jissbon.com")
def 杰士邦安心福利社(data: Request):
    updateFile("m.jissbon.com.txt", 'jsbaxfls', data.headers['Access-Token'])
    return data.headers['Access-Token']

@app.post("/www.kozbs.com")
def 植白说(data: Request):
    updateFile("www.kozbs.com.txt", 'zbsxcx', data.headers['X-Dts-Token'])
    return data.headers['X-Dts-Token']
@app.post("/kraftheinzcrm.kraftheinz.net.cn")
def 卡夫亨(data: Request):
    updateFile("kraftheinzcrm.kraftheinz.net.cn.txt", 'kfw_data', data.headers['token'])
    return data.headers['token']

@app.post("/api.wincheers.net")
def 罗技粉丝俱乐部(data: Request):
    updateFile("api.wincheers.net.txt", 'ljfsjlbCookie', data.headers['Authorization'])
    return data.headers['Authorization']

def 隐藏cmd对话框():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)


def get_list_item_by_index(data_list):
    """根据索引获取列表项"""
    cnt = 0
    for x in data_list:
        print(f'{cnt} -- {x}')
        cnt += 1
    index = int(input("请输入要获取的列表项索引:"))
    if index < 0 or index >= len(data_list):
        raise Exception("索引超出范围")

    return (data_list[index])

if __name__ == '__main__':
    电话号码列表 = [
        '13055789923',
        '13107644225',
        '13107631307',
        '13255991819',
        '空数据'
    ]
    目前电话 = get_list_item_by_index(电话号码列表)
    uvicorn.run(app, host="0.0.0.0", port=8989)
