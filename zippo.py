
"""
cron: 30 7 * * *
new Env("微信小程序-zippo")
env add tpyqc_common_session_id
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
            # 'Content-Length': '291',
            'x-app-id': 'zippo',
            'x-platform-id': 'wxaa75ffd8c2d75da7',
            'x-platform-env': 'release',
            'x-platform': 'wxmp',
            'Authorization': data,
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819) XWEB/8531',
            'xweb_xhr': '1',
            'Referer': 'https://servicewechat.com/wxaa75ffd8c2d75da7/69/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        pass


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
            zippo(i).login()
