"""
cron: 0 7 * * *
new Env("微信小程序-红旗空间")
env add hqkj_data
hqkj_data 值为cookie 内容为 JSESSIONID=XXX 即可
可能返回是报错 实际是积分加的
"""

import json
import os
import traceback
import requests
import urllib3

import ApiRequest
import mytool

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

title = '微信小程序-红旗空间'
tokenName = 'hqkj_data'


class hqkj(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'hqpp-gw.faw.cn',
            'Connection': 'keep-alive',
            'cookie': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819) XWEB/8531',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wxf076d8670405c937/166/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        params = {
            '_timestamp': str(mytool.getMSecTimestamp()),
        }
        rj = self.sec.get('https://hqpp-gw.faw.cn/gimc-hongqi-webapp/f/checkin/user-checkin/', params=params).json()
        print(rj) # 虽然报错 但是实际上能签到成功



if __name__ == '__main__':
    # DEBUG
    # if os.path.exists('debug.py'):
    #     import debug
    #     debug.setDebugEnv()
    #
    # if mytool.getlistCk(f'{tokenName}') is None:
    #     print(f'请检查你的变量名称 {tokenName} 是否填写正确')
    #     exit(0)
    # else:
    #     for i in mytool.getlistCk(f'{tokenName}'):
    #         hqkj(i).login()
    ApiRequest.ApiMain(['login']).run(tokenName, hqkj)