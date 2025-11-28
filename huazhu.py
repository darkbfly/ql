"""
new Env("微信小程序-华住签到")
cron 0 7 * * *
环境变量名称 huazhu_cookies

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""

import ApiRequest
import mytool
from script_utils import (
    log_event,
    parse_response_content,
    normalize_result,
    parse_token_fields,
    request_with_retry,
)

title = '微信小程序-华住签到'
tokenName = 'huazhu_cookies'


class huazhu(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = '华住签到'
        (cookie_str,) = parse_token_fields(data, expected_fields=1, field_names=('Cookie',))
        self.sec.headers = {
            "Host": "appgw.huazhu.com",
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "Client-Platform": "WX-MP",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11275",
            "Origin": "http",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "http",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": cookie_str,
        }

    def login(self):
        url = f"https://appgw.huazhu.com/game/sign_in?date={mytool.getSecTimestamp()}"
        try:
            resp = request_with_retry(self.sec, 'GET', url)
            payload = parse_response_content(resp)
            success, message = normalize_result(payload)
            log_event('huazhu_checkin_result', success=success, msg=message)
            if success:
                self.sendmsg += f'✅ 华住签到成功：{message}\n'
            else:
                self.sendmsg += f'❌ 华住签到失败：{message}\n'
        except Exception as exc:  # noqa: BLE001
            log_event('huazhu_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ 华住签到失败：{exc}\n'
            raise

if __name__ == "__main__":
    ApiRequest.ApiMain(['login']).run(tokenName, huazhu)
