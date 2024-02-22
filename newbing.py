"""
cron: 0 5 * * * newbing.py
new Env("WEB-必应")

Edge必应自动搜索赚积分
使用Edge浏览器打开必应 https://rewards.bing.com/ F12抓取Cookie即可  正确的CK格式是以MUID=xxxxxxx开头的
当前版本：v1.4

变量名：bingCK  多账号换行
URL后置参数变量名 bingUrlSuffix
bingDetectionStop 是否检测到积分未增长自动停止任务  默认为true  不需要该功能则额外定义变量，值为false

如果执行的发现积分不增长，且脚本上显示的积分跟实际不符，很有可能不是同一个账号的cookie，建议重新抓取。
玄学报错目前无解，凑合用吧！
"""
import datetime
import os
import random
import re
import time
import urllib.parse

import requests

old_Balance = 0
bingDetectionStop = os.getenv("bingDetectionStop")


# 获取用户信息
def getDashboard(bingCK):
    try:
        url = 'https://rewards.bing.com/pointsbreakdown'
        headers = {
            "cookie": bingCK,
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
        };
        resp = requests.get(url, headers=headers).text
        str_start = 'var dashboard = '
        str_end = '{}};'
        retStr = find(resp, str_start, str_end) + "{}}"
        return retStr
    except Exception as e:
        return '调用接口出现异常' + str(e)


# 获取当前积分
def getBalance(bingCK):
    try:
        url = 'https://cn.bing.com/rewardsapp/reportActivity'
        headers = {
            "cookie": bingCK,
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
        };
        resp = requests.get(url, headers=headers).text
        str_start = 'RewardsBalance":'
        str_end = ',"GiveBalance'
        retStr = find(resp, str_start, str_end)
        return retStr
    except Exception as e:
        return '调用接口出现异常' + str(e)

def randomchar(length):
    str = ''
    for i in range(length):
        str += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return str

# 搜索
def bing_rewards(q_str, bingCK, isPc):
    print(urllib.parse.unquote(q_str))
    # 用户需要先手动在Bing搜索一下，在你的搜索结果返回的URL中，把搜索词后面 & 开始的所有部分复制过来。
    # 原始脚本中没有附带这些参数，直接调用了搜索，不会记录 Reward 积分
    if os.getenv("bingUrlSuffix") is None:
        return '没有参数'
    else :
        q_suffix = os.getenv("bingUrlSuffix")
        q_suffix = re.sub(r'cvid=[\w\d]+', f'cvid={randomchar(32)}', q_suffix)
    try:
        url = f'https://cn.bing.com/search?q={q_str}{q_suffix}'
        print(url)
        if isPc == 1:
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
        else:
            ua = "Mozilla/5.0 (Linux; Android 12; Mi 10 Pro Build/SKQ1.220303.001; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 BingSapphire/23.5.2110003534"

        headers = {
            "cookie": bingCK,
            "referer": "https://cn.bing.com",
            "User-Agent": ua
        }
        resp = requests.get(url, headers=headers)
        code = resp.status_code
        if code == 200:
            msg = '成功'
        else:
            msg = '失败'
        retStr = msg
        return retStr
    except Exception as e:
        return '调用接口出现异常' + str(e)


# 随机生成一个汉字
def get_random_char():
    # 汉字编码的范围是0x4e00 ~ 0x9fa5
    random.seed()
    val = random.randint(0x4e00, 0x9fa5)
    # 转换为Unicode编码
    return chr(val)


# 分割函数
def find(str, str_start, str_end):
    start_index = str.find(str_start) + len(str_start)
    end_index = str.find(str_end)
    retStr = str[start_index: end_index].rstrip()
    return retStr


# 执行
def startMain(bingCK):
    '''
    try:
        userDashboard_json = json.loads(getDashboard(bingCK))
        activeLevel = userDashboard_json['userStatus']['levelInfo']['activeLevel']
        activeLevelName = userDashboard_json['userStatus']['levelInfo']['activeLevelName']
        progress = userDashboard_json['userStatus']['levelInfo']['progress']
        progressMax = userDashboard_json['userStatus']['levelInfo']['progressMax']
        if activeLevel == 'Level1':
            printLog('当前等级',f'{activeLevelName}[{progress}/{progressMax}]')
        else:
            printLog('当前等级',f'{activeLevelName}[{progress}]')
    except Exception as e:
        activeLevel = 'Level2'
        printLog('当前等级','获取失败')
    '''
    # 根据当前积分判断用户组
    start_Balance = getBalance(bingCK)
    if int(start_Balance) < 500:
        activeLevel = 'Level1'
        printLog('当前用户组', '第一阶段')
        upBalance = getBalanceGap(start_Balance, 500)
        printLog('距离升级下一阶段', f'还需要{upBalance}积分')
    else:
        activeLevel = 'Level2'
        printLog('当前用户组', '第二阶段')
        printLog(f'积分', getBalance(bingCK))
    old_Balance = start_Balance
    if activeLevel == 'Level1':
        # pc端搜索10次
        for i, msg in enumerate(gethotwords(10), start=0):
            q_str = urllib.parse.quote(msg.encode('utf-8'))
            printLog(f'电脑搜索第{i + 1}次', bing_rewards(q_str, bingCK, 1))
            new_Balance = getBalance(bingCK)
            printLog(f'积分', new_Balance)
            if bingDetectionStop != 'false':
                if getBalanceGap(old_Balance, new_Balance) <= 0:
                    printLog('检测', '积分未变动，停止运行！')
                    break
                old_Balance = new_Balance
            rand = random.randint(3, 5)
            time.sleep(rand)
    else:
        # pc端搜索35次
        for i, msg in enumerate(gethotwords(35), start=0):
            q_str = urllib.parse.quote(msg.encode('utf-8'))
            printLog(f'电脑搜索第{i + 1}次', bing_rewards(q_str, bingCK, 1))
            new_Balance = getBalance(bingCK)
            printLog(f'积分', new_Balance)
            if bingDetectionStop != 'false':
                if getBalanceGap(old_Balance, new_Balance) <= 0:
                    printLog('检测', '积分未变动，停止运行！')
                    break
                old_Balance = new_Balance
            rand = random.randint(10, 15)
            time.sleep(rand)
            # 安卓端搜索20次

        rand = random.randint(10, 15)
        time.sleep(rand)
        for i, msg in enumerate(gethotwords(20), start=0):
            q_str = urllib.parse.quote(msg.encode('utf-8'))
            printLog(f'安卓搜索第{i + 1}次', bing_rewards(q_str, bingCK, 0))
            new_Balance = getBalance(bingCK)
            printLog(f'积分', new_Balance)
            if bingDetectionStop != 'false':
                if getBalanceGap(old_Balance, new_Balance) <= 0:
                    printLog('检测', '积分未变动，停止运行！')
                    break
                old_Balance = new_Balance
            rand = random.randint(10, 15)
            time.sleep(rand)
    end_Balance = getBalance(bingCK)
    increase_Balance = getBalanceGap(start_Balance, end_Balance)
    printLog('本次增加积分', f'{increase_Balance}')


# 计算积分增长数
def getBalanceGap(old_Balance, new_Balance):
    return int(new_Balance) - int(old_Balance)


# nvl函数
def nvl(str):
    if not str is None:
        out = str
    else:
        out = ''
    return out


# 输出日志
def printLog(title, msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now + f' [{title}]:' + nvl(msg))

def gethotwords(length):
    defaultset = {"游戏", "编程", "动漫", "射击游戏", "网游", "社交软件", "搜索引擎",
        "论坛", "美食", "宠物", "工作", "编程", "视频网站", "短视频", "英雄",
        "搜索引擎", "文学", "角色", "食物", "学习", "购物", "新闻", "音乐",
        "电影", "股票", "旅游", "体育", "健身", "时尚", "汽车", "科技",
        "健康", "房地产", "家具", "饮食", "美容", "婚恋", "育儿", "电子产品",
        "手机", "数码", "电脑", "办公", "家电", "摄影", "导航", "邮箱", "地图",
        "翻译", "天气", "购物", "图书", "校园", "问答", "职业", "视觉", "设计",
        "棋牌", "经营", "安全", "网络", "效率", "日常", "社会", "法律", "投资",
        "理财", "医疗", "心理", "辅导", "装修", "手工", "烘焙", "园艺", "运动",
        "旅行", "摄影", "美食", "宠物", "电影", "绘画", "手账", "收集", "诗歌", "写作",
        "吉他", "钢琴", "唱歌", "舞蹈", "机器人",
        "物理", "化学", "生物", "数学", "考古", "历史", "哲学", "心理学", "社会学", "经济学",
        "机械", "土木", "建筑", "电子", "通信", "计算机", "环境", "能源", "交通",
        "创业", "投资", "财务", "银行", "证券", "保险", "市场", "销售", "人力", "运营",
        "品牌", "传媒", "设计", "艺术", "策划", "整形", "影视", "广告", "公关", "法律",
        "医学", "护理", "药学", "中医", "瑜伽", "跑步", "骑行", "游泳", "攀岩",
        "电竞", "棋牌", "桌游", "卡牌", "探险", " Safari", "旅游", "摄影", "美食",
        "动漫", "游戏", "电影", "电视剧", "小说", "音乐", "舞蹈", "手工", "美妆",
        "服装", "宠物", "汽车", "科技", "体育", "健身", "家居", "育儿", "教育",
        "职业", "金融", "环保", "公益", "政治", "军事", "历史", "哲学", "宗教",
        "心理"}
    myset = set()
    try:
        url = 'https://api.oioweb.cn/api/common/HotList'
        rj = requests.get(url, timeout=5).json()
        if rj['code'] == 200:
            print("返回成功")
            while len(myset) < length:
                msglist = rj['result'][random.choice(list(rj['result'].keys()))]
                if len(msglist[random.randint(0, len(msglist) - 1)]['title']) > 0:
                    myset.add(msglist[random.randint(0, len(msglist) - 1)]['title'])
    except Exception:
        pass
    if len(myset) == 0:
        # 从备用字典随机组合2个
        while len(myset) < length:
            myset.add(random.choice(list(defaultset)) + random.choice(list(defaultset)))
    print(myset)
    return list(myset)


if __name__ == '__main__':
    # print(gethotwords(10))
    if bingDetectionStop == '':
        bingDetectionStop = 'true'
    bingCK = os.getenv("bingCK")
    cks = bingCK.split("\n")
    print(f"检测到{len(cks)}个账号,即将开始...")
    i = 1
    for ck in cks:
        print(f"\n---开始第{i}个账号---")
        i += 1
        startMain(ck)
        rand = random.randint(5, 20)
        if i > len(cks):
            break
        print(f"\n等待{rand}s后进行下一个账号")
        time.sleep(rand)
