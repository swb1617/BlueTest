from selenium.webdriver.common.by import By


class Data:
    def GetDataBack(self):  # 详情页返回按钮
        DataBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.RelativeLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout[1]")
        return DataBack

    def GetDataShare(self):  # 详情也分享按钮
        DataShare = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.RelativeLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.ImageView[2]")
        return DataShare

    def GetDataShareBack(self):  # 详情页分享返回按钮
        DataShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.ImageView[1]")
        return DataShareBack

    def GetDataShareWatermarkPhoto(self):  # 详情页分享水印照片按钮
        DataShareWatermarkPhoto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.LinearLayout[2]")
        return DataShareWatermarkPhoto

    def GetDataWatermarkPhotoSave(self):
        DataWatermarkPhotoSave = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout"
                                                                             "/android.widget.LinearLayout/android"
                                                                             ".widget.FrameLayout/android.widget"
                                                                             ".LinearLayout/android.widget"
                                                                             ".FrameLayout/android.widget"
                                                                             ".LinearLayout/android.widget"
                                                                             ".FrameLayout/android.widget"
                                                                             ".LinearLayout/android.widget"
                                                                             ".LinearLayout[1]")
        return DataWatermarkPhotoSave

    def GetDataWatermarkPhotoChangePhoto(self):
        DataWatermarkPhotoChangePhoto = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".ScrollView/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".TextView[2]")
        return DataWatermarkPhotoChangePhoto

    def GetDataWatermarkPhotoChoosePhoto(self):
        DataWatermarkPhotoChoosePhoto = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".RelativeLayout/androidx"
                                                                                    ".recyclerview.widget"
                                                                                    ".RecyclerView/android.widget"
                                                                                    ".RelativeLayout["
                                                                                    "2]/android.widget.TextView")
        return DataWatermarkPhotoChoosePhoto

    def GetDataWatermarkRestoreDefault(self):
        DataWatermarkRestoreDefault = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget"
                                                                                  ".FrameLayout/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".FrameLayout/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".FrameLayout/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".FrameLayout/android.widget"
                                                                                  ".ScrollView/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".TextView[1]")
        return DataWatermarkRestoreDefault

    def GetDataWatermarkPhotoSeePhoto(self):
        GetDataWatermarkPhotoSeePhoto = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".RelativeLayout/android.widget"
                                                                                    ".RelativeLayout["
                                                                                    "2]/android.widget.TextView[3]")
        return GetDataWatermarkPhotoSeePhoto

    def GetDataWatermarkPhotoBack(self):  # 水印照片返回按钮
        DataWatermarkPhotoBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.RelativeLayout["
                                                                             "1]/android.widget.LinearLayout[1]")
        return DataWatermarkPhotoBack

    def GetDataWatermarkPhotoData(self):  # 水印照片第一tap
        DataWatermarkPhotoData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.ScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.HorizontalScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout[1]")
        return DataWatermarkPhotoData

    def GetDataWatermarkPhotoAlt(self):  # 水印照片第二tap
        DataWatermarkPhotoAlt = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.ScrollView["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.HorizontalScrollView["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout[2]")
        return DataWatermarkPhotoAlt

    def GetDataWatermarkPhotoTrack(self):  # 水印照片第三tap
        DataWatermarkPhotoTrack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.ScrollView["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.HorizontalScrollView["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.LinearLayout[3]")
        return DataWatermarkPhotoTrack

    def GetDataMenuInfo(self):  # 详情页菜单按钮
        DataMenuInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.ImageView[3]")
        return DataMenuInfo

    def GetDataName(self):  # 详情页数据名称
        DataName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.RelativeLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "2]/android.widget.LinearLayout["
                                                               "2]/android.widget.TextView[2]")
        return DataName

    def GetDataDistance(self):  # 详情页里程
        DataDistance = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.ScrollView["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "2]/android.widget.LinearLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/androidx.recyclerview.widget.RecyclerView["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.TextView[1]")
        return DataDistance

    def GetDataMapStyleInto(self):  # 详情页切换地图样式按钮
        DataMapStyleInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.ImageView[1]")
        return DataMapStyleInto

    def GetDataMapStyleMode(self):  # 地图样式Dark
        DataMapStyleMode = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "4]/android.widget.ImageView[1]")
        return DataMapStyleMode

    def GetDataMapStyleSave(self):  # 保存地图样式
        DataMapStyleSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.Button[1]")
        return DataMapStyleSave

    def GetDataMapStyleGoals(self):  # 公里点打开关闭按钮
        DataMapStyleGoals = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.Switch[ "
                                                                        "1]")
        return DataMapStyleGoals

    def GetDataMenuToEditActivity(self):  # 修改活动名称
        DataEditActivity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.TextView[1]")
        return DataEditActivity

    def GetDataSwitchChart(self):
        DataSwitchChart = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.RelativeLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "2]/android.view.ViewGroup["
                                                                      "1]/android.widget.FrameLayout[2]")
        return DataSwitchChart

    def GetDataSwitchingDetails(self):
        DataSwitchingDetails = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "2]/android.view.ViewGroup["
                                                                           "1]/android.widget.FrameLayout[3]")
        return DataSwitchingDetails

    def GetDataMenuToSaveMyLine(self):  # 保存到我的线路
        DataMenuToSaveMyLine = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[2]")
        return DataMenuToSaveMyLine

    def GetDataMenuToSendFriend(self):  # 发送给好友
        DataMenuToSendFriend = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[3]")
        return DataMenuToSendFriend

    def GetDataMenuToSendFriendAddFriend(self):
        DataMenuToSendFriendAddFriend = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button")
        return DataMenuToSendFriendAddFriend

    def GetDataMenuToExportFile(self):  # 保存数据到文件
        DataMenuToExportFile = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[4]")
        return DataMenuToExportFile

    def GetDataMenuToDeleteData(self):  # 删除数据按钮
        DataMenuToDeleteData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[5]")
        return DataMenuToDeleteData

    def GetDataLineNumber(self):
        DataLineNumber = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.RelativeLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.RelativeLayout["
                                                                     "1]/android.widget.TextView[2]")
        return DataLineNumber

    def GetDataLineDistance(self):
        DataLineDistance = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "2]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.TextView[1]")
        return DataLineDistance

    def GetDataRidingTime(self):
        DataRidingTime = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.RelativeLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "2]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/androidx.recyclerview.widget.RecyclerView["
                                                                     "1]/android.widget.RelativeLayout["
                                                                     "2]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.TextView[1]")
        return DataRidingTime

    def GetDataAverageVelocity(self):
        DataAverageVelocity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.RelativeLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.ScrollView["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "2]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/androidx.recyclerview.widget"
                                                                          ".RecyclerView["
                                                                          "1]/android.widget.RelativeLayout["
                                                                          "3]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.TextView[1]")
        return DataAverageVelocity

    def GetDataMaximumSpeed(self):
        DataMaximumSpeed = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "2]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "4]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.TextView[1]")
        return DataMaximumSpeed

    def GetDataAverageHeartRate(self):
        DataAverageHeartRate = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.ScrollView["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "2]/android.widget.LinearLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/androidx.recyclerview.widget"
                                                                           ".RecyclerView["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "5]/android.widget.LinearLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[1]")
        return DataAverageHeartRate

    def GetDataAverageStepFrequency(self):
        DataAverageStepFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.RelativeLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.ScrollView["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "2]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/androidx.recyclerview.widget"
                                                                               ".RecyclerView["
                                                                               "1]/android.widget.RelativeLayout["
                                                                               "6]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.TextView[1]")
        return DataAverageStepFrequency

    def GetDataCalorie(self):
        DataCalorie = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.ScrollView["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "2]/android.widget.LinearLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/androidx.recyclerview.widget.RecyclerView["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "14]/android.widget.LinearLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.TextView[1]")
        return DataCalorie

    def GetDataChartSpeedChart(self):
        DataChartSpeedChart = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.RelativeLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.ScrollView["
                                                                          "1]/androidx.recyclerview.widget"
                                                                          ".RecyclerView["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "2]/android.view.ViewGroup[1]")
        return DataChartSpeedChart

    def GetDataEquipmentModel(self):
        DataEquipmentModel = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.ScrollView["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "2]/android.widget.LinearLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "2]/android.widget.TextView[1]")
        return DataEquipmentModel

    def GetDataDeviceVersion(self):
        DataDeviceVersion = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "2]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "2]/android.widget.TextView[2]")
        return DataDeviceVersion

    def GetDataEditText(self):  # 数据修改名字文本框
        DataEditActivity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.view.ViewGroup["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.RelativeLayout[2]")
        return DataEditActivity

    def GetDataEditSave(self):  # 数据修改名字保存
        DataEditSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.view.ViewGroup["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.TextView[3]")
        return DataEditSave

    def GetDataSendToFriendText(self):  # 好友id输入框
        DataSendToFriendText = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.RelativeLayout[1]")
        return DataSendToFriendText

    def GetDataSendToFriend(self):  # 发送给好友按钮
        DataSendToFriend = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.TextView[2]")
        return DataSendToFriend

    def GetDataSendMessageBack(self):  # 消息界面返回
        DataSendMessageBack = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
        return DataSendMessageBack

    def GetDataSendMessageFriendName(self):  # 消息界面好友的名字
        DataSendMessageFriendName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.RelativeLayout[1]")
        return DataSendMessageFriendName

    def GetDataSendFriendName(self):  # 发送给好友的名字
        DataSendFriendName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/androidx.recyclerview.widget"
                                                                         ".RecyclerView["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.TextView[1]")
        return DataSendFriendName

    def GetDataExportDataBack(self):  # 数据导出返回
        DataExportDataBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.LinearLayout[1]")
        return DataExportDataBack

    def GetDataExportDataFit(self):  # fit文件格式
        DataExportDataFit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/androidx.recyclerview.widget.RecyclerView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return DataExportDataFit

    def GetDataExportDataGpx(self):  # gpx格式
        DataExportDataGpx = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/androidx.recyclerview.widget.RecyclerView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "2]/android.widget.LinearLayout[1]")
        return DataExportDataGpx

    def GetDataExportDataTcx(self):  # 数据导出界面tcx文件格式
        DataExportDataTcx = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/androidx.recyclerview.widget.RecyclerView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "3]/android.widget.LinearLayout[1]")
        return DataExportDataTcx

    def GetDataExportDataDowload(self):  # 数据导出下载按钮
        DataExportDataDowload = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.Button[2]")

        return DataExportDataDowload

    def GetDataExportDataSave(self):  # 数据导出保存
        DataExportDataSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.view.ViewGroup["
                                                                         "1]/android.support.v4.widget.DrawerLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "2]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "2]/android.widget.TextView[1]")
        return DataExportDataSave

    def GetDataDeleteDataOk(self):
        DataDeleteDataOk = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.view.ViewGroup["
                                                                       "2]/android.widget.Button[2]")
        return DataDeleteDataOk