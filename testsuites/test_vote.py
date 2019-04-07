from testsuites.base_testcase import BaseTestCase
from pageobjects.login import ForumLoginPage
from pageobjects.logout import ForumLogoutPage
from pageobjects.forumdisplay import ForumDisplayPage
import unittest
from framework.logger import Logger
import time


logger=Logger(logger="TestVote").getlog()

class TestVote(BaseTestCase):

    def test_four(self):
        login=ForumLoginPage(self.driver)
        logout=ForumLogoutPage(self.driver)
        forum = ForumDisplayPage(self.driver)
        name = login.login("admin", "admin")
        logger.info("管理员登录成功")
        if "admin" in name:
            self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
            forum.send_vote("3333","4","5","dsjnfefjkajksddhjbffkjf")
            time.sleep(15)
            logout.logout()




if __name__=="__main__":
    unittest.main(verbosity=2)