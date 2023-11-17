"""
new Env("微信小程序-AMD玩家俱乐部")
cron: 0 8 * * *
环境变量名称 amd_data
"""

import os
import ApiRequest
import mytool

title = '微信小程序-AMD玩家俱乐部'
tokenName = 'amd_data'


class amd(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'amdfans.giftreward.cn',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309080f)XWEB/8461',
            'Content-Type': 'application/json',
            'Referer': 'https://servicewechat.com/wx5407fbacfae2c2ce/56/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.xcxopenid = data[0]
        self.token = data[1]
        self.userId = data[2]

    def login(self):
        json_data = {
            'xcxopenid': self.xcxopenid,
            'token': self.token,
            'userId': int(self.userId),
        }

        response = self.sec.post(
            f'https://amdfans.giftreward.cn/api/services/app/UserDaySignIn/Create?Random=0.9771798641378846&xcxopenid={self.xcxopenid}&token={self.token}&',
            json=json_data,
        )
        print(response.json())

if __name__ == '__main__':
    # DEBUG
    if os.path.exists('debug.py'):
        import debug

        debug.setDebugEnv()
    if mytool.getlistCk(f'{tokenName}') == None:
        print(f'请检查你的变量名称 {tokenName} 是否填写正确')
        exit(0)
    else :
        for i in mytool.getlistCk(f'{tokenName}'):
            amd(i.split("#")).login()