"""
cron: 0 3 * * *
new Env("微信小程序-芈姐生活馆")
env add wx_mijie

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

tokenName = "wx_mijie"
msg = ""


class mijie(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = "芈姐生活馆签到"
        (auth_token,) = parse_token_fields(data, expected_fields=1, field_names=("Authori-zation",))
        self.sec.headers = build_weapp_headers(
            host="www.mijielive.store",
            referer="https://servicewechat.com/wx88534cdc1fae6707/95/page-frame.html",
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/126.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI "
                        "MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/13487"),
            extra_headers={"Authori-zation": auth_token},
        )

    def login(self):
        url = "https://www.mijielive.store/api/api/front/user/sign/user"
        json_data = {
            "all": 0,
            "integral": 0,
            "sign": 1,
        }
        try:
            resp = request_with_retry(
                self.sec,
                "POST",
                url,
                json=json_data,
            )
        except Exception as exc:  # noqa: BLE001
            log_event("mijie_checkin_failed", reason=str(exc))
            self.sendmsg += f"❌ 芈姐生活馆签到失败：{exc}\n"
            raise

        payload = parse_response_content(resp)
        success, message = normalize_result(payload)
        log_event("mijie_checkin_result", success=success, msg=message)
        if success:
            self.sendmsg += f"✅ 芈姐生活馆签到成功：{message}\n"
        else:
            self.sendmsg += f"❌ 芈姐生活馆签到失败：{message}\n"


if __name__ == "__main__":
    ApiRequest.ApiMain(["login"]).run(tokenName, mijie)
