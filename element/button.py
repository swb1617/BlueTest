from selenium.webdriver.common.by import By


class Tap:
    def GetToHome(self):
        ToHome = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                             "1]/android.widget.LinearLayout["
                                                             "1]/android.widget.FrameLayout["
                                                             "1]/android.widget.LinearLayout["
                                                             "1]/android.widget.FrameLayout["
                                                             "1]/android.widget.LinearLayout["
                                                             "1]/android.widget.FrameLayout[2]/android.view.ViewGroup["
                                                             "1]/android.widget.FrameLayout[1]")
        return ToHome

    def GetToActivity(self):
        ToActivity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "2]/android.view.ViewGroup["
                                                                 "1]/android.widget.FrameLayout[2]")
        return ToActivity

    def GetToDevice(self):
        ToDevice = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "2]/android.view.ViewGroup["
                                                               "1]/android.widget.FrameLayout[3]")
        return ToDevice

    def GetToMe(self):
        ToMe = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                           "1]/android.widget.LinearLayout["
                                                           "1]/android.widget.FrameLayout["
                                                           "1]/android.widget.LinearLayout["
                                                           "1]/android.widget.FrameLayout["
                                                           "1]/android.widget.LinearLayout["
                                                           "1]/android.widget.FrameLayout[2]/android.view.ViewGroup["
                                                           "1]/android.widget.FrameLayout[4]")
        return ToMe


class Jurisdiction:
    def GetAgreeJurisdiction(self):
        AgreeJurisdiction = self.driver.find_element(by=By.ID,
                                                     value="com.android.packageinstaller:id/permission_allow_button")
        return AgreeJurisdiction

    def GetJurisdictionMessage(self):
        JurisdictionMessage = self.driver.find_element(by=By.ID,
                                                       value="com.android.packageinstaller:id/permission_message")
        return JurisdictionMessage
