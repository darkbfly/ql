"""
0 5, 6, 7, 13, 18 * * * wyyx-wxapp.py
new Env("网易严选微信小程序")
env add wyyx_wxcookies
"""
import datetime
# !/usr/bin/env python3
# coding: utf-8

import json
import os
import traceback
import requests
import mytool
from notify import send

title = '网易严选微信小程序'
tokenName = 'wyyx_wxcookies'


class wyyx_wxapp():
    def __init__(self, data):
        self.headers = {
            'Host': 'miniapp.you.163.com',
            'Connection': 'keep-alive',
            'version': '20.10.9',
            'X-WX-3RD-Session': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI '
                          'MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8391',
            'Content-Type': 'application/json',
            'yx-s-tid': 'tid_web_c31256528f8b44ffb00c7f269ac6225b_eca148a72_1',
            'WX-PIN-SESSION': data,
            'yx-aui': 'lhIECRWpVi3Yeut8hLKB05esg1zoBsPd',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wx5b768b801d27f022/517/page-frame.html',
            'Accept-Language': 'zh-CN,zh',
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        self.sec.verify = False;
        pass

    def GET_EVERYDAY_FREE(self):
        """
        desc=每日免费领水滴
        """
        params = {
            'taskId': 'GET_EVERYDAY_FREE',
            'taskRecordId': '',
            'subTaskId': '',
        }
        try:
            rj = self.sec.get('https://miniapp.you.163.com/orchard/task/water/get.json', params=params).json()
            if rj['code'] == 200 and rj['result']['result'] == 1:
                msg = f"每日免费领水滴 成功\n获得{rj['result']['water']}水滴"
            else:
                msg = f"每日免费领水滴 失败\n" + json.loads(rj)
            print(msg)
            send(title, msg)
        except:
            traceback.print_exc()
            pass
        pass

    def GET_EVERYDAY_RANDOM(self):
        """
        desc=每日7-9点，12-14点，18-21点随机掉落水滴
        """
        # 如果时间在北京时间7到9点,12到14点,18到21点则运行下面语句
        if mytool.gettime().hour in range(7, 9) or mytool.gettime().hour in range(12,
                                                                                  14) or mytool.gettime().hour in range(
                18, 21):
            params = {
                'taskId': 'GET_EVERYDAY_RANDOM',
                'taskRecordId': '',
                'subTaskId': '',
            }
            try:
                rj = self.sec.get('https://miniapp.you.163.com/orchard/task/water/get.json', params=params).json()
                if rj['code'] == 200 and rj['result']['result'] == 1:
                    msg = f"随机掉落水滴 成功\n获得{rj['result']['water']}水滴"
                else:
                    msg = f"随机掉落水滴 失败\n" + json.loads(rj)
                print(msg)
                send(title, msg)
            except:
                traceback.print_exc()
                pass

    def drop(self):
        try:
            rj = self.sec.get('https://miniapp.you.163.com/orchard/game/water/drop.json').json()
            if rj['code'] == 200 and rj['result']['success']:
                msg = f"浇水 成功\n获得{rj['result']['water']}水滴"
            else:
                msg = f"浇水 失败\n" + json.loads(rj)
            print(msg)
            send(title, msg)
        except:
            traceback.print_exc()
            pass

    def visitItem(self, itemId):
        params = {
            'itemId': f'{itemId}',
        }

        try:
            rj = self.sec.get('https://miniapp.you.163.com/orchard/task/visitItem.json', params=params).json()
            if rj['code'] == 200 and rj['result'] == 1:
                msg = f"浏览商品 成功\n"
                return True
            else:
                msg = f"浏览商品 失败\n" + json.loads(rj)
                return False
            print(msg)
            # send(title, msg)
        except:
            traceback.print_exc()
            pass

    def getVisitItemList(self):
        if mytool.gettime().hour in range(7, 9):
            params = {
                'scene': '1',
                'type': '0',
                'size': '20',
                'lastItemId': '0',
            }
            count = 5
            try:
                rj = self.sec.get('https://miniapp.you.163.com/xhr/rcmd/indexV2.json', params=params).json()
                if rj['code'] == 200:
                    msg = f"获取商品列表 成功\n"
                    for i in rj['data']['rcmdItemList']:
                        if i['categoryItem'] is not None and count > 0:
                            print(i['categoryItem']['id'])
                            if self.visitItem(i['categoryItem']['id']):
                                count -= 1
                            mytool.sleep(3, 5)
                else:
                    msg = f"获取商品列表 失败\n" + json.loads(rj)
            except:
                traceback.print_exc()
                pass
    def GET_TASK(self):
        try:
            rj = self.sec.get('https://miniapp.you.163.com/orchard/task/list.json?taskIdList=%%5B%%22FRIEND_HELP%%22'
                              '%%2C%%22VISIT_ITEM%%22%%2C%%22PAY_ITEM%%22%%2C%%22GET_EVERYDAY_RANDOM%%22%%2C'
                              '%%22NOTIFY_TOMORROW%%22%%2C%%22GET_EVERYDAY_FREE%%22%%2C%%22PAY_SUPER_MC%%22%%2C'
                              '%%22FINISH_PIN%%22%%2C%%22DROP_WATER_CONTINUOUS%%22%%2C%%22VISIT_PAGE%%22%%2C'
                              '%%22GARDEN_CHECK_IN_MUTUAL_GUIDE%%22%%5D').json()
            if rj['code'] == 200:
                msg = f"获取任务列表 成功\n"
                if rj['data']['GET_EVERYDAY_FREE']['maxCount'] != rj['data']['GET_EVERYDAY_FREE']['count']:
                    self.GET_EVERYDAY_FREE()
                if rj['data']['VISIT_ITEM']['status'] != 3:
                    self.getVisitItemList()
                else:
                    return
            else:
                msg = f"获取商品列表 失败\n" + json.loads(rj)
        except:
            traceback.print_exc()


if __name__ == '__main__':
    os.environ[f'{tokenName}'] = '89d31cf6f05d406cc1d2179fb31116cd'
    if mytool.getlistCk(f'{tokenName}') is None:
        print(f'请检查你的变量名称 {tokenName} 是否填写正确')
        exit(0)
    else:
        for i in mytool.getlistCk(f'{tokenName}'):
            wyyx_wxapp(i).GET_TASK()
            # wyyx_wxapp(i).GET_EVERYDAY_FREE()
            wyyx_wxapp(i).GET_EVERYDAY_RANDOM()
            wyyx_wxapp(i).drop()
            # wyyx_wxapp(i).getVisitItemList()
