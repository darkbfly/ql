"""
cron: 30 7 * * *
new Env("微信小程序-康师傅畅饮社")
env add ksfcys_data
"""
import json
import os
import traceback
import requests

import ApiRequest
import mytool
from notify import send
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '微信小程序-康师傅畅饮社'
tokenName = 'ksfcys_data'


class ksfcys(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'club.biqr.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'xweb_xhr': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309080f)XWEB/8501',
            'Token': data,
            'Content-Type': 'application/x-www-form-urlencoded;',
            'Referer': 'https://servicewechat.com/wx54f3e6a00f7973a7/470/page-frame.html',
        }

    def login(self):
        response = self.sec.post('https://club.biqr.cn/api/signIn/integralSignIn', params='', data='{}')
        if response.status_code == 200:
            rj = response.json()
            if rj['code'] == 0:
                msg = f"签到成功"
            else:
                msg = f"签到失败\n" + json.dumps(rj, ensure_ascii=False)
        else:
            msg = f"签到失败\n" + json.dumps(response.text, ensure_ascii=False)
        print(msg)

if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, ksfcys)