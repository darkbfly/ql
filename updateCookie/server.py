import json
import os
import pprint
from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


def updateFile(file_path, name, value):
    if not os.path.exists(file_path):
        # 文件不存在,创建文件并写入内容
        with open(file_path, 'w') as f:
            content = {'name': name, 'value': value}
            json.dump(content, f)

    else:
        # 文件已存在,判断内容是否相同
        with open(file_path, 'r') as f:
            content = json.load(f)

        if content['value'] != value:
            content['value'] = value
            # 内容不同,修改内容
            with open(file_path, 'w') as f:
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

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8989)
