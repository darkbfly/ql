"""
cron: 0 7 * * *
new Env("微信小程序-奈雪")
env add wx_miss = Authorization#lat#lng#openId

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""

import base64
import hashlib
import hmac
import ApiRequest
import mytool

tokenName = 'wx_nx'
msg = ''
class nx(ApiRequest.ApiRequest):
    def sign(self, nonce, openId, timestamp):
        msg = f"nonce={nonce}&openId={openId}&timestamp={timestamp}"
        print(msg)
        key = 'sArMTldQ9tqU19XIRDMWz7BO5WaeBnrezA'
        return base64.b64encode(hmac.new(key.encode(), msg.encode(), hashlib.sha1).digest()).decode()

    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'tm-web.pin-dao.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': data.split('#')[0],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129',
            'Content-Type': 'application/json',
            'Origin': 'https://tm-web.pin-dao.cn',
            # 'Referer': 'https://tm-web.pin-dao.cn/naixue/sign-in?sf=&accessToken=eyJhbGciOiJIUzI1NiJ9.eyJ1bmlvbkNvZGUiOiJQNjQ4NDAyMzkyNDA4NzA3MDgwMSIsInVzZXJJZCI6IjE5ODU4ODgzNCIsImJyYW5kIjoiMjYwMDAyNTIiLCJwaG9uZSI6Im9iOXlBNHNVRktCd0hEUS1ER1lzbGZnYUpNNDAiLCJpc3MiOiJwZC1wYXNzcG9ydCIsInN1YiI6IjE5ODU4ODgzNCIsImlhdCI6MTcxNDE1OTUzNSwiZXhwIjoxNzI0NTI3NTM1fQ.cyu6ky5gv6dyj539-RWYpqlvj0NvEOLS0d0GCOX3RbQ&commonParams=%257B%2522common%2522%253A%257B%2522platform%2522%253A%2522wxapp%2522%252C%2522version%2522%253A%25225.2.22%2522%252C%2522imei%2522%253A%2522%2522%252C%2522osn%2522%253A%2522microsoft%2522%252C%2522sv%2522%253A%2522Windows%252010%2520x64%2522%252C%2522lat%2522%253A26.081350326538086%252C%2522lng%2522%253A119.32842254638672%252C%2522lang%2522%253A%2522zh_CN%2522%252C%2522currency%2522%253A%2522CNY%2522%252C%2522timeZone%2522%253A%2522%2522%252C%2522nonce%2522%253A405605%252C%2522openId%2522%253A%2522QL6ZOftGzbziPlZwfiXM%2522%252C%2522timestamp%2522%253A1714609483%252C%2522signature%2522%253A%2522ui9tudCqCAjoE1TbNIWIIoRusZE%253D%2522%257D%252C%2522params%2522%253A%257B%2522businessType%2522%253A1%252C%2522brand%2522%253A26000252%252C%2522tenantId%2522%253A1%252C%2522channel%2522%253A2%252C%2522stallType%2522%253A%2522PD_S_004%2522%252C%2522storeId%2522%253A26074341%252C%2522storeType%2522%253A1%252C%2522cityId%2522%253A350100%252C%2522appId%2522%253A%2522wxab7430e6e8b9a4ab%2522%257D%257D&static_time=1714609483772',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.lat = data.split('#')[1]
        self.lng = data.split('#')[2]
        self.openId = data.split('#')[3]
    def login(self):
        signDate = f"{mytool.gettime().year}-{mytool.gettime().month}-{mytool.gettime().day}"
        timestamp = mytool.getSecTimestamp()
        nonce = mytool.randomint(6)
        json_data = {
            'common': {
                'platform': 'wxapp',
                'version': '5.2.22',
                'imei': '',
                'osn': 'microsoft',
                'sv': 'Windows 10 x64',
                'lat': float(self.lat),
                'lng': float(self.lng),
                'lang': 'zh_CN',
                'currency': 'CNY',
                'timeZone': '',
                'nonce': nonce,
                'openId': self.openId,
                'timestamp': timestamp,
                'signature': self.sign(nonce, self.openId, timestamp),
            },
            'params': {
                'businessType': 1,
                'brand': 26000252,
                'tenantId': 1,
                'channel': 2,
                'stallType': 'PD_S_004',
                'storeId': 26074341,
                'storeType': 1,
                'cityId': 350100,
                'appId': 'wxab7430e6e8b9a4ab',
                'signDate': signDate,
            },
        }
        response = self.sec.post('https://tm-web.pin-dao.cn/user/sign/save', json=json_data)
        print(response.text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, nx)