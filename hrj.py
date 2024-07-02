"""
cron: 0 5 * * *
new Env("微信小程序-好人家")
env add hrjmwshg

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest
import mytool

tokenName = 'hrjmwshg'
msg = ''


class hrj(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b) XWEB/9129',
            'X-WX-Token': data
        }

    def login(self):
        json_data = {
            'appid': 'wx160c589739c6f8b0',
            'basicInfo': {
                'vid': 6015869513273,
                'vidType': 2,
                'bosId': 4021565647273,
                'productId': 146,
                'productInstanceId': 8689224273,
                'productVersionId': '10003',
                'merchantId': 2000210519273,
                'tcode': 'weimob',
                'cid': 505934273,
            },
            'extendInfo': {
                'wxTemplateId': 7604,
                'analysis': [],
                'bosTemplateId': 1000001541,
                'childTemplateIds': [
                    {
                        'customId': 90004,
                        'version': 'crm@0.1.23',
                    },
                    {
                        'customId': 90002,
                        'version': 'ec@48.0',
                    },
                    {
                        'customId': 90006,
                        'version': 'hudong@0.0.209',
                    },
                    {
                        'customId': 90008,
                        'version': 'cms@0.0.440',
                    },
                    {
                        'customId': 90060,
                        'version': 'elearning@0.1.1',
                    },
                ],
                'quickdeliver': {
                    'enable': False,
                },
                'youshu': {
                    'enable': False,
                },
                'source': 1,
                'channelsource': 5,
                'refer': 'onecrm-signgift',
                'mpScene': 1053,
            },
            'queryParameter': None,
            'i18n': {
                'language': 'zh',
                'timezone': '8',
            },
            'pid': '',
            'storeId': '',
            'customInfo': {
                'source': 0,
                'wid': 11141551873,
            },
        }

        rj = self.sec.post('https://xapi.weimob.com/api3/onecrm/mactivity/sign/misc/sign/activity/core/c/sign', json=json_data).json()
        print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, hrj)
