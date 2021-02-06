from ywyrobot.common import *
from lib.webCommon import webCommon
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

force_tags = ['供应商','商品提报']

def suite_setup():
    INFO('商家提报')
    driver = webCommon().get_global_webdriver()
    goodsManage = driver.find_element_by_css_selector('li:nth-child(2) > div > span:nth-child(2)')
    goodsManage.click()
    time.sleep(1)
    # 跳转到提报列表
    supplyApply_ele = driver.find_element_by_xpath("//a[@href='#/goodsManage/supplyApply']")
    supplyApply_ele.click()
    time.sleep(1)

def screen(driver, itemName):
    INFO('进入商品提报筛选方法，筛选条件为itemName=%s' % itemName)
    itemName_input_ele = driver.find_element_by_xpath('//*[@id="spuName"]')
    #双击全选,然后删除
    itemName_input_ele.click()
    itemName_input_ele.click()
    itemName_input_ele.send_keys(Keys.DELETE)
    #输入需要查询的商品名称
    itemName_input_ele.send_keys(itemName)
    INFO(itemName_input_ele.get_attribute('outerHTML'))
    screen = driver.find_element_by_css_selector('#rc-tabs-12-panel-1 > div.row > form > div > button.ant-btn.ant-btn-primary > span')
    INFO(screen.text)
    screen.click()
    time.sleep(5)