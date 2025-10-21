"""
cron: 0 6,18 * * * kbj.py
new Env("微信小程序-康佰家")
env add kbj_token

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
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
tokenName = 'kbj_token1'


class kbj(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'vip-mall.kbjcn.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541110) XWEB/16729',
            'xweb_xhr': '1',
            'oldToken': data,
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wxe727824701ee66d4/209/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }


    def login(self):
        rj = self.sec.post('https://vip-mall.kbjcn.com/vip/integral/sign', json={}).json()
        print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, kbj)
