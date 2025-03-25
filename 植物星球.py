"""
cron: 0 3 * * *
new Env("微信小程序-植物星球")
env add wx_zwxq

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""

import ApiRequest
import mytool

tokenName = "wx_zwxq"
msg = ""


class zwxq(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            "Host": "api.pftp2012.com",
            "Connection": "keep-alive",
            # 'Content-Length': '72',
            "xweb_xhr": "1",
            "Authorization": "Bearer",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/13487",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://servicewechat.com/wxd7296b6421fc974e/1/page-frame.html",
            # 'Accept-Encoding': 'gzip, deflate, br',
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        self.userName = data.split("#")[0]
        self.pwd = data.split("#")[1]

    def login(self):
        data = {
            "userName": self.userName,
            "userPwd": mytool.calculate_md5(self.pwd),
            "channel": "40",
        }

        rj = self.sec.post(
            "https://api.pftp2012.com/api/Member/Login", data=data
        ).json()
        if rj["Status"] == 100:
            self.sec.headers["Authorization"] = (
                "Bearer " + rj["Data"]["MemberInfo"]["Token"]
            )

    def signIn(self):
        data = {
            "channel": "40",
        }
        rj = self.sec.post(
            "https://api.pftp2012.com/api/Member/SignIn", data=data
        ).json()
        print(rj)

    def completeMission(self):
        data = {
            "type": "60",
            "channel": "40",
        }

        rj = self.sec.post(
            "https://api.pftp2012.com/api/Member/CompleteMemberMission",
            data=data,
        ).json()
        print(rj)


if __name__ == "__main__":
    ApiRequest.ApiMain(["login", "signIn", "completeMission"]).run(tokenName, zwxq)
