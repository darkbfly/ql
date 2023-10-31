"""
cron: 0 5,6,7,13,18 * * * wyyx-wxapp.py
new Env("微信小程序-网易严选")
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
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

title = '微信小程序-网易严选'
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
        self.sec.verify = False
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
                msg = f"每日免费领水滴 失败\n" + json.dumps(rj, ensure_ascii=False)
            print(msg)
        except:
            traceback.print_exc()
            pass
        pass

    def GET_EVERYDAY_RANDOM(self):
        """
        desc=每日7-9点，12-14点，18-21点随机掉落水滴
        """
        # 如果时间在北京时间7到9点,12到14点,18到21点则运行下面语句
        if mytool.gettime().hour in range(7, 9) or mytool.gettime().hour in range(12, 14) or mytool.gettime().hour in range(18, 21):
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
                    msg = f"随机掉落水滴 失败\n" + json.dumps(rj, ensure_ascii=False)
                print(msg)
            except:
                traceback.print_exc()
                pass

    def getleftNumber(self):

        try :
            rj = self.sec.get('https://miniapp.you.163.com/orchard/game/water/index.json', params={'channelId': '0'}).json()
            if rj['code'] == 200:
                return rj['result']['leftNumber'] - 10
            else:
                print(json.dumps(rj, ensure_ascii=False))
                return 1
        except:
            traceback.print_exc()
            return 1
    def drop(self):
        count = self.getleftNumber()
        while count > 0:
            mytool.sleep(3, 5)
            count -= 1
            try:
                rj = self.sec.get('https://miniapp.you.163.com/orchard/game/water/drop.json').json()
                if rj['code'] == 200 and rj['result']['success']:
                    msg = f"浇水 成功\n"
                else:
                    msg = f"浇水 失败\n" + json.dumps(rj, ensure_ascii=False)
                print(msg)
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
                msg = f"浏览商品 成功"
                print(msg)
                return True
            else:
                msg = f"浏览商品 失败\n" + json.dumps(rj, ensure_ascii=False)
                print(msg)
                return False
        except:
            traceback.print_exc()
            pass

    def getVisitItemList(self):
        msg = ""
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
                if rj['code'] == '200':
                    msg = f"获取商品列表 成功"
                    for i in rj['data']['rcmdItemList']:
                        if i['categoryItem'] is not None and count > 0:
                            print(i['categoryItem']['id'])
                            if self.visitItem(i['categoryItem']['id']):
                                count -= 1
                            mytool.sleep(3, 5)

                    rj = self.sec.get('https://miniapp.you.163.com/orchard/task/finish.json',
                                      params={
                                          'taskId': 'VISIT_ITEM',
                                          'taskRecordId': '0',
                                      }).json()
                    if rj['code'] == 200:
                        msg += f"浏览商品结束 成功\n"
                    else:
                        msg += f"浏览商品结束 失败\n" + json.dumps(rj, ensure_ascii=False)
                else:
                    msg = f"获取商品列表 失败\n" + json.dumps(rj, ensure_ascii=False)
            except:
                traceback.print_exc()
                pass
        print(msg)

    def GET_TASK(self):
        try:
            rj = self.sec.get(
                'https://miniapp.you.163.com/orchard/task/list.json?taskIdList=["FRIEND_HELP","VISIT_ITEM","PAY_ITEM","GET_EVERYDAY_RANDOM","NOTIFY_TOMORROW","GET_EVERYDAY_FREE","PAY_SUPER_MC","FINISH_PIN","DROP_WATER_CONTINUOUS","VISIT_PAGE","GARDEN_CHECK_IN_MUTUAL_GUIDE"]').json()
            if rj['code'] == 200:
                msg = f"获取任务列表 成功\n"
                if rj['result']['GET_EVERYDAY_FREE']['maxCount'] != rj['result']['GET_EVERYDAY_FREE']['count']:
                    self.GET_EVERYDAY_FREE()
                if rj['result']['VISIT_ITEM']['status'] != 3:
                    self.getVisitItemList()
                else:
                    return
            else:
                msg = f"获取任务列表 失败\n" + json.dumps(rj, ensure_ascii=False)
        except:
            traceback.print_exc()

    def REWARD_TOMORROW(self):
        if mytool.gettime().hour in range(18, 21):
            taskRecordId = self.getTaskRecordId()
            if taskRecordId == '':
                print('未找到 taskRecordId')
                return
            params = {
                'taskId': 'REWARD_TOMORROW',
                'taskRecordId': taskRecordId,
            }
            try:
                rj = self.sec.get('https://miniapp.you.163.com/orchard/task/water/get.json', params=params).json()
                if rj['code'] == 200:
                    msg = f"REWARD_TOMORROW 成功\n"
                else:
                    msg = f"REWARD_TOMORROW 失败\n" + json.dumps(rj, ensure_ascii=False)

                print(msg)
            except:
                traceback.print_exc()

    def getTaskRecordId(self):
        params = {
            'taskIdList': '["REWARD_TOMORROW"]',
        }
        try:
            rj = self.sec.get('https://miniapp.you.163.com/orchard/task/list.json', params=params).json()
            if rj['code'] == 200:
                return rj['result']['REWARD_TOMORROW']['taskRecords'][0]['taskRecordId']
            else:
                print(json.dumps(rj, ensure_ascii=False))
                return ''
        except:
            traceback.print_exc()
            pass

if __name__ == '__main__':
    # DEBUG
    if os.path.exists('debug.py'):
        import debug
        debug.setDebugEnv()

    if mytool.getlistCk(f'{tokenName}') is None:
        print(f'请检查你的变量名称 {tokenName} 是否填写正确')
        exit(0)
    else:
        for i in mytool.getlistCk(f'{tokenName}'):
            wyyx_wxapp(i).GET_TASK()
            wyyx_wxapp(i).GET_EVERYDAY_RANDOM()
            wyyx_wxapp(i).drop()
            wyyx_wxapp(i).REWARD_TOMORROW()