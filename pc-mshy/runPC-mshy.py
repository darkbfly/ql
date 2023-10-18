import subprocess

from mytool import *

微信路径 = "D:\Program Files (x86)\Tencent\WeChat\WeChat.exe"

subprocess.run(微信路径)
点击图片中心(png="1.png")
if 寻找是否存在(png="2.png") is False:
    raise Exception("未找到搜一搜图片")
else:
    输入中文('慕思会员')
    点击图片中心(png="3.png")
    点击图片中心(png="4.png")
    点击图片中心(png="5.png")
    点击图片中心(png="6.png")
    点击图片中心(png="7.png")