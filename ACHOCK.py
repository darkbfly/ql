"""
cron: 0 3 * * *
new Env("微信小程序-ACHOCK")
env add wx_achock

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import ApiRequest
import mytool
from script_utils import (
    build_weapp_headers,
    log_event,
    parse_token_fields,
    request_json_with_retry,
)

tokenName = 'wx_achock'
msg = ''


class achock(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = 'ACHOCK 签到'
        access_token, sid, uuid = parse_token_fields(
            data,
            expected_fields=3,
            field_names=('access_token', 'sid', 'uuid'),
        )
        self.access_token = access_token
        self.sid = sid
        self.uuid = uuid
        self.sec.headers = build_weapp_headers(
            host='h5.youzan.com',
            referer='https://servicewechat.com/wxecf8fab05dbec020/7/page-frame.html',
            user_agent=('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI '
                        'MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b17)XWEB/9185'),
        )
        self.sec.headers['Extra-Data'] = (
            f'{{"is_weapp":1,"sid":"{self.sid}","version":"2.160.6.101","client":"weapp","bizEnv":"wsc","uuid":"{self.uuid}","ftime":{mytool.getMSecTimestamp()}}}'
        )

    def login(self):
        params = {
            'checkinId': '3520910',
            'app_id': 'wxecf8fab05dbec020',
            'kdt_id': '129380009',
            'access_token': self.access_token,
        }

        try:
            rj = request_json_with_retry(
                self.sec,
                'GET',
                'https://h5.youzan.com/wscump/checkin/checkinV2.json',
                params=params,
            )
        except Exception as exc:  # noqa: BLE001
            log_event('achock_checkin_failed', sid=self.sid, reason=str(exc))
            self.sendmsg += f'❌ ACHOCK 签到失败：{exc}\n'
            raise

        success = bool(rj.get('success') or rj.get('code') in (0, '0'))
        message = rj.get('msg') or rj.get('message') or rj
        log_event('achock_checkin_result', sid=self.sid, success=success, msg=message)
        if success:
            self.sendmsg += f'✅ ACHOCK 签到成功：{message}\n'
        else:
            self.sendmsg += f'❌ ACHOCK 签到失败：{message}\n'


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, achock)
