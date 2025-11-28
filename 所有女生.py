"""
cron: 0 3 * * *
new Env("微信小程序-所有女生")
env add wx_syns

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

tokenName = 'wx_syns'
msg = ''


class syns(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = "所有女生签到"
        access_token, authorization = parse_token_fields(
            data,
            expected_fields=2,
            field_names=("AccessToken", "Authorization"),
        )
        self.access_token = access_token
        self.sec.headers = build_weapp_headers(
            host="7.wawo.cc",
            referer="http",
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI "
                        "MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c1f)XWEB/11581"),
            extra_headers={
                "activityCode": "D2L0T1T4",
                "AccessToken": access_token,
                "Authorization": authorization,
            },
        }

    def login(self):
        url = "https://7.wawo.cc/api/activity/wx/task/sign/signIn"
        try:
            resp = request_with_retry(
                self.sec,
                "POST",
                url,
                data="{}",
            )
        except Exception as exc:  # noqa: BLE001
            log_event("syns_checkin_failed", accessToken=self.access_token, reason=str(exc))
            self.sendmsg += f"❌ 所有女生签到失败：{exc}\n"
            raise

        payload = parse_response_content(resp)
        success, message = normalize_result(payload)
        log_event("syns_checkin_result", accessToken=self.access_token, success=success, msg=message)
        if success:
            self.sendmsg += f"✅ 所有女生签到成功：{message}\n"
        else:
            self.sendmsg += f"❌ 所有女生签到失败：{message}\n"


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, syns)
