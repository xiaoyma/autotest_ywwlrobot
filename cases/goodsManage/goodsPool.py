from ywyrobot.common import *
from lib.webCommon import webCommon
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

force_tags = ['供应商','商家商品池']


def suite_setup():
    INFO('商家商品池')
    driver = webCommon().get_global_webdriver()
    goodsManage = driver.find_element_by_css_selector('li:nth-child(2) > div > span:nth-child(2)')
    goodsManage.click()
    time.sleep(1)
    supplyGoods = driver.find_element_by_xpath("//a[@href='#/goodsManage/supplyGoods']")
    supplyGoods.click()
    time.sleep(1)

def screen(driver, itemName):
    INFO('进入商品池筛选方法，筛选条件为itemName=%s' % itemName)
    itemName_input_ele = driver.find_element_by_xpath('//*[@id="itemName"]')
    #点击公司名称输入框的清楚按钮
    itemName_input_ele.send_keys('0')
    driver.find_element_by_css_selector('div:nth-child(2) > div.ant-col.ant-legacy-form-item-control-wrapper > div > span > span > span > span > svg').click()
    itemName_input_ele.send_keys(itemName)
    INFO(itemName_input_ele.get_attribute('outerHTML'))
    screen = driver.find_element_by_xpath('//*[@id="search"]')
    INFO(screen.text)
    screen.click()
    time.sleep(5)

def get_driver():
    driver = webCommon().get_global_webdriver()
    return driver


class c2101:
    # 测试用例名字
    name = '商家商品池 - UI-2101'

    # 测试用例步骤
    def teststeps(self):
        driver = webCommon().get_global_webdriver()

        STEP(1, '进入创建商品页面')
        #点击新增按钮
        add_button_ele = driver.find_element_by_css_selector('button:nth-child(2) > span:nth-child(2)')
        add_button_ele.click()
        time.sleep(2)

        STEP(2, '输入SPU信息')
        #点击供应商选择框
        supplier_select_ele = driver.find_element_by_css_selector('div>div>div>form>div>div>div>span>div>div>span>#supplierNo')
        #输入供应商名称=进鑫门业（自动化测试）退
        supplier_select_ele.send_keys('进鑫门业（自动化测试）退')
        time.sleep(3)
        #搜索到结果后，点击回车
        supplier_select_ele.send_keys(Keys.ENTER)
        time.sleep(2)

        #点击类目选择框
        catergory_select_ele = driver.find_element_by_css_selector('div.ant-col.ant-col-16.ant-legacy-form-item-control-wrapper > div > span > span > span')
        INFO(catergory_select_ele.get_attribute('outerHTML'))
        time.sleep(1)
        catergory_select_ele.click()
        catergory_input_ele = driver.find_element_by_css_selector('div.ant-col.ant-col-16.ant-legacy-form-item-control-wrapper > div > span > span > input')
        time.sleep(1)
        #选择食品酒水
        catergory_input_ele.send_keys(Keys.DOWN)
        catergory_input_ele.send_keys(Keys.DOWN)
        time.sleep(1)
        #选择休闲零食
        catergory_input_ele.send_keys(Keys.ARROW_RIGHT)
        time.sleep(1)
        #选择饮料
        catergory_input_ele.send_keys(Keys.ARROW_RIGHT)
        time.sleep(1)
        #选择其他饮料
        catergory_input_ele.send_keys(Keys.ARROW_RIGHT)
        catergory_input_ele.send_keys(Keys.ENTER)
        time.sleep(1)

        #输入品牌=进鑫铝材
        brand_input_ele = driver.find_element_by_css_selector('div.ant-col.ant-col-22.ant-legacy-form-item-control-wrapper > div > span > input')
        brand_input_ele.send_keys('进鑫铝材')
        time.sleep(1)

        #输入SPU名称=自动化测试商品-勿动
        spuName_input_ele = driver.find_element_by_css_selector('div > span > #itemName')
        spuName_input_ele.send_keys('自动化测试商品-勿动')
        time.sleep(1)

        #输入供应商编码

        #上传一张图片
        itemPics_input_ele = driver.find_element_by_css_selector('#itemPics')
        itemPics_input_ele.send_keys(r'C:\Users\ywwl\Pictures\automationTestPic.jpg')
        time.sleep(1)

        STEP(3, '输入SKU资料')
        #输入国际码
        skuCode_input_ele = driver.find_element_by_css_selector('td:nth-child(3) > div > div > div > span > input')
        skuCode_input_ele.send_keys('automationSkuCode-001')
        time.sleep(1)

        #输入颜色
        color_input_ele = driver.find_element_by_css_selector('td:nth-child(5) > div > div > div > span > input')
        color_input_ele.send_keys('蓝色')
        time.sleep(1)

        #点击确定
        submit_input_ele = driver.find_element_by_css_selector('div.ant-modal-footer > button.ant-btn.ant-btn-primary > span')
        submit_input_ele.click()
        time.sleep(5)

        STEP(4, '校验是否出现创建成功的弹窗')
        create_success_ele = driver.find_element_by_css_selector('div.ant-modal-confirm-body > div')
        create_success = create_success_ele.text
        CHECK_POINT('校验弹窗文案为创建成功', create_success == '商品已成功创建！')

        # STEP(5, '从创建成功的弹窗，退回到列表页')
        # itemName_input_ele = driver.find_element_by_xpath('//*[@id="itemName"]')
        # itemName_input_ele.send_keys(Keys.ESCAPE)
        # itemName_input_ele.send_keys(Keys.ESCAPE)
        # itemName_input_ele.send_keys(Keys.ESCAPE)
        # time.sleep(5)

        STEP(5, '通过弹窗，跳转到提报信息页')
        #弹窗上的去提报按钮
        go_item_submit = driver.find_element_by_css_selector('div.ant-modal-confirm-btns > button:nth-child(2) > span')
        go_item_submit.click()
        time.sleep(2)

        STEP(6, '提交提报信息')
        #勾选采购入库
        caigouruku_input_ele = driver.find_element_by_css_selector('#addnewForm_supplyType > label:nth-child(1) > span.ant-radio > input')
        caigouruku_input_ele.click()
        #是否配合直播加减库存，勾选是
        is_coordinate_ele = driver.find_element_by_css_selector('#addnewForm_isCoordinate > label:nth-child(1) > span.ant-radio > input')
        is_coordinate_ele.click()
        #是否提供主播，勾选是
        is_assist_ele = driver.find_element_by_css_selector('#addnewForm_isAssist > label:nth-child(1) > span.ant-radio > input')
        is_assist_ele.click()
        #输入是否全国包邮
        is_country_express_free_ele = driver.find_element_by_css_selector('#addnewForm_isCountryExpressFree')
        is_country_express_free_ele.send_keys('全国包邮')

        #输入SKU价格
        #供货价
        supply_price_or_commission_rate = driver.find_element_by_css_selector('td:nth-child(7) > div > div > div > span > div > div.ant-input-number-input-wrap > input')
        supply_price_or_commission_rate.send_keys('1')
        #建议价
        suggest_price = driver.find_element_by_css_selector('td:nth-child(8) > div > div > div > span > div > div.ant-input-number-input-wrap > input')
        suggest_price.send_keys('1')
        #日常价
        daily_price = driver.find_element_by_css_selector('td:nth-child(9) > div > div > div > span > div > div.ant-input-number-input-wrap > input')
        daily_price.send_keys('1')
        #历史最低价
        history_min_price = driver.find_element_by_css_selector('td:nth-child(10) > div > div > div > span > div > div.ant-input-number-input-wrap > input')
        history_min_price.send_keys('1')
        #可供库存
        sku_size_ele = driver.find_element_by_css_selector('td:nth-child(11) > div > div > div > span > input')
        sku_size_ele.send_keys('1')
        #发货时效
        delivery_time_ele = driver.find_element_by_css_selector('td:nth-child(15) > div > div > div > span > input')
        delivery_time_ele.send_keys('1')
        #提交按钮
        INFO('提交按钮')
        item_submit_ele = driver.find_element_by_css_selector('button.ant-btn.ant-btn-primary.ant-btn-lg.mgr20 > span')
        item_submit_ele.click()
        time.sleep(3)

        #取消创建商品按钮
        create_back_ele = driver.find_element_by_css_selector('div.ant-modal-footer > button:nth-child(1) > span')
        INFO(create_back_ele)
        create_back_ele.click()
        time.sleep(1)

        STEP(7, '校验创建的提报记录能否查询')
        #跳转到提报列表
        supplyApply_ele = driver.find_element_by_xpath("//a[@href='#/goodsManage/supplyApply']")
        supplyApply_ele.click()

