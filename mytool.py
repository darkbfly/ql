import os
import random
import re
import time
from datetime import datetime
from zoneinfo import ZoneInfo


def getlistCk(ckname):
    if os.getenv(ckname) is None:
        return None
    # 字符串用回车或@符号分开为list
    return re.split(r'\n|@', os.getenv(ckname))

# 获取北京时间 带时区
def gettime():
    return datetime.now(tz=ZoneInfo('Asia/Shanghai'))
# 随机休眠几秒 随机数为float
def sleep(x, y):
    time.sleep(random.uniform(x, y))