from tools.get_driver import GetDriver
from page.page_in import PageIn
from log.get_logger import GetLogger
import pytest

from tools.read_yaml import read_yaml

log = GetLogger.get_logger()


class TestAppArticle:
    # 1.初始化
    def setup(self):
        # 1.获取driver
        driver = GetDriver.get_app_driver()
        # 2.获取页面统一入口对象
        self.page_in = PageIn(driver)
        # 3.调用登录成功方法
        self.page_in.page_get_PageAppLogin().page_app_login_success()
        # 4.获取PageAppArticle对象
        self.article = self.page_in.page_get_PageAppArticle()

    # 2.结束
    def teardown(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 3.文章测试方法
    @pytest.mark.parametrize("data", read_yaml("app_article.yaml"))
    def test_app_article(self, data):
        channel=data['channel']
        title=data['title']
        try:
            # 调用文章业务方法
            self.article.page_app_article(channel, title)
        except Exception as e:
            # 1.日志
            log.error("断言出错，错误原因：{}".format(e))
            # 2.截图
            self.article.base_get_img()
            # 3.抛出异常
            raise
