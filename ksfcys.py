"""
cron: 30 7 * * *
new Env("微信小程序-康师傅畅饮社")
env add ksfcys_data

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import json
import os
import traceback
import requests

import ApiRequest
import mytool
from notify import send
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '微信小程序-康师傅畅饮社'
tokenName = 'ksfcys_data'


class ksfcys(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'club.gdshcm.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'xweb_xhr': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309080f)XWEB/8501',
            'Token': data,
            'Content-Type': 'application/x-www-form-urlencoded;',
            'Referer': 'https://servicewechat.com/wx54f3e6a00f7973a7/470/page-frame.html',
        }

    def login(self):
        response = self.sec.post('https://club.gdshcm.com/api/signIn/integralSignIn', params='', data='{}')
        if response.status_code == 200:
            rj = response.json()
            if rj['code'] == 0:
                msg = f"签到成功"
            else:
                msg = f"签到失败\n" + json.dumps(rj, ensure_ascii=False)
        else:
            msg = f"签到失败\n" + json.dumps(response.text, ensure_ascii=False)
        print(msg)

if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, ksfcys)