from ywyrobot.common import *
from lib.webCommon import webCommon
import time

def suite_setup():
    INFO('进入入驻审核页')
    driver = webCommon().get_global_webdriver()
    inAudit = driver.find_element_by_xpath("//a[@href='#/supplyManage/inAudit']")
    inAudit.click()


class c1101:
    # 测试用例名字
    name = '入驻审核页 - UI-1101'

    # 测试用例步骤
    def teststeps(self):
        driver = webCommon().get_global_webdriver()
        STEP(1, '筛选 进鑫门业有限公司（测试）')
        companyName = driver.find_element_by_xpath('//*[@id="name"]')
        companyName.send_keys('进鑫门业有限公司（测试）')
        INFO(companyName.get_attribute('outerHTML'))
        screen = driver.find_element_by_xpath('//*[@type="submit"]')
        INFO(screen.text)
        screen.click()
        time.sleep(5)

        STEP(2, '检查筛选结果')
        data = driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]')
        result_01 = data.find_element_by_xpath('td[1]').text
        result_02 = driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div[2]/div[2]/div/div/div/ul/li[1]').text
        results = [result_01, result_02]
        INFO(result_01 + result_02)
        CHECK_POINT('筛选结果是否正确', results == ['进鑫门业有限公司（测试）', '共 1 条记录'])

        STEP(3, '导出筛选结果')
        export = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[2]/div[1]/div[2]/div/button[2]/span')
        export.click()
        time.sleep(10)


