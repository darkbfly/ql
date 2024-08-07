"""
cron: 30 11 * * *
new Env("微信小程序-向太的会客厅会员中心")
env add wx_xt

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import json
from datetime import datetime

import ApiRequest
from notify import send

title = '微信小程序-向太的会客厅会员中心'
tokenName = 'wx_xt'


class xt(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'smp-api.iyouke.com',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
            'Authorization': data,
            'Content-Type': 'application/json',
            'xweb_xhr': '1',
            'appId': 'wxa20c0c10a072172e',
            'envVersion': 'release',
            'version': '1.9.32',
            'Referer': 'https://servicewechat.com/wxa20c0c10a072172e/14/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        response = self.sec.get(f'https://smp-api.iyouke.com/dtapi/pointsSign/user/sign?date={datetime.now().strftime("%Y/%m/%d")}&')
        print(response.text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, xt)
