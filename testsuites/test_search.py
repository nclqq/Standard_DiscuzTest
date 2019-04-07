from testsuites.base_testcase import BaseTestCase
from pageobjects.login import ForumLoginPage
from pageobjects.logout import ForumLogoutPage
from pageobjects.forumdisplay import ForumDisplayPage
import unittest
from framework.logger import Logger
from ddt import ddt,data,unpack


logger=Logger(logger="TestSearch").getlog()

@ddt
class TestSearch(BaseTestCase):

    @unpack
    def test_three(self):
        login=ForumLoginPage(self.driver)
        forumDis = ForumDisplayPage(self.driver)
        logout=ForumLogoutPage(self.driver)
        name = login.login("admin", "admin")
        logger.info("登录成功")
        if "admin" in name:
            self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
            result=forumDis.search_mail("haotest")
            try:
                self.assertEqual(result, "haotest", msg=result)
                logout.logout()
            except Exception as e:
                print("搜索错误或查找不到")



if __name__=="__main__":
    unittest.main(verbosity=2)