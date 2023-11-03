import requests

import notify


class ApiRequest:
    def __init__(self):
        self.sec = requests.session()
        self.sec.verify = False
        self.sec.trust_env = False
        self.sendmsg = ''
        self.title = ''

    def send(self):
        notify.send(self.title, self.sendmsg)
