# -*- coding: utf-8 -*-
# @Time: 2023年04月06日14时26分
"""
0 7 * * * yljf.py
new Env("WEB-雨云")
env add yljf_token
"""
import os

import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path
import logging
import json

import mytool

''''脚本使用说明：
 后缀名改成py
 
白嫖的项目：签到白嫖游戏服务器或者稳定的虚拟主机，攒着提现也可以（2018年以来一直稳定运行的，自己可以查一查资料）

 第一步：上传本脚本到青龙（本脚本是py不是js 别搞错了）
 第二步：去  https://www.rainyun.cc/?ref=MzUxMzA= 注册一个账号（不提现只抢游戏云和主机的话不用实名）
 想提现的话6万积分起提现...绑定支付宝提现（稳到，亲测过，也有官方用户群）。
 第三步：本脚本里第121行122行里设置一下自己注册的账号和密码！！！
         本脚本里第121行122行里设置一下自己注册的账号和密码！！！
         本脚本里第121行122行里设置一下自己注册的账号和密码！！！
 第四步：时间规则：0 0 23 * * ?    #每天 23 点执行一次 （可以按自己的需求，每天执行一次）
 
  积分规则及说明:本脚本是每天实现自动签到（每天300个积分），入门级游戏云或者虚拟主机2000积分一周。
这样下来一直用积分续费，想提现的话6万积分起提现...绑定支付宝提现（稳到）。


注册地址：
https://www.rainyun.cc/?ref=rain

https://www.rainyun.cc/?ref=rain


提现规则：6万积分起提现（稳到，不过建议用来续费游戏云比较划算）

 新人完成积分任务以后大概会有7000积分（积分商城每天20点刷新，自己抢一下一个主机或者游戏云）。
而2000积分就可以领取一个免费的MC服务器或者主机，而且可以用积分进行续费！续费也只需要2000积分！
前期积分任务做完加上每日签到，足够免费续费一个月了！后面一直用积分续费。


注册地址：
https://www.rainyun.cc/?ref=rain

'''

tokenName = 'yuyun_userInfo'
# 忽略 不验证ssl的提示
import warnings
warnings.filterwarnings('ignore')

class RainYun():

    def __init__(self, user: str, pwd: str) -> None:
        # 认证信息
        self.user = user.lower()
        self.pwd = pwd
        self.json_data = json.dumps({
            "field": self.user,
            "password": self.pwd,
        })
        # 日志输出
        self.logger = logging.getLogger(self.user)
        formatter = logging.Formatter(datefmt='%Y/%m/%d %H:%M:%S',
                                      fmt="%(asctime)s 雨云 %(levelname)s: 用户<%(name)s> %(message)s")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        # 签到结果初始化
        self.signin_result = False
        # 请求设置
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            "Origin": "https://api.rainyun.com",
            "Referer": "https://api.rainyun.com"
        })
        self.login_url = "https://api.v2.rainyun.com/user/login"
        self.signin_url = "https://api.v2.rainyun.com/user/reward/tasks"
        self.logout_url = "https://api.v2.rainyun.com/user/logout"
        self.query_url = "https://api.v2.rainyun.com/user/"
        # 忽略 .cc ssl错误
        self.session.verify = False

    def login(self) -> None:
        """登录"""
        res = self.session.post(
            url=self.login_url, headers={"Content-Type": "application/json"}, data=self.json_data)
        if res.text.find("200") > -1:
            self.logger.info("登录成功")
            self.session.headers.update({
                "X-CSRF-Token": res.cookies.get("X-CSRF-Token", "")
            })
        else:
            self.logger.error(f"登录失败，响应信息：{res.text}")

    def signin(self) -> None:
        """签到"""
        res = self.session.post(url=self.signin_url, headers={"Content-Type": "application/json"}, data=json.dumps({
            "task_name": "每日签到",
            "verifyCode": ""
        }))
        self.signin_date = datetime.utcnow()
        if res.text.find("200") > -1:
            self.logger.info("成功签到并领取积分")
            self.signin_result = True
        else:
            self.logger.error(f"签到失败，响应信息：{res.text}")
            self.signin_result = False

    def logout(self) -> None:
        res = self.session.post(url=self.logout_url)
        if res.text.find("200") > -1:
            self.logger.info('已退出登录')
        else:
            self.logger.warning(f"退出登录时出了些问题，响应信息：{res.text}")

    def query(self) -> None:
        res = self.session.get(url=self.query_url)
        self.points = None
        if res.text.find("200") > -1:
            data = res.json()["data"]
            self.points = data.get("Points", None) or data["points"]
            self.logger.info("积分查询成功为 " + repr(self.points))
        else:
            self.logger.error(f"积分信息失败，响应信息：{res.text}")

    def log(self, log_file: str, max_num=5) -> None:
        """存储本次签到结果的日志"""
        # 北京时间
        time_string = self.signin_date.replace(tzinfo=timezone.utc).astimezone(
            timezone(timedelta(hours=8))).strftime("%Y/%m/%d %H:%M:%S")
        file = Path(log_file)
        record = {
            "date": time_string,
            "result": self.signin_result,
            "points": self.points
        }
        previous_records = {}
        if file.is_file():
            try:
                with open(log_file, 'r') as f:
                    previous_records = json.load(f)
                if not previous_records.get(self.user):
                    previous_records[self.user] = []
                previous_records[self.user].insert(0, record)
                previous_records[self.user] = previous_records[self.user][:max_num]
            except Exception as e:
                self.logger.error("序列化日志时出错："+repr(e))
        else:
            previous_records[self.user] = [record]
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(previous_records, f, indent=4)
        self.logger.info('日志保存成功')


if __name__ == '__main__':
    if os.path.exists('debug.py'):
        import debug

        debug.setDebugEnv()

    if mytool.getlistCk(f'{tokenName}') is None:
        print(f'请检查你的变量名称 {tokenName} 是否填写正确')
        exit(0)
    else:
        for i in mytool.getlistCk(f'{tokenName}'):
            ry = RainYun(i.split("#")[0], i.split("#")[1])  # 实例
            ry.login()  # 登录
            ry.signin()  # 签到
            ry.query()  # 查询积分
            ry.logout()  # 登出