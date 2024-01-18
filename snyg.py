import requests

cookies = {
    'custno': '7099805453',
    'sncnstr': 'Bx82FJNq7bw7YzmN3%2BoCPg%3D%3D',
    'ecologyLevel': 'ML100100',
    'secureToken': '30457F483AADC974464498B022831DD7',
    'serviceTicketId': 'STrMLNuYTtPb0xW0uYl0H6faDtG3LLAgTt',
    'logonStatus': '2',
    'roleType': '142000000154',
    'custLevel': '161000000110',
    'authId': 'sibKtVuZ2BUwinCowh9cgem35KkuYAhjUu',
    'nick': '130******23',
    'TGC': 'TGTtT6P28aJMQYAm2zr9baGrM7TBikuW37VymUxiojt',
    'tradeMA': '13',
    'ids_r_me': 'NzA5OTgwNTQ1M19CUk9XU0VSXzE3MDU1MzkwNTE4MDhfMTcwNTUzOTA1MTgwOF8wX2YzYmQxODA1YWNjNDliYzk0NzkwZDk3YTg2NzEzYjg2',
    'rememberMe': 'true',
    'route': 'fa0195b42cd5a032c155a10ebcfc040b',
    'JSESSIONID': 'kpHlp3iVIGLGsje5zt6H57sN.sngameprdapp282',
}

headers = {
    'Host': 'ifast.suning.com',
    'Connection': 'keep-alive',
    'xweb_xhr': '1',
    # 'Cookie': 'custno=7099805453;sncnstr=Bx82FJNq7bw7YzmN3%2BoCPg%3D%3D;ecologyLevel=ML100100;secureToken=30457F483AADC974464498B022831DD7;serviceTicketId=STrMLNuYTtPb0xW0uYl0H6faDtG3LLAgTt;logonStatus=2;roleType=142000000154;custLevel=161000000110;authId=sibKtVuZ2BUwinCowh9cgem35KkuYAhjUu;nick=130******23;TGC=TGTtT6P28aJMQYAm2zr9baGrM7TBikuW37VymUxiojt;tradeMA=13;ids_r_me=NzA5OTgwNTQ1M19CUk9XU0VSXzE3MDU1MzkwNTE4MDhfMTcwNTUzOTA1MTgwOF8wX2YzYmQxODA1YWNjNDliYzk0NzkwZDk3YTg2NzEzYjg2;rememberMe=true;route=fa0195b42cd5a032c155a10ebcfc040b;JSESSIONID=kpHlp3iVIGLGsje5zt6H57sN.sngameprdapp282',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819) XWEB/8531',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wx681b1e78da02dd16/341/page-frame.html',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = {
    'activityCode': 'ACT0000013850',
    'deviceSessionId': 'TWLv1a18d1a0c95cfSAu011cb___w7DDuMKCwrgSw5UZbMOwKmvCrMOOBMODw7FewqvCvMOk',
    'dfpToken': 'TWLv1a18d1a0c95cfSAu011cb___w7DDuMKCwrgSw5UZbMOwKmvCrMOOBMODw7FewqvCvMOk',
    'sceneCode': '',
    'termiType': 'M-phone',
    'termiSys': 'Android',
    'appType': 'mini-program',
    'miniSource': 'wechat',
    'appVersion': '',
    'openId': 'oz9wP0QoJPp6b9nFfA5AaY9iQuCI',
    'unionId': 'oM7AytwnsvhNDvZdIOdDzYzBeWQY',
    'businessSystem': 'SNGAME',
    'businessChannel': '01',
    'channel': 'WAP',
}

response = requests.get(
    'https://ifast.suning.com/sngame/mpapi/sngame-web/msign/gateway/sign.do',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.text)