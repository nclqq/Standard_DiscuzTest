from testsuites.base_testcase import BaseTestCase
from pageobjects.login import ForumLoginPage
from pageobjects.logout import ForumLogoutPage
from pageobjects.forumdisplay import ForumDisplayPage
import unittest
from framework.logger import Logger


logger=Logger(logger="TestLoginSend").getlog()

class TestLoginSend(BaseTestCase):

    # 测试登录
    def test_login_search(self):
        login = ForumLoginPage(self.driver)
        forumDis=ForumDisplayPage(self.driver)
        logout=ForumLogoutPage(self.driver)
        name=login.login("admin","admin")
        logger.info("管理员登录成功")
        if "admin" in name:
            self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
            forumDis.sendmail_M("5", "8787878")
            logger.info("帖子发表成功")
            forumDis.replay_mail("888")
            logger.info("回复帖子成功")
            logout.logout()
            logger.info("退出成功")



if __name__=="__main__":
    unittest.main(verbosity=2)