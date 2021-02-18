from ywyrobot.common import *
from tools.apiCommon import apiCommon

force_tags = ['供应商内部端','入驻审核页']


class a1101:
    # 测试用例名字
    name = '筛选 - API-1101'

    # 测试用例步骤
    def teststeps(self):
        STEP(1, '筛选 进鑫门业（自动化测试）')
        testId = 'API-1101-01'
        apiCommon().check_data(testId)

class a1102:
    name = '查询类目 - API-1102'
    def teststeps(self):
        STEP(1, "查询类目")
        testId = 'API-1102-01'
        apiCommon().check_data(testId)

class a1103:
    name = '查询供应商详情 - API-1103'
    def teststeps(self):
        STEP(1, "查询供应商详情")
        testId = 'API-1103-01'
        apiCommon().check_data(testId)

class a1104:
    name = '下载供应商资质附件 - API-1104'
    def teststeps(self):
        STEP(1, "下载供应商资质附件")
        testId = 'API-1104-01'
        apiCommon().check_success(testId)

class a1105:
    name = '导出供应商 - API-1105'
    def teststeps(self):
        STEP(1, "导出供应商")
        testId = 'API-1105-01'
        apiCommon().check_success(testId)

class a1106:
    name = '查询业务分组 - API-1106'
    def teststeps(self):
        STEP(1, "查询业务分组")
        testId = 'API-1106-01'
        apiCommon().check_data(testId)

class a1107:
    name = '查询采销 - API-1107'
    def teststeps(self):
        STEP(1, "查询采销")
        testId = 'API-1107-01'
        apiCommon().check_data(testId)

class a1108:
    name = '供应商入驻-资质图片上传 - API-1108'
    def teststeps(self):
        STEP(1, "供应商入驻-资质图片上传")
        testId = 'API-1108-01'
        apiCommon().check_data(testId)

if __name__ == "__main__":
    a1108().teststeps()