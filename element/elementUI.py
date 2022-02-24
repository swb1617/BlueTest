from selenium.webdriver.common.by import By

class UI():
    def GetDevicesIntelligentNotificationInfo(self):
        DevicesIntelligentNotificationInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[5]")
        return DevicesIntelligentNotificationInfo

    def GetDevicesIntelligentNotificationBack(self):
        DevicesIntelligentNotificationBack = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout")
        return DevicesIntelligentNotificationBack

    def GetDevicesRealTimeTrackingInfo(self):
        DevicesRealTimeTrackingInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[6]")
        return DevicesRealTimeTrackingInfo

    def GetDevicesRealTimeTrackingBack(self):
        DevicesRealTimeTrackingBack = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
        return DevicesRealTimeTrackingBack
    
    def GetDevicesRealTimeTrackingOpen(self):
        DevicesRealTimeTrackingOpen = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button")
        return DevicesRealTimeTrackingOpen

    def GetDevicesRealTimeTrackingClose(self):
        DevicesRealTimeTrackingClose = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
        return DevicesRealTimeTrackingClose

    def GetDevicesSensorInfo(self):
        DevicesSensorInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[7]")
        return DevicesSensorInfo
    
    def GetDevicesSensorBack(self):
        DevicesSensorBack = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
        return DevicesSensorBack


    




