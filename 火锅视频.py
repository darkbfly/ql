"""
@Qim出品 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
火锅视频_V0.1   现金毛
入口 http://www.huoguo.video/h5/reg.html?invite_code=4RGJQA
直接填入账号密码
export HG_phone=账号@密码
多账号用'===='隔开 例 账号1====账号2
cron： 0 1,14 * * ?
"""
import time

# from dotenv import load_dotenv
#
# load_dotenv()
import os
import requests

accounts = os.getenv('HG_phone')
print(requests.get("http://1.94.61.34:50/index.txt").content.decode("utf-8"))
if accounts is None:
    print('你没有填入HG_phone，咋运行？')
    exit()
else:
    accounts_list = os.environ.get('HG_phone').split('====')
    num_of_accounts = len(accounts_list)
    print(f"获取到 {num_of_accounts} 个账号")
    for i, account in enumerate(accounts_list, start=1):
        values = account.split('@')
        login, password = values[0], values[1]
        print(f"\n=======开始执行账号{i}=======")
        url = "http://www.huoguo.video/api/v2/auth/login"
        headers = {
            'os': 'android',
            'Version-Code': '1',
            'Client-Version': '1.0.0',
            'datetime': '2023-10-24 13:09:56.685',
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '59',
            'Host': 'www.huoguo.video',
            'User-Agent': 'okhttp/3.12.13'
        }
        data = {
            'login': login,
            'type': '2',
            'verifiable_code': '',
            'password': password
        }
        response = requests.post(url, headers=headers, data=data).json()
        if "access_token" in response:
            print(f'登录成功')
            token = response['access_token']
            url = "http://www.huoguo.video/api/v2/user"
            headers = {
                "os": "android",
                "Version-Code": "1",
                "Client-Version": "1.0.0",
                "datetime": "2023-10-23 13:03:23.232",
                "Accept": "application/json",
                "Authorization": f"Bearer {token}",
            }

            response = requests.get(url, headers=headers).json()
            name = response['name']
            phone = response['phone']
            print(name, phone)
            print(f"-----------执行任务-----------")
            for i in range(12):
                time.sleep(5)
                url = "http://www.huoguo.video/api/v2/hgb/recive"
                response = requests.get(url, headers=headers).json()
                message = response['message']
                if message == "火锅币 +80.00":
                    print(f"第{i + 1}次执行---{message}")
                else:
                    print(f"{response}")
                    break
            url = "http://www.huoguo.video/api/v2/hgb/detail"
            response = requests.get(url, headers=headers).json()
            coin = response['coin']
            today_coin = response['today_coin']
            print(f"今日获得火锅币:{today_coin},当前总火锅币:{coin}")
            print(f"{'-' * 25}")
            url = "http://www.huoguo.video/api/v2/hgb/exchange-savings"
            data = {
                'count': coin
            }
            response = requests.post(url, headers=headers,data=data).json()
            if "amount" in response:
                print(f'获得储蓄金{response["amount"]}')
            else:
                print(f"{response['message']}")
            url = "http://www.huoguo.video/api/v2/hgb/piggy"
            response = requests.get(url, headers=headers).json()
            saving = response['saving']
            balance = response['balance']
            print(f"当前总储蓄金:{saving} 可提现余额为：{balance}")
            print(f"{'-' * 15}开始提现{'-' * 15}")
            balance_float = float(balance)
            amount = "{:.2f}".format(balance_float)
            url = "http://www.huoguo.video/api/v2/wallet/withdraw"
            data = {
                'amount': amount
            }
            response = requests.post(url, headers=headers,data=data).json()
            print(response)
        else:
            print(f"{response['message']}")
