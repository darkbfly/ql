"""
cron: 0 7 * * * mncjhy.py
new Env("微信小程序-甄爱粉俱乐部")
env add zaf_auth
"""
# !/usr/bin/env python3
# coding: utf-8
import os
import requests
import urllib3

import ApiRequest
import mytool
from notify import send
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '微信小程序-甄爱粉俱乐部'
tokenName = 'zaf_auth'
msg = ''

class zaf(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'ucode-openapi.aax6.cn',
            'Connection': 'keep-alive',
            'serialId': '0b7d9e70-1092-45dd-a67e-e1bc77377f70',
            'appId': 'wx888d2a452f4a2a58',
            'Authorization': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
            'Referer': 'https://servicewechat.com/wx888d2a452f4a2a58/155/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        json_data = {
            'promotionId': 1001681,
            'promotionCode': 'CRM-QD',
            'pointRecordRemark': '连续签到',
        }
        rj = self.sec.post('https://ucode-openapi.aax6.cn/lottery/checkIn', json=json_data).json()
        print(json.dumps(rj, ensure_ascii=False))
        try:
            if rj['isHit']:
                msg = f"签到成功, 获得:{rj['award']['name']}"
            else:
                msg = f"签到失败\n" + json.dumps(rj, ensure_ascii=False)
        except:
            msg = f"签到异常\n" + json.dumps(rj, ensure_ascii=False)

        print(msg)
        send(title, msg)

if __name__ == '__main__':
    if os.path.exists('debug.py'):
        import debug
        debug.setDebugEnv()

    if mytool.getlistCk(f'{tokenName}') is None:
        print(f'请检查你的变量名称 {tokenName} 是否填写正确')
        exit(0)
    else:
        for i in mytool.getlistCk(f'{tokenName}'):
            zaf(i).login()