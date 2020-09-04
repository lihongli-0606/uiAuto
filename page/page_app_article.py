from base.app_base import AppBase
import page
from log.get_logger import GetLogger


log=GetLogger.get_logger()


class PageAppArticle(AppBase):
    # 1.查找频道方法封装
    def page_click_channel(self, channel):
        """

        :param click_text: 频道名称
        :return:
        """
        # 调用从右向左滑动方法即可
        self.app_base_right_swipe_left(page.app_channel_area, channel)

    # 2.查找文章方法封装
    def page_click_article(self,title):
        """

        :param title: 文章标题
        :return:
        """
        # 调用从下向上滑动方法
        self.app_base_down_swipe_up(page.app_article_area,title)

    # 3.组合查找文章业务方法
    def page_app_article(self, channel,title):
        log.info("正在调用查找文章业务方法，所属频道：{}，文章标题：{}".format(channel,title))
        # 1.调用查找频道
        self.page_click_channel(channel)
        # 2.调用查找文章
        self.page_click_article(title)
