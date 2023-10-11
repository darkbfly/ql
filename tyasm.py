"""
0 7 * * * tyasm.py
new Env("统一阿萨姆")
env add tyasm_cookies = X-WX-Token#auth-token#cookies下的rprm_cuid
"""
import json
# !/usr/bin/env python3
# coding: utf-8
import os
import traceback
import requests
import urllib3
import mytool

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '统一阿萨姆'
tokenName = 'tyasm_cookies'
msg = ''


class tyasm():
    def __init__(self, data):
        self.headers = {
            'Host': 'capi.weimobcloud.com',
            # 'Content-Length': '728',
            'auth-token': data[1],
            'x-wmsdk-close-store': 'v2',
            'x-component-is': 'packages/wm-cloud-assam/task/index',
            'x-platform': 'mpg',
            'x-sign': '49f98e135abe4c21488580b01e5c1863879003b9',
            'cloud-project-name': 'tongyixiangmu',
            'x-page-route': 'packages/wm-cloud-assam/task/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
            'Content-Type': 'application/json;charset=UTF-8',
            'X-WX-Token': data[0],
            'Referer': 'https://servicewechat.com/wx532ecb3bdaaf92f9/173/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.cookies = {'rprm_cuid': data[2], }
        self.sec = requests.session()
        self.sec.headers = self.headers
        pass

    def 每日签到(self):
        json_data = {
            'appid': 'wx532ecb3bdaaf92f9',
            'basicInfo': {
                'bosId': 4020112618957,
                'tcode': 'weimob',
                'cid': 176205957,
            },
            'extendInfo': {
                'wxTemplateId': 7224,
                'analysis': [],
                'bosTemplateId': 1000001178,
                'childTemplateIds': [
                    {
                        'customId': 90004,
                        'version': 'crm@0.0.173',
                    },
                    {
                        'customId': 90002,
                        'version': 'ec@35.4',
                    },
                    {
                        'customId': 90006,
                        'version': 'hudong@0.0.185',
                    },
                    {
                        'customId': 90008,
                        'version': 'cms@0.0.356',
                    },
                ],
                'quickdeliver': {
                    'enable': False,
                },
                'youshu': {
                    'enable': False,
                },
                'source': 1,
                'channelsource': 5,
                'mpScene': 1053,
            },
            'queryParameter': {
                'tracePromotionId': '100006218',
                'tracepromotionid': '100006218',
            },
            'i18n': {
                'language': 'zh',
                'timezone': '8',
            },
            'pid': '4020112618957',
            'storeId': '0',
            'umaData': '{"sceneKey":"asm_mrqd"}',
            'tracePromotionId': '100006218',
            'tracepromotionid': '100006218',
        }
        try:
            rj = self.sec.post('https://capi.weimobcloud.com/api3/api/asmmp/activity/v1/activity/join',
                               cookies=self.cookies, json=json_data)
            if rj['success'] is True:
                msg = f"登录成功\n"
            else:
                msg = f"登录失败\n" + json.dumps(rj, ensure_ascii=False)
            print(msg)
        except:
            traceback.print_exc()
            pass
        pass

    def 每日查看推广海报(self):
        json_data = {
            'appid': 'wx532ecb3bdaaf92f9',
            'basicInfo': {
                'bosId': 4020112618957,
                'tcode': 'weimob',
                'cid': 176205957,
            },
            'extendInfo': {
                'wxTemplateId': 7224,
                'analysis': [],
                'bosTemplateId': 1000001178,
                'childTemplateIds': [
                    {
                        'customId': 90004,
                        'version': 'crm@0.0.173',
                    },
                    {
                        'customId': 90002,
                        'version': 'ec@35.4',
                    },
                    {
                        'customId': 90006,
                        'version': 'hudong@0.0.185',
                    },
                    {
                        'customId': 90008,
                        'version': 'cms@0.0.356',
                    },
                ],
                'quickdeliver': {
                    'enable': False,
                },
                'youshu': {
                    'enable': False,
                },
                'source': 1,
                'channelsource': 5,
                'mpScene': 1053,
            },
            'queryParameter': {
                'tracePromotionId': '100045812',
                'tracepromotionid': '100045812',
            },
            'i18n': {
                'language': 'zh',
                'timezone': '8',
            },
            'pid': '4020112618957',
            'storeId': '0',
            'umaData': '{"sceneKey":"asm_mrfxyl"}',
            'tracePromotionId': '100045812',
            'tracepromotionid': '100045812',
        }
        try:
            rj = self.sec.post('https://capi.weimobcloud.com/api3/api/asmmp/activity/v1/activity/join',
                               cookies=self.cookies, json=json_data)
            if rj['success'] is True:
                msg = f"登录成功\n"
            else:
                msg = f"登录失败\n" + json.dumps(rj, ensure_ascii=False)
            print(msg)
        except:
            traceback.print_exc()
            pass
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
            tyasm(i).每日签到()
            tyasm(i).每日查看推广海报()
