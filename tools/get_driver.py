# web自动化需要导入的包
from selenium import webdriver
# app自动化需要导入的包
import appium.webdriver
import page


class GetDriver:
    # 1.声明driver变量
    # web中
    __web_driver = None
    # app中
    __app_driver = None

    # 2.获取web_driver方法  声明为类方法，无需实例化，可通过类名直接调用，更加方便
    @classmethod
    def get_web_driver(cls, driver_type, url):
        # 判断是否为空
        if not cls.__web_driver:
            # 1.获取浏览器
            if driver_type == 'chrome':
                cls.__web_driver = webdriver.Chrome()
            elif driver_type == 'firefox':
                cls.__web_driver = webdriver.Firefox()
            # 2.最大化浏览器
            cls.__web_driver.maximize_window()
            # 3.打开网址
            cls.__web_driver.get(url)
        return cls.__web_driver

    # 3.退出web_driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作  重点
            cls.__web_driver = None

    # 4.获取app driver的方法
    @classmethod
    def get_app_driver(cls):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "5.1",
            "deviceName": "192.168.0.1:5555",  # 安卓平台 设备名可随便填，不为空即可
            "appPackage": page.appPackage,
            "appActivity": page.appActivity
        }
        if cls.__app_driver is None:
            cls.__app_driver = appium.webdriver.Remote("http://localhost:4723/wd/hub/", desired_caps)
        return cls.__app_driver

    # 5.退出app driver的方法
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None
