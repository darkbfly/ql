"""
cron: 0 3 * * *
new Env("微信小程序-ZOSEE")
env add wx_zosee

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import datetime

import ApiRequest
from script_utils import (
    build_weapp_headers,
    log_event,
    parse_response_content,
    normalize_result,
    parse_token_fields,
    request_with_retry,
)

tokenName = 'wx_zosee'
msg = ''


class ZOSEE(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = 'ZOSEE签到'
        (auth_token,) = parse_token_fields(data, expected_fields=1, field_names=('Authorization',))
        self.sec.headers = build_weapp_headers(
            host='smp-api.iyouke.com',
            referer='http',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11275',
            extra_headers={
                'Authorization': auth_token,
                'appId': 'wx755f4d86f9328dce',
                'envVersion': 'release',
                'version': '2.4.35',
                'Accept-Encoding': 'gzip, deflate, br',
            },
        )

    def login(self):
        url = f"https://smp-api.iyouke.com/dtapi/pointsSign/user/sign?date={datetime.datetime.now().year}%2F{datetime.datetime.now().month}%2F{datetime.datetime.now().day}"
        try:
            resp = request_with_retry(self.sec, 'GET', url)
            payload = parse_response_content(resp)
            success, message = normalize_result(payload)
            log_event('zosee_checkin_result', success=success, msg=message)
            if success:
                self.sendmsg += f'✅ ZOSEE签到成功：{message}\n'
            else:
                self.sendmsg += f'❌ ZOSEE签到失败：{message}\n'
        except Exception as exc:  # noqa: BLE001
            log_event('zosee_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ ZOSEE签到失败：{exc}\n'
            raise


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, ZOSEE)
