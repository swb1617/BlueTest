import time
import unittest
from appium import webdriver
from common.retryTest import retry

from common.tool import Tool
from config import desired_caps, max_number
from element.elementData import Data
from element.elementDevice import Device
from element.button import Tap
from element.elementMenu import Menu


class TestDevice(unittest.TestCase):
    def setUp(self) -> None:  # 执行方法前准备工作
        self.driver.implicitly_wait(20)  # 稳定元素

    def tearDown(self) -> None:  # 执行方法后工作
        # print("...........结束..............")
        time.sleep(3)

    @classmethod
    def setUpClass(cls) -> None:
        cls.parme = {"port": 4723}
        cls.driver = webdriver.Remote('http://localhost:%s/wd/hub' % str(cls.parme['port']), desired_caps)
        Tool.judge_app_state(cls)

    def DataUpload(self):
        time.sleep(2)
        Device.GetDeviceDataManagementData1(self).click()
        time.sleep(15)
        Tool.SwipeDown(self)
        time.sleep(3)
        Device.GetDeviceDataManagementData1(self).click()
        time.sleep(10)
        if Data.GetDataName(self).text:
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToDeleteData(self).click()
            Data.GetDataDeleteDataOk(self).click()
            time.sleep(3)
            Tool.SwipeDown(self)
            time.sleep(3)
            # Device.GetDeviceDataManagementBack(self).click()

    @retry(max_n=max_number)
    def testApp(self):  # TODO 630 620 520 618 50 50s 同步活动稳定性  训练下发**520
        try:
            Tap.GetToHome(self).click()
            time.sleep(5)
            linkState = Menu.GetMenuDeviceConnectionStatus(self).text
            if linkState:
                Tap.GetToDevice(self).click()
                time.sleep(3)
                Device.GetDeviceDataManagementInfo(self).click()
                time.sleep(2)
                try:
                    for i in range(100):
                        self.DataUpload()
                        print("完成", i + 1, "次")
                except Exception as e:
                    print(e)
                    Tool.ReStartApp(self)
                    raise
        except AttributeError as a:
            print(a)
            self.driver.save_screenshot('1.png')
            Tool.ReStartApp(self)
            raise



