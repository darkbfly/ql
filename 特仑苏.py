"""
cron: 0 7 * * *
new Env("微信小程序-特仑苏")
env add wx_tls = openid

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest
import mytool
from script_utils import (
    log_event,
    parse_response_content,
    normalize_result,
    parse_token_fields,
    request_with_retry,
)

tokenName = 'wx_tls'
msg = ''


class tls(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = '特仑苏签到'
        (openid,) = parse_token_fields(data, expected_fields=1, field_names=('openid',))
        self.openid = openid
        self.sec.headers = {
            'Host': 'mall.telunsu.net',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://mall.telunsu.net',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://mall.telunsu.net/minlifeh5/himilk/vip/vipCommunityOld.html?navType=1',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.cookies = {
            'HWWAFSESTIME': str(mytool.getMSecTimestamp()),
            'MY_OPENID': self.openid,
            'sajssdk_2015_cross_new_user': '1',
        }

    def login(self):
        json_data = {'openid': self.openid}
        try:
            resp = request_with_retry(
                self.sec,
                'POST',
                'https://mall.telunsu.net/wxapi/user/signIn',
                params='',
                cookies=self.cookies,
                json=json_data,
            )
            payload = parse_response_content(resp)
            success, message = normalize_result(payload)
            log_event('tls_checkin_result', success=success, msg=message)
            if success:
                self.sendmsg += f'✅ 特仑苏签到成功：{message}\n'
            else:
                self.sendmsg += f'❌ 特仑苏签到失败：{message}\n'
        except Exception as exc:  # noqa: BLE001
            log_event('tls_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ 特仑苏签到失败：{exc}\n'
            raise


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, tls)
