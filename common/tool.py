import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from element.button import Jurisdiction
from config import apk_path
from common.packageparse import get_apk_lautc, get_apkname


class Tool:
    def GetToast(self, toast_message):
        message = '//*[@text=\'{}\']'.format(toast_message)
        toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(by=By.XPATH, value=message))
        print(toast_element.text)
        assert toast_element.text == toast_message
        return toast_element.text

    def PressEnter(self):  # 定义回车键
        self.driver.press_keycode(66)

    def PressBack(self):  # 定义返回键
        self.driver.keyevent(4)

    def PressMoveEnd(self):  # 定义光标移动文本末尾
        self.driver.keyevent(123)

    def SwipeDown(self):  # 定义下滑动方法
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.5
        y1, y2 = height * 0.35, height * 0.7
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1200)

    def SwipeFriendLeft(self):  # 定义下滑动方法
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1, x2 = width * 0.9, width * 0.1
        y1 = y2 = height * 0.35
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)

    def SwipeLittleUp(self):  # 定义上滑动方法
        size = self.driver.get_window_size()  # 获取手机屏幕尺寸
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.7
        y1, y2 = height * 0.89, height * 0.86
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)  # 滑动方法

    def SwipeLittleDown(self):  # 定义切换性别的下滑动方法
        size = self.driver.get_window_size()  # 获取手机屏幕尺寸
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.7
        y1, y2 = height * 0.9, height * 0.95
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)  # 滑动方法

    def SwipeUp(self):  # 定义上滑动方法
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.5
        y1, y2 = height * 0.7, height * 0.35
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)

    def ReStartApp(self):
        time.sleep(3)
        self.driver.close_app()  # 定义关闭APP方法
        time.sleep(3)
        self.driver.start_activity(get_apkname(apk_path), get_apk_lautc(apk_path))

    def StartApp(self):
        # if Tool.app_state(self) == 4:
        #     time.sleep(3)
        # elif Tool.app_state(self) == 1:
        #     Tool.InstallApp(self)
        # else:
        #     time.sleep(3)
        self.driver.start_activity(get_apkname(apk_path), get_apk_lautc(apk_path))
        time.sleep(3)

    def InstallApp(self):
        APP = self.driver.is_app_installed(get_apkname(apk_path))
        print("APP安装状态is", APP)
        if APP:
            self.driver.remove_app(get_apkname(apk_path))
            time.sleep(5)
            print("删除APPing")
            self.driver.install_app(apk_path)
            print("安装APPing")
            time.sleep(5)
        else:
            time.sleep(5)
            self.driver.install_app(apk_path)
            print("安装APPing")

    def reset_app(self):
        self.driver.reset(get_apkname(apk_path))

    def AgreeJurisdiction(self):
        try:
            time.sleep(1)
            Message = Jurisdiction.GetJurisdictionMessage(self)
            if Message:
                Jurisdiction.GetAgreeJurisdiction(self).click()
            else:
                pass
        except:
            pass

    def get_app_state(self):
        state: int = self.driver.query_app_state(get_apkname(apk_path))
        if state == 4:
            print("APP正在前台运行")
        elif state == 3:
            print("APP在后台运行")
        elif state == 2:
            print("APP刮起")
        elif state == 1:
            print("APP未运行")
        else:
            print("APP未安装")
        return state

    def judge_app_state(self):
        app_state = Tool.get_app_state(self)
        if app_state == 4:
            time.sleep(3)
            # Tool.ReStartApp(self)
        elif app_state == 0:
            print("APP未安装")
            quit(self)
        elif app_state == 1:
            Tool.StartApp(self)
        elif app_state == 2:
            Tool.StartApp(self)
        elif app_state == 3:
            Tool.StartApp(self)
        else:
            raise
