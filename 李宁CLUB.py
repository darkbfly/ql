"""
cron: 30 4 * * *
new Env("微信小程序-李宁CLUB")
env add wx_nl_club

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import ApiRequest
from script_utils import (
    build_weapp_headers,
    log_event,
    normalize_result,
    parse_response_content,
    parse_token_fields,
    request_with_retry,
)

tokenName = 'wx_ln_club'
msg = ''


class lining(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = '李宁CLUB 签到'
        (auth_token,) = parse_token_fields(data, expected_fields=1, field_names=('Authorization',))
        self.sec.headers = build_weapp_headers(
            host='mcenter-gateway.wx.lining.com',
            referer='https://servicewechat.com/wx54df8ea3b9c8ec10/175/page-frame.html',
            user_agent=('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI '
                        'MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c1f)XWEB/11581'),
            extra_headers={'Authorization': auth_token},
        )

    def login(self):
        try:
            resp = request_with_retry(
                self.sec,
                'GET',
                'https://mcenter-gateway.wx.lining.com/customer/v1/sign',
            )
        except Exception as exc:  # noqa: BLE001
            log_event('lining_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ 李宁CLUB 签到失败：{exc}\n'
            raise

        payload = parse_response_content(resp)
        success, message = normalize_result(payload)
        log_event('lining_checkin_result', success=success, msg=message)
        if success:
            self.sendmsg += f'✅ 李宁CLUB 签到成功：{message}\n'
        else:
            self.sendmsg += f'❌ 李宁CLUB 签到失败：{message}\n'


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, lining)
