from ywyrobot.common import *
from tools.apiCommon import apiCommon
from tools.mysql import mysql

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

class  a1203:
    name = '变更供应商名称 - API-1203'
    def teststeps(self):
        STEP(1,'变更供应商名称 QY2021010100006')
        testId = 'API-1203-01'
        apiCommon().check_data(testId)

        STEP(2, '恢复供应商名称')
        testId = 'API-1203-02'
        apiCommon().check_data(testId)

class  a1204:
    name = '查询供应商的采销列表 - API-1204'
    def teststeps(self):
        STEP(1,'查询供应商的采销列表 QY2021010100006')
        testId = 'API-1204-01'
        apiCommon().check_data(testId)

class  a1205:
    name = '查询采销-post接口 - API-1205'
    def teststeps(self):
        STEP(1,'查询采销-post接口')
        testId = 'API-1205-01'
        apiCommon().check_data(testId)

class  a1206:
    name = '添加供应商采销 - API-1206'
    def teststeps(self):
        STEP(1,'添加供应商采销 QY2021010100006')
        testId = 'API-1206-01'
        apiCommon().check_data(testId)

        STEP(2, '重复添加供应商采销')
        testId = 'API-1206-02'
        apiCommon().check_data(testId,isCheckSucces=False)

class  a1207:
    name = '删除供应商采销 - API-1207'
    def teststeps(self):
        STEP(1, '获取当前采销列表中第二位采销的SMC编号 ')
        paramdict = apiCommon().get_response(testId='API-1204-01')
        resData = paramdict.get('resData')
        supplierManagerNo = resData.get('list')[1].get('supplierManagerNo')

        STEP(2, '将SRM编号拼接成新的interface，更新数据库')
        interface = '/admin/supplierManager/deleted/' + supplierManagerNo
        testId = 'API-1207-01'
        mysql().updateSQL_interface(testId,interface)

        STEP(3,'删除供应商采销 QY2021010100006')
        apiCommon().check_data(testId)

class  a1208:
    name = '查询采销变更日志 - API-1208'
    def teststeps(self):
        STEP(1,'查询供应商详情 QY2021010100006')
        testId = 'API-1208-01'
        apiCommon().check_data(testId)

class  a1209:
    name = '重置供应商密码 - API-1209'
    def teststeps(self):
        STEP(1,'重置供应商密码 QY2021010100006')
        testId = 'API-1209-01'
        apiCommon().check_data(testId)

class  a1210:
    name = '供应商账号停用 - API-1210'
    def teststeps(self):
        STEP(1,'供应商账号停用 QY2021010100006')
        testId = 'API-1210-01'
        apiCommon().check_data(testId)

        STEP(2, '供应商账号启用 QY2021010100006')
        testId = 'API-1210-02'
        apiCommon().check_data(testId)



if __name__ == "__main__":
    a1209().teststeps()