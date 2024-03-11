"""
cron: 0 7 * * *
new Env("微信小程序-特仑苏")
env add wx_tls = openid
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest
import mytool

tokenName = 'wx_tls'
msg = ''


class tls(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'mall.telunsu.net',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://mall.telunsu.net',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://mall.telunsu.net/minlifeh5/himilk/vip/vipCommunityOld.html?navType=1',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.openid = data
        self.cookies = {
            'HWWAFSESTIME': str(mytool.getMSecTimestamp()),
            'MY_OPENID': data,
            'sajssdk_2015_cross_new_user': '1',
        }

    def login(self):

        params = ''

        json_data = {
            'openid': self.openid,
        }

        response = self.sec.post(
            'https://mall.telunsu.net/wxapi/user/signIn',
            params=params,
            cookies=self.cookies,
            json=json_data,
        )
        print(response.text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, tls)
