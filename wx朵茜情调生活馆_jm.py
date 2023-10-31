# -- coding:UTF-8 --
import datetime
import json
import time, sys  # re 用于正规则处理,os可能要用于文件路径读取与判断
import requests as req
import multiprocessing as mp

import mytool
from costtime import time_counts  # 用来统计时间
import sendNotify  # 发通知

#################################
'''
 作者：newhackerman
 日期：2023-10-13
 功能 	朵茜情调生活馆签到 积分换实物
 抓包：搜checkin  - url中的 access_token  header-extra-data中的 sid，uuid,
 变量格式：export dqqdshgck='access_token&sid&uuid'
 定时：1天一次
 cron: 2 8 * * *
 无邀请码
 用于青龙，其它平台未测试
 [task_local]

 [rewrite_local]

 [MITM]

new Env("微信小程序-朵茜情调生活馆")
 '''
#################################

import os, sys  # line:1

configfile = '/ql/data/config/config.sh'  # line:4
configfile1 = './config.sh'  # line:5
configdict = {}  # line:7


def get_configdict():  # line:8
    if os.path.exists(configfile):  # line:9
        with open(configfile, 'r', encoding='utf8') as O00O0O000O000O0O0:  # line:10
            O0OO0O00OOOO00OOO = O00O0O000O000O0O0.readlines()  # line:11
            if O0OO0O00OOOO00OOO is None:  # line:12
                sys.exit()  # line:13
            for OO0OO0OO0O00000O0 in O0OO0O00OOOO00OOO:  # line:14
                OO0OO0OO0O00000O0 = str(OO0OO0OO0O00000O0).replace('\n', '').replace('\'', '', -1).replace('\"', '',
                                                                                                           -1)  # line:15
                if OO0OO0OO0O00000O0 == '' or OO0OO0OO0O00000O0 is None:  # line:16
                    continue  # line:17
                if OO0OO0OO0O00000O0.strip()[0] == '#':  # line:18
                    continue  # line:19
                if 'export' in OO0OO0OO0O00000O0.strip():  # line:20
                    OO0OO0OO0O00000O0 = OO0OO0OO0O00000O0.replace('export', '', -1)  # line:21
                OO0OO0OO0O00000O0 = OO0OO0OO0O00000O0.split('=', 1)  # line:22
                if len(OO0OO0OO0O00000O0) < 2:  # line:23
                    continue  # line:24
                OOO0O0000OOOOOOO0 = OO0OO0OO0O00000O0[0].strip()  # line:25
                O00OO0O0OO00OO00O = OO0OO0OO0O00000O0[1].strip()  # line:26
                configdict[OOO0O0000OOOOOOO0] = O00OO0O0OO00OO00O  # line:27
    elif os.path.exists(configfile1):  # line:28
        with open(configfile1, 'r', encoding='utf8') as O00O0O000O000O0O0:  # line:29
            O0OO0O00OOOO00OOO = O00O0O000O000O0O0.readlines()  # line:30
            if O0OO0O00OOOO00OOO is None:  # line:31
                sys.exit()  # line:32
            for OO0OO0OO0O00000O0 in O0OO0O00OOOO00OOO:  # line:33
                OO0OO0OO0O00000O0 = str(OO0OO0OO0O00000O0).replace('\n', '').replace('\'', '', -1).replace('\"', '',
                                                                                                           -1)  # line:34
                if OO0OO0OO0O00000O0 == '' or OO0OO0OO0O00000O0 is None:  # line:35
                    continue  # line:36
                if OO0OO0OO0O00000O0.strip()[0] == '#':  # line:37
                    continue  # line:38
                if 'export' in OO0OO0OO0O00000O0.strip():  # line:39
                    OO0OO0OO0O00000O0 = OO0OO0OO0O00000O0.replace('export', '', -1)  # line:40
                OO0OO0OO0O00000O0 = OO0OO0OO0O00000O0.split('=', 1)  # line:41
                if len(OO0OO0OO0O00000O0) < 2:  # line:42
                    continue  # line:43
                OOO0O0000OOOOOOO0 = OO0OO0OO0O00000O0[0].strip()  # line:44
                O00OO0O0OO00OO00O = OO0OO0OO0O00000O0[1].strip()  # line:45
                configdict[OOO0O0000OOOOOOO0] = O00OO0O0OO00OO00O  # line:46
    else:  # line:47
        print('未找到配置文件！！，请检查配置文件路径与文件名')  # line:48


get_configdict()  # line:50


def getconfig(O0000O0OOO0000O0O):  # line:52
    return configdict[O0000O0OOO0000O0O]  # line:53


def setconfig(OO0OO0O0O0O0O0O00, O0OOO00OOOOO0O000):  # line:56
    configdict[OO0OO0O0O0O0O0O00] = O0OOO00OOOOO0O000  # line:57


def change_param_value_tofile(OO0O0O000O0O00O0O, OO000OOOOO0O00O0O):  # line:59
    if os.path.exists(configfile):  # line:61
        O00O000O00OO0O00O = []  # line:62
        with open(configfile, 'r', encoding='utf8') as O0000OOOO0OOOO0OO:  # line:63
            O0O00OOO0O0000O00 = O0000OOOO0OOOO0OO.readlines()  # line:64
            for O00OO0O00O00OOO00 in O0O00OOO0O0000O00:  # line:65
                if OO0O0O000O0O00O0O in O00OO0O00O00OOO00.strip():  # line:66
                    OOOO0000OO0OO0OO0 = getconfig(OO0O0O000O0O00O0O)  # line:67
                    O00OO0O00O00OOO00 = O00OO0O00O00OOO00.replace(OOOO0000OO0OO0OO0, OO000OOOOO0O00O0O)  # line:68
                    O00O000O00OO0O00O.append(O00OO0O00O00OOO00)  # line:69
                else:  # line:70
                    O00O000O00OO0O00O.append(O00OO0O00O00OOO00)  # line:71
        if len(O00O000O00OO0O00O) > 0:  # line:73
            with open(configfile, 'r', encoding='utf8') as OOOO00O0OOO0O000O:  # line:74
                OOOO00O0OOO0O000O.writelines(O00O000O00OO0O00O)  # line:75
    elif os.path.exists(configfile1):  # line:77
        O00O000O00OO0O00O = []  # line:78
        with open(configfile1, 'r', encoding='utf8') as O0000OOOO0OOOO0OO:  # line:79
            O0O00OOO0O0000O00 = O0000OOOO0OOOO0OO.readlines()  # line:80
            for O00OO0O00O00OOO00 in O0O00OOO0O0000O00:  # line:81
                if OO0O0O000O0O00O0O in O00OO0O00O00OOO00:  # line:83
                    OOOO0000OO0OO0OO0 = getconfig(OO0O0O000O0O00O0O)  # line:84
                    print('替换前：', O00OO0O00O00OOO00)  # line:85
                    O00OO0O00O00OOO00 = O00OO0O00O00OOO00.replace(OOOO0000OO0OO0OO0, OO000OOOOO0O00O0O)  # line:86
                    print('替换后：', O00OO0O00O00OOO00)  # line:87
                    O00O000O00OO0O00O.append(O00OO0O00O00OOO00)  # line:88
                else:  # line:89
                    O00O000O00OO0O00O.append(O00OO0O00O00OOO00)  # line:90
        if len(O00O000O00OO0O00O) > 0:  # line:93
            with open(configfile1, 'w', encoding='utf8') as OOOO00O0OOO0O000O:  # line:94
                OOOO00O0OOO0O000O.writelines(O00O000O00OO0O00O)  # line:95
        else:  # line:96
            print('未找到配置文件')  # line:97


def getcookies(OO00000000O00O0O0):  # line:99
    O000OOO0000O0000O = []  # line:100
    OO0O00000O000OOOO = ''  # line:101
    if mytool.getlistCk(OO00000000O00O0O0) is None:
        O00O0O000OO0O0000 = configdict[OO00000000O00O0O0]  # line:102
        O00O0O000OO0O0000 = str(O00O0O000OO0O0000).strip().split('#')  # line:103
        return O00O0O000OO0O0000  # line:104
    else:
        return mytool.getlistCk(OO00000000O00O0O0)


def dict_to_str(OO0000O000O0000O0):  # line:106
    O0OOO0OOO0OOO00O0 = ''  # line:107
    if OO0000O000O0000O0:  # line:108
        if isinstance(OO0000O000O0000O0, dict):  # line:109
            for O00000OOO0OO00OOO, O00O0O00OO0O000O0 in OO0000O000O0000O0.items():  # line:111
                O0O0O0OO0000OOO0O = f'%s: %s \n' % (O00000OOO0OO00OOO, O00O0O00OO0O000O0)  # line:112
                O0OOO0OOO0OOO00O0 += O0O0O0OO0000OOO0O  # line:113
        else:  # line:114
            return OO0000O000O0000O0  # line:115
    return O0OOO0OOO0OOO00O0


# ------------------------------
session = req.session()  #


def starttask(OO0O0O0OOOO0OO0O0, OO0OOO00OO00OOOOO, OO00O000O00O000OO, O00OO00O0O0OO0OO0):  #
    OOO000O0000OOO0O0 = tasks(OO0O0O0OOOO0OO0O0, OO0OOO00OO00OOOOO, OO00O000O00O000OO, O00OO00O0O0OO0OO0)  #
    OOO000O0000OOO0O0.runtasklist()  #


class tasks():  #
    def __init__(O0O00O00000O00O0O, O00OOO0OOOOOOO00O, O0O0OOO0O00OO0OOO, OOO00O0O0000OO000, O0O0O0O00000O0O0O):  #
        O0OO0O0O0OOOOO00O = '第%s 个账号：%s' % (O0O0O0O00000O0O0O, O0O0OOO0O00OO0OOO)  #
        O0O00O00000O00O0O.resultdict = {}  #
        O0O00O00000O00O0O.resultdict['说明'] = '签到积分换实物'  #
        O0O00O00000O00O0O.resultdict[O0OO0O0O0OOOOO00O] = '->'  #
        OO0O0O0O0OOO0OOOO = time.time()  #
        O0O00O00000O00O0O.st = str(round(OO0O0O0O0OOO0OOOO * 1000))  #
        O0O0OO000O0O000OO = time.strftime('%Y%m%d', time.localtime())  #
        O0O00O00000O00O0O.access_token = O00OOO0OOOOOOO00O  #
        O0O00O00000O00O0O.sid = O0O0OOO0O00OO0OOO  #
        O0O00O00000O00O0O.uuid = OOO00O0O0000OO000  #
        O00OO00OO0O0O0O0O = {"is_weapp": 1, "sid": O0O00O00000O00O0O.sid, "version": "2.149.9.101", "client": "weapp",
                             "bizEnv": "wsc", "uuid": O0O00O00000O00O0O.uuid, "ftime": O0O00O00000O00O0O.st}  #
        O0O00O00000O00O0O.headers = {'extra-data': json.dumps(O00OO00OO0O0O0O0O),
                                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8391',
                                     'content-type': 'application/json', 'accept': '*/*',
                                     'sec-fetch-site': 'cross-site',
                                     'referer': 'https://servicewechat.com/wx46d8e6f162c5deba/85/page-frame.html',
                                     'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh',
                                     'cookie': 'KDTWEAPPSESSIONID=' + O0O00O00000O00O0O.sid}  #

    @time_counts  #
    def runtasklist(OO00O00OO0O00OOOO):  #
        OO00O0OOO00O0OOO0 = OO00O00OO0O00OOOO.dqqdshgck_sign()  #
        time.sleep(2)  #
        OO00O0OOO00O0OOO0 = OO00O00OO0O00OOOO.dqqdshgck_select()  #
        print(OO00O00OO0O00OOOO.resultdict)  #
        sendNotify.send('朵茜情调生活馆执行结果：', OO00O00OO0O00OOOO.resultdict)  #

    def dqqdshgck_sign(OOOOO00O0OOOO000O):  #
        OO00000000000O0O0 = time.strftime('%Y-%m-%d', time.localtime())  #
        OO00O00OO0000O00O = time.time()  #
        OOOOO00O0OOOO000O.st = str(int(OO00O00OO0000O00O))  #
        O0000OOO00O0OOO0O = f"https://h5.youzan.com/wscump/checkin/checkinV2.json?checkinId=3262&app_id=wx46d8e6f162c5deba&kdt_id=2741062&access_token={OOOOO00O0OOOO000O.access_token}"  #
        try:  #
            OO0O0O0O0000OO0OO = session.get(url=O0000OOO00O0OOO0O, headers=OOOOO00O0OOOO000O.headers, timeout=5)  #
            if OO0O0O0O0000OO0OO.status_code == 200:  #
                O000OOOOOOO00OOO0 = OO0O0O0O0000OO0OO.json()  #
                if O000OOOOOOO00OOO0['msg'] == 'ok':  #
                    try:  #
                        if O000OOOOOOO00OOO0.get('data'):  #
                            OOOOO00O0OOOO000O.resultdict['签到积分'] = O000OOOOOOO00OOO0['data']['list'][0]['infos'][
                                'title']  #
                    except BaseException as OOOO0O0OOO0OO0OO0:  #
                        print(OOOO0O0OOO0OO0OO0)  #
                else:  #
                    OOOOO00O0OOOO000O.resultdict['签到'] = O000OOOOOOO00OOO0['msg']  #
            else:  #
                print(OO0O0O0O0000OO0OO.content.decode('utf8'))  #
        except BaseException as O0OO0OO0O00OOOO0O:  #
            print(O0OO0OO0O00OOOO0O)  #

    def dqqdshgck_select(OO0OOOO0OO0OO00OO):  #
        O0OOO0OOOOO000000 = time.strftime('%Y-%m-%d', time.localtime())  #
        O00O0OO000OO0O000 = time.time()  #
        OO0OOOO0OO0OO00OO.st = str(int(O00O0OO000OO0O000 * 1000))  #
        O000OO0O0OOO00O0O = f"https://h5.youzan.com/wscump/pointstore/getCustomerPoints.json"  #
        try:  #
            OO0OOOO0OOO000000 = session.get(url=O000OO0O0OOO00O0O, headers=OO0OOOO0OO0OO00OO.headers, timeout=5)  #
            if OO0OOOO0OOO000000.status_code == 200:  #
                O000OO00000O0O000 = OO0OOOO0OOO000000.json()  #
                if O000OO00000O0O000['msg'] == 'ok':  #
                    OO0OOOO0OO0OO00OO.resultdict['当前积分'] = O000OO00000O0O000['data']['currentAmount']  #
                else:  #
                    OO0OOOO0OO0OO00OO.resultdict['当前积分'] = O000OO00000O0O000.get('msg')  #
        except BaseException as O0OO0O0O0OO0O00O0:  #
            print(O0OO0O0O0OO0O00O0)  #
        return OO0OOOO0OO0OO00OO.resultdict  #


if __name__ == '__main__':  #
    if os.path.exists('debug.py'):
        import debug

        debug.setDebugEnv()
    cookies = getcookies('dqqdshgck')  #
    if len(cookies) > 5:  #
        print('请勿一次性跑太多账号，造成服端与本机压力！')  #
    i = 0  #
    if cookies is not None:  #
        for cookie1 in cookies:  #
            cookie = str(cookie1).split('#')  #
            access_token = cookie[0]  #
            sid = cookie[1]  #
            uuid = cookie[2]  #
            i += 1  #
            process = mp.Process(target=starttask, args=(access_token, sid, uuid, i,))  #
            process.start()  #
            if i % 5 == 0:  #
                time.sleep(120)  #
        sys.exit()  #
    else:  #
        print('未配置cookies')  #
        sys.exit(0)  #
