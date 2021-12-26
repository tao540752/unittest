import unittest
import time
from scripts.test01_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
from scripts.test02_employee import TestEmployee
# 组装测试套件
suite = unittest.TestSuite()
# 登录接口测试用例
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(TestLogin('test_login'))
suite.addTest(unittest.makeSuite(TestEmployee))

# 指定测试报告的路径
report = "./report/report.html"
# 打开文件流
with open(report, "wb") as f:
    # 创建HTMLTestRunner运行器
    runner = HTMLTestRunner(f, title="API Report")

    # 执行测试套件
    runner.run(suite)
