from selenium.webdriver.common.by import By


class Menu:

    def GetMenuTitle(self):  # 首页标题
        MenuTitle = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout[ "
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout[ "
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout[ "
                                                                "1]/android.widget.RelativeLayout["
                                                                "1]/android.widget.TextView[1]")
        return MenuTitle

    def GetMenuMessageInto(self):  # 首页消息按钮
        MessageInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout[ "
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout[ "
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout[ "
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.view.ViewGroup[1]")
        return MessageInto

    def GetMenuFriendInto(self):  # 首页好友按钮
        MenuFriendInto = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android"
                                                                     ".widget.LinearLayout/android.widget.FrameLayout"
                                                                     "/android.widget.LinearLayout/android.widget"
                                                                     ".FrameLayout/android.widget.LinearLayout/android"
                                                                     ".widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout/android.widget"
                                                                     ".FrameLayout/android.widget.RelativeLayout/android"
                                                                     ".view.ViewGroup[2]")
        return MenuFriendInto

    def GetMenuFriendBack(self):
        MenuFriendBack = self.driver.find_element(by=By.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]")
        return MenuFriendBack

    def GetMenuTrainingGoalsInto(self):  # 首页修改训练按钮
        TrainingGoalsInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.view.ViewGroup["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout[1]")
        return TrainingGoalsInto

    def GetMenuMonthGoals(self):  # 首页月骑行目标数据（float）
        MonthGoals = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.view.ViewGroup["
                                                                 "1]/android.widget.ScrollView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.RelativeLayout["
                                                                 "1]/android.widget.TextView[4]")
        return MonthGoals

    def GetMenuFirstData(self):  # 首页第一天数据
        FirstData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.view.ViewGroup["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "2]/android.widget.FrameLayout["
                                                                "1]/androidx.recyclerview.widget.RecyclerView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.RelativeLayout["
                                                                "1]/android.widget.LinearLayout[1]")
        return FirstData

    def GetMenuSecondData(self):  # 首页第二条数据
        SecondData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.view.ViewGroup["
                                                                 "1]/android.widget.ScrollView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "2]/android.widget.FrameLayout["
                                                                 "1]/androidx.recyclerview.widget.RecyclerView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "2]/android.widget.RelativeLayout["
                                                                 "1]/android.widget.LinearLayout[1]")
        return SecondData

    def GetMenuThirData(self):  # 首页第三条数据
        ThirdData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.view.ViewGroup["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "2]/android.widget.FrameLayout["
                                                                "1]/androidx.recyclerview.widget.RecyclerView["
                                                                "1]/android.widget.LinearLayout["
                                                                "3]/android.widget.RelativeLayout["
                                                                "1]/android.widget.LinearLayout[1]")
        return ThirdData

    def GetMenuFirstTraining(self):  # 首页第一条训练
        FirstTraining = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.view.ViewGroup["
                                                                    "1]/android.widget.ScrollView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "2]/android.widget.FrameLayout["
                                                                    "1]/androidx.recyclerview.widget.RecyclerView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.LinearLayout[1]")
        return FirstTraining

    def GetMenuFirstTrainingName(self):
        MenuFirstTrainingName = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]")
        return MenuFirstTrainingName

    def GetMenuSecondTraining(self):  # 首页第二条训练
        SecondTraining = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.view.ViewGroup["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "2]/android.widget.FrameLayout["
                                                                     "1]/androidx.recyclerview.widget.RecyclerView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "2]/android.widget.RelativeLayout["
                                                                     "1]/android.widget.LinearLayout[1]")
        return SecondTraining

    def GetMenuThirdTraining(self):  # 首页第三条训练
        ThirdTraining = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.view.ViewGroup["
                                                                    "1]/android.widget.ScrollView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "2]/android.widget.FrameLayout["
                                                                    "1]/androidx.recyclerview.widget.RecyclerView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "3]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.LinearLayout[1]")
        return ThirdTraining

    def GetMenuMoreTraining(self):
        MenuMoreTraining = self.driver.find_element(by=By.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout")
        return MenuMoreTraining

    def GetMenuMoreTrainingBack(self):
        MenuMoreTrainingBack = self.driver.find_element(by=By.XPATH,
                                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
        return MenuMoreTrainingBack

    def GetMenuDeviceConnectionStatus(self):
        MenuDeviceConnectionStatus = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
        return MenuDeviceConnectionStatus

    def GetMenuDeviceName(self):
        MenuDeviceName = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
        return MenuDeviceName

    def GetMenuOneKeySynchronization(self):
        MenuOneKeySynchronization = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View")
        return MenuOneKeySynchronization




