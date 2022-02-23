from selenium.webdriver.common.by import By

from common.packageparse import get_apkname
from config import apk_path


class Training:
    def GetTrainingRecommendTrainingTap(self):
        TrainingRecommendTrainingTap = self.driver.find_element(by=By.XPATH,
                                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]")
        return TrainingRecommendTrainingTap

    def GetTrainingRecommendFirstTrainingName(self):
        TrainingRecommendFirstTrainingName = self.driver.find_element(by=By.XPATH,
                                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView")
        return TrainingRecommendFirstTrainingName

    def GetTrainingPeaksTap(self):
        TrainingPeaksTap = self.driver.find_element(by=By.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]")
        return TrainingPeaksTap

    def GetTrainingDiyTrainingTap(self):
        TrainingDiyTrainingTap = self.driver.find_element(by=By.XPATH,
                                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]")
        return TrainingDiyTrainingTap

    def GetTrainingAddTraining(self):
        TrainingAddTraining = self.driver.find_element(by=By.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout")
        return TrainingAddTraining

    def GetTrainingAddTrainingBack(self):
        TrainingAddTrainingBack = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")
        return TrainingAddTrainingBack

    def GetTrainingAddSave(self):
        TrainingAddSave = self.driver.find_element(by=By.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[2]")
        return TrainingAddSave

    def GetTrainingAddStep(self):
        TrainingAddStep = self.driver.find_element(by=By.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.Button[1]")
        return TrainingAddStep

    def GetTrainingAddRepeat(self):
        TrainingAddRepeat = self.driver.find_element(by=By.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.Button[2]")
        return TrainingAddRepeat

    def GetTrainingAddChangeName(self):
        TrainingAddChangeName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView[2]")
        return TrainingAddChangeName

    def GetTrainingNameEdit(self):
        TrainingNameEdit = self.driver.find_element(by=By.ID, value=get_apkname(apk_path) + ":id/et_title")
        return TrainingNameEdit

    def GetTrainingNameSave(self):
        TrainingNameSave = self.driver.find_element(by=By.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button")
        return TrainingNameSave

    def GetTrainingDetailsBack(self):
        TrainingDetailsBack = self.driver.find_element(by=By.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")
        return TrainingDetailsBack

    def GetTrainingDetailsMenu(self):
        TrainingDetailsMenu = self.driver.find_element(by=By.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]")
        return TrainingDetailsMenu

    def GetTrainingDetailsMenuToEdit(self):
        TrainingDetailsMenuToEdit = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
        return TrainingDetailsMenuToEdit

    def GetTrainingDetailsMenuToDelete(self):
        TrainingDetailsMenuToDelete = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
        return TrainingDetailsMenuToDelete

    def GetTrainingDetailsDown(self):
        TrainingDetailsDown = self.driver.find_element(by=By.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]")
        return TrainingDetailsDown
