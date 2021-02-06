from ywyrobot.common import *
from lib.webCommon import webCommon


# force_tags = ['冒烟测试','订单功能']

def suite_setup():
    INFO('打开浏览器，并登录遥望云')
    driver = webCommon().open_browser()
    webCommon().login(driver)
    # 切入供应商项目的frame
    driver.switch_to_frame('_inner_content_data')

def suite_teardown():
    INFO('关闭浏览器')
    driver = webCommon().get_global_webdriver()
    driver.quit()

