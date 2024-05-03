"""
new Env("微信小程序-格力高")
cron 0 7 * * *
环境变量名称 wx_glg
"""

import ApiRequest

title = '微信小程序-格力高'
tokenName = 'wx_glg'


class glg(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'crm.glico.cn',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'X-Auth-Token': data,
            'X-App-Source': 'weixin_mp',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI '
                          'MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129',
            'Referer': 'https://servicewechat.com/wx0245348276df851b/147/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        json_data = {}
        response = self.sec.put('https://crm.glico.cn/miniapp/member/checkin', json=json_data)
        print(response.text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, glg)
