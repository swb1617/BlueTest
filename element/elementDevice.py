from selenium.webdriver.common.by import By


class Device:
    def GetDeviceConnectionStatus(self):
        DeviceConnectionStatus = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout"
                                                                             "/android.widget.LinearLayout/android"
                                                                             ".widget.FrameLayout/android.widget"
                                                                             ".LinearLayout/android.widget"
                                                                             ".FrameLayout/android.widget"
                                                                             ".LinearLayout/android.widget"
                                                                             ".FrameLayout["
                                                                             "1]/androidx.compose.ui.platform"
                                                                             ".ComposeView/android.view.View/android"
                                                                             ".view.View/android.view.View["
                                                                             "2]/android.view.View["
                                                                             "1]/android.view.View[1]")
        return DeviceConnectionStatus

    def GetDeviceName(self):
        DeviceName = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android"
                                                                 ".widget.LinearLayout/android.widget.FrameLayout"
                                                                 "/android.widget.LinearLayout/android.widget"
                                                                 ".FrameLayout/android.widget.LinearLayout/android"
                                                                 ".widget.FrameLayout["
                                                                 "1]/androidx.compose.ui.platform.ComposeView/android"
                                                                 ".view.View/android.view.View/android.view.View["
                                                                 "2]/android.view.View[1]/android.view.View[2]")
        return DeviceName

    def GetDeviceVersionNumber(self):
        DeviceVersionNumber = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout"
                                                                          "/android.widget.LinearLayout/android"
                                                                          ".widget.FrameLayout/android.widget"
                                                                          ".LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[3]/android.view.View")
        return DeviceVersionNumber

    def GetDeviceAutoSyncButton(self):
        DeviceAutoSyncButton = self.driver.find_element(by=By.XPATH,
                                                        value="/hierarchy/android.widget.FrameLayout/android.widget"
                                                              ".LinearLayout/android.widget.FrameLayout/android"
                                                              ".widget.LinearLayout/android.widget.FrameLayout"
                                                              "/android.widget.LinearLayout/android.widget"
                                                              ".FrameLayout["
                                                              "1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.Switch")
        return DeviceAutoSyncButton

    def GetDeviceAddDeviceRightInfo(self):
        DeviceAddDeviceRightInfo = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]")
        return DeviceAddDeviceRightInfo

    def GetDeviceDataManagementInfo(self):
        DeviceDataManagementInfo = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[1]")
        return DeviceDataManagementInfo

    def GetDeviceSecondInfo(self):
        DeviceSecondInfo = self.driver.find_element(by=By.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[3]")
        return DeviceSecondInfo

    def GetDeviceThirdInfo(self):
        DeviceThirdInfo = self.driver.find_element(by=By.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View[3]")
        return DeviceThirdInfo

    def GetDeviceFourthInfo(self):
        DeviceFourthInfo = self.driver.find_element(by=By.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View[4]")
        return DeviceFourthInfo

    def GetDeviceFifthInfo(self):
        DeviceFifthInfo = self.driver.find_element(by=By.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View[5]")
        return DeviceFifthInfo

    def GetDeviceSixthInfo(self):
        DeviceSixthInfo = self.driver.find_element(by=By.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View[6]")
        return DeviceSixthInfo

    def GetDeviceSeventhInfo(self):
        DeviceSevenththInfo = self.driver.find_element(by=By.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View[7]")
        return DeviceSevenththInfo

    def GetDeviceEighthInfo(self):
        DeviceEighthInfo = self.driver.find_element(by=By.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View[8]")
        return DeviceEighthInfo

    def GetDeviceDataManagementBack(self):
        DeviceDataManagementBack = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]")
        return DeviceDataManagementBack

    def GetDeviceDataManagementActivityTap(self):
        DeviceDataManagementActivityTap = self.driver.find_element(by=By.XPATH,
                                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout")
        return DeviceDataManagementActivityTap

    def GetDeviceDataManagementRoadTap(self):
        DeviceDataManagementRoadTap = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        return DeviceDataManagementRoadTap

    def GetDeviceDataManagementChooseDataButton(self):
        DeviceDataManagementChooseDataButton = self.driver.find_element(by=By.XPATH,
                                                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]")
        return DeviceDataManagementChooseDataButton

    def GetDeviceDataManagementAutomaticSynchronizationButton(self):
        DeviceDataManagementAutomaticSynchronizationButton = self.driver.find_element(by=By.XPATH,
                                                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]")
        return DeviceDataManagementAutomaticSynchronizationButton

    def GetDeviceDataManagementAllDataNumber(self):
        DeviceDataManagemenAllDataNumber = self.driver.find_element(by=By.XPATH,
                                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[3]")
        return DeviceDataManagemenAllDataNumber

    def GetDeviceDataManagementChooseDataNumber(self):
        DeviceDataManagemenChooseDataNumber = self.driver.find_element(by=By.XPATH,
                                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")
        return DeviceDataManagemenChooseDataNumber

    def GetDeviceDataManagementData1(self):
        DeviceDataManagementData1 = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
        return DeviceDataManagementData1

    def GetDeviceDataManagementData1Info(self):
        DeviceDataManagementData1Info = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView[2]")
        return DeviceDataManagementData1Info

    def GetDeviceDataUpError(self):
        DeviceDataUpError = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView")
        return DeviceDataUpError
    def GetDeviceDataUpErrorOk(self):
        DeviceDataUpErrorOk = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
        return DeviceDataUpErrorOk

    def GetDeviceDataNetworkError(self):
        DeviceDataNetworkError = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView")
        return DeviceDataNetworkError

    def GetDeviceDataNetworkErrorOk(self):
        DeviceDataNetworkErrorOk = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button")
        return DeviceDataNetworkErrorOk

    def GetDeviceDataManagementData2(self):
        DeviceDataManagementData2 = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]")
        return DeviceDataManagementData2

    def GetDeviceDataManagementData3(self):
        DeviceDataManagementData3 = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]")
        return DeviceDataManagementData3

    def GetDeviceDataManagementData4(self):
        DeviceDataManagementData4 = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]")
        return DeviceDataManagementData4

    def GetDeviceDataManagementData5(self):
        DeviceDataManagementData5 = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]")
        return DeviceDataManagementData5

    def GetDeviceDataManagementData6(self):
        DeviceDataManagementData6 = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[6]")
        return DeviceDataManagementData6

    def GetDeviceDataManagementData7(self):
        DeviceDataManagementData7 = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]")
        return DeviceDataManagementData7

    def GetDeviceDataManagementData8(self):
        DeviceDataManagementData8 = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[8]")
        return DeviceDataManagementData8

    def GetDeviceDataManagementData9(self):
        DeviceDataManagementData9 = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[9]")
        return DeviceDataManagementData9

    def GetDeviceDeleteDataButton(self):
        DeviceDeleteDataButton = self.driver.find_element(by=By.XPATH,
                                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]")
        return DeviceDeleteDataButton

    def GetDeviceDeleteDataSureButton(self):
        DeviceDeleteDataSureButton = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
        return DeviceDeleteDataSureButton
