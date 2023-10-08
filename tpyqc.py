
"""
30 7 * * * tpyqc.py
new Env("太平洋汽车")
env add tpyqc_common_session_id
"""
#!/usr/bin/env python3
# coding: utf-8
import json
import os
import time
import traceback
import requests
import mytool
from notify import send
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '太平洋汽车'
tokenName = 'tpyqc_common_session_id'

class tpyqc():
    def __init__(self, data):
        self.headers = {
            'Host': 'app-server.pcauto.com.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; R11&s Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36',
            'Origin': 'https://www1.pcauto.com.cn',
            'X-Requested-With': 'cn.com.pcauto.android.browser',
            'Referer': 'https://www1.pcauto.com.cn/auto-c/front-end-projects/app-h5/index.html',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        self.sec.verify = False
        # self.common_session_id = data
        self.username = data.split('&')[0]
        self.password = data.split('&')[1]

    def login(self):

        response = requests.post('https://mrobot.pcauto.com.cn/auto_passport3_back_intf/passport3/rest/login_new.jsp',
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                 verify=False,
                                 data=f'password={self.password}&username={self.username}')
        if response.status_code == 200:
            rj = response.json()
            print(json.dumps(rj))
            if rj['status'] == 0:
                time.sleep(1)
                params = {
                    'common_session_id': rj['common_session_id'],
                }
                json_data = {}
                response = self.sec.post('https://app-server.pcauto.com.cn/api/info/sign/register', params=params,
                                         json=json_data)
                if response.status_code == 200:
                    rj = response.json()
                    print(json.dumps(rj))
                    if rj['code'] == 0:
                        msg = f"签到成功\n获得{rj['results']}积分！"
                    else:
                        msg = f"签到失败\n" + json.dumps(rj, ensure_ascii=False)
                else:
                    msg = f"签到失败\n" + json.dumps(response.json(), ensure_ascii=False)

            else:
                msg = f"登录失败\n" + json.dumps(rj, ensure_ascii=False)
        else:
            msg = f"登录失败\n" + json.dumps(response.json(), ensure_ascii=False)

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
            tpyqc(i).login()
