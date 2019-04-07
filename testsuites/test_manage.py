from testsuites.base_testcase import BaseTestCase
from pageobjects.login import ForumLoginPage
from pageobjects.logout import ForumLogoutPage
from pageobjects.forumdisplay import ForumDisplayPage
from pageobjects.managerCenter import ManagePage
import unittest
from framework.logger import Logger


logger=Logger(logger="TestManageCreate").getlog()

class TestManageCreate(BaseTestCase):

    def test_two(self):
        login = ForumLoginPage(self.driver) #登录
        forumDis = ForumDisplayPage(self.driver) #帖子
        logout = ForumLogoutPage(self.driver) #登出
        manage= ManagePage(self.driver) #管理中心
        name = login.login("admin", "admin")
        logger.info("管理员登录成功")
        if "admin" in name:
            self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
            forumDis.del_mail()
            logger.info("删除帖子成功")
            manage.create_newbankuai("admin","your")
            logger.info("添加新版块成功")

            nameTwo = login.login("ncc", "nccncc")
            logger.info("普通用户登录成功")
            if "ncc" in nameTwo:
                self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
                forumDis.sendmail_P("177","555vgdfghjjknjgyuh")
                logger.info("帖子发表成功")
                forumDis.replay_mail("11111")
                logger.info("回复帖子成功")
                logout.logout()
                logger.info("退出成功")





if __name__=="__main__":
    unittest.main(verbosity=2)