"""
cron: 0 6,18 * * * kbj.py
new Env("微信小程序-康佰家")
env add kbj_token

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

title = '微信小程序-康佰家'
tokenName = 'kbj_token1'


class kbj(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = title
        (token,) = parse_token_fields(data, expected_fields=1, field_names=('oldToken',))
        self.sec.headers = build_weapp_headers(
            host='vip-mall.kbjcn.com',
            referer='https://servicewechat.com/wxe727824701ee66d4/209/page-frame.html',
            user_agent=('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI '
                        'MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541110) '
                        'XWEB/16729'),
            extra_headers={'oldToken': token},
        )


    def login(self):
        try:
            resp = request_with_retry(
                self.sec,
                'POST',
                'https://vip-mall.kbjcn.com/vip/integral/sign',
                json={},
            )
        except Exception as exc:  # noqa: BLE001
            log_event('kbj_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ 康佰家签到失败：{exc}\n'
            raise

        payload = parse_response_content(resp)
        success, message = normalize_result(payload)
        log_event('kbj_checkin_result', success=success, msg=message)
        if success:
            self.sendmsg += f'✅ 康佰家签到成功：{message}\n'
        else:
            self.sendmsg += f'❌ 康佰家签到失败：{message}\n'


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, kbj)
