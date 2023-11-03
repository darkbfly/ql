"""
cron: 0 7 * * * ryytn.py
new Env("微信小程序-认养一头牛商城")
env add lx_data
"""

import json
import os
import traceback
import requests
import urllib3
import mytool

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

title = '微信小程序-认养一头牛商城'
tokenName = 'ryytn_data'

class lx():
    def __init__(self, data):
        self.sec = requests.session()
        self.sec.headers = {
            'Host': 'www.milkcard.mall.ryytngroup.com',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'X-Auth-Token': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309071d)XWEB/8461',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wx0408f3f20d769a2f/234/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        response = self.sec.post('https://www.milkcard.mall.ryytngroup.com/mall/xhr/task/checkin/save', json={}).json()
        print(response)

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
            lx(i).login()