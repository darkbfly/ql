"""
cron: 0 4 * * *
new Env("微信小程序-分分有礼滴滴赏")
env add wx_ffyl

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import datetime

# !/usr/bin/env python3
# coding: utf-8

import ApiRequest

title = '微信小程序-分分有礼滴滴赏'
tokenName = 'wx_ffyl'
msg = ''


class yljf(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'ucode-openapi.aax6.cn',
            'Connection': 'keep-alive',
            'Authorization': data.split('#')[0],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b)XWEB/9185',
            'Content-Type': 'application/json',
            'xweb_xhr': '1',
            # 'serialId': data.split('#')[1],
            'openId': data.split('#')[1],
            'appId': 'wx2da5d5ba2087726a',
            'version': '2.0.0',
            'Referer': 'https://servicewechat.com/wx2da5d5ba2087726a/183/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        params = {
            'promotionId': '107',
            'days': str(datetime.datetime.now().day),
        }
        rj = self.sec.get('https://ucode-openapi.aax6.cn/user/checkIn', params=params).json()
        print(rj)



if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, yljf)
