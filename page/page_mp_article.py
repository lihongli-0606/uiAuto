from base.web_base import WebBase
import page
from time import sleep
from log.get_logger import GetLogger

log=GetLogger.get_logger()


class PageMpArticle(WebBase):
    # 点击 内容管理
    def page_click_content_manage(self):
        sleep(1)
        self.base_click(page.mp_content_manage)

    # 点击 发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_artible)

    # 输入 标题
    def page_input_title(self, title):
        self.base_input(page.mp_title, title)

    # 输入 内容
    def page_input_content(self, text):
        # 1.切换frame
        iframe = self.base_find_element(page.mp_iframe)  # 找到iframe元素
        self.driver.switch_to.frame(iframe)
        # 通过元素切换，而不是通过id或者name，因为通过元素切换时，元素未加载时激活显示等待，而id或name是字符串，无法激活显示等待
        # 2.输入内容
        sleep(1)
        self.base_input(page.mp_content, text)
        # 3.回到默认目录
        self.driver.switch_to.default_content()
        sleep(1)

    # 选择 封面-自动
    def page_click_cover(self):
        self.base_click(page.mp_cover_auto)
        sleep(1)

    # 选择 频道
    def page_click_channel(self):
        self.web_base_click_element("请选择", "数据库")
        sleep(1)

    # 点击 发表按钮
    def page_click_submit(self):
        sleep(1)
        self.base_click(page.mp_submit)
        sleep(3)

    # 获取 发表提示信息-->测试脚本断言时使用
    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    # 组合发布文章业务方法
    def page_mp_article(self, title, text):
        log.info("正在执行发布文章操作，输入的标题是{},输入的正文是{}".format(title,text))
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(text)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()
