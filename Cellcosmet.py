"""
cron: 30 7 * * *
new Env("微信小程序-Cellcosmet")
env add wx_cellcosmet

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import json
import ApiRequest
from notify import send

title = '微信小程序-Cellcosmet'
tokenName = 'wx_cellcosmet'


class cellcosmet(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'cellcosmet.haoduoke.cn',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'orgClientId': '1',
            'appId': 'wxa72c343870a41479',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wxa72c343870a41479/6/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        self.userCode = data

    def login(self):
        json_data = {
            'userCode': self.userCode,
            'customerId': self.userCode,
            'counterId': 203652716557,
            'userId': None,
            'signOid': 326279852111,
            'appOid': 59278884243,
            'orgClientId': 1,
        }

        rj = self.sec.post('https://cellcosmet.haoduoke.cn/custom/free/memc/sign/commit', json=json_data).json()
        print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, cellcosmet)
