from selenium.webdriver.common.by import By


class Route:
    def GetRouteImportCircuit(self):
        RouteImportCircuit = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.view.View[2]")
        return RouteImportCircuit

    def GetRouteIdName(self):
        RouteIDName = self.driver.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")
        return RouteIDName

