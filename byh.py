"""
cron: 30 5 * * * byh.py
new Env("微信小程序-棒约翰点单")
env add dcjd_data
"""
import json
import ApiRequest
from notify import send

title = '微信小程序-棒约翰点单'
tokenName = 'wx_byh'


class byh(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'wechat.dairyqueen.com.cn',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'Cookie': data,
            'channel': '202',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b) XWEB/9129',
            'tenant': '2',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wxe12e908d0febcd9b/126/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        print(self.sec.post('https://wechat.dairyqueen.com.cn/memSignIn/signIn', json={}).text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, byh)
