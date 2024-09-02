import requests

def setProxy():
    # return "http://120.197.40.219:9002";

    rj = requests.get('https://api.douyadaili.com/proxy/?service=GetIp&authkey=96ocyWiAHe5KbYRiPUlv&num=1&lifetime=15&region=jx&noregion=fj&prot=1&format=json&isp=1&detail=1').json()
    print(rj)
    if rj['ret'] == 200:
        ip = rj['data'][0]['ip']
        port = rj['data'][0]['port']
        user = rj['data'][0]['user']
        pwd = rj['data'][0]['pwd']
        return f"http://{user}:{pwd}@{ip}:{port}"
    else:
        return None


def runUrl(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; 1503-M02 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 XWEB/4.5.0 Chrome/47.0.2526.111 Mobile'
    }
    proxy = setProxy()
    if proxy is None:
        return
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    rep = requests.get(url, headers=header, proxies=proxies)
    rep.encoding = 'utf-8'
    print(rep.status_code)  # 返回状态值
    print(rep.text)  # 返回html

# 请求地址
url = "http://4c7c091432_y54c1.uaufskp.cn/ustgtmps/00f225438e61468dcb2de6be92590e03?uid=15"

if __name__ == '__main__':
    print(runUrl(url))



