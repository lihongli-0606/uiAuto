from selenium.webdriver.common.by import By
import page
from tools.read_yaml import read_yaml

"""以下数据为自媒体、后台管理模块url"""
# mp地址
mp_url = "http://ttmp.research.itcast.cn/#/login"
# 后台管理
mis_url = 'http://ttmis.research.itcast.cn/#/'

"""以下为文章相关数据"""
data = read_yaml('mp_article.yaml')
title = data[0]['title']
channel = data[0]['channel']

"""以下数据为自媒体模块配置数据"""
# 用户名
mp_username_loc = By.CSS_SELECTOR, "[placeholder='请输入手机号']"
# 密码
mp_password_loc = By.CSS_SELECTOR, "[placeholder='验证码']"
# 登录按钮
mp_login_btn_loc = By.CSS_SELECTOR, ".el-button--primary"
# 昵称
mp_nickname_loc = By.CSS_SELECTOR, ".user-name"
# 内容管理
mp_content_manage = By.XPATH, "//*[text()='内容管理']/.."
# 发布文章
mp_publish_artible = By.XPATH, "//*[contains(text(),'发布文章')]"
# 文章标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 文章内容  定位到body，勿定位到p标签
mp_content = By.CSS_SELECTOR, "#tinymce"
# 封面
mp_cover_single = By.XPATH, "//*[text()='单图']"
mp_cover_three = By.XPATH, "//*[text()='三图']"
mp_cover_no = By.XPATH, "//*[text()='无图']"
mp_cover_auto = By.XPATH, "//*[text()='自动']"
# 频道
# 已经在WebBase中封装单独的方法，无需再次写
# 发表按钮 定位到span后再往上一级，为button
mp_submit = By.XPATH, "//*[text()='发表']/.."
# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

"""以下数据为后台管理模块配置数据"""
# 用户名
mis_username_loc = By.CSS_SELECTOR, "[name='username']"
# 密码
mis_password_loc = By.CSS_SELECTOR, "[name='password']"
# 登录按钮
mis_login_btn_loc = By.CSS_SELECTOR, "#inp1"
# 昵称
mis_nickname_loc = By.CSS_SELECTOR, ".user_info"
# 信息管理
mis_info_manage_loc = By.XPATH, "//*[text()='信息管理']/."
# 内容审核
mis_content_audit_loc = By.XPATH, "//*[text()='内容审核']/."
# 文章标题
mis_article_title_loc = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 频道
mis_article_channel_loc = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 状态 调用WebBase中封装的方法即可
# 文章id(查询结果的第一个文章id）
mis_article_id_loc = By.CSS_SELECTOR, ".cell>span"
# 查询按钮
mis_find_btn_loc = By.CSS_SELECTOR, ".find"
# 通过
mis_pass_loc = By.XPATH, "//span[text()='通过']/.."
# 确认通过
mis_confirm_pass_loc = By.CSS_SELECTOR, ".el-button--primary"

"""以下为app应用配置信息"""
# 包名
appPackage = "com.itcast.toutiaoApp"
# 启动名
appActivity = ".MainActivity"
# 手机号
app_phone = By.XPATH, "//*[@class='android.widget.EditText' and @index = '1']"
# 验证码
app_code = By.XPATH, "//*[@class='android.widget.EditText' and @index = '2']"
# 登录按钮
app_login_btn = By.XPATH, "//*[@text='登录' and @class='android.widget.Button']"
# 我的 菜单
app_me = By.XPATH, "//*[contains(text(),'我的') and @index='3']"
# 频道区域
app_channel_area=By.XPATH,"//*[@class='android.widget.HorizontalScrollView']"
# 文章区域
app_article_area=By.XPATH,"//*[@bounds='[0,520][1440,2288]' and @index = '2']"
