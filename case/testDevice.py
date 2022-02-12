import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from common.retryTest import retry

from common.tool import Tool
from config import desired_caps, max_number
from element.elementData import Data
from element.elementDevice import Device
from element.button import Tap
from element.elementMenu import Menu


class TestDevice(unittest.TestCase):
    def setUp(self) -> None:  # 执行方法前准备工作
        self.driver.implicitly_wait(15)  # 稳定元素

    def tearDown(self) -> None:  # 执行方法后工作
        # print("...........结束..............")
        time.sleep(3)

    @classmethod
    def setUpClass(cls) -> None:
        cls.parme = {"port": 4723}
        cls.driver = webdriver.Remote('http://localhost:%s/wd/hub' % str(cls.parme['port']), desired_caps)
        Tool.judge_app_state(cls)

    def DataUpload(self):
        global i,j
        i = 0
        j = 0
        while True:
            try:
                if Device.GetDeviceDataManagementData1Info(self):
                    print('数据已上传，准备删除数据')
                    Device.GetDeviceDataManagementData1Info(self).click()
            except:
                print("数据未上传，准备上传数据")
                Device.GetDeviceDataManagementData1(self).click()
                time.sleep(25)
                try:
                    if Device.GetDeviceDataManagementData1Info(self):
                        print('数据已上传，准备删除数据')
                        Device.GetDeviceDataManagementData1Info(self).click()
                except:
                    if Device.GetDeviceDataManagementData1(self):
                        j = j + 1
                        print("上传失败 " + str(j) + " 次")
            try:
                if Data.GetDataMenuInfo(self):
                    Data.GetDataMenuInfo(self).click()
                    Data.GetDataMenuToDeleteData(self).click()
                    Data.GetDataDeleteDataOk(self).click()
                    time.sleep(5)
                    Tool.SwipeDown(self)
                    Tool.PressBack(self)
                    time.sleep(3)
                elif Device.GetDeviceDataNetworkError(self).text:
                    Device.GetDeviceDataNetworkErrorOk(self).click()
                    i = i + 1
                    print("网络错误" + str(i) + "次")
            except:
                self.driver.save_screenshot('3.png')
                if Device.GetDeviceDataNetworkError(self):
                    Device.GetDeviceDataNetworkErrorOk(self).click()
                    i = i + 1
                    print("网络错误" + str(i) + "次")
                else:
                    pass
            # try:
            #     if Data.GetDataMenuInfo(self):
            #         Data.GetDataMenuInfo(self).click()
            #         Data.GetDataMenuToDeleteData(self).click()
            #         Data.GetDataDeleteDataOk(self).click()
            #         time.sleep(5)
            #         Tool.SwipeDown(self)
            #         Tool.PressBack(self)
            #         time.sleep(3)
            #     else:
            #         Device.GetDeviceDataNetworkErrorOk(self).click()
            # except:
            #     self.driver.save_screenshot('3.png')
            #     if Device.GetDeviceDataNetworkError(self):
            #         Device.GetDeviceDataNetworkErrorOk(self).click()
            #         i = i+1
            #         print("网络错误" + str(i) + "次")
            #     else:
            #         pass

    # @retry(max_n=max_number)
    def testApp(self):  # TODO 630 620 520 618 50 50s 同步活动稳定性  训练下发**520
        try:
            Tap.GetToHome(self).click()
            time.sleep(5)
            linkState = Menu.GetMenuDeviceConnectionStatus(self).text
            if linkState:
                print(linkState)
                Tap.GetToDevice(self).click()
                time.sleep(5)
                Device.GetDeviceDataManagementInfo(self).click()
                time.sleep(2)
                try:
                    self.DataUpload()
                except:
                    self.driver.save_screenshot('0.png')
                    time.sleep(3)
                    # Tool.ReStartApp(self)
                    raise
        except:
            raise
