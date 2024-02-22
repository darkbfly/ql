"""
cron: 0 8 * * *
new Env("微信小程序-正佳")
env add wx_zj
"""
# !/usr/bin/env python3
# coding: utf-8

import ApiRequest

title = '微信小程序-正佳'
tokenName = 'wx_zj'


class zj(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'member-pro.zhengjiamax.com',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'MemberSession': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
            'Referer': 'https://servicewechat.com/wxca39f7dc54b49819/315/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        response = self.sec.post(
            'https://member-pro.zhengjiamax.com/memberSign/memberSign',
            params='',
            json={},
        )
        print(response.text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, zj)
