import time
import unittest

from appium import webdriver

from common.tool import Tool
from config import desired_caps
from element.button import Tap
from element.elementData import Data
from element.elementDevice import Device
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
        global detailsNetworkErrorCount, ossUploadErrorCount, uploadCount, blueToothErrorCount
        detailsNetworkErrorCount = 0
        ossUploadErrorCount = 0
        uploadCount = 0
        blueToothErrorCount = 0
        timeNumber = 15
        while True:
            try:
                if Device.GetDeviceDataManagementData1Info(self):
                    # print('数据已上传，准备删除数据')
                    Device.GetDeviceDataManagementData1Info(self).click()
            except:
                # print("数据未上传，准备上传数据")
                Device.GetDeviceDataManagementData1(self).click()
                time.sleep(timeNumber)
                try:
                    if Device.GetDeviceDataManagementData1Info(self):
                        # print('数据已上传，准备删除数据')
                        Device.GetDeviceDataManagementData1Info(self).click()
                except:
                    if Device.GetDeviceDataManagementData1(self):
                        Device.GetDeviceDataManagementData1(self).click()
                        # print("Device.GetDeviceDataManagementData1(self).click()")
                    if Device.GetDeviceDataUpError(self).text == "同步失败，是否重新同步":
                        print("message is " + Device.GetDeviceDataUpError(self).text)
                        # ossUploadErrorCount = ossUploadErrorCount + 1  # 网络错误
                        self.driver.save_screenshot('error' + str(ossUploadErrorCount) + '.png')
                        while True:
                            # print("while True:")
                            Device.GetDeviceDataUpErrorOk(self).click()
                            time.sleep(timeNumber)
                            try:
                                if Device.GetDeviceDataManagementData1Info(self):
                                    ossUploadErrorCount = ossUploadErrorCount + 1  # 网络错误
                                    print("GetDeviceDataManagementData1Info")
                                    Device.GetDeviceDataManagementData1Info(self).click()
                                    break
                            except:
                                print("重新上传")
                                ossUploadErrorCount = ossUploadErrorCount + 1  # 网络错误
                                Device.GetDeviceDataManagementData1(self).click()
                                continue
                    elif Device.GetDeviceDataUpError(self).text == "文件异常，请联系售后":
                        print("message is " + Device.GetDeviceDataUpError(self).text)
                        blueToothErrorCount = blueToothErrorCount + 1
                        self.driver.save_screenshot('error' + str(blueToothErrorCount) + '.png')
                        while True:
                            Device.GetDeviceDataUpErrorOk(self).click()
                            time.sleep(timeNumber)
                            try:
                                if Device.GetDeviceDataManagementData1Info(self):
                                    blueToothErrorCount = blueToothErrorCount + 1
                                    Device.GetDeviceDataManagementData1Info(self).click()
                                    break
                            except:
                                print("重新上传")
                                blueToothErrorCount = blueToothErrorCount + 1
                                Device.GetDeviceDataManagementData1(self).click()
                                continue
                    else:
                        print("未知错误")
                        self.driver.save_screenshot('weizhierror.png')
            try:
                if Data.GetDataMenuInfo(self):
                    time.sleep(0.5)
                    uploadCount = uploadCount + 1
                    Data.GetDataMenuInfo(self).click()
                    Data.GetDataMenuToDeleteData(self).click()
                    Data.GetDataDeleteDataOk(self).click()
                    # time.sleep(5)
                    # Tool.SwipeDown(self)
                    # Tool.PressBack(self)
                    time.sleep(3)
                    print("630同步活动统计: 共 " + str(uploadCount) + " 次 " " 蓝牙传输一次成功 : " + str(
                        uploadCount - blueToothErrorCount - ossUploadErrorCount) + " 次 ""上传至云端服务器失败 : " + str(
                        ossUploadErrorCount) + " 次 ""蓝牙数据传输失败 : " + str(
                        blueToothErrorCount) + " 次" " 详情网络错误 : " + str(detailsNetworkErrorCount) + " 次")
                elif Device.GetDeviceDataNetworkError(self).text:
                    Device.GetDeviceDataNetworkErrorOk(self).click
                    detailsNetworkErrorCount = detailsNetworkErrorCount + 1
            except:
                if Device.GetDeviceDataNetworkError(self):
                    Device.GetDeviceDataNetworkErrorOk(self).click()
                    detailsNetworkErrorCount = detailsNetworkErrorCount + 1
                else:
                    pass

    # @retry(max_n=max_number)
    def testApp(self):  # TODO 630 620 520 618 50 50s 同步活动稳定性 训练下发
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
                    self.driver.save_screenshot('aload.png')
                    time.sleep(3)
                    # Tool.ReStartApp(self)
                    raise
        except:
            raise
