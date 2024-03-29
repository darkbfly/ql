import datetime
import json
import os
import traceback

from listDialog import runDialog
from updateCookie_Util import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from plyer import notification

with open('config.json', 'r') as f:
    config = json.load(f)
电话号码列表 = config['phoneList']


def find_txt(path):
    data = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                data.append(os.path.join(root, file))
    return data


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".txt"):
            print(f'文件 {event.src_path} 已经被修改')
            changeenv(event.src_path)


def changeenv(src_path):
    updateFlag = True
    try:
        with open(src_path, 'r') as f:
            json_data = json.load(f)
        data = searchEnvs(json_data['name'])
        for y in data:
            if y['value'] == json_data['value']:
                print("无需更新")
                updateFlag = False

        if updateFlag:
            if json_data['remark'] == '':
                json_data['remark'] = 电话号码列表[runDialog(dialogMsg)]
            for y in data:
                if json_data['remark'] == y['remarks']:
                    deleteEnv(y['id'])
            if postEnv(json_data['name'], json_data['value'], json_data['remark']):
                if json_data['run']:
                    # 执行脚本
                    runTask(searchTask(json_data['taskName']))
            notification.notify(
                title=f'更新{json_data["taskName"]}',
                message="更新成功",
                timeout=5,
            )
    except:
        traceback.print_exc()
        pass

if __name__ == '__main__':

    隐藏cmd对话框()
    dialogMsg = {}
    count = 0
    for x in 电话号码列表:
        dialogMsg[x] = count
        count += 1

    # 单次运行
    # changeenv('13055789923-pepcoinnew.pepcoinbypepsico.com.cn.txt')

    path_to_watch = os.path.dirname(os.path.abspath(__file__))
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)

    print(f"开始监听 {path_to_watch}...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
