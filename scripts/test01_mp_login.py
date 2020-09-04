from tools.get_driver import GetDriver
import page
from page.page_in import PageIn
import pytest
from tools.read_yaml import read_yaml
from log.get_logger import GetLogger

log=GetLogger.get_logger()

class TestMpLogin:
    # 初始化
    def setup(self):
        # 1.获取driver对象
        driver = GetDriver.get_web_driver('chrome', page.mp_url)
        # 2.通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 退出  一定要调用自定义的quit，保证每次打开的driver都是同一个
    def teardown(self):
        GetDriver.quit_web_driver()

    # 测试的业务方法
    @pytest.mark.parametrize("data", read_yaml('mp_login.yaml'))
    # @pytest.mark.parametrize("username,password,expect", read_yaml('mp_login.yaml'))
    def test_mp_login(self, data):
    # def test_mp_login(self, username,password,expect):
        # print(data)
        username = data['username']
        password = data['password']
        expect = data['expect']
        # 调用登录业务方法
        self.mp.page_mp_login(username, password)
        # 断言（异常截图）
        # print('获取到的昵称是：',self.mp.page_get_nickname())
        try:
            assert self.mp.page_get_nickname() == expect
        except Exception as e:
            log.error("断言错误，错误信息{}".format(e))
            # print("错误原因：",e)
            self.mp.base_get_img()
            # 再把异常抛出
            raise
