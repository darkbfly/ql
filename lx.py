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
        self.lenovoId = data[3]
        self.sec.headers = {
            'Host': 'mmembership.lenovo.com.cn',
            'Connection': 'keep-alive',
            # 'Content-Length': '2',
            'accessToken': data[0],
            'serviceToken': data[1],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309071d)XWEB/8461',
            'tenantId': '25',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'SERVICE-AUTHENTICATION': data[2],
            'clientId': '4',
            'xweb_xhr': '1',
            'lenovoId': self.lenovoId,
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wx87d0173173a58332/162/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        params = {
            'lenovoId': self.lenovoId
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
            for y in i.split('#'):
                print(y)
            lx(i.split('#')).login()