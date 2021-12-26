import requests
import unittest

class LoginApi:
    def __init__(self):
        self.url='http://ihrm-test.itheima.net/api/sys/login'

    def login(self,data_login):
        return requests.post(url=self.url,json=data_login)
