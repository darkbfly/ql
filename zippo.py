
"""
cron: 30 7 * * *
new Env("微信小程序-zippo")
env add zippo_auth
未完成
"""
#!/usr/bin/env python3
# coding: utf-8
import ApiRequest
from script_utils import (
    build_weapp_headers,
    log_event,
    parse_response_content,
    normalize_result,
    parse_token_fields,
    request_with_retry,
)

title = '微信小程序-zippo'
tokenName = 'zippo_auth'


class zippo(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = 'zippo签到'
        (auth_token,) = parse_token_fields(data, expected_fields=1, field_names=('Authorization',))
        self.sec.headers = build_weapp_headers(
            host='wx-center.zippo.com.cn',
            referer='https://servicewechat.com/wxaa75ffd8c2d75da7/69/page-frame.html',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819) XWEB/8531',
            extra_headers={
                'Authorization': auth_token,
                'x-app-id': 'zippo',
                'x-platform-id': 'wxaa75ffd8c2d75da7',
                'x-platform-env': 'release',
                'x-platform': 'wxmp',
                'Content-Type': 'application/json;charset=UTF-8',
            },
        )

    def login(self):
        try:
            resp = request_with_retry(
                self.sec,
                'POST',
                'https://wx-center.zippo.com.cn/api/daily-signin',
                params='',
                json={},
            )
            payload = parse_response_content(resp)
            success, message = normalize_result(payload)
            log_event('zippo_checkin_result', success=success, msg=message)
            if success:
                self.sendmsg += f'✅ zippo签到成功：{message}\n'
            else:
                self.sendmsg += f'❌ zippo签到失败：{message}\n'
        except Exception as exc:  # noqa: BLE001
            log_event('zippo_checkin_failed', reason=str(exc))
            self.sendmsg += f'❌ zippo签到失败：{exc}\n'
            raise

    def favorited(self):
        jsonData = {
            "targetType": "sku",
            "targetId": "265",
            "favorited": True
        }
        rj = self.sec.post('https://wx-center.zippo.com.cn/api/favorites', params='', json=jsonData).json()
        print(rj)

        rj = self.sec.post('https://wx-center.zippo.com.cn/api/missions/5/rewards', params='', json={"id":5}).json()
        print(rj)
        pass

    def unfavorited(self):
        jsonData = {
            "targetType": "sku",
            "targetId": "265",
            "favorited": False
        }
        rj = self.sec.post('https://wx-center.zippo.com.cn/api/favorites', params='', json=jsonData).json()
        print(rj)
        pass



if __name__ == '__main__':
    ApiRequest.ApiMain(['login', 'unfavorited', 'favorited']).run(tokenName, zippo)