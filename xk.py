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
            'Proxy-Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'DNT': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://www.xkdaili.com',
            'Referer': 'http://www.xkdaili.com/main/usercenter.aspx',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
        }
        self.cookies = {
            'ASP.NET_SessionId': data,
            # 'Hm_lvt_d76458121a7604d3e55d998f66ef0be6': '1698978156,1699335435',
            # 'Hm_lpvt_d76458121a7604d3e55d998f66ef0be6': '1699335435',
            # 'dt_cookie_user_name_remember': 'DTcms=13107644225',
            # 'dt_cookie_user_pwd_remember': 'DTcms=wlwzzfz123',
        }

    def login(self):
        data = {
            'type': 'login',
        }

        rj = self.sec.post(
            'http://www.xkdaili.com/tools/submit_ajax.ashx?action=user_receive_point&',
            data=data,
            cookies=self.cookies
        )
        print(rj.text)

if __name__ == "__main__":

    # DEBUG
    if os.path.exists('debug.py'):
        import debug

        debug.setDebugEnv()
    if mytool.getlistCk(f'{tokenName}') is None:
        print(f'请检查你的变量名称 {tokenName} 是否填写正确')
        exit(0)
    else :
        for i in mytool.getlistCk(f'{tokenName}'):
            xk(i).login()