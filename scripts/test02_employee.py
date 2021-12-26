import unittest
import requests
from api.employee import EmployeeApi
import app
class TestEmployee(unittest.TestCase):
    employee_id = None
    def setUp(self):
        self.employee_api=EmployeeApi()

    def test01_add_employee(self):
        add_employee_data = {
            "username": "pt0540",  # 用户名唯一
            "mobile": "18027290143",  # 手机号唯一
            "timeOfEntry": "2020-07-09",
            "formOfEmployment": 1,
            "workNumber": "540728",  # 员工ID唯一性
            "departmentName": "销售",
            "departmentId": "1266699057968001024",
            "correctionTime": "2020-07-30T16:00:00.000Z"
        }
        response = self.employee_api.add_employee(add_employee_data=add_employee_data)
        print(response.json())

        # TestEmployee.employee_id = response.json().get("data").get("id")
        print(TestEmployee.employee_id)

