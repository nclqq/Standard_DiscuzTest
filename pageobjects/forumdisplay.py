from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger

logger=Logger(logger="ForumDisplayPage").getlog()

#继承BasePage类
class ForumDisplayPage(BasePage):

        morenbankuai_btn_search_loc = (By.CSS_SELECTOR, "tr h2 a")  # 默认板块

        # 普通用户登陆后的新版块
        putongsendMail_a = (By.CSS_SELECTOR, "#category_1 tr:nth-last-child(2) h2 a")

        #快速发帖
        mail_title__input_search_loc = (By.NAME, "subject") # 查找帖子主题
        mail_content__input_search_loc = (By.CSS_SELECTOR,".pt") # 查找帖子内容
        mail_click_button_search_loc = (By.CSS_SELECTOR, ".ptm button") # 发表按钮

        #回帖
        repaly_area_area_search_loc = (By.CSS_SELECTOR, ".area>.pt")  # 回复文本框
        replay_click_button_search_loc = (By.NAME, "replysubmit")  # 回复按钮

        #发帖按钮
        fatie_img_search_loc = (By.ID, "newspecial")  # 发帖按钮
        vote_link_search_loc = (By.LINK_TEXT, "发起投票")  # 发起投票

        # 搜索帖子
        srchtext_input_search_loc = (By.NAME, "srchtxt")  # 搜索框
        srbtn__button_search_loc = (By.ID, "scbar_btn")  # 搜索按钮
        srtxt_a_search_loc = (By.CSS_SELECTOR, ".xs3 a")  # 进入搜索的帖子
        findthetitle_search_loc = (By.CSS_SELECTOR, ".ts span")  # 标题

        #发起投票
        votitle_input_search_loc = (By.ID, "subject")  # 发起投票的标题
        voFirst_input_search_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(1) input")  # 第一个
        voSecond_input_search_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")  # 第二个
        # voThird_input_search_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")  # 第三个
        voText = (By.TAG_NAME, "body")  # 查找iframe中的元素
        send_vote_btn = (By.CSS_SELECTOR, ".mbm button")  # 发起投票按钮

        vote_one_btn = (By.CSS_SELECTOR, ".pcht tr:nth-child(1) .pslt")  # 第一个投票按钮
        # vote_two_btn = (By.CSS_SELECTOR, ".pcht tr:nth-child(3) .pslt")  # 第二个投票按钮
        vote_submit_btn = (By.CSS_SELECTOR, ".pcht tr:nth-child(5) button")  # 提交投票按钮

        # 投票各个选项的名称和比例
        vote_first_name = (By.CSS_SELECTOR, ".pcht tr:nth-child(1) .pvt label")  # 第一个名字
        vote_first_percent = (By.CSS_SELECTOR, ".pcht tr:nth-child(2) td:last-of-type")  # 第一个比例
        vote_second_name = (By.CSS_SELECTOR, ".pcht tr:nth-child(3) .pvt label")  # 第二个名字
        vote_second_percent = (By.CSS_SELECTOR, ".pcht tr:nth-child(4) td:last-of-type")  # 第二个比例
        vote_title = (By.CSS_SELECTOR, ".ts span")  # 投票主题

        #删除帖子
        del__input_search_loc = (By.CSS_SELECTOR, ".o input")  # 查找对勾
        delmail__link_search_loc = (By.LINK_TEXT, "删除")  # 查找删除
        suredel_click_button_search_loc = (By.CSS_SELECTOR, ".pns #modsubmit")  # 确定删除按钮



        # 删除帖子
        def del_mail(self):
            time.sleep(4)
            self.current_window()
            self.click(*self.morenbankuai_btn_search_loc)  # 点击默认板块
            self.current_window()
            self.click(*self.del__input_search_loc)  # 选择要删除的
            self.current_window()
            self.get_windows_img()
            time.sleep(6)
            self.click(*self.delmail__link_search_loc)  # 点击删除链接
            self.get_windows_img()
            time.sleep(6)
            self.click(*self.suredel_click_button_search_loc)  # 点击确定删除按钮
            logger.info("删除帖子成功")
            time.sleep(6)

        # 发表投票
        def send_vote(self, title, First_Content, Second_Content, vote_text):
            self.click(*self.morenbankuai_btn_search_loc)  # 点击默认板块
            self.click(*self.fatie_img_search_loc)  # 点击发帖
            self.get_windows_img()
            self.current_window()  # 激活当前
            self.click(*self.vote_link_search_loc)  # 点击发起投票
            self.get_windows_img()
            time.sleep(3)

            self.sendkeys(title, *self.votitle_input_search_loc)  # 输入标题
            self.sendkeys(First_Content, *self.voFirst_input_search_loc)  # 输入第一个
            self.sendkeys(Second_Content, *self.voSecond_input_search_loc)  # 输入第二个
            time.sleep(3)
            self.get_frame(0)  # 进入iframe
            self.sendkeys(vote_text, *self.voText)  # 输入内容
            time.sleep(3)
            self.current_window()
            self.get_windows_img()
            self.click(*self.send_vote_btn)  # 点击发表投票按钮

            self.current_window()
            self.click(*self.vote_one_btn)  # 点击进行投票
            self.get_windows_img()
            time.sleep(3)
            self.click(*self.vote_submit_btn)  # 点击提交投票

            self.current_window()
            self.get_windows_img()

            logger.info("第一个选项的名称：%s" % self.findelement(*self.vote_first_name).text)
            logger.info("第一个选项的比例：%s" % self.findelement(*self.vote_first_percent).text)
            logger.info("第二个选项的名称：%s" % self.findelement(*self.vote_second_name).text)
            logger.info("第二个选项的比例：%s" % self.findelement(*self.vote_second_percent).text)
            logger.info("投票的主题：%s" % self.findelement(*self.vote_title).text)

            time.sleep(10)

        #管理员发帖
        def sendmail_M(self,mail_title,mail_content):
            time.sleep(4)
            self.click(*self.morenbankuai_btn_search_loc)  # 点击默认板块
            self.sendkeys(mail_title, *self.mail_title__input_search_loc)  # 输入帖子主题
            time.sleep(3)
            self.sendkeys(mail_content, *self.mail_content__input_search_loc)  # 输入帖子正文
            time.sleep(3)
            self.get_windows_img()
            self.click(*self.mail_click_button_search_loc)  # 点击发帖按钮
            logger.info("帖子信息填写成功")
            time.sleep(3)

        #普通用户在新板块下发帖
        def sendmail_P(self,title,content):
            self.click(*self.putongsendMail_a)
            self.sendkeys(title, *self.mail_title__input_search_loc)  # 输入帖子主题
            time.sleep(3)
            self.sendkeys(content, *self.mail_content__input_search_loc)  # 输入帖子正文
            time.sleep(3)
            self.get_windows_img()
            self.click(*self.mail_click_button_search_loc)  # 点击发帖按钮
            logger.info("帖子信息填写成功")
            time.sleep(3)


        #回帖
        def replay_mail(self,replay_area):
            self.current_window()  # 激活当前页面
            time.sleep(3)
            self.sendkeys(replay_area, *self.repaly_area_area_search_loc)  # 输入回复的内容
            time.sleep(3)
            self.get_windows_img()
            self.click(*self.replay_click_button_search_loc)  # 点击发帖按钮
            logger.info("回复帖子信息填写成功")
            time.sleep(3)

        #搜索帖子
        def search_mail(self,sr_content):
            self.sendkeys(sr_content, *self.srchtext_input_search_loc)  # 输入搜索内容
            self.get_windows_img()
            time.sleep(6)
            self.click(*self.srbtn__button_search_loc)  # 点击搜索按钮
            self.get_handlers(1) #获取新窗口
            self.get_windows_img()
            self.click(*self.srtxt_a_search_loc)  # 点击进入搜索的帖子
            self.get_handlers(2)  # 激活新窗口
            time.sleep(6)
            return self.findelement(*self.findthetitle_search_loc).text
            time.sleep(3)

