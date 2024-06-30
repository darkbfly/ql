"""
cron: 0 5 * * *
new Env("微信小程序-观美日本")
env add wx_gmrb

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest
import mytool

tokenName = 'wx_gmrb'
msg = ''


class gmrb(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'gtj-api.shiseidochina.cn',
            'Connection': 'keep-alive',
            # 'Content-Length': '54',
            'x-ma-c': data.split('#')[1],
            'xweb_xhr': '1',
            'x-auth-token': data.split('#')[0],
            'x-shop-c': 'gtj',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b11)XWEB/9185',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wxbeb52e1c3bd2e11c/76/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        json_data = {
            'progressIds': [
                1538753,
            ],
            'missionName': '签到任务',
        }
        rj = self.sec.post('https://gtj-api.shiseidochina.cn/api/v1/mission/accept/reward', json=json_data).json()
        print(rj)

    def readArticle(self):
        # 循环3次
        for i in range(3):
            id = str(mytool.randomint(75))
            json_data = [
                {
                    'code': 'view_article',
                    'param': {
                        'article': id,
                    },
                },
                {
                    'code': 'be_read_article',
                    'param': {
                        'article': id,
                    },
                },
            ]
            rj = self.sec.post('https://gtj-api.shiseidochina.cn/api/v1/ubt/event/add', json=json_data).json()
            print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login', 'readArticle']).run(tokenName, gmrb)
