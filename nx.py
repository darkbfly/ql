"""
cron: 0 7 * * *
new Env("微信小程序-奈雪")
env add wx_miss = Authorization#lat#lng#openId

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""

import base64
import hashlib
import hmac

import ApiRequest
import mytool
from script_utils import (
    log_event,
    parse_response_content,
    normalize_result,
    parse_token_fields,
    request_with_retry,
)

tokenName = 'wx_nx'
msg = ''


class nx(ApiRequest.ApiRequest):
    def sign(self, nonce, openId, timestamp):
        msg = f"nonce={nonce}&openId={openId}&timestamp={timestamp}"
        print(msg)
        key = 'sArMTldQ9tqU19XIRDMWz7BO5WaeBnrezA'
        return base64.b64encode(hmac.new(key.encode(), msg.encode(), hashlib.sha1).digest()).decode()

    def __init__(self, data):
        super().__init__()
        self.title = '奈雪签到'
        auth_token, lat, lng, open_id = parse_token_fields(
            data, expected_fields=4, field_names=('Authorization', 'lat', 'lng', 'openId')
        )
        self.lat = lat
        self.lng = lng
        self.openId = open_id
        self.sec.headers = {
            'Host': 'tm-web.pin-dao.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': auth_token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129',
            'Content-Type': 'application/json',
            'Origin': 'https://tm-web.pin-dao.cn',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    def login(self):
        signDate = f"{mytool.gettime().year}-{mytool.gettime().month}-{mytool.gettime().day}"
        timestamp = mytool.getSecTimestamp()
        nonce = mytool.randomint(6)
        json_data = {
            'common': {
                'platform': 'wxapp',
                'version': '5.2.22',
                'imei': '',
                'osn': 'microsoft',
                'sv': 'Windows 10 x64',
                'lat': float(self.lat),
                'lng': float(self.lng),
                'lang': 'zh_CN',
                'currency': 'CNY',
                'timeZone': '',
                'nonce': nonce,
                'openId': self.openId,
                'timestamp': timestamp,
                'signature': self.sign(nonce, self.openId, timestamp),
            },
            'params': {
                'businessType': 1,
                'brand': 26000252,
                'tenantId': 1,
                'channel': 2,
                'stallType': 'PD_S_004',
                'storeId': 26074341,
                'storeType': 1,
                'cityId': 350100,
                'appId': 'wxab7430e6e8b9a4ab',
                'signDate': signDate,
            },
        }
        try:
            resp = request_with_retry(
                self.sec, 'POST', 'https://tm-web.pin-dao.cn/user/sign/save', json=json_data
            )
            payload = parse_response_content(resp)
            success, message = normalize_result(payload)
            log_event('nx_checkin_result', success=success, msg=message)
            if success:
                self.sendmsg += f'✅ 奈雪签到成功：{message}\n'
            else:
                self.sendmsg += f'❌ 奈雪签到失败：{message}\n'
        except Exception as exc:  # noqa: BLE001
            log_event('nx_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ 奈雪签到失败：{exc}\n'
            raise


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, nx)