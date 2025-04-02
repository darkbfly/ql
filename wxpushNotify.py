from wxpusher import WxPusher
import re, sys, os
from collections import deque


def sendpush(arrayObject, msg):
    if arrayObject:
        msg = msg + "\n" + "\n".join(arrayObject)
        WxPusher.send_message(
            msg,
            topic_ids=[os.environ["wxpusherTopicId"]],
            token=os.environ["wxpusherAppToken"],
        )


def get_ql_path():
    if re.search("/ql/data/", sys.path[0]):
        return "/ql/data/"
    else:
        return "/ql/"


def get_ql_logfile(name):
    for path, dir_list, file_list in os.walk(get_ql_path() + "log/"):
        if name in path:
            files = [
                f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
            ]
            # 如果文件夹为空，返回 None
            if not files:
                return None
            # 根据文件的修改时间进行排序
            files.sort(
                key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True
            )
            # 返回最新的文件名
            return os.path.join(path, files[0])


def split_file_by_delimiter(
    file_path, delimiter="----------------------------------------"
):
    """
    读取文件并根据指定的分隔符分割内容。

    :param file_path: 文件路径
    :param delimiter: 分隔符，默认为 "-------------------"
    :return: 分割后的字符串列表
    """
    try:
        # 打开文件并读取内容
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # 使用分隔符分割内容
        parts = content.split(delimiter)

        # 去除每部分的多余空白字符（如换行符、空格等）
        parts = [part.strip() for part in parts if part.strip()]

        return parts

    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return []
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return []


class checkObject:
    def __init__(self, name, logfile_name, keyword):
        self.err_list = []
        self.msg = f"检查{name}发现异常"
        self.logfile_name = logfile_name
        self.keyword = keyword

    def checkLogfile(self, beforeLine=0):
        queue = None
        if beforeLine > 0:
            queue = deque(maxlen=beforeLine)
        file_name = get_ql_logfile(self.logfile_name)
        if file_name:
            with open(file_name, "r") as file:
                for line_number, line in enumerate(file, start=1):
                    if queue is not None:
                        queue.append(line)
                    # 使用正则表达式查找包含关键字的行
                    if re.search(self.keyword, line):
                        if queue is not None:
                            self.err_list.append("".join(queue))
                            queue.clear()
                        else:
                            self.err_list.append(line.strip())
        else:
            self.msg += "\n未检测到日志文件"
        print(self.err_list)
        sendpush(self.err_list, self.msg)


if __name__ == "__main__":
    checkObject("京东", "jd_CheckCK", "已失效").checkLogfile(0)
    checkObject("饿了么", "elm_", "需要登录").checkLogfile(2)
    checkObject("植白说", "植白说_", "undefined").checkLogfile(0)
    checkObject("百事乐元", "百事乐元_", "请重新登录").checkLogfile(0)
    checkObject("朵茜", "朵茜_", "invalid session").checkLogfile(0)
    checkObject("zippo", "zippo_", "Unauthorized").checkLogfile(0)
    checkObject("好人家美味生活馆", "hrj_", "获取登录信息失败,请重新登录").checkLogfile(
        0
    )
    checkObject("拼多多果园", "拼多多果园_", "失效").checkLogfile(0)
    checkObject("Tank", "Tank_", "token已失效，请重新登录").checkLogfile(0)
    checkObject("北京汽车", "bjqc_", "登录失败").checkLogfile(0)
    checkObject("立白", "立白VIP_", "undefined").checkLogfile(0)
    checkObject("zhengjia", "zhengjia_", "失败").checkLogfile(0)
    checkObject("骁龙骁友会", "wx_xlxyh_", "非法请求").checkLogfile(0)
    checkObject("海天美味馆", "htmwg_", "登录状态已失效").checkLogfile(0)
    checkObject("三只松鼠", "三只松鼠_", "invalid").checkLogfile(0)
    checkObject("蜜丝miss", "Miss_", "token无效").checkLogfile(0)
    checkObject("MAMMUT", "MAMMUT_", "invalid").checkLogfile(0)
    checkObject("伊利积分", "yljf_", "Token已过期").checkLogfile(0)
    checkObject("爱依服", "爱依服_", "invalid").checkLogfile(0)
    checkObject("三养", "三养_", "invalid").checkLogfile(0)

    # jd资产推送
    file_name = get_ql_logfile("shufflewzc_faker3_main_jd_bean_change_")
    if file_name:
        for x in split_file_by_delimiter(file_name):
            # print("内容为:\n" + x)
            WxPusher.send_message(
                x,
                topic_ids=[os.environ["wxpusherTopicId"]],
                token=os.environ["wxpusherAppToken"],
            )
