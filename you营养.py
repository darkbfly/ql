"""
cron: 0 5 * * *
new Env("微信小程序-you营养")
env add wx_yyy

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest

tokenName = 'wx_yyy'
msg = ''


class yyy(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'hdyx.by-health.com',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b11)XWEB/9185',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
            'Accept': '*/*',
            'Origin': 'https://hdyx.by-health.com',
            'Referer': 'https://hdyx.by-health.com/web/byhealth-task-center/index.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.data = data

    def login(self):
        data = {
            'openid': self.data,
        }
        rj = self.sec.post('https://hdyx.by-health.com/taskCenter/api/sign/saveSign', data=data).json()
        print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, yyy)
