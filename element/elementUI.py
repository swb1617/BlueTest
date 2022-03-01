from selenium.webdriver.common.by import By


class UI():
    def GetDevicesIntelligentNotificationInfo(self):
        DevicesIntelligentNotificationInfo = self.driver.find_element(by=By.XPATH,
                                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[5]")
        return DevicesIntelligentNotificationInfo

    def GetDevicesIntelligentNotificationBack(self):
        DevicesIntelligentNotificationBack = self.driver.find_element(by=By.XPATH,
                                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout")
        return DevicesIntelligentNotificationBack

    def GetDevicesRealTimeTrackingInfo(self):
        DevicesRealTimeTrackingInfo = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[6]")
        return DevicesRealTimeTrackingInfo

    def GetDevicesRealTimeTrackingBack(self):
        DevicesRealTimeTrackingBack = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
        return DevicesRealTimeTrackingBack

    def GetDevicesRealTimeTrackingOpen(self):
        DevicesRealTimeTrackingOpen = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button")
        return DevicesRealTimeTrackingOpen

    def GetDevicesRealTimeTrackingClose(self):
        DevicesRealTimeTrackingClose = self.driver.find_element(by=By.XPATH,
                                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
        return DevicesRealTimeTrackingClose

    def GetDevicesSensorInfo(self):
        DevicesSensorInfo = self.driver.find_element(by=By.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[7]")
        return DevicesSensorInfo

    def GetDevicesSensorBack(self):
        DevicesSensorBack = self.driver.find_element(by=By.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
        return DevicesSensorBack

    def GetDevicesRidingModeInfo(self):
        DevicesRidingModeInfo = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[10]")
        return DevicesRidingModeInfo

    def GetDevicesRidingModeAdd(self):
        DevicesRidingModeAdd = self.driver.find_element(by=By.XPATH,
                                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]")
        return DevicesRidingModeAdd

    def GetDevicesRidingModeAddSave(self):
        DevicesRidingModeAddSave = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[9]/android.widget.Button")
        return DevicesRidingModeAddSave

    def GetDevicesRidingModeDelete(self):
        DevicesRidingModeDelete = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View[7]")
        return DevicesRidingModeDelete

    def GetDevicesRidingModeDeleteSave(self):
        DevicesRidingModeDeleteSave = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        return DevicesRidingModeDeleteSave

    def GetDevicesRidingModeBack(self):
        DevicesRidingModeBack = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
        return DevicesRidingModeBack

    def GetDevicesPageConfigurationInfo(self):
        DevicesPageConfigurationInfo = self.driver.find_element(by=By.XPATH,
                                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[11]")
        return DevicesPageConfigurationInfo

    def GetDevicesPageConfigurationEdit(self):
        DevicesPageConfigurationEdit = self.driver.find_element(by=By.XPATH,
                                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")
        return DevicesPageConfigurationEdit

    def GetDevicesPageConfigurationEditSave(self):
        DevicesPageConfigurationEditSave = self.driver.find_element(by=By.XPATH,
                                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView[2]")
        return DevicesPageConfigurationEditSave

    def GetDevicesPageConfigurationBack(self):
        DevicesPageConfigurationBack = self.driver.find_element(by=By.XPATH,
                                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
        return DevicesPageConfigurationBack

    def GetDevicesWarningSettingsInfo(self):
        DevicesWarningSettingsInfo = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[12]")
        return DevicesWarningSettingsInfo

    def GetDevicesWarningSettingsBack(self):
        DevicesWarningSettingsBack = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
        return DevicesWarningSettingsBack

    def GetDevicesAutomaticSettingInfo(self):
        DevicesAutomaticSettingInfo = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[13]")
        return DevicesAutomaticSettingInfo

    def GetDevicesAutomaticSettingBack(self):
        DevicesAutomaticSettingBack = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
        return DevicesAutomaticSettingBack

    def GetDevicesThemeStyleInfo(self):
        DevicesThemeStyleInfo = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]")
        return DevicesThemeStyleInfo

    def GetDevicesThemeStyleBack(self):
        DevicesThemeStyleBack = self.driver, find_element(by=By.XPATH, value="aa")
        return DevicesThemeStyleBack

    def GetDeviceDisplaySettingsInfo(self):
        DeviceDisplaySettingsInfo = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[3]")
        return DeviceDisplaySettingsInfo

    def GetDeviceDisplaySettingsBack(self):
        DeviceDisplaySettingsBack = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
        return DeviceDisplaySettingsBack

    def GetDevicesSoundSettingsInfo(self):
        DevicesSoundSettingsInfo = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[4]")
        return DevicesSoundSettingsInfo

    def GetDevicesSoundSettingsBack(self):
        DevicesSoundSettingsBack = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
        return DevicesSoundSettingsBack

    def GetDevicesUserSettingsInfo(self):
        DevicesUserSettingsInfo = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[5]")
        return DevicesUserSettingsInfo

    def GetDevicesUserSettingsBack(self):
        DevicesUserSettingsBack = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView")
        return DevicesUserSettingsBack

    def GetDevicesComputerSettingInfo(self):
        DevicesComputerSettingInfo = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[8]")
        return DevicesComputerSettingInfo

    def GetDevicesComputerSettingBack(self):
        DevicesComputerSettingBack = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout")
        return DevicesComputerSettingBack
