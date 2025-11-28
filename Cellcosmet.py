"""
cron: 30 7 * * *
new Env("微信小程序-Cellcosmet")
env add wx_cellcosmet

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import ApiRequest
from script_utils import (
    build_weapp_headers,
    log_event,
    parse_response_content,
    normalize_result,
    parse_token_fields,
    request_with_retry,
)

title = '微信小程序-Cellcosmet'
tokenName = 'wx_cellcosmet'


class cellcosmet(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = 'Cellcosmet签到'
        (user_code,) = parse_token_fields(data, expected_fields=1, field_names=('userCode',))
        self.userCode = user_code
        self.sec.headers = build_weapp_headers(
            host='cellcosmet.haoduoke.cn',
            referer='https://servicewechat.com/wxa72c343870a41479/6/page-frame.html',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185',
            extra_headers={
                'orgClientId': '1',
                'appId': 'wxa72c343870a41479',
            },
        )

    def login(self):
        json_data = {
            'userCode': self.userCode,
            'customerId': self.userCode,
            'counterId': 203652716557,
            'userId': None,
            'signOid': 326279852111,
            'appOid': 59278884243,
            'orgClientId': 1,
        }
        try:
            resp = request_with_retry(
                self.sec,
                'POST',
                'https://cellcosmet.haoduoke.cn/custom/free/memc/sign/commit',
                json=json_data,
            )
            payload = parse_response_content(resp)
            success, message = normalize_result(payload)
            log_event('cellcosmet_checkin_result', success=success, msg=message)
            if success:
                self.sendmsg += f'✅ Cellcosmet签到成功：{message}\n'
            else:
                self.sendmsg += f'❌ Cellcosmet签到失败：{message}\n'
        except Exception as exc:  # noqa: BLE001
            log_event('cellcosmet_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ Cellcosmet签到失败：{exc}\n'
            raise


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, cellcosmet)
