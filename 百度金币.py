"""
cron: 0 6 * * *
new Env("微信小程序-小度商城")
env add wx_bd_mall_cookie

变量格式:
wx_bd_mall_cookie="BAIDUID=xxx; BAIDUID_BFESS=xxx; ...; rk=xxx"
"""

import urllib.parse
import time

import ApiRequest
import mytool
from script_utils import log_event, normalize_result, request_json_with_retry

tokenName = "wx_bd_mall_cookie"


def parse_cookie_string(cookie_raw: str) -> dict:
    cookies = {}
    for item in cookie_raw.split(";"):
        item = item.strip()
        if not item or "=" not in item:
            continue
        key, value = item.split("=", 1)
        key = key.strip()
        value = urllib.parse.unquote(value.strip())
        if key:
            cookies[key] = value
    if not cookies:
        raise ValueError("cookie 解析失败，请检查 wx_bd_mall_cookie 格式")
    return cookies


class DuMall(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.title = "微信小程序-小度商城"
        self.cookies = parse_cookie_string(data)
        self.sec.cookies.update(self.cookies)
        self.sec.headers.update(
            {
                "Host": "dumall.baidu.com",
                "Connection": "keep-alive",
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/132.0.0.0 Safari/537.36 "
                    "MicroMessenger/7.0.20.1781(0x6700143B) "
                    "NetType/WIFI MiniProgramEnv/Windows "
                    "WindowsWechat/WMPF WindowsWechat(0x63090a13) "
                    "UnifiedPCWindowsWechat(0xf254181d) XWEB/19201 "
                    "miniProgram/wx3b2a29168df0cfa8"
                ),
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json;charset=UTF-8",
                "Origin": "https://dumall.baidu.com",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://dumall.baidu.com/",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
            }
        )

    def complete_gold_task(self, action_type: int):
        url = (
            "https://dumall.baidu.com/api/platform/gold/task/completeGoldTask"
            f"?timestamp={mytool.getMSecTimestamp()}"
        )
        payload = {
            "actionType": action_type,
            "source": "dumall",
            "channelId": "0",
            "platformId": 7,
        }
        try:
            result = request_json_with_retry(self.sec, "POST", url, json=payload)
        except Exception as exc:  # noqa: BLE001
            log_event(
                "dumall_complete_gold_task_failed",
                action_type=action_type,
                reason=str(exc),
            )
            self.sendmsg += f"❌ 金币任务(actionType={action_type})失败：{exc}\n"
            raise

        success, message = normalize_result(result)
        log_event(
            "dumall_complete_gold_task_result",
            action_type=action_type,
            success=success,
            message=message,
        )
        if success:
            self.sendmsg += f"✅ 金币任务(actionType={action_type})完成：{message}\n"
        else:
            self.sendmsg += f"❌ 金币任务(actionType={action_type})失败：{message}\n"

    def run_all_tasks(self):
        self.complete_gold_task(5)
        time.sleep(20)
        self.complete_gold_task(3)


if __name__ == "__main__":
    ApiRequest.ApiMain(["run_all_tasks"]).run(tokenName, DuMall)
