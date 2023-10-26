import json
import os

from listDialog import runDialog
from updateCookie_Util import *

电话号码列表 = [
    '13055789923',
    '13107644225',
    '13107631307',
    '13255991819',
    '空数据'
]


def find_txt(path):
    data = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                data.append(os.path.join(root, file))
    return data


if __name__ == '__main__':
    dialogMsg = {}
    count = 0
    for x in 电话号码列表:
        dialogMsg[x] = count
        count += 1

    for x in find_txt(os.path.dirname(os.path.abspath(__file__))):
        updateFlag = True
        with open(x, 'r') as f:
            json_data = json.load(f)
        data = searchEnvs(json_data['name'])
        for y in data:
            if y['value'] == json_data['value']:
                updateFlag = False

        if updateFlag:
            for y in data:
                deleteEnv(y['id'])
            if json_data['remark'] == '':
                json_data['remark'] = 电话号码列表[runDialog(dialogMsg)]
            postEnv(json_data['name'], json_data['value'], json_data['remark'])
