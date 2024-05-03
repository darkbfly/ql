"""
new Env("微信小程序-攀升科技")
cron 0 8 * * *
环境变量名称 wx_pskj
"""

import ApiRequest
import mytool

title = '微信小程序-攀升科技'
tokenName = 'wx_pskj'


class pskj(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'psjia.ipason.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '2',
            'xweb_xhr': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129',
            'token': data,
            'Referer': 'https://servicewechat.com/wxb0cd377dac079028/18/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        json_data = {}
        response = self.sec.post('https://psjia.ipason.com/api/v2.member.score_shop/signSub', json=json_data)
        print(response.text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, pskj)
