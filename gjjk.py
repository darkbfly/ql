"""
new Env("微信小程序-高济健康")
cron 0 7 * * *
环境变量名称 wx_gjjkpro_data

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""

import datetime
import json
import os
import traceback
import requests

import ApiRequest
import mytool
from notify import send

title = '微信小程序-高济健康'
tokenName = 'wx_gjjkpro_data'


class gjjk(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'api.gaojihealth.cn',
            'Connection': 'keep-alive',
            # 'Content-Length': '61',
            'Authorization': data.split('#')[1],
            'usign-group': 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiI0MDAzMDMwMDE5NDcxMTI5Iiwib3BlbklkIjpudWxsLCJyb2xlcyI6IltcIkdKX0FQUF9VU0VSXCJdIiwiYnVzaW5lc3NJZCI6IjcxMTI5IiwiaGVhZFVybCI6bnVsbCwiZ2pqRmxhZyI6dHJ1ZSwidHlwZSI6IjIiLCJwbGF0Zm9ybSI6ZmFsc2UsImNsaWVudF9pZCI6IndlYl9hcHAiLCJtaW5pT3BlbklkIjoib3B0eGQ1Yy0zS0dWaWd3ekNRV1JGOGM5Sk94ZyIsInBsYXRmb3JtQnVzaW5lc3NJZCI6IjIxMjc5OCIsInBsYXRmb3JtVXNlcklkIjoiNDAwMzAyNzI2MTAxMjc5OCIsInNjb3BlIjpbIm9wZW5pZCJdLCJsb2dpbk5hbWUiOjQwMDMwMzAwMTk0NzExMjksImV4cCI6MTY5OTI5MjU4NCwianRpIjoiYzI1YzdlOTYtZWYwMC00NzBiLThjZGMtMDE1YzA2MzA1ZTY1IiwidW5pb25JZCI6Im9XTXM0MU1OZFpkdFVRMzJ3elptRG1ibVZwYm8iLCJ1c2VySWQiOiI0MDAzMDMwMDE5NDcxMTI5IiwiYXV0aG9yaXRpZXMiOlsiR0pfQVBQX1VTRVIiXSwicGhvbmUiOiIxMzA1NTc4OTkyMyIsIm5hbWUiOm51bGwsImlzTmV3TWVtYmVyIjpmYWxzZSwiZW5jb2RlUGhvbmUiOiIxMzAqKioqOTkyMyIsInd4QmluZFN0YXR1cyI6dHJ1ZSwiZ3JhbnRUeXBlIjoiZ2pfYXBwX2F1dGgiLCJzdGF0dXMiOiIzIn0.a9ioxxm-uITw8Px2LfQmoV2JjCawiHp57287v99an5m5zkU8m5ZT6ALEbpEGdpIw7OOY_MID6ip3qw140PePvKOYGi3l-nqEQWvfaOzVpH2sxAHZjrmfPQaoa6IHFKJRbbx1gUR1pDys2anhFm2le9f6qVpt0MSd4eVagIhle6PiayBZ8DpJYStY5xQbkex5yEmuraaxfGt9YC0Ku5X5CjqtbNzRll4cqH_Sf8Y1WiWQT8QOyyNsc5prAcaSw9QfQ-1rrAWK82z2R6bicm8MY-YxJHGZbDrvKS0UpAbDNVkbLznxIz_mS6kHfR5V6nTOoNUjcSUJ9TxsNevH4-UlTQ',
            'siteId': 'miniprogram',
            'grantType': 'gj_app_auth',
            'biz-market': 'undefined',
            'from-channel': 'gjjk_pro',
            'lastStart': '1053',
            'biz-identity': 'undefined',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309071d)XWEB/8461',
            'Content-Type': 'application/json;charset=UTF-8;',
            'xweb_xhr': '1',
            'client-id': 'miniprogram',
            'from-channelv2': 'gjjk_pro',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wx73ec617ea0a6c8e8/1069/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.userId = data.split('#')[0]

    def login(self):
        params = ''

        json_data = {
            'businessId': 71129,
            'userId': self.userId,
            'taskId': 372,
        }
        rj = self.sec.post(
            'https://api.gaojihealth.cn/gulosity/api/dkUserEvent/everyDaySign',
            params=params,
            json=json_data,
        ).json()
        print(json.dumps(rj, ensure_ascii=False))


if __name__ == "__main__":
    # DEBUG
    # if os.path.exists('debug.py'):
    #     import debug
    #
    #     debug.setDebugEnv()
    #
    # if mytool.getlistCk(f'{tokenName}') is None:
    #     print(f'请检查你的变量名称 {tokenName} 是否填写正确')
    #     exit(0)
    # else:
    #     for i in mytool.getlistCk(f'{tokenName}'):
    #         gjjk(i.split('#')).login()
    ApiRequest.ApiMain(['login']).run(tokenName, gjjk)
