"""
new Env("华住签到")
cron 0 7 * * *
环境变量名称 huazhu_cookies
"""

import datetime
import json
import traceback
import requests
import mytool
from notify import send

title = '华住签到'
tokenName = 'huazhu_cookies'


class huazhu():
    def __init__(self, data):
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Client-Platform': 'WEB-APP',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'DNT': '1',
            'Origin': 'https://campaign.huazhu.com',
            'Referer': 'https://campaign.huazhu.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.67',
            'User-Token': 'null',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'Cookie': data,
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        pass

    def login(self):
        data = {
            'state': '1',
            'day': str(datetime.date.today().day),
        }
        try:
            rj = self.sec.post('https://hweb-mbf.huazhu.com/api/signIn', headers=self.headers, data=data).json()
            if rj['businessCode'] == "1000":
                msg = f"签到成功, 获得{rj['content']['point']}积分!"
            else:
                # json内容到msg
                msg = f"签到失败\n" + json.loads(rj)
            print(msg)
            send(title, msg)
        except:
            traceback.print_exc()
            pass
        pass



if __name__ == "__main__":
    if mytool.getlistCk(f'{tokenName}') == None:
        print(f'请检查你的变量名称 {tokenName} 是否填写正确')
        exit(0)
    else :
        for i in mytool.getlistCk(f'{tokenName}'):
            huazhu(i).login()