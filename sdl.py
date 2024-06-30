"""
cron: 0 7 * * *
new Env("微信小程序-三得利")
env add wx_sdl

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest

tokenName = 'wx_sdl'
msg = ''


class sdl(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'xiaodian.miyatech.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '17',
            'X-VERSION': '2.1.3',
            'Authorization': data,
            'HH-VERSION': '0.2.8',
            'HH-FROM': '20230130307725',
            'componentSend': '1',
            'HH-APP': 'wxb33ed03c6c715482',
            'appPublishType': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b11)XWEB/9185',
            'Content-Type': 'application/json;charset=UTF-8',
            'xweb_xhr': '1',
            'store': ',:,',
            'HH-CI': 'saas-wechat-app',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wxb33ed03c6c715482/28/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        json_data = {
            'miniappId': 159,
        }

        rj = self.sec.post('https://xiaodian.miyatech.com/api/coupon/auth/signIn', json=json_data).json()
        print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, sdl)
