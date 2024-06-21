"""
cron: 0 7 * * *
new Env("微信小程序-雀巢会员俱乐部")
env add wx_qchy = Authorization

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest

tokenName = 'wx_qchy'
msg = ''


class qchy(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'crm.nestlechinese.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '14',
            'xweb_xhr': '1',
            'Authorization': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wxc5db704249c9bb31/230/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        params = ''

        json_data = {
            'task_id': 17,
        }
        response = self.sec.post(
            'https://crm.nestlechinese.com/openapi/activityservice/api/task/add',
            params=params,
            json=json_data,
        )
        print(response.text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, qchy)
