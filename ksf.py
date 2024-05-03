"""
cron: 0 7 * * *
new Env("微信小程序-康师傅味道馆")
env add wx_ksf = encryptsessionid
"""

import ApiRequest
import mytool
tokenName = 'wx_ksf'
msg = ''
appid = 'wxb6d93d7af93f31da'
class ksf(ApiRequest.ApiRequest):

    def sign(self, e):
        n = list(e.values())
        i = appid + "wa_smartgo"
        o = sorted(n)
        r = ""
        for t in o:
            r += str(t)
        return r + i
    def data(self, e):
        dat = ""
        for t in e:
            dat += t + "=" + str(e[t]) + "&"
        return dat.rstrip('&')

    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'ksf.plscn.com',
            'Connection': 'keep-alive',
            'x-account-key': 'd3hiNmQ5M2Q3YWY5M2YzMWRh',
            'xweb_xhr': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129',
            # 'x-account-sign': '640b19377b6b9b3a39ca499cb2e94404',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://servicewechat.com/wxb6d93d7af93f31da/104/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.encryptsessionid = data
    def login(self):
        signday = f"{mytool.gettime().year}-{mytool.gettime().month}-{mytool.gettime().day}"
        json_data = {
            "signday": signday,
            "pageid": "733",
            "encryptsessionid": self.encryptsessionid,
            "qr": "0",
            "timestamp": str(mytool.getSecTimestamp()),
            "versionid": "1.1.0",
        }
        self.sec.headers['x-account-sign'] = self.sign(json_data)
        print(self.sec.post('https://ksf.plscn.com/brandwxa/api/bonus/signin', data=json_data).text)

if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, ksf)