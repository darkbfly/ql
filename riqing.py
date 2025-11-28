"""
cron: 0 7 * * *
new Env("微信小程序-日清食品体验馆")
env add wx_riqing = unionId#X-wx8465e1173d1e11b0-Token

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
from datetime import datetime

# !/usr/bin/env python3
# coding: utf-8
import ApiRequest
from script_utils import (
    log_event,
    parse_response_content,
    normalize_result,
    parse_token_fields,
    request_with_retry,
)

tokenName = 'wx_riqing'
msg = ''


class riqing(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = '日清食品体验馆签到'
        user_id, token = parse_token_fields(
            data, expected_fields=2, field_names=('User-Id', 'Token')
        )
        self.sec.headers = {
            'Host': 'prod-api.nissinfoodium.com.cn',
            'Connection': 'keep-alive',
            'User-Id': user_id,
            'Ep-Version': '1',
            'App-Path': 'my/sign-in/sign-in',
            'Extra': '{"scene":1053}',
            'Enterprise-Hash': '1246b9ecd0972c7b0e50b4c9cdad9f0c',
            'App-Name': '%E6%97%A5%E6%B8%85%E9%A3%9F%E5%93%81%E4%BD%93%E9%AA%8C%E9%A6%86',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
            'xweb_xhr': '1',
            'Api-Version': 'v1.0',
            'Token': token,
            'App-Version': 'V2.3.6',
            'Referer': 'https://servicewechat.com/wx21b71db59d93bd6d/66/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        日期 = datetime.now().strftime("%Y-%m-") + str(datetime.now().day)
        url = f'https://prod-api.nissinfoodium.com.cn/gw-shop/app/v1/signs/sign?date={日期}&type=1&'
        try:
            resp = request_with_retry(self.sec, 'GET', url)
            payload = parse_response_content(resp)
            success, message = normalize_result(payload)
            log_event('riqing_checkin_result', success=success, msg=message)
            if success:
                self.sendmsg += f'✅ 日清食品体验馆签到成功：{message}\n'
            else:
                self.sendmsg += f'❌ 日清食品体验馆签到失败：{message}\n'
        except Exception as exc:  # noqa: BLE001
            log_event('riqing_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ 日清食品体验馆签到失败：{exc}\n'
            raise


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, riqing)
