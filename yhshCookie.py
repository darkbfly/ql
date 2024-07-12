import json
import os

import requests

url = '127.0.0.1:5700'


def getToken():
    if os.path.isfile('/ql/data/config/auth.json'):
        with open('/ql/data/config/auth.json', 'r') as f:
            config = json.load(f)
            return 'Bearer ' + config['token']


if __name__ == '__main__':
    newUrl = f"http://{url}/open/envs"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    yhsh = []
    sec = requests.session()
    sec.verify = False
    sec.trust_env = False
    rj = sec.get(newUrl, headers=headers).json()
    if rj['code'] == 200:
        for x in rj['data']:
            if x['name'] == 'yhsh_cookies':
                yhsh.append(f"{x['value']}#{x['remarks']}")
        pass

    newUrl = f"http://{url}/open/envs"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    pupu = []
    sec = requests.session()
    sec.verify = False
    sec.trust_env = False
    rj = sec.get(newUrl, headers=headers).json()
    if rj['code'] == 200:
        for x in rj['data']:
            if x['name'] == 'pupu_cookies':
                pupu.append(f"{x['value']}#{x['remarks']}")
        pass

    with open('/ql/data/scripts/yang7758258_ohhh_QL-Script/pupuCookie.txt', 'w') as f:
        f.write('\n'.join(pupu))


