import os
import time
from config import BASE_PATH
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from log.get_logger import GetLogger

log = GetLogger.get_logger()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info("正在初始化driver：{}".format(driver))
        """ 解决driver问题 """
        self.driver = driver

    # 查找元素方法封装
    def base_find_element(self, loc, timeout=10, poll=0.5):
        """

        :param loc: 格式为列表或元组，内容：元素定位信息，使用By类
        :param timeout: 查找元素超时时间
        :param poll: 查找元素的频率
        :return: 返回元素
        """
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(*loc))  # *loc为解包 ==loc[0],loc[1]

    # 输入方法封装
    def base_input(self, loc, content):
        """

        :param loc: 元素定位信息
        :param content: 要输入的值
        """
        # 1.获取元素
        ele = self.base_find_element(loc)
        # 2.清空操作
        log.info("正在对元素:{}执行清空操作".format(loc))
        ele.clear()
        # 3.输入操作
        log.info("正在对元素:{}执行输入：{}操作".format(loc, content))
        ele.send_keys(content)

    # 点击方法封装
    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        """
        # 获取元素并点击
        log.info("正在对元素：{}执行点击操作".format(loc))
        self.base_find_element(loc).click()

    # 获取元素文本
    def base_get_text(self, loc):
        """
        别忘了return  text后面没有小括号
        :param loc: 元素定位信息
        :return: 返回元素的文本值
        """
        text = self.base_find_element(loc).text
        log.info("正在对元素：{} 执行获取文本操作,获取的值为{}".format(loc, text))
        return text

    # 截图方法
    def base_get_img(self):
        log.error("断言出错，正在执行截图操作...")  # 此处要用error级别的log
        time_str=time.strftime("%Y-%m-%d %H_%M_%S")
        file_path=BASE_PATH+os.sep+"image"+os.sep+time_str+".png"
        self.driver.get_screenshot_as_file(file_path)
        # 调用图片写入报告的方法
        log.error("正在将错误图片写入allure报告...")
        self.__base_write_img(file_path)

    # 将图片写入报告方法（私有方法）
    def __base_write_img(self,file_path):
        with open(file_path, 'rb') as f:
            # 调用allure报告附加描述方法
            allure.attach(f.read(), "错误原因：", allure.attachment_type.PNG)

