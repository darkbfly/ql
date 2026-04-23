"""
new Env("微信小程序-海天美味馆")
cron 0 8 * * *
环境变量名称 wx_htmw_auth = Authorization#X-Haday-Token#uuid

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import ApiRequest
from datetime import datetime
from script_utils import (
    build_weapp_headers,
    log_event,
    parse_response_content,
    normalize_result,
    parse_token_fields,
    request_with_retry,
)

title = '微信小程序-海天美味馆'
tokenName = 'wx_htmw_auth'


class htmwg(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = '海天美味馆签到'
        auth_token, haday_token, uuid = parse_token_fields(
            data,
            expected_fields=3,
            field_names=('Authorization', 'X-Haday-Token', 'uuid'),
        )
        extra_headers = {
            'Authorization': auth_token,
            'uuid': uuid,
            'envVersion': 'release',
            'X-Haday-Token': haday_token,
        }
        self.sec.headers = build_weapp_headers(
            host='cmallapi.xkmm.cn',
            referer='https://servicewechat.com/wx7a890ea13f50d7b6/767/page-frame.html',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf254186b) XWEB/19481',
            extra_headers=extra_headers,
        )

    def login(self):
        json_data = {'activity_code': datetime.now().strftime('%Y%m'), 'fill_date': ''}
        try:
            resp = request_with_retry(
                self.sec,
                'POST',
                'https://cmallapi.xkmm.cn/buyer-api/sign/activity/sign',
                json=json_data,
            )
            payload = parse_response_content(resp)
            success, message = normalize_result(payload)
            log_event('htmwg_checkin_result', success=success, msg=message)
            if success:
                self.sendmsg += f'✅ 海天美味馆签到成功：{message}\n'
            else:
                self.sendmsg += f'❌ 海天美味馆签到失败：{message}\n'
        except Exception as exc:  # noqa: BLE001
            log_event('htmwg_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ 海天美味馆签到失败：{exc}\n'
            raise


if __name__ == "__main__":
    ApiRequest.ApiMain(['login']).run(tokenName, htmwg)
