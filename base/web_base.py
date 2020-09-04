from time import sleep
from selenium.webdriver.common.by import By
from base.base import Base
from log.get_logger import GetLogger

log=GetLogger.get_logger()


class WebBase(Base):
    """ 以下为web项目专属方法
    placeholder属性是web元素专有的属性，app元素没有
    """
    # 根据显示文本点击指定元素
    def web_base_click_element(self,placeholder_text,click_text):
        log.info('正在调用web专属点击封装方法')
        # 1.点击复选框
        loc1=By.CSS_SELECTOR,"[placeholder='{}']".format(placeholder_text)
        self.base_click(loc1)
        # 2.暂停
        sleep(1)
        # 3.点击包含显示文本的元素
        loc2=By.XPATH,"//*[text()='{}']".format(click_text)
        self.base_click(loc2)

    # 判断web页面中是否存在指定元素
    def web_base_is_exist(self,text):
        log.info("正在调用判断web页面中是否存在指定元素{}的方法".format(text))
        # 组装loc
        loc=By.XPATH,"//*[text()='{}']".format(text)
        try:
            # 查找元素，修改默认的超时时长
            self.base_find_element(loc,timeout=3)
            # 输出找到信息
            log.info("在web页面中找到指定的元素：{}".format(loc))
            print("找到元素:{}".format(loc))
            # 返回True
            return True
        except Exception as e:
            # 未找到则打印错误消息
            log.error("在web页面中，未找到指定元素{}".format(loc))
            print("未找到元素：{}".format(loc))
            # 返回False
            return False

