# 例如  AUTHORIZATION#qm-params

# 变量名 qmreadck         多账号@或者回车分割
#幸运大转盘+幸运7抽奖
#抓包过程+抓包教程：https://www.bilibili.com/video/BV1Wm4y1678j/?spm_id_from=333.999.0.0&vd_source=d2bc76339a6a058a723333a49361bd97
import json,os

import requests,time
def xydzp(au,qm):
    for i in range(5):
        url = 'https://xiaoshuo.wtzw.com/api/v2/lucky-draw/do-extracting?activity_id=0&version=2021010401&apiVersion=20190309143259-1.9&t=' + str(int(time.time()))
        headers = {
            "Host": "xiaoshuo.wtzw.com",
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; 21051182C Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Safari/537.36 webviewversion/71700 webviewpackagename/com.kmxs.reader",
            "x-requested-with": "com.kmxs.reader",
            "referer": "https://xiaoshuo.wtzw.com/app-h5/freebook/wheelSurf?activity_id=0",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "authorization": au,
            "qm-params": qm
        }
        resp = requests.get(url=url, headers=headers)
        if '金币' in str(resp.text):
            print('幸运大转盘' + json.loads(resp.text)['data']['prize_title'])
        else:
            print('今日抽奖次数已用完，请明日再来')
        time.sleep(2)
    xyqcz(au,qm)
def xyqcz(au,qm):
    url = 'https://api-gw.wtzw.com/lucky-seven/h5/v1/lottery'
    headers = {
        "Host": "api-gw.wtzw.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://xiaoshuo.wtzw.com",
        "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; 21051182C Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045435 Safari/537.36 webviewversion/71700 webviewpackagename/com.kmxs.reader",
        "Referer": "https://xiaoshuo.wtzw.com/app-h5/freebook/lucky7/index?enable_close=1",
        "authorization": au,
        "qm-params": qm
        # "authorization": "eyJhbGciOiJSUzI1NiIsImNyaXQiOlsiaXNzIiwianRpIiwiaWF0IiwiZXhwIl0sImtpZCI6IjE1MzEyMDM3NjkiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2ODA2OTAzOTgsImlhdCI6MTY3OTM5NDM5OCwiaXNzIjoiIiwianRpIjoiY2Y3MzExMmYzMzM4ODE0OTIzOTY2OWM2NjkxY2UwNjUiLCJ1c2VyIjp7InVpZCI6NDQyNTU3NzQ5LCJuaWNrbmFtZSI6IuS4g-eMq-S5puWPi18wMzExNTA5ODU3MTAiLCJpbWVpIjoiIiwidXVpZCI6IiIsImRldmljZUlkIjoiIiwicmVnVGltZSI6MTY3ODUyNjE2MiwidmlwRXhwaXJlQXQiOjAsInNtX2lkIjoiMjAyMzAzMTExNzE1MjZlNWM0MWJiZmMxZDU3ZGRmY2Y5NjJiMzFhZTgyN2JjOTAwYzAzZDA4ZmQ4ZjVmZmQiLCJudXQiOjE2Nzg1MjYxNjIsImlmdSI6MCwiaXNfcmJmIjowLCJhY3RfaWQiOjAsImJpbmRfYXQiOjAsInRpZCI6IkRVMTF2bV9pZWQzTHJwWWtyMXA5OXdSVC00VWIxalJJUDQ2ZlJGVXhNWFp0WDJsbFpETk1jbkJaYTNJeGNEazVkMUpVTFRSVllqRnFVa2xRTkRabWMyaDEiLCJ0X21vZGUiOjJ9fQ.WM5YxHoMUPf8vTdOTnaRJlcIFP-oVO6ZqsXlZ2C-kifSe70EXl0CjowPlAhK-_qeUQr0ia5B3ev7NJVZnaba0JU1ULCsD_iBPZ4nD8OfupzLRer1jmVipaaET8zZukWJIS8yupB5qqjsK8YyYZHccx5QG2HooegaLjGgyhI3clg",
        # "qm-params": "cLGEByHQmqU2m3HWHT0nghHwAhHENh0MNegEg5HjHSsZBlY2tqn2uzRjHTZ53aHjHzUx4LHWHT9LAT9wAT9wAT9wAT9wAT9LH5w5uCR1paHWHzpzpzpzpzpztq0LAI-QgTFEgLMwgI9wth9wgI9ENTOn4eOLgaHjHSNDuCGTpCR1paHWHTfLNhHEglp-gTs2pIpTNIF5taGTBy22BSFQmqF5A5HngIOYpI0e4zHwNhHMgzfLH5w5OEkxuy2TCENTBEG2HTZ5garlNeOnNh0wAIgYNI4LgTK5taGD4q2-HTZ5H5w5u_GUOEk2paU1paHWH-kRgholBRJ1pqFeh_GwqqQLgC9YACu3RaMMRqHnm2GGfIFlp2GyRCxNqo1MqIGjBo10h-UTB-Gm4hNGcyN0meR-gf1Rhok3R22VkSoRmlnkh-kmBqgLmI05taG-pCp14lfQmqF5A5HLgIHegIgngh0Egh-wAqkzAqp-4TKlNefrph0EAhoxphxzghGxAhp-NyfEpTN-gI0YNIo2NTfe4qN54lfwp3HjHz2Qpq-5A5Hngh0LgI-LNefnNIOeNeH5taG5Ozo7paHWH2x14qJQm3HjHSuj45UUmqF5A5G0Rh0nuzU6mqR-gMnLOo2vOTowAh2Ef2FQNoR5gq133R9MNzp3k2RrhRxmuoKLBynmk0YN4lYaqz0e3CxTkyjUpIoiRfnff2ppm-pnRqQjffY0qzUTgzKnH5w5OE2etCp2O5HWHTO7g3rLH5w5BqJ-pqw5A5HLgh9Ugh0rg-g56F=="

    }
    ds=[0,2,5,1,3]
    for jk in ds:
        data = {
            # source 2   7天VIP会员减2元券    0   七猫3个会员碎片 随机0-5吧
            'source': str(jk),
            'apiVersion': '20190309143259-1.9',
            't': str(int(time.time()))
        }
        resp = requests.post(url=url, headers=headers, data=data)
        if 'data' in resp.text:
            print('七猫幸运抽奖' + json.loads(resp.text)['data']['title'])
        else:
            print('七猫幸运抽奖' + json.loads(resp.text)['errors']['title'])
        time.sleep(2)
if os.environ.get("qmreadck"):
    dvm = os.environ["qmreadck"]
    if dvm != '':
        if "@" in dvm:
            Coo = dvm.split("@")
        elif "&" in dvm:
            Coo = dvm.split('&')
        else:
            Coo = dvm.split('\n')
    adv=1
    for j in Coo:
        au=str(j).split('#')[0]
        qm=str(j).split('#')[1]
        xydzp(au,qm)
        time.sleep(2)
