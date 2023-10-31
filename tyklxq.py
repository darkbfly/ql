
"""
cron: 0 7 * * * tyklxq.py
new Env("微信小程序-统一快乐星球")
env add tyklxq_cookies
"""
#!/usr/bin/env python3
# coding: utf-8

import json
import os
import traceback
import requests
import mytool
from notify import send
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '微信小程序-统一快乐星球'
tokenName = 'tyklxq_cookies'


class klxq():
    def __init__(self, data):
        self.headers = {
            'Host': 'xapi.weimob.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8391',
            'Content-Type': 'application/json',
            'cloud-project-name': 'tongyixiangmu',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh',
            'X-WX-Token': data
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        pass

    def login(self):
        data = {"appid": "wx532ecb3bdaaf92f9",
                "basicInfo": {"vid": 6013753979957, "vidType": 2, "bosId": 4020112618957, "productId": 146,
                              "productInstanceId": 3168798957, "productVersionId": "12017", "merchantId": 2000020692957,
                              "tcode": "weimob", "cid": 176205957},
                "extendInfo": {"wxTemplateId": 7224, "analysis": [], "bosTemplateId": 1000001178,
                               "childTemplateIds": [{"customId": 90004, "version": "crm@0.0.173"},
                                                    {"customId": 90002, "version": "ec@35.4"},
                                                    {"customId": 90006, "version": "hudong@0.0.185"},
                                                    {"customId": 90008, "version": "cms@0.0.356"}],
                               "quickdeliver": {"enable": False}, "youshu": {"enable": False}, "source": 1,
                               "channelsource": 5, "refer": "onecrm-signgift", "mpScene": 1053},
                "queryParameter": {"tracePromotionId": "100006218", "tracepromotionid": "100006218"},
                "i18n": {"language": "zh", "timezone": "8"}, "pid": "4020112618957", "storeId": "0",
                "customInfo": {"source": 0, "wid": 10752782095}, "tracePromotionId": "100006218",
                "tracepromotionid": "100006218"}
        try:
            rj = self.sec.post('https://xapi.weimob.com/api3/onecrm/mactivity/sign/misc/sign/activity/core/c/sign', headers=self.headers, json=data).json()
            if rj['errcode'] == "0":
                msg = f"签到成功\n获得{rj['data']['fixedReward']['points']} + {rj['data']['extraReward']['points']}积分!\n" \
                      f"获得{rj['data']['fixedReward']['growth']} + {rj['data']['extraReward']['growth']}成长值!"
            else:
                msg = f"签到失败\n" + json.dumps(rj, ensure_ascii=False)
            print(msg)
            send(title, msg)
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
            klxq(i).login()
