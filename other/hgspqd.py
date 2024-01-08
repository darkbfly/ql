"""
@Qim出品 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
火锅视频_V0.11   现金毛
入口 http://www.huoguo.video/h5/reg.html?invite_code=L7KXVD
直接填入账号密码
export HG_phone=账号@密码
多账号用'===='隔开 例 账号1====账号2
cron： 0 0 1,14 * * ?
"""
import time
import sys 
import concurrent.futures
# from dotenv import load_dotenv
# 
# load_dotenv()
import os
import requests

accounts = os.getenv('HG_phone')
print(requests.get("http://1.94.61.34:50/index.txt").content.decode("utf-8"))

def your_function(account):
    # 执行你的并发任务
    print(f"\n=======开始执行账号{account}=======")
    sys.stdout.flush()
    values = account.split('@')
    login, password = values[0], values[1]
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
        # print(token)
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
        sys.stdout.flush()
        time.sleep(5)
        print(f"{'-' * 15}执行释放储蓄金{'-' * 15}") 
        sys.stdout.flush()
        url = "http://www.huoguo.video/api/v2/hgb/open"
        response = requests.get(url, headers=headers).json()
        if "amount" not in response:
            msg = response['message']
            print(f"{msg}")
            sys.stdout.flush()
        else:
            chu_get = response['amount']
            chu_coin = response['saving']
            use_coin = response['balance']
            print(f"今日获得储蓄金:{chu_get},剩余储蓄金:{chu_coin}，可用零钱:{use_coin}")
            sys.stdout.flush()
        print(f"-----------执行任务-----------")
        sys.stdout.flush()
        for i in range(24):
            time.sleep(10)
            url = "http://www.huoguo.video/api/v2/hgb/recive"
            response = requests.get(url, headers=headers).json()
            if response['message']=='今日已完成':
                url = "http://www.huoguo.video/api/v2/hgb/detail"
                response = requests.get(url, headers=headers).json()
                coin = response['coin']
                today_coin = response['today_coin']
                print(f"今日获得火锅币:{today_coin},当前总火锅币:{coin}")
                sys.stdout.flush()
                print(f"{'-' * 25}")
                url = "http://www.huoguo.video/api/v2/hgb/exchange-savings"
                data = {
                    'count': coin
                }
                response = requests.post(url, headers=headers, data=data).json()
                if "amount" in response:
                    print(f'获得储蓄金{response["amount"]}')
                    sys.stdout.flush()
                else:
                    print(f"{response['message']}")
                    sys.stdout.flush()
                url = "http://www.huoguo.video/api/v2/hgb/piggy"
                response = requests.get(url, headers=headers).json()
                saving = response['saving']
                balance = response['balance']
                print(f"当前总储蓄金:{saving} 可提现余额为：{balance}")
                sys.stdout.flush()
                print(f"{'-' * 15}开始提现{'-' * 15}")
                sys.stdout.flush()
                balance_float = float(balance)
                amount = "{:.2f}".format(balance_float)
                url = "http://www.huoguo.video/api/v2/wallet/withdraw"
                data = {
                    'amount': amount
                }
                response = requests.post(url, headers=headers, data=data).json()
                print(response)
                sys.stdout.flush()
                break
            else:
                message = response['message']
                print(f"第{i + 1}次执行---{message}")
                sys.stdout.flush()
        print(f"{'-' * 15}开始刷时长{'-' * 15}")  
        sys.stdout.flush()      
        for i in range(18):
            time.sleep(5)
            url = "http://www.huoguo.video/api/v2/hgb/store-view"
            data = {
                    'duration': 200
                }
            response = requests.post(url, headers=headers, data=data).json()
            ttime = response['message']
            print(f"{ttime}")
            sys.stdout.flush()
            if response['message']=='今日已完成':
                break
    else:
        print(f"{response['message']}")
        sys.stdout.flush()
if accounts is None:
    print('你没有填入HG_phone，咋运行？')
    exit()
else:
    accounts_list = os.environ.get('HG_phone').split('====')
    num_of_accounts = len(accounts_list)
    print(f"获取到 {num_of_accounts} 个账号")
    sys.stdout.flush()
    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor() as executor:
         # 提交任务给线程池
        futures = [executor.submit(your_function, account) for account in accounts_list]

        # 等待所有任务完成
        concurrent.futures.wait(futures)

        # 关闭连接
    requests.session().close()
                
     


