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

title = '微信小程序-亚朵'
tokenName = 'yd_wxcookies'


class yd(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'miniapp.yaduo.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
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
            'token': self.token,
            'platType': '6',
            'appVer': '3.24.2',
            'channelId': '300001',
            'activitySource': '',
            'activityId': '',
            'activeId': '',
        }

        res = self.sec.get('https://miniapp.yaduo.com/atourlife/signIn/signIn', params=params, cookies=self.cookies)
        print(res.text)

    def lottery(self):
        params = {
            'token': self.token,
            'platType': '6',
            'appVer': '3.24.2',
            'channelId': '300001',
            'activitySource': '',
            'activityId': '',
            'activeId': '',
            # 随机数0-5
            'code': 0,
        }

        res = self.sec.get('https://miniapp.yaduo.com/atourlife/signIn/lottery', params=params, cookies=self.cookies)
        print(res.text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, yd)
