"""
cron: 0 7 * * *
new Env("微信小程序-蜜丝miss")
env add wx_miss = unionId#X-wx8465e1173d1e11b0-Token
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest

tokenName = 'wx_miss'
msg = ''


class miss(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'clubwx.hm.liby.com.cn',
            'Connection': 'keep-alive',
            'platformCode': 'Miss',
            'xweb_xhr': '1',
            'appId': 'wx8465e1173d1e11b0',
            'unionId': data.split('#')[0],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
            'X-wx8465e1173d1e11b0-Token': data.split('#')[1],
            'Content-Type': 'application/json',
            'Referer': 'https://servicewechat.com/wx8465e1173d1e11b0/33/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        params = {
            'taskId': '156',
        }
        response = self.sec.get(
            'https://clubwx.hm.liby.com.cn/miniprogram/benefits/activity/sign/execute.htm',
            params=params
        )
        print(response.text)

if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, miss)
