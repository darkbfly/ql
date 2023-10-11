"""
0 7 * * * yxt.py
new Env("一心堂")
env add yxtGUid
"""
# !/usr/bin/env python3
# coding: utf-8

import json
import os
import traceback
import requests
import mytool
from notify import send
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '一心堂'
tokenName = 'yxtGUid'
msg = ''


class yxt():
    def __init__(self, data):
        self.headers = {
            'Host': 'shopapi.yxtmart.cn',
            'Connection': 'keep-alive',
            # 'Content-Length': '283',
            'xweb_xhr': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wx0730cf00e5f0de87/18/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        self.UserGuid = data
        pass

    def login(self):
        data = {
            'QueryType': 'User_signin',
            'UserGuid': self.UserGuid,
            'Params': '{"CRMCUSTOMERID":"1072014230"}',
        }
        rj = self.sec.post('https://shopapi.yxtmart.cn/PointsHandle', data=data).json()
        if rj['CODE'] == '1000':
            msg = f"登录成功\n"
        else:
            msg = f"登录失败\n" + json.dumps(rj, ensure_ascii=False)
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
            yxt(i).login()
