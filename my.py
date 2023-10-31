"""
0 6,18 * * * my.py
new Env("微信小程序-meiyang会员积分")
env add wyyx_wxcookies
"""
import datetime
# !/usr/bin/env python3
# coding: utf-8

import json
import os
import traceback
import requests
import mytool
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

title = '微信小程序-meiyang会员积分'
tokenName = 'my_auth'

class my():
    def __init__(self, data):
        self.sec = requests.session()
        self.sec.headers = {
            "Host": "smp-api.iyouke.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447",
            "Content-Type": "application/json",
            "xweb_xhr": "1",
            "appId": "wx6f13395a8ec0b261",
            "xy-extra-data": "appid=wx6f13395a8ec0b261;version=1.6.21;envVersion=release;senceId=1256",
            "envVersion": "release",
            "version": "1.6.21",
            "Accept": "*/*",
            "Referer": "https://servicewechat.com/wx755f4d86f9328dce/28/page-frame.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Authorization": data
        }

    def login(self):
        current_date = datetime.date.today().strftime("%Y/%m/%d")
        formatted_date = current_date.replace("/", "%2F")
        full_url = f"https://smp-api.iyouke.com/dtapi/pointsSign/user/sign?date={formatted_date}"
        response = self.sec.get(full_url)
        print(response.text)

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
            my(i).login()
