from tools.get_driver import GetDriver
import page
from page.page_in import PageIn
from log.get_logger import GetLogger
import pytest
from tools.read_yaml import read_yaml

log=GetLogger.get_logger()

class TestMisLogin:
    # 1.初始化
    def setup(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver('chrome', page.mis_url)
        # 2.通过统一入口类对象获取PageMisLogin对象
        self.mis = PageIn(driver).page_get_PageMisLogin()

    # 2.销毁
    def teardown(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3.登录业务测试方法
    @pytest.mark.parametrize("data",read_yaml("mis_login.yaml"))
    def test_mis_login(self,data):
        username=data['username']
        pwd=data['password']
        expect=data['expect']
        # 调用登录业务方法
        self.mis.page_mis_login(username=username,pwd=pwd)
        # 调试断言信息
        try:
            assert expect in self.mis.page_get_nickname()
        except Exception as e:
            # 日志
            log.error("断言出错，出错原因：{}".format(e))
            # 截图
            self.mis.base_get_img()
            # 异常抛出
            raise
