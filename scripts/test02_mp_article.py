import pytest

from tools.get_driver import GetDriver
import page
from page.page_in import PageIn
from log.get_logger import GetLogger
from tools.read_yaml import read_yaml

log=GetLogger.get_logger()


class TestMpArticle:
    # 1. 初始化
    def setup(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver('chrome', page.mp_url)
        # 2.获取统一入口类PageIn对象  由于需要获取两个page页面对象，所以将ageiIn单独实例化出来
        self.page_in = PageIn(driver)
        # 3.获取PageMpLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        # 4.获取PageMpArticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()

    # 2. 结束（注销）
    def teardown(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3. 测试发布文章方法
    @pytest.mark.parametrize("data",read_yaml("mp_article.yaml"))
    def test_mp_article(self,data):
        title=data['title']
        content=data['content']
        expect=data['expect']
        # 调用发布文章的方法
        self.article.page_mp_article(title, content)
        # 断言
        try:
            assert expect in self.article.page_get_info()
        except Exception as e:
            log.error("断言错误，错误信息{}".format(e))
            self.article.base_get_img()
            raise
