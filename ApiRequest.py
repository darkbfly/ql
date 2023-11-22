import requests
import urllib3

import notify


class ApiRequest:
    def __init__(self):
        urllib3.disable_warnings()
        self.sec = requests.session()
        self.sec.verify = False
        self.sec.trust_env = False
        self.sendmsg = ''
        self.title = ''

    def send(self):
        notify.send(self.title, self.sendmsg)
