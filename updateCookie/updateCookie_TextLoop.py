import json
import os

from updateCookie.updateCookie_Util import *


def find_txt(path):
    data = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                data.append(os.path.join(root, file))
    return data

if __name__ == '__main__':
    for x in find_txt(os.path.dirname(os.path.abspath(__file__))):
        with open(x, 'r') as f:
            json_data = json.load(f)
        for y in searchEnvs(json_data['name']):
            deleteEnv(y['id'])
        postEnv(json_data['name'], json_data['value'], '')
