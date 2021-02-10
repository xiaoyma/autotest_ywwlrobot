from ywyrobot.common import *
from tools.apiCommon import apiCommon
from tools.mysql import mysql
from tools.HttpUtil import HttpUtil
import json
from lib.goodsCommon import goodsCommon
from lib.login import Login

force_tags = ['供应商','合同列表']

#用于合同模块
headers = {
    "x-token": Login().login_yun(userPhone='18316321174',userPasswd='123456')
}

class a3101:
    # 测试用例名字
    name = '查询乙方公司列表 - API-3101'

    # 测试用例步骤
    def teststeps(self):
        STEP(1, '查询乙方公司列表')
        testId = 'API-3101-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3102:
    name = '查询合同列表 - API-3102'
    def teststeps(self):
        STEP(1, '查询合同列表')
        testId = 'API-3102-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3103:
    name = '下载合同最新模板 - API-3103'
    def teststeps(self):
        STEP(1, '下载合同最新模板')
        testId = 'API-3103-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3104:
    name = '下载单个线上合同 - API-3104'
    def teststeps(self):
        STEP(1, '下载单个线上合同')
        testId = 'API-3104-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3105:
    name = '批量下载多个线上合同 - API-3105'
    def teststeps(self):
        STEP(1, '批量下载多个线上合同')
        testId = 'API-3105-01'
        apiCommon().check_success(testId=testId,headers=headers)

class a3106:
    name = '查询合同资质附件 - API-3106'
    def teststeps(self):
        STEP(1, '查询合同资质附件')
        testId = 'API-3106-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3107:
    name = '查询合同详情 - API-3107'
    def teststeps(self):
        STEP(1, '查询合同详情')
        testId = 'API-3107-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3108:
    name = '查询合同流程树 - API-3108'
    def teststeps(self):
        STEP(1, '查询合同流程树')
        testId = 'API-3108-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3109:
    name = '查询执行单-推广平台列表 - API-3109'
    def teststeps(self):
        STEP(1, '查询执行单-推广平台列表')
        testId = 'API-3109-01'
        apiCommon().check_data(testId=testId,headers=headers)

        STEP(2, '查询执行单-销售平台列表')
        testId = 'API-3109-02'
        apiCommon().check_data(testId=testId, headers=headers)

        STEP(3, '查询执行单-结算平台列表')
        testId = 'API-3109-03'
        apiCommon().check_data(testId=testId, headers=headers)

class a3110:
    name = '查询归档附件列表 - API-3110'
    def teststeps(self):
        STEP(1, '查询归档附件列表')
        testId = 'API-3110-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3111:
    name = '合同评论 - API-3111'
    def teststeps(self):
        STEP(1, '合同评论')
        testId = 'API-3102-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3112:
    name = '获取新的合同编号 - API-3112'
    def teststeps(self):
        STEP(1, '获取新的合同编号')
        testId = 'API-3112-01'
        apiCommon().check_success(testId=testId,headers=headers)

class a3113:
    name = '获取合同模板 - API-3113'
    def teststeps(self):
        STEP(1, '获取合同模板')
        testId = 'API-3113-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3114:
    name = '新增合同-获取关联合同 - API-3114'
    def teststeps(self):
        STEP(1, '新增合同-获取关联合同')
        testId = 'API-3114-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3115:
    name = '新增合同-获取甲方基本信息 - API-3115'
    def teststeps(self):
        STEP(1, '新增合同-获取甲方基本信息')
        testId = 'API-3115-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3116:
    name = '获取流程节点-一般合同 - API-3116'
    def teststeps(self):
        STEP(1, '获取流程节点-一般合同')
        testId = 'API-3116-01'
        apiCommon().check_data(testId=testId,headers=headers)

        STEP(2, '获取流程节点-重要合同')
        testId = 'API-3116-02'
        apiCommon().check_data(testId=testId, headers=headers)

        STEP(1, '获取流程节点-重大合同')
        testId = 'API-3116-03'
        apiCommon().check_data(testId=testId, headers=headers)

class a3117:
    name = '执行单推广信息下载 - API-3117'
    def teststeps(self):
        STEP(1, '执行单推广信息下载')
        testId = 'API-3117-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3118:
    name = '执行单-获取导入文件任务编号 - API-3118'
    def teststeps(self):
        STEP(1, '执行单-获取导入文件任务编号')
        testId = 'API-3118-01'
        ret = apiCommon().check_success(testId=testId,headers=headers)

        STEP(2,'更新API-3119-01用例的testParams的任务编号')
        taskNo = ret.get('data').get('taskNo')
        testParams = 'taskNo=' + taskNo
        testId = 'API-3119-01'
        ret = mysql().updateSQL_interface(testId=testId,testParams=testParams)
        INFO(ret)

class a3119:
    name = '执行单-获取导入文件信息 - API-3119'
    def teststeps(self):
        #与上一个用例存在关联
        STEP(1, '执行单-获取导入文件信息')
        testId = 'API-3119-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3120:
    name = '执行单查询主播 - API-3120'
    def teststeps(self):
        STEP(1, '执行单查询主播')
        testId = 'API-3120-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3121:
    name = '执行单查询商品名称 - API-3121'
    def teststeps(self):
        STEP(1, '执行单查询商品名称')
        testId = 'API-3121-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3122:
    name = '获取经理节点人选 - API-3122'
    def teststeps(self):
        STEP(1, '获取经理节点人选')
        testId = 'API-3122-01'
        apiCommon().check_data(testId=testId,headers=headers)

        STEP(2, '获取会计经理节点人选')
        testId = 'API-3122-02'
        apiCommon().check_data(testId=testId, headers=headers)

class a3123:
    name = '查询抄送人 - API-3123'
    def teststeps(self):
        STEP(1, '查询抄送人')
        testId = 'API-3123-01'
        apiCommon().check_data(testId=testId,headers=headers)

if __name__ == "__main__":
    a3123().teststeps()