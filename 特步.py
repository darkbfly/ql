"""
cron: 0 3 * * *
new Env("微信小程序-特步")
env add wx_特步

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import ApiRequest
import mytool

tokenName = 'wx_tebu'
msg = ''


class tebu(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'wxa-tp.ezrpro.com',
            'Connection': 'keep-alive',
            'ezr-source': 'weapp',
            'limitType': '0',
            'ezr-sp': '2',
            'ezr-brand-id': '254',
            'ezr-client-name': 'EZR.FE.MultiMall.Mini',
            'ezr-ss': data.split("#")[0],
            'ezr-userid': data.split("#")[1],
            'ezr-cop-id': '143',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/9193',
            'Content-Type': 'application/json',
            'xweb_xhr': '1',
            'ezr-st': str(mytool.getMSecTimestamp()),
            'ezr-sv': '1',
            'ezr-vuid': data.split("#")[2],
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wx12e1cb3b09a0e6f0/122/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        json_data = {
            'ActId': 828,
            'ActRemindStatus': True,
        }

        rj = self.sec.post('https://wxa-tp.ezrpro.com/myvip/Vip/SignIn/SignIn', json=json_data)

        print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, tebu)
