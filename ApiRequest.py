import requests
class ApiRequest():
    def __init__(self):
        self.sec = requests.session()
        self.sec.verify = False
        self.sec.trust_env = False
