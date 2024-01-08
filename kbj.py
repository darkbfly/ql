"""
cron: 0 6,18 * * * kbj.py
new Env("微信小程序-康佰家")
env add kbj_token
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
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

title = '微信小程序-康佰家'
tokenName = 'kbj_token'


class kbj(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'app.fjxzj.com',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309071d)XWEB/8461',
            'token': data,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wxe727824701ee66d4/162/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        params = {
            'api': 'signin',
        }
        data = '{}'
        rj = self.sec.post('https://app.fjxzj.com/wxscrm/api/member.php', params=params, data=data).json()
        print(rj)


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
            kbj(i).login()
