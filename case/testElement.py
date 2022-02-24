"""
user:石文斌
time：2022/01/05

"""
import time
import unittest

from appium import webdriver

from config import desired_caps, max_number, userPassword, userID
from element.elementLogin import Login
from common.tool import Tool
from common.retryTest import retry


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:  # 执行方法前准备工作
        self.parme = {"port": 4723}
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % str(self.parme['port']), desired_caps)
        Tool.InstallApp(self)
        Tool.judge_app_state(self)
        self.driver.implicitly_wait(20)  # 稳定元素

    def tearDown(self) -> None:  # 执行方法后工作
        time.sleep(3)


