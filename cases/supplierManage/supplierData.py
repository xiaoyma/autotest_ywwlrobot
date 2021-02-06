from ywyrobot.common import *
from lib.webCommon import webCommon
import time
from selenium.webdriver.common.keys import Keys

force_tags = ['供应商','信息管理页']


def suite_setup():
    INFO('进入信息管理页')
    driver = webCommon().get_global_webdriver()
    supplyInfo = driver.find_element_by_xpath("//a[@href='#/supplyManage/supplyInfo']")
    supplyInfo.click()

def screen(driver, supplierName):
    INFO('进入信息管理页筛选方法，筛选条件为supplierName=%s' % supplierName)
    companyName = driver.find_element_by_xpath('//*[@id="supplierName"]')
    # #使用js清空输入框
    # js = 'document.querySelector("#supplierName").value="";'
    # driver.execute_script(js)
    #点击公司名称输入框的清楚按钮
    companyName.send_keys('0')
    driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[2]/div/form/div[2]/div[2]/div/span/span/span/span').click()
    companyName.send_keys(supplierName)
    INFO(companyName.get_attribute('outerHTML'))
    screen = driver.find_element_by_xpath('//*[@id="search"]')
    INFO(screen.text)
    screen.click()
    time.sleep(5)

def get_driver():
    driver = webCommon().get_global_webdriver()
    return driver


class c1201:
    # 测试用例名字
    name = '信息管理页 - UI-1201'

    # 测试用例步骤
    def teststeps(self):
        driver = webCommon().get_global_webdriver()

        STEP(1, '筛选 进鑫门业（自动化测试）退')
        screen(driver=driver, supplierName='进鑫门业（自动化测试）退')

        STEP(2, '检查筛选结果')
        data = driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr/td[3]/button/span')
        result_01 = data.text
        result_02 = driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/ul/li[1]').text
        results = [result_01, result_02]
        INFO(result_01 + result_02)
        CHECK_POINT('筛选结果是否正确', results == ['进鑫门业（自动化测试）退', '共1条数据'])

        STEP(3, '导出筛选结果')
        export = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[2]/div/div[1]/button/span')
        export.click()
        time.sleep(10)

        # STEP(4, '查看供应商详情资料')
        # supplierNo_ele = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr/td[2]/div/button/span')
        # supplierNo = supplierNo_ele.text
        # INFO('供应商编号为' + supplierNo)
        # supplierNo_ele.click()
        # # supplierName_ele = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/label[2]/span[2]')
        # # supplierName = supplierName_ele.text
        # # group_ele = driver.find_element_by_xpath('/html/body/div[13]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[5]/label[3]/span[2]')
        # # group = group_ele.text
        # # INFO('实际得到结果为' + supplierName + group)
        # # CHECK_POINT('结果是否正确', [supplierName, group] == ['进鑫门业（自动化测试）退', '直播业务'])
        # close = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button/span/span/svg')
        # close.click()

class c1202:
    name = '信息管理页 - UI-1202'

    def teststeps(self):
        driver = webCommon().get_global_webdriver()
        STEP(1, '筛选 进鑫门业（自动化测试）退')
        screen(driver=driver, supplierName='进鑫门业（自动化测试）退')

        STEP(2, '打开供应商名称修改页面')
        supplierName_ele = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr/td[3]/button/span')
        supplierName_ele.click()
        # eidtPage = driver.find_element_by_xpath('//*[@id="rcDialogTitle1"]').text
        INFO('打开修改名称页面')
        time.sleep(3)

        STEP(3, '修改未实名供应商名称')
        # driver.find_element_by_xpath('//*[@id="supplierName"]').send_keys('进鑫门业（自动化测试）改')
        # 名称变更页备注输入框
        remark_input = driver.find_element_by_xpath('//*[@id="remark"]')
        remark_input.send_keys('自动化测试-修改名称改')
        supplier_newName_input = driver.find_element_by_css_selector('div > span > #supplierName')
        # driver.execute_script('arguments[0].value="进鑫门业（自动化测试）改"',newName_ele)

        supplier_newName_input.send_keys('进鑫门业（自动化测试）改')
        INFO(supplier_newName_input.get_attribute('outerHTML'))
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]/span').click()
        submit = driver.find_element_by_css_selector('div.ant-modal-footer > button.ant-btn.ant-btn-primary > span')
        submit.click()
        time.sleep(5)

        STEP(4, '检查能否筛选到新的公司名称')
        screen(driver=driver, supplierName='进鑫门业（自动化测试）改')
        # 列表第一行的供应商名称字段
        list_one_supplierName_ele = driver.find_element_by_css_selector(
            'td:nth-child(3) > button > span')
        list_one_supplierName = list_one_supplierName_ele.text
        CHECK_POINT('检查新的名称', list_one_supplierName == '进鑫门业（自动化测试）改')

        STEP(5, '打开变更日志页面')
        # 列表第一行的供应商名称字段
        # list_one_supplierName_ele = driver.find_element_by_xpath(
        #     '//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]/button/span')
        list_one_supplierName_ele.click()
        time.sleep(3)
        # 名称变更日志入口按钮
        change_log = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/button/span')
        change_log.click()
        time.sleep(5)
        # # 日志列表最后一行
        # log_list_last0 = driver.find_elements_by_xpath(
        #     '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr[last()-0]/td')
        # 日志列表第一行
        log_list_last0 = driver.find_elements_by_xpath(
                '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td')
        texts = [txt.text for txt in log_list_last0]
        del texts[2]
        # CHECK_POINT('检查日志最近一次变更内容是否正确', texts == ['供应商自动化测试账号勿改','进鑫门业（自动化测试）退->进鑫门业（自动化测试）改', '自动化测试-修改名称改'])
        CHECK_POINT('检查日志最近一次变更内容是否正确', texts == ['麻小', '进鑫门业（自动化测试）->进鑫门业（自动化测试）改', '自动化测试修改名称'])

        STEP(6, '返回名称变更页，并改回原名称')
        # 变更日志页面关闭按钮
        time.sleep(3)
        # log_close = driver.find_element_by_css_selector('span.ant-modal-close-x')
        log_close = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button/span')
        INFO(log_close.get_attribute('outerHTML'))
        time.sleep(3)
        log_close.click()
        time.sleep(2)
        # 名称变更页新名称输入框
        supplier_newName_input = driver.find_element_by_css_selector('div > span > #supplierName')
        supplier_newName_input.send_keys('进鑫门业（自动化测试）退')
        time.sleep(3)
        # 名称变更页保存按钮
        submit = driver.find_element_by_css_selector('div.ant-modal-footer > button.ant-btn.ant-btn-primary > span')
        submit.click()
        time.sleep(3)

class c1203:
    name = '信息管理页 - UI-1203'

    def teststeps(self):
        driver = get_driver()

        STEP(1, '筛选 进鑫门业（自动化测试）退')
        screen(driver=driver, supplierName='进鑫门业（自动化测试）退')

        STEP(2, '打开供应商采销变更页')
        # 列表第一行数据的采销页入口
        manager_entry = driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[7]/a')
        manager_entry.click()
        time.sleep(3)

        STEP(3, '新增一个采销=麻小采销')
        # 采销新增按钮
        # manager_add = driver.find_element_by_xpath(
        #     '//*[@id="app"]/section/section/main/div[2]/div[1]/div/button[1]')
        manager_add = driver.find_element_by_css_selector('button.ant-btn.ant-btn-primary > span')
        INFO(manager_add.text)
        INFO(manager_add.get_attribute('outerHTML'))
        # driver.execute_script('arguments[0].click()', manager_add)
        manager_add.click()
        time.sleep(3)
        # 采销新增输入框
        managerName_input = driver.find_element_by_xpath('//*[@id="managerNo"]')
        managerName_input.send_keys('麻小采销')
        time.sleep(3)
        managerName_input.send_keys(Keys.ENTER)
        time.sleep(3)
        #点击搜索出来的 麻小采销 负责人
        # driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div/div').click()
        # 采销关联类目输入框
        # category_input = driver.find_element_by_xpath(
            # '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/span/span/span[1]')
        category_input = driver.find_element_by_css_selector('div.ant-col.ant-col-16.ant-legacy-form-item-control-wrapper > div > span > span')
        INFO(category_input.get_attribute('outerHTML'))
        category_input.click()
        time.sleep(2)
        #选择弹出来的第二个类目 食品酒水
        # driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[2]').click()
        shipin = driver.find_element_by_css_selector('div > div > ul > li:nth-child(2)')
        INFO(shipin.get_attribute('outerHTML'))
        shipin.click()
        time.sleep(2)
        category_input = driver.find_element_by_css_selector(
            'div.ant-col.ant-col-16.ant-legacy-form-item-control-wrapper > div > span > span')
        time.sleep(2)
        category_input.click()
        time.sleep(2)
        #选择弹出来的第三个类目 孕婴用品
        # driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[3]').click()
        yunyin = driver.find_element_by_css_selector('div > div > ul > li:nth-child(3)')
        INFO(yunyin.get_attribute('outerHTML'))
        yunyin.click()
        # 新增采销负责人保存按钮
        # manager_add_submit = driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]/span')
        manager_add_submit = driver.find_element_by_css_selector('div.ant-modal-footer > button.ant-btn.ant-btn-primary > span')
        manager_add_submit.click()
        time.sleep(3)
        # 采销列表最后一行
        manager_list_last0 = driver.find_elements_by_xpath(
            '//*[@id="app"]/section/section/main/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[last()-0]/td')

        manager_list_last0_texts = [txt.text for txt in manager_list_last0]
        INFO(manager_list_last0_texts)
        CHECK_POINT('检查最近新增的采销是否正确', manager_list_last0_texts == ['2', '麻小采销', '食品酒水;孕婴用品', '界面新增', '编辑删除'])

        STEP(4, '删除新增的采销,并返回信息管理列表')
        driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[5]/button[2]/span').click()
        time.sleep(2)
        driver.find_element_by_css_selector('div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary > span').click()
        # 采销列表返回按钮
        time.sleep(2)
        manager_list_back = driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div[2]/div[3]/button/span')
        manager_list_back.click()

class c1204:
    name = '信息管理页 - UI-1204'

    def teststeps(self):
        driver = get_driver()

        STEP(1, '筛选 进鑫门业（自动化测试）退')
        screen(driver=driver, supplierName='进鑫门业（自动化测试）退')

        STEP(2, '重置密码')
        #重置密码按钮
        password_reset = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[11]/a[1]')
        password_reset.click()
        time.sleep(2)
        #确认按钮
        # reset_yes = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]/span')
        reset_yes = driver.find_element_by_css_selector('div.ant-modal-footer > button.ant-btn.ant-btn-primary > span')
        reset_yes.click()
        time.sleep(2)
        #重置成功文案
        # reset_text = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/span').text
        reset_text = driver.find_element_by_css_selector('div.ant-result-title > span').text
        INFO(reset_text)
        CHECK_POINT('检查是否出现密码重置成功文案', '密码重置成功' in reset_text)

        STEP(3, '返回信息管理列表')
        #完成按钮
        # driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button/span').click()
        driver.find_element_by_css_selector('div.ant-modal-footer > button > span').click()
class c1205:
    name = '信息管理页 - UI-1205'

    def teststeps(self):
        driver = get_driver()

        STEP(1, '筛选 进鑫门业（自动化测试）退')
        screen(driver=driver, supplierName='进鑫门业（自动化测试）退')

        STEP(2, '停用供应商')
        #点击停用按钮
        stop_enable_button = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[11]/a[2]')
        stop_enable_button.click()
        time.sleep(2)
        #点击确认按钮
        # stop_enable_yes = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span')
        stop_enable_yes = driver.find_element_by_css_selector('div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary > span')
        stop_enable_yes.click()
        time.sleep(3)
        #获取启用按钮文案
        stop_enable_button = driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[11]/a[2]')
        enable_text = stop_enable_button.text
        INFO(enable_text)
        CHECK_POINT('检查停用按钮是否变成启用', enable_text == '启用')

        STEP(3, '启用供应商')
        stop_enable_button.click()
        time.sleep(2)
        # 点击确认按钮
        stop_enable_yes = driver.find_element_by_css_selector('div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary > span')
        stop_enable_yes.click()
        time.sleep(3)
        stop_enable_button = driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[11]/a[2]')
        enable_text = stop_enable_button.text
        INFO(enable_text)
        CHECK_POINT('检查启用按钮是否变成停用', enable_text == '停用')