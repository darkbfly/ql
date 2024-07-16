
"""
cron: 30 7 * * *
new Env("微信小程序-zippo")
env add zippo_auth
未完成
"""
#!/usr/bin/env python3
# coding: utf-8
import json
import os
import time
import traceback
import requests

import ApiRequest
import mytool
from notify import send
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '微信小程序-zippo'
tokenName = 'zippo_auth'


class zippo(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'wx-center.zippo.com.cn',
            'Connection': 'keep-alive',
            'x-app-id': 'zippo',
            'x-platform-id': 'wxaa75ffd8c2d75da7',
            'x-platform-env': 'release',
            'x-platform': 'wxmp',
            'Authorization': data,
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819) XWEB/8531',
            'xweb_xhr': '1',
            'Referer': 'https://servicewechat.com/wxaa75ffd8c2d75da7/69/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        rj = self.sec.post('https://wx-center.zippo.com.cn/api/daily-signin', params='', json={}).json()
        print(rj)
        pass

    def favorited(self):
        jsonData = {
            "targetType": "sku",
            "targetId": "265",
            "favorited": True
        }
        rj = self.sec.post('https://wx-center.zippo.com.cn/api/favorites', params='', json=jsonData).json()
        print(rj)

        rj = self.sec.post('https://wx-center.zippo.com.cn/api/missions/5/rewards', params='', json={"id":5}).json()
        print(rj)
        pass

    def unfavorited(self):
        jsonData = {
            "targetType": "sku",
            "targetId": "265",
            "favorited": False
        }
        rj = self.sec.post('https://wx-center.zippo.com.cn/api/favorites', params='', json=jsonData).json()
        print(rj)
        pass



if __name__ == '__main__':
    ApiRequest.ApiMain(['login', 'unfavorited', 'favorited']).run(tokenName, zippo)