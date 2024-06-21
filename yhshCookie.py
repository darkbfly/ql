import json
import os

import requests

url = '127.0.0.1:5700'

def getToken():
    if os.path.isfile('/ql/data/config/auth.json'):
        with open('/ql/data/config/auth.json', 'r') as f:
            config = json.load(f)
            return config['token']


if __name__ == '__main__':
    newUrl = f"http://{url}/open/envs"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    sec = requests.session()
    sec.verify = False
    sec.trust_env = False
    rj = sec.get(newUrl, headers=headers).json()
    if rj['code'] == 200:
        pass
