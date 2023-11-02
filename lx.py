"""
cron: 0 7 * * * lx.py
new Env("微信小程序-联想会员中心")
env add lx_data
"""

import json
import os
import traceback
import requests
import urllib3
import mytool

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

title = '微信小程序-联想会员中心'
tokenName = 'lx_data'

class lx():
    def __init__(self, data):
        self.sec = requests.session()
        self.sec.headers = {
            'Host': 'mmembership.lenovo.com.cn',
            'Connection': 'keep-alive',
            'accessToken': data[0],
            'serviceToken': f'Bearer {data[1]}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309071d)XWEB/8461',
            'tenantId': '25',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'SERVICE-AUTHENTICATION': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXJ2aWNlTmFtZSI6IjM5MiIsInNlcnZpY2VLZXkiOiIxMzQ1MTEyZGI4YmE0MjBhYjI1MzNjOTc1NjgzNjBjNCIsInNlcnZpY2VUeXBlIjoiMSIsInNlcnZpY2VBcHAiOiIxODMiLCJzZXJ2aWNlQ2x1c3RlciI6IjEwIiwianRpIjoiOWU2ODQ0M2E2ZDFiNDllNzk1YTNlZGFmODJhZmQxNjEiLCJpYXQiOjE1NTU5MDU5NDl9.rYH1XF9xjUgW9w-4XD6OxVzal_iK3qLvPxzkPBfo0fI',
            'lenovoId': '10270134324',
            'Referer': 'https://servicewechat.com/wx87d0173173a58332/162/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        params = {
            'lenovoId': '10270134324',
        }

        json_data = {}

        response = self.sec.post(
            'https://mmembership.lenovo.com.cn/member-hp-task-center/v1/task/checkIn',
            params=params,
            json=json_data,
        ).json()

        print(response)

if __name__ == '__main__':
    # DEBUG
    if os.path.exists('debug.py'):
        import debug
        debug.setDebugEnv()

    if mytool.getlistCk(f'{tokenName}') is None:
        print(f'请检查你的变量名称 {tokenName} 是否填写正确')
        exit(0)
    else:
        for i in mytool.getlistCk(f'{tokenName}'):
            lx(i.split('#')).login()