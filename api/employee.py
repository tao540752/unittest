import requests
import unittest
import app
class EmployeeApi:
    def __init__(self):
        self.url_add_employee = app.BASE_URL + "/api/sys/user"
        self.url_update_employee = app.BASE_URL + "/api/sys/user/{}"
        self.url_get_employee = app.BASE_URL + "/api/sys/user/{}"
        self.url_delete_employee = app.BASE_URL + "/api/sys/user/{}"

    def add_employee(self, add_employee_data):
        return requests.post(url=self.url_add_employee, json=add_employee_data,headers=app.headers_data)