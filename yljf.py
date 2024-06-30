"""
cron: 0 7 * * * yljf.py
new Env("微信小程序-伊利积分")
env add yljf_token

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
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
title = '微信小程序-伊利积分'
tokenName = 'yljf_token'
msg = ''


class yljf(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'msmarket.msx.digitalyili.com',
            'Connection': 'keep-alive',
            'access-token': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
            'Referer': 'https://servicewechat.com/wx1fb666a33da7ac88/13/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        global msg
        rj = self.sec.post('https://msmarket.msx.digitalyili.com/gateway/api/member/daily/sign', json={}).json()
        if rj['status']:
            msg = f"登录成功\n获得积分：{rj['data']['dailySign']['bonusPoint']}"
        else:
            msg = f"登录失败\n" + json.dumps(rj, ensure_ascii=False)
        print(msg)
        send(title, msg)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, yljf)