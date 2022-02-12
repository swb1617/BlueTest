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

    @retry(max_n=max_number)
    def test_LoginApp(self):
        UserName = userID
        Password = userPassword
        Login.GetLoginConsentToLaw(self).click()
        time.sleep(2)
        Login.GetLoginRegisterInfo(self).click()
        time.sleep(2)
        Login.GetLoginRegisterBack(self).click()
        Login.GetLoginLoginInfo(self).click()
        time.sleep(3)
        Login.GetLoginForgetPasswordInfo(self).click()
        time.sleep(2)
        Login.GetLoginForgetPasswordBack(self).click()
        time.sleep(1)
        Login.GetLoginUsernameEdit(self).click()
        Login.GetLoginUsernameEdit(self).send_keys(UserName)
        time.sleep(1)
        Login.GetLoginUserPassword(self).click()
        Login.GetLoginUserPassword(self).send_keys(Password)
        time.sleep(1)
        Login.GetLoginUserLogin(self).click()
        time.sleep(5)
        Message = Login.GetLoginUserLoginMessage(self).text
        if Message:
            time.sleep(3)
            Login.GetLoginUserLoginMessageAgree(self).click()
            time.sleep(1)
            Tool.AgreeJurisdiction(self)

    # TODO 退出登录重新登录未做(1)
    # TODO 注册流程未走通需万能验证码配合
