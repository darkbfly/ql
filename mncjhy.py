"""
0 7 * * * mncjhy.py
new Env("微信小程序-蒙牛超级会员")
env add mncjhy_token
"""
# !/usr/bin/env python3
# coding: utf-8
import os
import requests
import urllib3
import mytool
from notify import send
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '微信小程序-蒙牛超级会员'
tokenName = 'mncjhy_token'
msg = ''


class mncjhy():
    def __init__(self, data):
        self.headers = {
            'Host': 'h5.youzan.com',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'Extra-Data': f'{{"is_weapp":1,"sid":"YZ1161692133138784256YZQVT38EbS","version":"2.145.3.101024","client":"weapp","bizEnv":"wsc","uuid":"056Z2dlcvP6tQzK1697010559505","ftime":{mytool.getMSecTimestamp()}}}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wx4332719bca2e4089/58/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        self.token = data
        pass

    def login(self):
        global msg
        params = {
            'checkinId': '3549859',
            'app_id': 'wx4332719bca2e4089',
            'kdt_id': '130177909',
            'access_token': self.token,
        }
        rj = self.sec.get('https://h5.youzan.com/wscump/checkin/checkinV2.json', params=params).json()
        if rj['code'] == 0:
            msg = f"登录成功\n获得：{rj['data']['list'][0]['infos']['title']}"
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
            mncjhy(i).login()
