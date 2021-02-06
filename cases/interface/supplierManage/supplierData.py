from ywyrobot.common import *
from tools.apiCommon import apiCommon

force_tags = ['供应商','信息管理页']


class a1201:
    # 测试用例名字
    name = '筛选 - API-1201'

    # 测试用例步骤
    def teststeps(self):
        STEP(1, '筛选 进鑫门业（自动化测试）退')
        testId = 'API-1201-01'
        apiCommon().check_data(testId)

class  a1202:
    name = '查询供应商详情 - API-1202'
    def teststeps(self):
        STEP(1,'查询供应商详情 QY2021010100006')
        testId = 'API-1202-01'
        apiCommon().check_data(testId)





if __name__ == "__main__":
    a1202().teststeps()