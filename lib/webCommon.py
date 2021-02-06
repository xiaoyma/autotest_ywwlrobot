from ywyrobot.common import *
from selenium import webdriver

class webCommon():
    def open_browser(self):
        driver = webdriver.Chrome(r'D:\Program Files\webdrivers\chromedriver.exe')
        driver.implicitly_wait(10)
        #全局存储对象
        GSTORE['global_webdriver'] = driver
        return driver

    def get_global_webdriver(self):
        return GSTORE['global_webdriver']

    def login(self,driver):
        driver.get("https://yun.ywwl.com/login?projectId=PROSUPPLIER")
        driver.find_element_by_xpath("//input[@id='basic_userPhone']").send_keys("18800000000")
        driver.find_element_by_xpath("//input[@id='basic_userPasswd']").send_keys("123456")
        submit = driver.find_element_by_xpath("//button[@type='submit']")
        submit.click()

