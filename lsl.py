"""
cron: 0 3 * * * ryytn.py
new Env("微信小程序-冷酸灵")
env add wx_lsl

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
from datetime import datetime

import ApiRequest

title = '微信小程序-冷酸灵'
tokenName = 'wx_lsl'


class lsl(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'consumer-api.quncrm.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '18',
            'X-Account-Id': data.split('#')[1],
            'Accept': 'application/json, text/plain, */*',
            'xweb_xhr': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Access-Token': data.split('#')[0],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b)XWEB/9185',
            'Content-Type': 'application/json; charset=UTF-8',
            'Referer': 'https://servicewechat.com/wxc07244f8014793f0/78/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        params = {
            'maijsVersion': '1.50.0',
            'clientId': '0190498a-6c4e-76fe-48d2-6cae13576558',
            'appVersion': '1.91.49.9b319d9480d',
            'appName': '群脉电商',
            'envVersion': 'release',
            'clientTime': f'{datetime.now().strftime("%Y-%m-%d")}T{datetime.now().strftime("%H:%M:%S")}.315+08:00',
        }

        json_data = {
            'templateIds': [],
        }

        response = self.sec.post('https://consumer-api.quncrm.com/modules/campaigncenter/signin',
            params=params,
            json=json_data).json()
        print(response)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, lsl)
