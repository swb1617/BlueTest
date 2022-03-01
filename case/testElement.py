"""
user:石文斌
time：2022/01/05

"""
import logging
import time
import unittest

from appium import webdriver

from config import desired_caps, max_number, userPassword, userID
from element.button import Tap
from element.elementLogin import Login
from common.tool import Tool
from common.retryTest import retry
from element.elementUI import UI


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:  # 执行方法前准备工作
        self.parme = {"port": 4723}
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % str(self.parme['port']), desired_caps)
        # Tool.InstallApp(self)
        Tool.judge_app_state(self)
        self.driver.implicitly_wait(20)  # 稳定元素

    def tearDown(self) -> None:  # 执行方法后工作
        time.sleep(3)

    def testIntelligentNotification(self):
        Tap.GetToDevice(self).click()
        time.sleep(3)
        UI.GetDevicesIntelligentNotificationInfo(self).click()
        time.sleep(3)
        UI.GetDevicesIntelligentNotificationBack(self).click()

    def testRealTimeTracking(self):
        Tap.GetToDevice(self).click()
        time.sleep(3)
        UI.GetDevicesRealTimeTrackingInfo(self).click()
        time.sleep(2)
        UI.GetDevicesRealTimeTrackingOpen(self).click()
        time.sleep(3)
        UI.GetDevicesRealTimeTrackingClose(self).click()
        time.sleep(2)
        UI.GetDevicesRealTimeTrackingBack(self).click()

    def testSensor(self):
        Tap.GetToDevice(self).click()
        time.sleep(3)
        UI.GetDevicesSensorInfo(self).click()
        time.sleep(3)
        UI.GetDevicesSensorBack(self).click()

    def testDisplaySettings(self):
        Tap.GetToDevice(self).click()
        time.sleep(3)
        UI.GetDeviceDisplaySettingsInfo(self).click()
        time.sleep(3)
        UI.GetDeviceDisplaySettingsBack(self).click()

    def testAutomaticSetting(self):
        Tap.GetToDevice(self).click()
        time.sleep(3)
        UI.GetDevicesAutomaticSettingInfo(self).click()
        time.sleep(3)
        UI.GetDevicesAutomaticSettingBack(self).click()

    def testComputerSetting(self):
        Tap.GetToDevice(self).click()
        time.sleep(3)
        UI.GetDevicesComputerSettingInfo(self).click()
        time.sleep(3)
        UI.GetDevicesComputerSettingBack(self).click()

    def testPageConfiguration(self):
        Tap.GetToDevice(self).click()
        time.sleep(3)
        UI.GetDevicesPageConfigurationInfo(self).click()
        time.sleep(2)
        UI.GetDevicesPageConfigurationEdit(self).click()
        time.sleep(1)
        UI.GetDevicesPageConfigurationEditSave(self).click()
        time.sleep(2)
        UI.GetDevicesPageConfigurationBack(self).click()

    def test1(self):
        Tap.GetToDevice(self).click()
        time.sleep(3)
