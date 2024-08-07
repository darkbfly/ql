"""
cron: 0 3 * * *
new Env("微信小程序-谷雨")
env add wx_gy

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import ApiRequest
import mytool

tokenName = 'wx_gy'
msg = ''


class gy(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'h5.youzan.com',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'Extra-Data': '{"is_weapp":1,"sid":"YZ1270114534045401088YZaeFR03ul","version":"2.176.5.104","client":"weapp","bizEnv":"wsc","uuid":"sokZOvOBYgPiGWc1722860402962","ftime":1722860402957}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/9193',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wxfdb5babdb1f93f0d/171/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.access_token = data.split("#")[0]
        self.sid = data.split("#")[1]
        self.uuid = data.split("#")[2]
        self.sec.headers['Extra-Data'] = f'{{"is_weapp":1,"sid":"{self.sid}","version":"2.176.5.104","client":"weapp","bizEnv":"wsc","uuid":"{self.uuid}","ftime":{mytool.getMSecTimestamp()}}}'


    def login(self):
        params = {
            'checkinId': '4343814',
            'app_id': 'wxfdb5babdb1f93f0d',
            'kdt_id': '45817451',
            'access_token': self.access_token
        }

        rj = self.sec.get('https://h5.youzan.com/wscump/checkin/checkinV2.json', params=params)
        print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, gy)
