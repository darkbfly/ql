"""
cron: 0 6,18 * * *
new Env("微信小程序-亚朵")
env add yd_wxcookies
"""
import datetime
# !/usr/bin/env python3
# coding: utf-8

import json
import os
import traceback
import requests

import ApiRequest
import mytool
from notify import send
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

title = '微信小程序-亚朵'
tokenName = 'yd_wxcookies'


class yd(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'miniapp.yaduo.com',
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'Accept': 'application/json, text/plain, */*',
            'Client-DF': 'pWPSN1697676214tDDRG3cqfj9',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
            'Origin': 'https://wechat.yaduo.com',
            'Referer': 'https://wechat.yaduo.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.cookies = {
            'user-valid': data[0],
        }
        self.token = data[1]

    def login(self):
        params = {
            # 'r': '0.3972955364433912',
            'token': self.token,
            'platType': '6',
            'appVer': '3.20.0',
            'channelId': '300001',
            'activitySource': '',
            'activityId': '',
            'activeId': '',
        }

        res = self.sec.get('https://miniapp.yaduo.com/atourlife/signIn/signIn', params=params, cookies=self.cookies)
        print(res.text)


if __name__ == '__main__':
    # DEBUG
    # if os.path.exists('debug.py'):
    #     import debug
    #
    #     debug.setDebugEnv()
    #
    # if mytool.getlistCk(f'{tokenName}') is None:
    #     print(f'请检查你的变量名称 {tokenName} 是否填写正确')
    #     exit(0)
    # else:
    #     for i in mytool.getlistCk(f'{tokenName}'):
    #         yd(i.split("#")).login()
    ApiRequest.ApiMain(['login']).run(tokenName, yd)