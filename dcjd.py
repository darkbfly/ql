
"""
cron: 30 7 * * * dcjd.py
new Env("微信小程序-东呈酒店")
env add tyklxq_cookies
"""
#!/usr/bin/env python3
# coding: utf-8
import json
import os
import traceback
import requests
import mytool
from notify import send
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '微信小程序-东呈酒店'
tokenName = 'dcjd_data'

class dcjd():
    def __init__(self, data):
        self.headers = {
            'Host': 'campaignapi.dossen.com',
            'Connection': 'keep-alive',
            'Dossen-Platform': 'WxMiniApp',
            'DOSSENSESSIONID': 'D778FE1C3AFB426B88ED04AB41B0B0211696665839712',
            'access_token': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8391',
            'Content-Type': 'application/json',
            'Referer': 'https://servicewechat.com/wxa4b8c0bda7f71cfc/255/page-frame.html',
            'Accept-Language': 'zh-CN,zh',
        }
        self.sec = requests.session()
        self.sec.headers = self.headers

    def login(self):
        params = {
            'blackbox': 'eyJvcyI6Ind4YXBwIiwidCI6IisxSUlrZFVCb2pUK2dOZyt6Wk1xZzhhd0xqR0dwWHdnNjBqQzgrbk9URE1md0VCN3ZPSDZHWHcrRGJZK2I4WDN3dm5UVWQxcFErVjh3WFN1NUZpWUFnPT0iLCJ2IjoiSWxKSDRrQWpUbi9lb2dGM2FrZ2phRz09IiwicGFydG5lciI6ImRvc3NlbiIsInAiOjgxfQ==',
        }
        response = self.sec.get('https://campaignapi.dossen.com/selling/checkin/do', params=params, verify=False)
        if response.status_code == 200:
            rj = response.json()
            if rj['code'] == 0:
                msg = f"签到成功\n获得{rj['results']}积分！"
            else:
                msg = f"签到失败\n" + json.dumps(rj, ensure_ascii=False)
        else:
            msg = f"签到失败\n" + json.dumps(response.json(), ensure_ascii=False)

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
            dcjd(i).login()
