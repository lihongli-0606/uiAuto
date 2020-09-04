from tools.get_driver import GetDriver
import page
from page.page_in import PageIn
from log.get_logger import GetLogger


log=GetLogger.get_logger()

class TestMisAudit:
    # 1.初始化
    def setup(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver('chrome', page.mis_url)
        # 2.获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3.通过统一入口类对象获取PageMisLogin对象并调用登录成功方法
        self.page_in.page_get_PageMisLogin().page_mis_login_success()
        # 4.获取PageMisAudit对象
        self.mis = self.page_in.page_get_PageMisAudit()

    # 2.退出
    def teardown(self):
        GetDriver.quit_web_driver()

    # 3.测试脚本
    def test_mis_audit(self, title=page.title, channel=page.channel):
        # 调用审核文章业务方法
        self.mis.page_mis_audit(title, channel)
        # 断言处理
        try:
            assert self.mis.page_audit_assert()
        except Exception as e:
            # 1.日志
            log.error("断言出错，错误信息：{}".format(e))
            # 2.截图
            self.mis.base_get_img()
            # 3.抛异常
            raise


