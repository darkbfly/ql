"""
cron: 0 * * * *
new Env("环境变量修改")
"""
import os
import json
import requests

url = '127.0.0.1:5700'


def getToken():
    if os.path.isfile('/ql/data/config/auth.json'):
        with open('/ql/data/config/auth.json', 'r') as f:
            config = json.load(f)
            return 'Bearer ' + config['token']

def changeString(before, after, split):
    newUrl = f"http://{url}/open/envs"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    envList = []
    sec = requests.session()
    sec.verify = False
    sec.trust_env = False
    rj = sec.get(newUrl, headers=headers).json()
    if rj['code'] == 200:
        for x in rj['data']:
            if x['name'] == before:
                envList.append(x['value'])
        pass
    rj = sec.post(newUrl, headers=headers, json=[{
        "name": after,
        "value": split.join(envList)
    }]).json()

    print(rj)

if __name__ == '__main__':
    changeString('lbvip2', "lbvip", "\n")
