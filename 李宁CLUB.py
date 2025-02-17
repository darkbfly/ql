"""
cron: 30 4 * * *
new Env("微信小程序-李宁CLUB")
env add wx_nl_club

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import ApiRequest
import mytool

tokenName = 'wx_ln_club'
msg = ''


class lining(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {'Host': 'mcenter-gateway.wx.lining.com', 'Connection': 'keep-alive', 'xweb_xhr': '1',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c1f)XWEB/11581',
                            'Content-Type': 'application/json', 'Accept': '*/*', 'Sec-Fetch-Site': 'cross-site',
                            'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty',
                            'Referer': 'https://servicewechat.com/wx54df8ea3b9c8ec10/175/page-frame.html',
                            'Accept-Language': 'zh-CN,zh;q=0.9', 'Authorization': data}

    def login(self):
        rj = self.sec.get('https://mcenter-gateway.wx.lining.com/customer/v1/sign').json()
        print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, lining)
