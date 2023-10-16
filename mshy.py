"""
new Env("微信小程序-慕思会员")
cron 0 7 * * *
环境变量名称 musi_data
"""
import json
import os
from datetime import date

import requests
import mytool
from notify import send

title = '微信小程序-慕思会员'
tokenName = 'musi_data'

class mshy():
    def __init__(self, data):
        self.sec = requests.session()
        self.sec.headers = {
            'Host': 'atom.musiyoujia.com',
            'api_version': '1.0.0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
            'Content-Type': 'application/json',
            'api_token': '1712347195925712898',
            'api_client_code': '65',
            'api_timestamp': '1697090459806',
            'api_sign': 'F916A2CA6C169A641B4A876D24073FE9',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wx03527497c5369a2c/102/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.data = data

    def login(self):
        json_data = {
            'appId': 'wx03527497c5369a2c',
            'appType': 'WECHAT_MINI_PROGRAM',
            'osType': 'windows',
            'model': 'microsoft',
            'browser': '微信小程序',
            'platform': '1',
            'sourceType': '5',
            'sourceChannel': '会员小程序',
            'siteId': '',
            'visitorId': '',
            'deviceId': '',
            'spotId': '',
            'campaignId': '',
            'deviceType': '',
            'eventLabel': '',
            'eventValue': '',
            'eventAttr2': mytool.gettime().strftime("%Y.%m.%d"),
            'eventAttr3': '',
            'eventAttr4': '',
            'eventAttr5': '',
            'eventAttr6': '',
            'googleCampaignName': '',
            'googleCampaignSource': '',
            'googleCampaignMedium': '',
            'googleCampaignContent': '',
            'memberType': 'DeRUCCI',
            'customId': '3661603eac7846efad9408843aaaf065',
            'locationUrl': '/pages/user/signIn',
            'url': '/pages/user/signIn',
            'pageTitle': '每日签到',
            'logType': 'event',
            'behaviorIds': [
                1,
                3,
            ],
            'eventCategory': '用户签到',
            'eventAction': '签到',
            'eventAttr1': 1,
            'openId': self.data,
        }
        rj = self.sec.post('https://atom.musiyoujia.com/member/memberbehavior/add', json=json_data).json()
        if rj['code'] == 0:
            msg = f"登录成功\n获得积分：{rj['data']['point']}"
        else:
            msg = f"登录失败\n" + json.dumps(rj, ensure_ascii=False)
        print(msg)
        send(title, msg)
        pass

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
            mshy(i).login()
