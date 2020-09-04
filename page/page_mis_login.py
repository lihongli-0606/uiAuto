from base.web_base import WebBase
import page
from log.get_logger import GetLogger

log=GetLogger.get_logger()

class PageMisLogin(WebBase):
    # 1.输入用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username_loc,username)

    # 2.输入密码
    def page_input_password(self, pwd):
        self.base_input(page.mis_password_loc,pwd)
    # 3.点击登录按钮
    def page_click_login(self):
        # 处理js代码
        js="document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)
        # 点击登录
        self.base_click(page.mis_login_btn_loc)

    # 4.获取登录后昵称  --> 测试脚本层断言使用
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname_loc)

    # 5.组合登录业务方法--> 测试脚本层调用
    def page_mis_login(self, username, pwd):
        log.info('正在调用mis后台管理模块的登录方法，用户名{},密码{}'.format(username,pwd))
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login()

    # 6.组合登录业务方法  -->后台系统审核文章时需要先登录
    def page_mis_login_success(self, username='testid', pwd='testpwd123'):
        log.info('正在调用mis后台管理模块的成功登录依赖方法，用户名{},密码{}'.format(username, pwd))
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login()
