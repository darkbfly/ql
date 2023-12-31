from wxpusher import WxPusher
import re, sys, os


def sendpush(arrayObject, msg):
    if arrayObject:
        msg = msg + '\n' + '\n'.join(arrayObject)
        WxPusher.send_message(msg,
                              topic_ids=[os.environ['wxpusherTopicId']],
                              token=os.environ['wxpusherAppToken'])


def get_ql_path():
    if re.search('/ql/data/', sys.path[0]):
        return '/ql/data/'
    else:
        return '/ql/'


def get_ql_logfile(name):
    for path, dir_list, file_list in os.walk(get_ql_path() + 'log/'):
        if name in path:
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            # 如果文件夹为空，返回 None
            if not files:
                return None
            # 根据文件的修改时间进行排序
            files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True)
            # 返回最新的文件名
            return os.path.join(path, files[0])


class checkObject:
    def __init__(self, name, logfile_name, keyword):
        self.err_list = []
        self.msg = f'检查{name}发现异常'
        self.logfile_name = logfile_name
        self.keyword = keyword

    def checkLogfile(self):
        file_name = get_ql_logfile(self.logfile_name)
        if file_name:
            with open(file_name, 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    # 使用正则表达式查找包含关键字的行
                    if re.search(self.keyword, line):
                        self.err_list.append(line.strip())
        else:
            self.msg += '\n未检测到日志文件'
        print(self.err_list)
        sendpush(self.err_list, self.msg)


def 检查京东():
    checkObject('京东', 'jd_CheckCK', '已失效').checkLogfile()


def 检查饿了么():
    checkObject('饿了么', 'elm_842', '需要登录').checkLogfile()


if __name__ == '__main__':
    检查京东()
    检查饿了么()

