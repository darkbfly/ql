"""
new Env("微信小程序-卡西欧")
cron 0 3 * * *
环境变量名称 wx_kxo

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import json

import ApiRequest
import mytool

title = '微信小程序-卡西欧'
tokenName = 'wx_kxo'


class kxo(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'api.casioonline.com.cn',
            'Connection': 'keep-alive',
            # 'Content-Length': '2',
            'x-debug-trace': str(mytool.getMSecTimestamp()),
            'xweb_xhr': '1',
            'Authorization': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b)XWEB/9185',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wx0a834189b8d0249e/361/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        json_data = {}
        response = self.sec.post('https://api.casioonline.com.cn/miniprogram/fans-garden/user-sign', json=json_data)
        print(json.loads(response.text))


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, kxo)
