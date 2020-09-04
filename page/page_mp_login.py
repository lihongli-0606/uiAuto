import page
from time import sleep

from base.web_base import WebBase
from log.get_logger import GetLogger


log=GetLogger.get_logger()


class PageMpLogin(WebBase):

    # 1.输入用户名
    def page_input_username(self, content):
        # 调用父类中输入方法
        self.base_input(page.mp_username_loc, content)

    # 输入密码
    def page_input_password(self, content):
        # 调用父类中输入方法
        self.base_input(page.mp_password_loc, content)

    # 点击登录按钮
    def page_click_login(self):
        # 调用父类中点击方法
        sleep(1)
        self.base_click(page.mp_login_btn_loc)

    # 获取昵称 --> 测试脚本层断言使用
    def page_get_nickname(self):
        # 调用父类中获取文本方法
        return self.base_get_text(page.mp_nickname_loc)

    # 组合业务方法 --> 在测试脚本层调用
    def page_mp_login(self,username,password):
        """调用相同页面测试步骤，跨页面暂时不考虑"""
        log.info('正在调用自媒体模块登录操作，用户名{},密码{}'.format(username,password))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login()

    # 组合业务方法 --> 发布文章依赖使用
    def page_mp_login_success(self,username="13812345678",password="246810"):
        log.info('正在调用自媒体模块登录操作，用户名{},密码{}'.format(username,password))
        self.page_input_username(username)  # 正确的用户名
        self.page_input_password(password)   # 正确的密码
        self.page_click_login()
