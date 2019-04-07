from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger
from pageobjects.logout import ForumLogoutPage

logger=Logger(logger="ManagePage").getlog()

#继承BasePage类
class ManagePage(BasePage):

        #创建新版块
        mokuaiManage_link_search_loc=(By.LINK_TEXT,"管理中心") #管理中心，点击后要查找句柄，激活当前窗口
        pwdSecond_input_search_loc=(By.NAME,"admin_password") #输入密码
        submit_click_button_search_loc = (By.NAME, "submit")  # 提交按钮

        # 判断管理中心登录
        manage_isornot_login = (By.CLASS_NAME, "uinfo")

        luntan_click_li_search_loc = (By.LINK_TEXT, "论坛")  # 查找论坛的那一列
        addnewbankuai_link_search_loc = (By.CSS_SELECTOR, ".lastboard>a")  # 查找添加新版块
        addnewbankuai_name_link_search_loc = (By.NAME, "newforum[1][]")  # 查找添加新版块名称
        # addnewbankuai_jicheng_select_search_loc = (By.NAME, "newinherited[1][]")  # 查找添加继承指定板块
        newbankuai_submit_click_search_loc = (By.CSS_SELECTOR, ".fixsel .btn")  # 提交按钮

        luntan_out_click_search_loc = (By.LINK_TEXT, "退出")  # 查找退出按钮

        putongsendMail_a=(By.CSS_SELECTOR,"#category_1 tr:nth-last-child(2) h2 a")  #普通用户登陆后的新版块
        mail_title__input_search_loc = (By.NAME, "subject")  # 查找帖子主题
        mail_content__input_search_loc = (By.CSS_SELECTOR, ".pt")  # 查找帖子内容
        mail_click_button_search_loc = (By.CSS_SELECTOR, ".ptm button")  # 发表按钮



        #创建新版块
        def create_newbankuai(self,pwdTwo,newbankuaiName):
            main_window=self.driver.current_window_handle
            self.driver.switch_to.window(main_window)
            self.click(*self.mokuaiManage_link_search_loc)  # 点击管理中心
            self.get_windows_img()
            time.sleep(5)
            self.get_handlers(1)
            self.sendkeys(pwdTwo, *self.pwdSecond_input_search_loc)  # 输入密码
            self.get_windows_img()
            self.click(*self.submit_click_button_search_loc)  # 点击提交
            time.sleep(3)
            if "admin" in self.findelement(*self.manage_isornot_login).text:
                logger.info("登录管理中心成功")
                self.click(*self.luntan_click_li_search_loc)  # 点击论坛
                self.get_windows_img()
                time.sleep(3)
                self.get_frame(0)
                self.click(*self.addnewbankuai_link_search_loc)  # 点击添加新版块
                self.get_windows_img()
                time.sleep(3)
                self.clear(*self.addnewbankuai_name_link_search_loc) #清空内容
                self.sendkeys(newbankuaiName, *self.addnewbankuai_name_link_search_loc)  # 输入新版块名称
                self.get_windows_img()
                time.sleep(3)
                self.click(*self.newbankuai_submit_click_search_loc)  # 点击提交
                logger.info("添加新版块成功")
                time.sleep(6)
                self.current_window()
                self.click(*self.luntan_out_click_search_loc) #退出管理中心
                self.get_windows_img()
                self.current_window()
                ForumLogoutPage.logout(self.driver)
                time.sleep(6)




