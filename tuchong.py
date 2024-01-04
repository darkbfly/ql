# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/4 15:34
# @Author  : ziyou
# -------------------------------
# cron "11 8,22 * * *" script-path=xxx.py,tag=匹配cron用
# const $ = new Env('图虫')
# 图虫
# export tuchong_ck='账号#密码&账号#密码',多账号使用换行或&
# 注意：密码中不能包含 & # \n
# https://t.me/q7q7q7q7q7q7q7_ziyou

import base64
import os
import re
import sys
import time
import urllib.parse
import requests
import rsa

CK_LIST = []


# 加载环境变量
def get_env():
    global CK_LIST
    env_str = os.getenv("tuchong_ck")
    if env_str:
        CK_LIST += env_str.replace("&", "\n").split("\n")


# 用于加密密码
def encrypted_password(t):
    o = "D8CC0180AFCC72C9F5981BDB90A27928672F1D6EA8A57AF44EFFA7DAF6EFB17DAD9F643B9F9F7A1F05ACC2FEA8DE19F023200EFEE9224104627F1E680CE8F025AF44824A45EA4DDC321672D2DEAA91DB27418CFDD776848F27A76E747D53966683EFB00F7485F3ECF68365F5C10C69969AE3D665162D2EE3A5BA109D7DF6C7A5"
    key = rsa.PublicKey(int(o, 16), 65537)
    encrypted = rsa.encrypt(urllib.parse.quote(t).encode('utf-8'), key)
    return encrypted.hex()


class TuChong:
    def __init__(self, ck):
        phone_number, password = ck.split('#')
        self.user = {"account": phone_number, "password": password}
        self.session = requests.Session()
        self.token = ''
        self.nonce = ''
        self.headers = {}

    # 登录
    def login(self):
        for _ in range(3):
            response = self.session.post('https://tuchong.com/rest/captcha/image')
            response_dict = response.json()
            captcha_id = response_dict.get('captchaId')
            data = {
                'zone': '0086',
                'account': self.user.get('account'),
                'password': encrypted_password(self.user.get('password')),
                'remember': 'on',
                'captcha_id': captcha_id,
            }
            self.session.post('https://tuchong.com/rest/accounts/login', data=data)
            # print(response.json())
            self.token = self.session.cookies.get('token')
            if self.token:
                # print(self.token)
                print(f'登录成功')
                response = self.session.get('https://tuchong.com')
                self.nonce = re.findall(r"window.nonce = '(.*?)';", response.text)[0]
                self.headers = {
                    "accept": "application/json, text/plain, */*",
                    "token": self.token,
                    "Host": "m.tuchong.com",
                    "platform": "android",
                    "content-type": "application/x-www-form-urlencoded",
                    "x-requested-with": "com.ss.android.tuchong",
                    "user-agent": "Mozilla/5.0 (Linux; Android 11; M2011K2C Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 Tuchong/7.39.1(android)"
                }
                return True
            print('登录失败')
            time.sleep(1)
        return False

    # 获取用户信息
    def get_user_info(self):
        response = self.session.get("https://api.tuchong.com/everphoto/isbind")
        # print(response.json())
        response_dict = response.json()
        mobile_number = response_dict.get('mobile_number')
        return mobile_number

    # 签到
    def check_in(self):
        response = self.session.get("https://m.tuchong.com/tuchongrest/point/check-in", headers=self.headers)
        # print(response.json())
        response_dict = response.json()
        if response_dict.get('result') == 'SUCCESS':
            print('签到成功')
            return
        print(response_dict.get('message'))

    # 获取每日任务信息
    def get_daily_task_information(self):
        url = "https://m.tuchong.com/tuchonggapi/misc/point/v2/status?platform=android&version=7.40.0"
        response = self.session.get(url, headers=self.headers)
        response_dict = response.json()
        # print(response_dict)
        task_type_list = response_dict.get('other_point_list')
        for task_type in task_type_list:
            if task_type.get('title') == '每日任务':
                return task_type.get('task_info_list'), response_dict

    # 开宝箱
    def open_treasure_chest(self):
        _, response_dict = self.get_daily_task_information()
        if response_dict.get('status').get('gold_box_switch') is False:
            print('今天10次开宝箱的机会已用完')
            return
        for _ in range(10):
            url = "https://m.tuchong.com/tuchonggapi/reward/point/box"
            response = self.session.get(url, headers=self.headers)
            # print(response.json())
            response_dict = response.json()
            if response_dict.get('result') == 'SUCCESS':
                print('开宝箱成功')
                time.sleep(1)
                continue
            print(f'开宝箱失败 {response_dict}')
            break

    # 获取作品列表  网页端的最新
    def get_works_list(self):
        response = self.session.get('https://tuchong.com/rest/categories/%E6%9C%80%E6%96%B0/recommend')
        response_dict = response.json()
        # print(response_dict)
        return response_dict.get('feedList')

    # 点赞
    def like(self):
        task_info_list, _ = self.get_daily_task_information()
        # print(task_info_list)
        for task in task_info_list:
            if task.get('text') != '给作品点赞':
                continue
            if task.get('status') == 1:  # 0为待完成，1为已完成
                print('任务已完成')
                break
            day_limit = task.get('day_limit')
            day_finish_num = task.get('day_finish_num')
            feed_list = self.get_works_list()
            for index in range(day_limit - day_finish_num):
                post_id = feed_list[index].get('post_id')
                data = {'post_id': post_id, 'nonce': self.nonce, }
                response = self.session.put('https://tuchong.com/gapi/interactive/favorite', data=data)
                print(response.json().get('message'))
                time.sleep(1)

    # 关注用户
    def follow_users(self):
        task_info_list, _ = self.get_daily_task_information()
        # print(task_info_list)
        for task in task_info_list:
            if task.get('text') != '关注摄影师':
                continue
            if task.get('status') == 1:  # 0为待完成，1为已完成
                print('任务已完成')
                break
            day_limit = task.get('day_limit')
            day_finish_num = task.get('day_finish_num')
            feed_list = self.get_works_list()
            for index in range(day_limit - day_finish_num):
                site_id = feed_list[index].get('site_id')
                data = {'site_id': site_id, 'nonce': self.nonce, }
                response = self.session.put('https://tuchong.com/gapi/interactive/follow', data=data)
                print(response.json().get('message'))
                time.sleep(1)
                self.unfollow_user(site_id)
                time.sleep(1)

    # 取关用户
    def unfollow_user(self, site_id):
        params = {'site_id': site_id, }
        data = {'nonce': self.nonce, }
        response = self.session.delete('https://tuchong.com/gapi/interactive/follow', params=params, data=data)
        print(response.json().get('message'))

    # 分享
    def share(self):
        task_info_list, _ = self.get_daily_task_information()
        # print(task_info_list)
        for task in task_info_list:
            if task.get('text') != '分享作品':
                continue
            if task.get('status') == 1:  # 0为待完成，1为已完成
                print('任务已完成')
                break
            day_limit = task.get('day_limit')
            day_finish_num = task.get('day_finish_num')
            feed_list = self.get_works_list()
            for index in range(day_limit - day_finish_num):
                site_id = feed_list[index].get('site_id')
                post_id = feed_list[index].get('post_id')
                data = f"share_id={post_id}&content_type=photo&author_id={site_id}&platform=WechatFriend"
                headers = {'token': self.token, 'Content-Type': 'application/x-www-form-urlencoded', }
                response = self.session.post("https://api.tuchong.com/share/recall", headers=headers, data=data)
                # print(response.text)
                response_dict = response.json()
                if response_dict.get('result') == 'SUCCESS':
                    print('分享成功')

    # 查询余额
    def check_balances(self):
        response = self.session.get('https://m.tuchong.com/tuchongrest/4/users/self/rewards', headers=self.headers)
        print(f'可提现金额为：{response.json().get("balance") / 100}元')

    # 获取金币数量
    def get_coins_count(self):
        url = "https://m.tuchong.com/tuchonggapi/misc/point/v2/status?platform=android&version=7.40.0"
        response = self.session.get(url, headers=self.headers)
        response_dict = response.json()
        # print(response_dict)
        print(f"金币：{response_dict.get('status').get('balance_point')}")

    # 查询金币明细
    def query_gold_coin_details(self):
        params = {
            'count': '10',
        }
        response = self.session.get('https://tuchong.com/gapi/misc/point/get-detail-list', params=params)
        print(response.json())

    # 获取看视频奖励
    def get_watching_videos_rewards(self):
        url = 'https://api-access.pangolin-sdk-toutiao.com/api/ad/union/sdk/reward_video/reward/'
        _json = {
            "message": "312c5f1e431662c7513620c132a62b052e6b80429deb7dc1dZdrMnSF8NQFTIieNaMz9lP7a+c3kpY3kenCbCNPQmlfLBaKaOIo5qhHVY6IqSEDG3lFL+mVyGNXk\neZ9Tbpi5Nm3ckpURjobWAwTgp2pkM5FFn3cHOK5o+DZkR+VXBg5BYgPIIuYzNFf6PvbmfDFBVL8l\n561NSCiV\/LZXQqAPJP\/cUje21VJVYP2YLaRDF27lMeJ+5AUmt7kVBSb6ag0HwnHzl8lnWAZmF6Aj\n7y3VgXS+wTJ+M68ZnKjqxEe7rkGOnWyyKYKUEX3wtyDXPOezIF\/IgP+w3QC6LVKaGLtuMEKCXEow\nG\/NJYVfUcDuqBuqIm3\/cWUIDpr09VdQMpbUVmK08XS66RSHFF5sb0qxpVhP\/oJoEz5nix7K\/ohpN\nJdsw1lGojsnXf2\/q6j+xp81rZU8J00OlJaRSTFF2f\/CibAtA7SVKmpjSwRQNLCQVkWBjnKHmf7X5\nyzt1Hs8LeYL1ecBuCkWVZtt3gabXorUoL\/47Lp9\/+q8BJSWyYSzt3mw7Lvh7iODE7ZFEiclMJ0mb\nqLQj+fcPks9s1nI9NK+fcX7Q5DUIz4HQaaRYNSWqKyRj9YGbCxAdtaWr698LXjALcRB597c9CeJM\nGTfjSJXNPGe6dCqyD3FcJk8e+c2I6IcNorbOKBVcCripjd0Ue5brcddjWlkgbYZtxzDTMfozZHw4\n89gv0gh04W8Z\/tOBE1bqlpG+eUzhn16LB1SGHjlYJOSu+s4edONoxwYE4IYONdovmTMS+k2ymj1H\nzG0u0Vrx3f+COIZjXKeZ0SQ31l3KVFlVnKxzEISlwYgBdqiEaGRHkp+4im8\/wYG2SNoOqw1q14Ph\nfEiTYU19oMPbg0SHHbonlKCPKKzqj7Kr88wOqu8K3TcyoAJG9zABSiBQNY7uBLNv1XE2Aia3qO\/l\n+ez3RvAYj5xH7gLqyYKCo9+LyUS+\/hPkrLbhbjvQZlG6HLiKXfcS476qpnd8OEYcddepv4SwC10F\nShJIexkKaCERShjXC3VQajXmOVniPvHELVlI0O6ELGUzk652ZoxSKilyjQaeENC0FEzgyU4GCbfd\nbr0wNDXctuV686Vagf1ODzxUNkBEfb17NSQP4RjC4uC4V224DtP3UkzZnamp0e\/qt7cdZ1psV71a\nhTcWSRR30e\/+izQmqkPbJR6TPpH9uT16K89S3Oepgg70d5A9sXy2XwV6xjBeur7cdjHIp8CgLqQf\n15R7LQE9veEDpUYKnNQXz3kDAq2S2U\/GR\/2\/s19tPAY9qn6ljGbgImkblkv0E3Nghbs7SQbrhS25\nbiDOeQez4uIZRcVhnlyJJw2XJrkpBtJD7mhEgdHwEOCD4VZNR+ZIYsS0hrle5yfRmnwowbTgT8p2\nbbg3vxvFOzyIuB0wOS6SKlyqgEBAB3F7xyIlfRTtiRw+4YZJ27noENWW1Mi5FHygXvmNkKhlghKH\nUE7Gg\/bepQ4VkeHEDgsXlCH\/kkks9JpegozIMDcIIrZy3pqiWwDSPgLXN8W+xWIiKyirVByY556F\nrVCtDnz4UGRYrb2JEytM5adT05hRAFJOgXOLjuagnsp2gzka96TvLuFtsdqiOaXIxjHKQ0jlbQmk\nPD6GpN6ibtI\/brECf3CyvlaHSSc3zCidOkiA1Di9WMthyWgOlaN1jrWuf7rlgTchf79uDCl5Y9Z9\n5kKmGPB8IrkBjwoWnriq+xO1lQfiBxdY+GTcEd+KuKDVgPdS\/FLWXDyrQfKCX8oKJeQgeCAqlG\/W\nrWMDiJdWbNgFiq\/x\/BkLHaQ7GohCoGwM6lUG21TJ4L9rSeT2\/sIp0zcEDJJN24mxv8U+18QKKF8E\n5Hn9B0HA0RcMEZ3wiIKyGcyqG3NLx0cEuPg4sL0j78GlnUEYe8GR6WwM4tfY0CBBXPXDnGuAbhqN\ns421qEjIWocMSylJR2np9rAUhjiswpj5UIstOC5abpboXtuI5oKBjlaZI7hFV++tiNmVTz6WRjPv\n13d\/oI5COnQ6f\/OickEzxr8YdQzSAxLi5P0Eowgj8RK\/zEoRmjJ3+BMnxJlZTaefU7fJRh5AQOwK\nxpoR+fMUAq97XKJYAtdDrFCRcH4w\/pcHubz7Z1C3hCSePh6PdZuS1MgITPR\/EqLL73F8yfTQsIjI\nY4at4DD5SCGrshp8wSvEq2kElUNE5PgCQLUfZQBhbUbArjsJ1GWwZDvetumeA77w0Qcycz\/iaTTg\naTgORpc2GBxdJPbBBSoFJ2baE33LPLGq+guzCVEq7aAsFfx9Iye834O0U24WPBUtHkxTzUeGm7lO\nmwV0Hqcu2cm0+OwkVlgsXJMvsTBaccugXQrLOF0nzArqrULxdSIaNmBWk4IcgdvR8JZ5Iph9uB+h\nsDKOmS9+JyDdKEZPAkkHd4k33UrqH\/koPRmSNWMFxd1FAeRTw0o7mK9aI6uyfTnCMbjwLtuNyRON\nZM08LRB6HltAFhKL0e1YCG4wABUwBm4lXNzDJE60IhnI\/zlsx4hL5lM2H8bP56XXty7l5jh3kuHH\nfxcQxoREF+rftaiHpekIsJl7oEveUNzHn2S3H2Y2K36XToCIADlOxBcLMt\/kvEryOhGn6WhbZHgg\nyoTqYaldfLstroVWIFCyw5FEgG9Zu6M3qNqmJYZWU8ufyyuCr34KEqtUDnseOwr0sXjUzTlVGlgs\nfBryC3ED+GzGWu5xzNfBSd3Mq1y0DETg\/\/h3bmgbEuWuc6t\/HjrWckfRaVoqSTkA2DzuWutciL4G\nytBGfeoH+akmvxBpciJdg3B7SudvLFuOVUEKqy1bogbyLw\/+2H4uMjz8uBcX+ALRIQvR0+b\/l77e\naE9Jufhoyj\/OWcrmM0Moa14FsubuwpcpKcuMSBhnjK36TNkD3apuH0\/0XvraeikdVyg9\/fgZfPTH\nMAlbqSVeynAdne5MCC26dO+giCWyExe+88\/nFu2VcgLBRMHeaz8EMSHthTVff0mQ\/cIE88r3y\/q4\n4xY8IyHPr45ND1IQOVzA\/71B7vsjUj\/TiCPJN2Bhf4llXoVwZfiqEULl+IwQk4CdESa\/FNcSTbbw\npD6leCg5BiumdYiDaVGAqqGOgnhnfrgwuVbOu2xKdt7QK9tfxcCqG4TiJ\/Jj8SnNmaIGfvEM+UmV\n5VkfLl+3FS8wQi0pWAmkTXLYsWLShn9\/WOplzy59TpHj9Ujrrcq86U9Ywtg5\/DWMR2g+b+tQsdTv\nV\/XU0uS1eBvHKw9YKta4Wer08kCsWXiulTZsX89sVqncsVEaJrrIQcf5oNdm3Y89cGSrUvyq\/ytE\nKzhL8PVDWFKepqfTtX22wIG3I3fLYvEGFpRoMB6c2vidQtMi6Mg3\/alok5Wu2lCmkgcDCQxDuVBS\nfIITTdeVc3KkTBoMLjlDkImqjYhahz3tlJMw6Vv1OhsUmbVB4tDFN+t6INforuQOPPJW\/wS9ILpy\nrMfZs8vBIwBADhujneOrTVxUbJUGaQXwI1\/Lf3xDhXbi\/3ZhK5ZeV05yWV6xq4bEJqyWW3qm8Wp1\nNi2FAAQ79bAmWrGiDzZCMYVvfAHJmy+0QEK1ZA7QZ7Dme2pocIhnOASWlMhrpCzT8OaORcJofFxF\nxtOCgxgaHUTjhjvaDC8wUtOX4szC+69AgNIOMdpX9OSIuMx6ctMsGpSw0vTNQxpo0xILkkSXZCgD\n6QEsu4FYvJ7JLF8n\/uAymZnTazkUx22ChNS0ckodv8WU2uJqqCasUuBnbNXElzPi4Vcm\/doDPEHB\n0jYH20f1PjFoACI+vVxRXU+9tV1xRdL9Wyowx+ZdMcWksIlbM3GG+72t8Ji992aOl8sBfnmdt3jL\nVvVz+aCofwmSRGTds9IVjnMscMdkm4g\/E7SZMG+amDFWbTjK8TTUUjjvBNRwOIZ666T+SL50MmrS\nB6rnE8F8o6x6+dbmKMa9SZJOCQ14mgEUnkHpCB5q1TQWXPgezCbxsccMmYkCCsxmkCnUP8RU8RFC\nDOz7FoywlucelxKGyoadBuDDvzTtxzTxRJqm+uS\/Lk+TYLVPn8x4KP8dgutJQZs3qTtIC7mkYhOc\n2JmxWb96siuWoPy6cQHblAPG1QiriNC2p8Y8wwFYnouYSfd6Wiha0p+9ZQssatgllO4Kj2kAthjw\nElsOMjJXFGR9+1jz1kajOh0RpSkaiqXnikRbZOZm+R9fEDVUgWZyCiGYcoDsbWYkVewWLo6jOBT9\n6wakFVSHFEM3kBzMDkUJcNqh45\/KBRMAlwGzpvUhEbz08huzSD7FfT+sxw129WLWpVyc9unO\/BsG\nxrCdb5PfSdu8yK3abz6mkWhaeeQSmU06yL0\/4gALMQwBcNnze6YMe1g4OZ0nFeSLi2Q9S\/cMwSXb\nABv4ZDIcFfqhNg7pEQGAasIWsNO2CHn7xrdgvEy4s1OrCcd5OqRjF\/WrSrhPIeinoFxC11Zgxvvq\nNjsQ7uW5gIxKVGwiBHK5\/DdQVsXBuu6eKPNcOIHrO2IqxUpN\/dQeSNWK0SKyfmrVDTfvl23\/nc8t\nXtI8+qPM\/B7jMvZJK3wcvjbYJb0QrSpeaZYg6xXOX1\/cKgcv4ppkWS6bhy86VEHavMI0bdgHZ5\/A\nEgaoa75s7+YZ2WBD7+cLGYRuea7mJhJn64r0MFWp2dyPfnTL1Thp9Y+4e5W0OVvTDyfPpgUK8C\/t\nbPT7LcT+ydbMvfaEJ7M5xJuwBRrKaQL913M4cU4fah2yARaWfIo\/nSLA6vRdS1c15OM4T7BMCruU\nKKKFxFMTdrXPNsPdg7DAeS5lTIMzLlzfM61OSscwjZiNhZwqXNYachrqKn+YOTrZcORZI7xFd5yy\njyVKwV5co5KjseZf0DrVlWm1g3tJQUV0pfkdyPzj4qOdv9dZyZAgpl0Y6jpeBuaRyXHqCYuwgm1+\nScZXFMEwd6ZDTnJUGK7EZx+hBs9e2oqDYUfR\/4Pmwi8m5AmJfe2nKizcfqFt9yoemGo\/F2sxvi19\nHUV04p8jVhX7F9au3xGEUwYSUx5JZfWhUc8RoA63Lm18wR9MlRYicTMoDPvzX9BSCp0bMmUkOoFS\nR7FR1i5cHi12wX5gnKVDLGPUTNeKgaSVhG2kp1IHW\/5CXZ5yXjaVZuZhCykYAAi6GOpw1my5cWkp\nLXOnAWzJ\/YrhsZ7ziU+fjJrQLSUtDyW0fl1tM92fCUn7Gk6c9k9G00HyY6t6UWi9X9LmgvRqFceF\ngTn87v0SZoNI9Lrs0lqDnGo0kl\/eyxUGj7GEDyoAeeYWE+OK09kqybQKfM\/dXdxrXvWaxdv3UkRq\n6g6dd72s5Fi5Pg1aKBKtmq13CWfqsY5pv1KhMzueoL3O5pkN8aeDUnjgAk3EoywYKMClYy19RNIV\n2NUV4T6g02n2RuuorIxhEzFcnWICMM\/ENgNX6xPChxNbPzyeIKO+tLsDFWq8OQuLQ+5u0ZGgfwru\nkL0QZHsPt6hcYg70ewg4xEtCTCc6hXJxshFtAPGKNp9vAZILIuIXV2QFeV0zX6Q56dlMXLaud6bD\nZwfehPGHcpEWadqYPn18U4rZl1HWZdZuGeDTl3W60VtJVzWwlycrW5hz4lTTJ31Iq5o8lXHhO0Zb\nWgzBQlEoVEQyRpcSCzxtjSoKy5xOYoLE1d4zsXv\/u4LgdB5vBE\/zVJ5bAHLZ4TVfBTX36zcecxAG\ncMZuY4HMgm2pGqDE5VNDpr0QSDm86iGqjqflBIpc9lPVzwRPwcl4F5INd3MpT9vQs39bnRjQUsnZ\nhY7y2XwHf5xhjQz2Q2Ikew3Esr\/czThhtK\/Zr2A5snBE\/Eds1j8ccpE1gbXNNO+xd5dJKJ66\/+Tl\nP3iKV0WNAPYXp2UH\/DvnXhIgcwWw9aIovEYTYRT25H+dSgtIn0AtuvXS3hlLWNrCYE6INmLBjwlI\ndi+yn8AW51pL8zEpUlOgy7hRwFgmku5HMqVhRg2MsZ+YatzZYepnpTPGqzZKH\/iHjB6pwMv62SRU\ndwW6eMKBxsR+Qy7llN+BlH8C+DI\/+Z8egIG+C\/s+pTjIW8fNUHXqKZeDe7WHciGzmpCyEl7TIWo+\n8oDzB0Ms3JGAbL9YY7VX1\/SYKYwUGvKHmCbuYh3EDjun6HJEruD0S4K4iSu6EKrsa9EkswHcl59+\nXqJOOn5SVaYkUssXR6ZzCLWpQCI5VdGrVHNcELfIOQ8iLkwQNob4XkpgnIAEVjciZFsjbJVLSPLh\nJGhvHib+zVhzYEyamqZCHf8K4oyswEuT\/46w6k9vkk8e0gzWs\/nNKTTYlvB37mlS45yOYRVJxcmS\nzGSOEDZEVt847JtZuwjPe1PTtxbQMFCSELlctgPoZvXf2RiwHv2szRfRWKCV\/Y\/ruXxft\/oKluEl\nLPLFVfPDwzxuNBp5b+Kw2i1v2veih\/tfUw+RANVKWyn7eXL3Qin8wBpVtLYGSlZ0BCi83KsHWNxF\nWBl1xaCr67qpfXAjsUoRvVLvPIJSfjEna5c+BHuiM6pyVD\/KiEmuVwvwYa68BKuGxHVme\/qNjE0H\nK3cA1Erl\/0fKMAiezrtvaIiwtt17f8tFeDNil1LdStjg6fr\/xrNr+gM+3ZLLGwofRT3cRTnDnCdQ\njyiFoVbhhTwn7SOzJOt8uOCpM926AZynU4B2\/PYpOBKShwI1qZREA0Bna7D+YNtYtPAmrH4Buu+K\nkPGC+ism9tSFpo7Is3Uco8rXMIEX38yAKpvjvkCuoTa4gRQ6vdMgFZaKJ0JjyLQcIni8\/Q9PlZt\/\nfPDvst9WnkwAk6tL6NSDLDk61l6JWxzHBfzrA3C4KtsiCsy6oVmfSKm2zvqzdDL+X6eU0fFHGXdB\nYxsAiE45v4MEOaBPtZkwzAsQuhpyJ+0087agHK6EyTRISoDanDnhqgkGOUV3ktgPc26fIbKrs2DR\nBmwYX9JfLWclnhemU47sK1yPigSmdxEYNMb\/DKxKAq+8Q17Wjk0j3wFI8TBIj+CNZCf1dtnQ6S1U\nEVzSKVZIuh8HZDSkUBDYgH6oE5\/nFJRcoewnLeRl3dTaL3yIYONxFw9zpY8+hXgsplavAdYVB6oe\n3BK3ORkl8uIt2FhZgs\/osVuH9FXjxnL7o5npfjdnfBjcj+NyORfRlBn2StISne95UCA66Fdimi8I\ng4M9fo8x2SfAoJPz5tIZJDZ26CjOYtDxXhsn4NQCQwnE7DO1wWMtngZEa7+aT1RoJnK\/TLKVyQ+y\n9GfvicBBvCx9x2SEiP6I0cDZX8KQKesVd6jSQxD7SEomtbgL6Hr8lUDlaaxliRHqO15UPnYzmjkb\nkqs0WytcyV6qnrQnoGpk5S+pki0EUyU6QT1QtHezPDljM7nHbwI1WEJnwyIBjaJYZpLwldGA8qgA\ngEekPK9ThKMHRdgJCtWspbgzonCL3o30Mc5\/WpVzQNFsemO3GnbU1N\/AN2\/ngsuOcVwNQNs\/aHGX\nzR6Pc+7M1bShToxV9f5FKtIscrA+SS0Ln85mB6IJbOegnt+Bu573PtDQ02G9TGNhYxJfJTHByXwG\ni4uyznwaldJb2KoTEH409Bd4PO3O6PLqnbOVilVl8AStHeMJ6XoCFtUOYKFfE2vmkP1iljGgk6oo\nXClKW4FU7kzokvgkxSkfGSBFy6mcw7kzycC9GM28qV+NAUCERftP7sbAkSJ6y1s3X6xXDD8k9os7\neFQ3\/jO1mKXgFKRFoupPzMqWERM4Tpx2IVYLwjCRsOnkYkc0xrA0S5vi+9H+D2iwsrruHxZP7eev\nKLdmF4Aw9voh51YQYmTDiyvueW562LzoU+ePk7XzduJK\/iARe1ftQt02zawDobcF6q6Mxf\/WuN0u\nw7S5asr1h\/JbcFQ\/MUCCl\/Wgz\/q8dNjD\/0WXIRfRoL6y3+mZpTyA5piUuvWx5eDizYXA+TK4ziqw\nQ6hRGQRYHw22RJKgeMKRQk7ujCtIO1cVQzs8mztQ5UbvWQluBRyIqNCE7LPEFydQzP82zraFq8oH\nXMzs5MBE9D2YwqveEoIB4zqZJeoecJv+rVLOCX6g1yVGXAaSu5UwCMJEHJsFrQNmHd1HxDrGLqPO\nzTVvhjI+fFel6CtQvrPETpLozfQtU9W5KMcZyK6oPz2lSxNG1hnv2dnXTFxJ6WsPNs0e7OvHy0mA\nXyUZ\/6FHRgZR8ELfnyTtoXEH5BzpfHkn8+M6f9pzh+qzORZis9QuCs6N9Ir1j9GAME4g\/ZwgAI5g\nrBhxy2FRM5I39OLMv92cAu495ctERKshXKUJM0jJQvT7p\/Vy3KWeETTcJIeLWTrjZzaEQghAC+vR\nHuQXmLExI\/Yeb7KJmeDjv9YsyoSfOUJ6coGC1DQQ9ODrz2mANtUqoavwkiXPYq8DF0hIXOaEc6N8\nKd38e8z+cUqt2mI0jCnP9lUVMf1z7f1CgqLl2WnEjldFm3rkvKrgf\/k\/0fZm7Qc1VnrGFqYEoySQ\naQfBWdCZiowGnTg6JuJcoa3mMmuz1d26Bzy4TMuCvUtsmQaceUEyqhv6Q60sfChsUPAW9oiHnuLA\nrbRGHoUFSH2JWOhFUTzMLoebCdG2ikqLn4a6tX0lQlzQbswJAIj0bvD3O50zSX\/m3qqxtnZT1Har\nGjbaGLRX9V0e8TO3ftZpxT3nc0dJjOem\/uIN3xYBhbG2b2ZVj\/4ajKcfRDO6aho0UJm1P7cDRbmy\nCmbO+bWGT+GVLISEJ\/xutMBhGmrEv8s=\n",
            "cypher": 3
        }
        response = requests.post(url, json=_json)
        response_dict = response.json()
        print(response_dict)
        pass

    def main(self):
        character = '★★'
        print(f'{character}开始登录')
        if not self.login():
            return
        self.get_coins_count()  # 获取金币数量
        print(f'{character}开始签到')
        self.check_in()
        print(f'{character}开始开10次宝箱')
        self.open_treasure_chest()
        print(f'{character}开始完成点赞任务')
        self.like()
        print(f'{character}开始完成关注任务')
        self.follow_users()
        print(f'{character}开始完成分享任务')
        self.share()
        time.sleep(2)
        self.get_coins_count()  # 获取金币数量
        self.check_balances()  # 查询余额
        # self.get_watching_videos_rewards()


# 主程序
def main(ck_list):
    if not ck_list:
        print('没有获取到账号！')
        return
    print(f'获取到{len(ck_list)}个账号')
    for index, ck in enumerate(ck_list):
        print(f'*****第{index + 1}个账号*****')
        TuChong(ck).main()
        print('\n')


if __name__ == '__main__':
    get_env()
    main(CK_LIST)
    sys.exit()
