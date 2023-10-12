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
            'Connection': 'keep-alive',
            'auth-token': data[1],
            'x-apm-parent-page-id': '0f735520-ed05-f34f-6a96-93ab2fb5d5',
            'x-wmsdk-close-store': 'v2',
            'x-component-is': 'packages/wm-cloud-assam/task/index',
            'weimob-pid': '4020112618957',
            'x-platform': 'mpg',
            'cloud-pid': '4020112618957',
            'parentrpcid': '3882cdeaf0dca57a',
            # 'x-sign': '6aff0f47d36d781b710be1a86a64736189410306',
            'cloud-project-name': 'tongyixiangmu',
            'x-page-route': 'packages/wm-cloud-assam/task/index',
            'x-ts': str(mytool.getMSecTimestamp()),
            'cloud-app-id': '31536475456-asmxiangmu-pod',
            'wos-x-channel': '0:TITAN',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
            'cloud-bosid': '4020112618957',
            'Content-Type': 'application/json;charset=UTF-8',
            'X-WX-Token': data[0],
            # 'x-wmsdk-bc': '12 1697072760652',
            # 'weimob-bosId': '4020112618957',
            # 'x-cms-sdk-request': '1.3.149',
            # 'x-apm-page-id': '987a2933-2b00-b5df-033c-aa26b1773f',
            # 'x-apm-conversation-id': 'cdeccb91-2a4e-22c7-7155-b0d00e2449',
            # 'x-req-from': 'cloud-fe-yunsdk-platform',
            'Referer': 'https://servicewechat.com/wx532ecb3bdaaf92f9/173/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        self.sec.cookies = {'rprm_cuid': data[2]}
        pass

    def 每日签到(self):
        json_data = {"appid": "wx532ecb3bdaaf92f9",
                     "basicInfo": {"bosId": 4020112618957, "cid": 176205957, "tcode": "weimob"},
                     "extendInfo": {"analysis": [], "bosTemplateId": 1000001178, "channelsource": 5,
                                    "childTemplateIds": [{"customId": 90004, "version": "crm@0.0.173"},
                                                         {"customId": 90002, "version": "ec@35.4"},
                                                         {"customId": 90006, "version": "hudong@0.0.185"},
                                                         {"customId": 90008, "version": "cms@0.0.356"}],
                                    "mpScene": 1053, "quickdeliver": {"enable": False}, "source": 1,
                                    "wxTemplateId": 7224, "youshu": {"enable": False}},
                     "i18n": {"language": "zh", "timezone": "8"}, "pid": "4020112618957",
                     "queryParameter": {"tracepromotionid": "100006218", "tracePromotionId": "100006218"},
                     "storeId": "0", "tracepromotionid": "100006218", "tracePromotionId": "100006218",
                     "umaData": "{\"sceneKey\":\"asm_mrqd\"}"}
        try:
            rj = self.sec.post('https://capi.weimobcloud.com/api3/api/asmmp/activity/v1/activity/join',
                               json=json_data).json()
            if rj['success'] is True:
                msg = f"登录成功\n"
            else:
                msg = f"登录失败\n" + json.dumps(rj, ensure_ascii=False)
            print(msg)
        except:
            print(json.dumps(rj, ensure_ascii=False))
            traceback.print_exc()
            pass
        pass

    def 每日查看推广海报(self):
        json_data = {"appid": "wx532ecb3bdaaf92f9",
                     "basicInfo": {"bosId": 4020112618957, "cid": 176205957, "tcode": "weimob"},
                     "extendInfo": {"analysis": [], "bosTemplateId": 1000001178, "channelsource": 5,
                                    "childTemplateIds": [{"customId": 90004, "version": "crm@0.0.173"},
                                                         {"customId": 90002, "version": "ec@35.4"},
                                                         {"customId": 90006, "version": "hudong@0.0.185"},
                                                         {"customId": 90008, "version": "cms@0.0.356"}],
                                    "mpScene": 1053, "quickdeliver": {"enable": False}, "source": 1,
                                    "wxTemplateId": 7224, "youshu": {"enable": False}},
                     "i18n": {"language": "zh", "timezone": "8"}, "pid": "4020112618957",
                     "queryParameter": {"tracepromotionid": "100045812", "tracePromotionId": "100045812"},
                     "storeId": "0", "tracepromotionid": "100045812", "tracePromotionId": "100045812",
                     "umaData": "{\"sceneKey\":\"asm_mrfxyl\"}"}
        try:
            rj = self.sec.post('https://capi.weimobcloud.com/api3/api/asmmp/activity/v1/activity/join',
                               json=json_data).json()
            if rj['success'] is True:
                msg = f"登录成功\n"
            else:
                msg = f"登录失败\n" + json.dumps(rj, ensure_ascii=False)
            print(msg)
        except:
            print(json.dumps(rj, ensure_ascii=False))
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
            tyasm(i.split("#")).每日签到()
            tyasm(i.split("#")).每日查看推广海报()
