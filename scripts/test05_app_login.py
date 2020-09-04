import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
from log.get_logger import GetLogger
from tools.read_yaml import read_yaml

log = GetLogger.get_logger()


class TestAppLogin:
    # 1.初始化
    def setup(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取PageAppLogin对象
        self.login = PageIn(driver).page_get_PageAppLogin()

    # 2.结束
    def teardown(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 3.测试脚本
    @pytest.mark.parametrize('data',read_yaml('app_login.yaml'))
    def test_app_login(self, data):
        phone=data['phone']
        code=data['code']
        # 1.调用app登录业务方法
        self.login.page_app_login(phone, code)
        # 2.断言
        try:
            assert self.login.page_is_login_success()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_img()
            # 抛出异常
            raise
