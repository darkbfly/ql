"""
cron: 30 11 * * *
new Env("APP-探我")
env add app_tanwo
"""
import json
import ApiRequest
from notify import send

title = 'APP-探我'
tokenName = 'app_tanwo'


class tanwo(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'tw.api.allture.vip',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; R11&s Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36',
            'token': data,
            'Accept': '*/*',
            'Origin': 'https://popularize.allture.vip',
            'X-Requested-With': 'com.xx.tanwo',
            'Referer': 'https://popularize.allture.vip/pages/mysteryBox/index',
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

    def login(self):
        response = self.sec.get('https://tw.api.allture.vip/appApi/activity/blindBoxLuckDraw')
        print(response.text)

if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, tanwo)