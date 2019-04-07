from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger

logger=Logger(logger="ForumLoginPage").getlog()

#继承BasePage类
class ForumLoginPage(BasePage):
        #登录
        username_input_search_loc = (By.NAME, "username") #用户名
        pwd__input_search_loc = (By.NAME, "password") #密码
        login_click_button_search_loc=(By.XPATH,"//button") #登录按钮

        #判断登录
        isornot_login=(By.CSS_SELECTOR,".vwmy a")


    # 输入搜索内容，并提交
        def login(self,username,pwd):
            self.sendkeys(username,*self.username_input_search_loc) #输入用户名
            self.sendkeys(pwd, *self.pwd__input_search_loc) #输入密码
            self.get_windows_img()
            self.click(*self.login_click_button_search_loc) #点击登录按钮
            logger.info("信息填写成功")
            return self.findelement(*self.isornot_login).text


