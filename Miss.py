"""
cron: 0 7 * * *
new Env("微信小程序-蜜丝miss")
env add wx_miss = unionId#X-wx8465e1173d1e11b0-Token

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest
from script_utils import (
    build_weapp_headers,
    log_event,
    normalize_result,
    parse_response_content,
    parse_token_fields,
    request_with_retry,
)

tokenName = 'wx_miss'
msg = ''


class miss(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = '蜜丝签到'
        union_id, token = parse_token_fields(
            data,
            expected_fields=2,
            field_names=('unionId', 'token'),
        )
        self.union_id = union_id
        self.sec.headers = build_weapp_headers(
            host='clubwx.hm.liby.com.cn',
            referer='https://servicewechat.com/wx8465e1173d1e11b0/33/page-frame.html',
            user_agent=('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI '
                        'MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555'),
            extra_headers={
                'platformCode': 'Miss',
                'appId': 'wx8465e1173d1e11b0',
                'unionId': union_id,
                'X-wx8465e1173d1e11b0-Token': token,
            },
        )


    def login(self):
        try:
            resp = request_with_retry(
                self.sec,
                'GET',
                'https://clubwx.hm.liby.com.cn/miniprogram/benefits/activity/sign/execute.htm',
                params={'taskId': '840'},
            )
        except Exception as exc:  # noqa: BLE001
            log_event('miss_checkin_failed', unionId=self.union_id, reason=str(exc))
            self.sendmsg += f'❌ 蜜丝签到失败：{exc}\n'
            raise

        payload = parse_response_content(resp)
        success, message = normalize_result(payload)
        log_event('miss_checkin_result', unionId=self.union_id, success=success, msg=message)
        if success:
            self.sendmsg += f'✅ 蜜丝签到成功：{message}\n'
        else:
            self.sendmsg += f'❌ 蜜丝签到失败：{message}\n'

if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, miss)
