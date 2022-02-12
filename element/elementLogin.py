from selenium.webdriver.common.by import By

from common.packageparse import get_apkname
from config import apk_path


class Login:
    def GetLoginConsentToLaw(self):
        LoginConsentToLaw = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[2]")
        return LoginConsentToLaw

    def GetLoginNoConsentToLaw(self):
        LoginNoConsentToLaw = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[1]")

        return LoginNoConsentToLaw

    def GetLoginRegisterInfo(self):
        LoginRegisterInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button[1]")
        return LoginRegisterInfo

    def GetLoginRegisterBack(self):
        LoginRegisterBack = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout")
        return LoginRegisterBack

    def GetLoginLoginInfo(self):
        LoginLoginInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button[2]")
        return LoginLoginInfo

    def GetLoginUsernameEdit(self):
        LoginUsernameEdit = self.driver.find_element(by=By.ID, value=get_apkname(apk_path)+":id/et_email")
        return LoginUsernameEdit

    def GetLoginUserPassword(self):
        LoginUserPassword = self.driver.find_element(by=By.ID, value=get_apkname(apk_path)+":id/et_password")
        return LoginUserPassword

    def GetLoginUserLogin(self):
        LoginUserLogin = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.Button")
        return LoginUserLogin

    def GetLoginUserLoginMessage(self):
        LoginUserLoginMessage = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[2]")
        return LoginUserLoginMessage

    def GetLoginUserLoginMessageAgree(self):
        LoginUserLoginMessageAgree = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[2]")
        return LoginUserLoginMessageAgree

    def GetLoginForgetPasswordInfo(self):
        LoginForgetPasswordInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.TextView")
        return LoginForgetPasswordInfo

    def GetLoginForgetPasswordBack(self):
        LoginForgetPasswordBack = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout")
        return LoginForgetPasswordBack








