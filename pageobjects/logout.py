from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger

logger=Logger(logger="ForumLogoutPage").getlog()

#继承BasePage类
class ForumLogoutPage(BasePage):

        #登出
        logout_click_button_search_loc = (By.LINK_TEXT, "退出")  # 退出按钮

        def logout(self):
            time.sleep(3)
            self.click(*self.logout_click_button_search_loc)  # 点击退出按钮
            self.get_windows_img()
            logger.info("登出进行")


