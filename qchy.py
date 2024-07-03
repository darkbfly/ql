"""
cron: 0 7 * * *
new Env("微信小程序-雀巢会员俱乐部")
env add wx_qchy = Authorization

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import requests

# !/usr/bin/env python3
# coding: utf-8
import ApiRequest
import ssl

tokenName = 'wx_qchy'
msg = ''

# 创建自定义适配器
class TLSAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.set_ciphers("DEFAULT")
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)


class qchy(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'crm.nestlechinese.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '14',
            'xweb_xhr': '1',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk1RDNEQzJDRDg0REM5Nzc1MDE0NzhBQkVDQjBBQ0Q5MjU3QjRGMjNSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6ImxkUGNMTmhOeVhkUUZIaXI3TENzMlNWN1R5TSJ9.eyJuYmYiOjE3MTg5NjkwMTcsImV4cCI6MTcyMTU2MTAxNywiaXNzIjoiaHR0cDovL2lkZW50aXR5OjgwODAiLCJjbGllbnRfaWQiOiJ3ZWNoYXRNaW5pIiwic3ViIjoib2lySWQxYkk0QmU2elRWOW1YR25rck5XUW5kdyIsImF1dGhfdGltZSI6MTcxODk2OTAxNywiaWRwIjoibG9jYWwiLCJ1bmlvbmlkIjoib2lySWQxYkk0QmU2elRWOW1YR25rck5XUW5kdyIsIm1pbmlfb3BlbmlkIjoib050SzE1SWF4SndOdzRpZjNxckpVSWVCSFZOdyIsInVzZXJfaWQiOiIxNzY3MDI4NjAxNTA0MzY2NTkyIiwianRpIjoiNjhERjlFNzU0QTJCRUE5RTE0REI3QzM2OTgzQkE5NDIiLCJpYXQiOjE3MTg5NjkwMTcsInNjb3BlIjpbImdhdGV3YXlfYXBpIiwiZ29vZHMiLCJtZW1iZXIiLCJvcmRlcnMiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsid2VjaGF0X2F1dGhfY29kZSJdfQ.U2_-oKfFOm-Ylz7eZGtVelEZiIiw88qoHL89SDpgEgI41PPW6H_E27LDZR-WFPpLYVPWdJL-e_p0xuVXWEaxIe2NanaeCXDS13VWLV716NwObxl761gox-x4_XR2_CYR2Q1Z6SxVxYvmYxvbNuMSywEZWdySIVjJ0OIb3Ao4C4alBVadZUuZP9VBzcNwZb36gJO0zg-xqTe8ftDoSEI1SWzDYrJZG0zWPRUpaQ4I-U8sU_fFEDfFTw9ipIJvarsTpekMkb_BXTd7kf0vFPuw_5cPT7ihoTmhlcBj5d__zfw6R2ppByZNy-Mv7yxt6VwmmVZaM0IJL337g9yEED-_ew',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b11)XWEB/9185',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wxc5db704249c9bb31/301/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        json_data = {
            'task_id': 17,
        }
        session = requests.Session()
        session.mount('https://', TLSAdapter())
        session.verify = False
        response = session.post('https://crm.nestlechinese.com/openapi/activityservice/api/task/add', headers=self.sec.headers, json=json_data).json()
        print(response)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, qchy)
