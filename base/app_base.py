from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.base import Base
from log.get_logger import GetLogger

log = GetLogger.get_logger()


class AppBase(Base):
    # 1.查找页面是否存在指定元素
    def app_base_is_exist(self, loc):
        """以下是app专属方法，判断当前页面是否存在指定元素"""
        log.info("正在调用判断app页面中是否存在指定元素：{}".format(loc))
        try:
            # 调用查找方法  -->timeout默认30秒，改为3秒，不然超时时长太长
            self.base_find_element(loc, timeout=3)
            # 找到了输出信息
            log.info("在app中找到指定元素：{}".format(loc))
            print("找到元素：{}".format(loc))
            # 返回True
            return True
        except Exception as e:
            # 未找到输出信息
            log.error("在app中未找到元素{}".format(loc))
            print("未找到元素{}".format(loc))
            # 返回False
            return False

    # 2.在指定区域从右向左滑动屏幕
    def app_base_right_swipe_left(self, loc_area, click_text):
        """

        :param loc_area: 查找区域
        :param click_text: 查找内容
        :return:
        """
        log.info("正在调用从右往左滑动屏幕方法。。。")
        # 1. 查找区域元素
        ele = self.base_find_element(loc_area)
        # 2. 获取区域元素的位置 location  y坐标点  x为0
        location = ele.location
        y = location['y']
        # 3. 获取区域元素的宽高 size
        height = ele.size['height']
        width = ele.size['width']
        # 4. 计算start_x,start_y,end_x,end_y
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5

        # 组合频道元素配置信息
        # loc=By.XPATH, "//*[contains(text(),'{}')]".format(click_text)
        # 添加父级限制，在指定区域找
        # loc=By.XPATH, "//*[@class='android.widget.HorizontalScrollView']//*[contains(text(),'{}')]".format(click_text)
        loc=By.XPATH, "//android.widget.HorizontalScrollView/*[contains(text(),'{}')]".format(click_text)
        # 5. 循环操作 page_source
        while True:
            # 1.获取当前屏幕页面元素
            page_source=self.driver.page_source
            # 2.捕获异常
            try:
                sleep(2)
                # 1.查找元素
                ele = self.base_find_element(loc,timeout=3)
                # 2.输出提示信息
                print("找到了元素：{},频道名称为：{}".format(loc,ele.text))
                # 3.点击元素
                sleep(2)
                ele.click()
                # 4.退出循环
                break

            # 3.处理异常
            except:
                # 1.输出提示信息
                print("当前页面未找到元素")
                # 2.滑动
                self.driver.swipe(start_x,start_y,end_x,end_y,duration=2000)

            # 4.判断是否为最后一页
            # 滑动前和滑动后的page_source如果一样，说明已经到以后一页了
            if self.driver.page_source == page_source:
                # 1.输出提示信息
                print("已经到最后一页了，未找到")
                # 2.抛出未找到元素异常
                raise NoSuchElementException

    # 3.在指定区域从下往上滑动屏幕
    def app_base_down_swipe_up(self, loc_area, click_text):
        log.info('正在调用从下往上滑动屏幕方法。。。')
        # 1. 查找区域元素
        ele = self.base_find_element(loc_area)
        # 2. 获取区域元素的宽高 size
        height = ele.size['height']
        width = ele.size['width']
        # 3. 计算start_x,start_y,end_x,end_y
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2

        # 组合频道元素配置信息
        # loc=By.XPATH, "//*[contains(text(),'{}')]".format(click_text)
        # 添加父级限制，在指定区域找
        # loc=By.XPATH, "//*[@class='android.widget.HorizontalScrollView']//*[contains(text(),'{}')]".format(click_text)
        loc=By.XPATH, "//*[@bounds='[0,520][1440,2288]']/*[contains(text(),'{}')]".format(click_text)
        # 5. 循环操作 page_source
        while True:
            # 1.获取当前屏幕页面元素
            page_source=self.driver.page_source
            # 2.捕获异常
            try:
                sleep(2)
                # 1.查找元素
                ele = self.base_find_element(loc,timeout=3)
                # 2.输出提示信息
                print("找到了元素：{},文章标题为{}".format(loc,ele.text))
                # 3.点击元素
                sleep(2)
                ele.click()
                # 4.退出循环
                break

            # 3.处理异常
            except:
                # 1.输出提示信息
                print("当前页面未找到元素")
                # 2.滑动
                self.driver.swipe(start_x,start_y,end_x,end_y,duration=2000)

            # 4.判断是否为最后一页
            # 滑动前和滑动后的page_source如果一样，说明已经到以后一页了
            if self.driver.page_source == page_source:
                # 1.输出提示信息
                print("已经到最后一页了，未找到")
                # 2.抛出未找到元素异常
                raise NoSuchElementException