
"""
cron: 30 8 * * * tpyqc.py
new Env("微信小程序-雀巢专业餐饮大厨精英荟")
env add qczy_token
"""
#!/usr/bin/env python3
# coding: utf-8
import json
import os
import time
import traceback
import requests
import mytool
from notify import send
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '微信小程序-雀巢专业餐饮大厨精英荟'
tokenName = 'qczy_token'

class qczy():
    def __init__(self, data):
        self.sec = requests.session()
        self.sec.headers = {
            'Host': 'consumer-api.quncrm.com',
            'Connection': 'keep-alive',
            'X-Account-Id': data[1],
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Access-Token': data[0],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309071d)XWEB/8461',
            'Content-Type': 'application/json; charset=UTF-8',
            'Referer': 'https://servicewechat.com/wx48d4ccf2ec281bf5/48/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.sec.verify = False

    def login(self):
        params = {
            'maijsVersion': '1.28.0',
            'clientId': 'e7cb9435-0be2-3893-c373-25fb2a85cf91',
        }

        json_data = {
            'templateIds': [],
        }

        response = self.sec.post(
            'https://consumer-api.quncrm.com/modules/campaigncenter/signin',
            params=params,
            json=json_data,
        )
        if response.status_code == 200:
            rj = response.json()
            msg = f'登录成功\n获得成长值:{rj["rewardGroup"][0]["growth"]} 积分{rj["rewardGroup"][1]["score"]}'
        else:
            msg = f"登录失败\n" + json.dumps(response.json(), ensure_ascii=False)

        print(msg)
        send(title, msg)


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
            qczy(i.split("#")).login()
