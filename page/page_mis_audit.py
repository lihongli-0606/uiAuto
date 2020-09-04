from base.web_base import WebBase
from time import sleep
import page
from log.get_logger import GetLogger


log=GetLogger.get_logger()


class PageMisAudit(WebBase):
    # 文章id
    article_id = None

    # 1.点击信息管理
    def page_click_info_manage(self):
        # 1.暂停时间
        sleep(1)
        # 2.点击
        self.base_click(page.mis_info_manage_loc)

    # 2.点击文章审核
    def page_click_content_audit(self):
        # 1.暂停时间
        sleep(1)
        # 2.点击
        self.base_click(page.mis_content_audit_loc)

    # 3.输入文章名称
    def page_input_title(self, title):
        self.base_input(page.mis_article_title_loc, title)

    # 4.输入频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_article_channel_loc, channel)

    # 5.选择状态
    def page_click_status(self, placeholder_text="请选择状态", click_text="待审核"):
        self.web_base_click_element(placeholder_text, click_text)

    # 6.点击查询
    def page_click_find(self):
        # 1.点击查询按钮
        self.base_click(page.mis_find_btn_loc)
        # 2.暂停
        sleep(2)

    # 7.获取文章id
    def page_get_article_id(self):
        article_id=self.base_get_text(page.mis_article_id_loc)
        return article_id

    # 8.点击通过
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass_loc)

    # 9.点击确定
    def page_click_confirm_pass(self):
        # 1.暂停
        sleep(1)
        # 2.点击
        self.base_click(page.mis_confirm_pass_loc)
        sleep(1)

    # 10.组合审核文章业务方法  -->测试脚本层调用
    def page_mis_audit(self, title, channel):
        log.info("正在调用审核文章业务方法，文章title:{},频道:{}".format(title,channel))
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_find()
        self.article_id = self.page_get_article_id()
        print("获取到的文章id为：",self.article_id)
        self.page_click_pass_btn()
        self.page_click_confirm_pass()

    # 组装断言业务操作方法
    def page_audit_assert(self):
        log.info("正在调用断言业务操作方法")
        # 1.暂停3秒
        sleep(3)
        # 2.修改查询状态为已审核
        self.page_click_status(click_text="审核通过")
        # 3.点击查询按钮
        self.page_click_find()
        # 4.判断当前页面是否存在指定元素
        return self.web_base_is_exist(self.article_id)
