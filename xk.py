"""
new Env("WEB-星空代理IP")
cron 0 7 * * *
环境变量名称 xk_data
"""

import datetime
import json
import os
import traceback
import ApiRequest
import mytool
from notify import send

title = 'WEB-星空代理IP'
tokenName = 'xk_data'


class xk(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'www.xkdaili.com',
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://www.xkdaili.com',
            'Referer': 'https://www.xkdaili.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.username = data[0]
        self.password = data[1]

    def login(self):

        data = {
            'username': self.username,
            'password': self.password,
            'remember': '1',
            'code': '',
        }

        rj = self.sec.post('https://www.xkdaili.com/tools/submit_ajax.ashx?action=user_login&site_id=1&', data=data).json()
        if rj['status'] == 1:
            print('登录成功')
            self.sign()
        else:
            print('登录失败\n' + json.dumps(rj, ensure_ascii=False))

    def sign(self):
        data = {
            'type': 'login',
        }

        rj = self.sec.post(
            'http://www.xkdaili.com/tools/submit_ajax.ashx?action=user_receive_point&',
            data=data,
        )
        print(rj.text)


if __name__ == "__main__":
    ApiRequest.ApiMain(['login']).run(tokenName, xk)