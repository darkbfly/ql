import pprint
import re
import time
from MyQR import myqr
import requests
import logging

logger = logging.getLogger(__name__)
# getSToken请求获取，s_token用于发送post请求是的必须参数
s_token = ""
# getSToken请求获取，guid,lsid,lstoken用于组装cookies
guid, lsid, lstoken = "", "", ""
# 由上面参数组装生成，getOKLToken函数发送请求需要使用
cookies = ""
# getOKLToken请求获取，token用户生成二维码使用、okl_token用户检查扫码登录结果使用
token, okl_token = "", ""
# 最终获取到的可用的cookie
jd_cookie = ""

qrFile = 'D:\\dumpSave\\genQRCode.png'

def parseGetRespCookie(headers, get_resp):
    global s_token
    global cookies
    s_token = get_resp.get('s_token')
    set_cookies = headers.get('set-cookie')
    logger.info(set_cookies)

    guid = re.findall(r"guid=(.+?);", set_cookies)[0]
    lsid = re.findall(r"lsid=(.+?);", set_cookies)[0]
    lstoken = re.findall(r"lstoken=(.+?);", set_cookies)[0]

    cookies = f"guid={guid}; lang=chs; lsid={lsid}; lstoken={lstoken}; "
    logger.info(cookies)

def getSToken():
    time_stamp = int(time.time() * 1000)
    get_url = 'https://plogin.m.jd.com/cgi-bin/mm/new_login_entrance?lang=chs&appid=300&returnurl=https://wq.jd.com/passport/LoginRedirect?state=%s&returnurl=https://home.m.jd.com/myJd/newhome.action?sceneval=2&ufc=&/myJd/home.action&source=wq_passport' % time_stamp
    get_header = {
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-cn',
        'Referer': 'https://plogin.m.jd.com/login/login?appid=300&returnurl=https://wq.jd.com/passport/LoginRedirect?state=%s&returnurl=https://home.m.jd.com/myJd/newhome.action?sceneval=2&ufc=&/myJd/home.action&source=wq_passport' % time_stamp,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Host': 'plogin.m.jd.com'
    }
    try:
        resp = requests.get(url=get_url, headers=get_header)
        parseGetRespCookie(resp.headers, resp.json())
        logger.info(resp.headers)
        logger.info(resp.json())
    except Exception as error:
        logger.exception("Get网络请求异常", error)


def parsePostRespCookie(headers, data):
    global token
    global okl_token

    token = data.get('token')
    print(headers.get('set-cookie'))
    okl_token = re.findall(r"okl_token=(.+?);", headers.get('set-cookie'))[0]

    logger.info("token:" + token)
    logger.info("okl_token:" + okl_token)


def getOKLToken():
    post_time_stamp = int(time.time() * 1000)
    post_url = 'https://plogin.m.jd.com/cgi-bin/m/tmauthreflogurl?s_token=%s&v=%s&remember=true' % (
        s_token, post_time_stamp)
    post_data = {
        'lang': 'chs',
        'appid': 300,
        'returnurl': 'https://wqlogin2.jd.com/passport/LoginRedirect?state=%s&returnurl=//home.m.jd.com/myJd/newhome.action?sceneval=2&ufc=&/myJd/home.action' % post_time_stamp,
        'source': 'wq_passport'
    }
    post_header = {
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'Cookie': cookies,
        'Referer': 'https://plogin.m.jd.com/login/login?appid=300&returnurl=https://wqlogin2.jd.com/passport/LoginRedirect?state=%s&returnurl=//home.m.jd.com/myJd/newhome.action?sceneval=2&ufc=&/myJd/home.action&source=wq_passport' % post_time_stamp,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Host': 'plogin.m.jd.com',
    }
    try:
        global okl_token
        resp = requests.post(url=post_url, headers=post_header, data=post_data, timeout=20)
        parsePostRespCookie(resp.headers, resp.json())
        logger.info(resp.headers)
    except Exception as error:
        logger.exception("Post网络请求错误", error)

def parseJDCookies(headers):
    global jd_cookie
    logger.info("扫码登录成功，下面为获取到的用户Cookie。")
    set_cookie = headers.get('Set-Cookie')
    pt_key = re.findall(r"pt_key=(.+?);", set_cookie)[0]
    pt_pin = re.findall(r"pt_pin=(.+?);", set_cookie)[0]
    logger.info(pt_key)
    logger.info(pt_pin)
    jd_cookie = f'pt_key={pt_key};pt_pin={pt_pin};'

def chekLogin():
    logger.info("开始检测是否登录")
    expired_time = time.time() + 60 * 3
    while True:
        time.sleep(1)
        check_time_stamp = int(time.time() * 1000)
        check_url = 'https://plogin.m.jd.com/cgi-bin/m/tmauthchecktoken?&token=%s&ou_state=0&okl_token=%s' % (
            token, okl_token)
        check_data = {
            'lang': 'chs',
            'appid': 300,
            'returnurl': 'https://wqlogin2.jd.com/passport/LoginRedirect?state=%s&returnurl=//home.m.jd.com/myJd/newhome.action?sceneval=2&ufc=&/myJd/home.action' % check_time_stamp,
            'source': 'wq_passport'

        }
        check_header = {
            'Referer': f'https://plogin.m.jd.com/login/login?appid=300&returnurl=https://wqlogin2.jd.com/passport/LoginRedirect?state=%s&returnurl=//home.m.jd.com/myJd/newhome.action?sceneval=2&ufc=&/myJd/home.action&source=wq_passport' % check_time_stamp,
            'Cookie': cookies,
            'Connection': 'Keep-Alive',
            'Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',

        }
        resp = requests.post(url=check_url, headers=check_header, data=check_data, timeout=30)
        data = resp.json()
        pprint.pprint(data)
        if data.get("errcode") == 0:
            parseJDCookies(resp.headers)
            return data.get("errcode")
        if data.get("errcode") == 21:
            return data.get("errcode")
        if time.time() > expired_time:
            return "超过3分钟未扫码，二维码已过期。"

def genQRCode():
    global qr_code_path
    cookie_url = f'https://plogin.m.jd.com/cgi-bin/m/tmauth?appid=300&client_type=m&token=%s' % token
    version, level, qr_name = myqr.run(
        words=cookie_url,
        # 扫描二维码后，显示的内容，或是跳转的链接
        version=5,  # 设置容错率
        level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
        colorized=True,  # 黑白(False)还是彩色(True)
        contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
        brightness=1.0,  # 用来调节图片的亮度，用法同上。
        save_name=qrFile,  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    )
    return qr_name

def showImage():
    from PIL import Image
    # 打开PNG文件
    image = Image.open(qrFile)
    # 可以进行各种图像操作，如显示图像、保存图像、编辑图像等
    # 例如，显示图像:
    image.show()

    # 当您完成操作后，不要忘记关闭图像文件
    image.close()

if __name__ == '__main__':
    getSToken()
    getOKLToken()
    qr_code_path = genQRCode()
    showImage()
    return_msg = chekLogin()
    if return_msg == 0:
        print(f'获取Cookie成功\n{jd_cookie}')

    elif return_msg == 21:
        print('二维码已经失效，请重新获取')
    else:
        print(return_msg)