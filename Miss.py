"""
cron: 0 7 * * *
new Env("微信小程序-蜜丝miss")
env add wx_miss = unionId#X-wx8465e1173d1e11b0-Token

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
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
            'taskId': '840',
        }
        response = self.sec.get(
            'https://clubwx.hm.liby.com.cn/miniprogram/benefits/activity/sign/execute.htm',
            params=params
        )
        print(response.text)

if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, miss)
