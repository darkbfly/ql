"""
cron: 0 6,18 * * *
new Env("微信小程序-朴朴")
env add pupu_token
userid#cityzip#suid#auth#lat#lng
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

title = '微信小程序-朴朴'
tokenName = 'pupu_token'


class pupu(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'j1.pupuapi.com',
            'Connection': 'keep-alive',
            'pp-userid': data[0],
            'pp-cityzip': data[1],
            'pp-suid': data[2],
            'Authorization': data[3],
            'pp-os': '001',
            'Accept': 'application/json, text/plain, */*',
            # 'pp-placeid': '42758daa-78ec-451a-b668-a270b17e88e3',
            'pp-version': '2023019200',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819) XWEB/8531',
            # 'pp_storeid': '7f7adc3e-ffa5-473d-a082-9a346fdf929c',
            'Origin': 'https://ma.pupumall.com',
        }
        self.params = {
            'supplement_id': '',
            'lat_y': data[4],
            'lng_x': data[5],
        }

    def login(self):

        data = '{}'
        rj = self.sec.post('https://app.fjxzj.com/wxscrm/api/member.php', params=self.params, data=data).json()
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
            pupu(i.split('#')).login()
