import requests
import unittest
import json
from api.login import LoginApi
from parameterized import parameterized
import app

'''
def build_data():
    test_data=[]
    with open('C:\putao\pych\IHRMtest\data\login.json',encoding='utf-8') as f:
        data_json=json.load(f)
        for case_data in data_json:
            login_data=case_data['login_data']
            status_code=case_data['status_code']
            success=case_data['success']
            message=case_data['message']
            test_data.append((login_data,status_code,success,message))
    print(test_data)
    return test_data
'''
class TestLogin(unittest.TestCase):
    Token=None
    def setUp(self):
        self.login_api=LoginApi()

    def test_login(self):

        login_data= {
            "mobile": "13800000002",
            "password": "123456"
        }
        response=self.login_api.login(login_data)

        self.assertEqual(200,response.status_code)
        self.assertEqual('操作成功！',response.json().get('message'))
        print(response.json())
        app.TOKEN='Bearer '+response.json().get("data")
        print(app.TOKEN)
        app.headers_data['Authorization']=app.TOKEN
        print(app.headers_data['Authorization'])





