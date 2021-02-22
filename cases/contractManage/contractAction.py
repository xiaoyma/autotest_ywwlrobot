from ywyrobot.common import *
from tools.apiCommon import apiCommon
from tools.mysql import mysql
from tools.HttpUtil import HttpUtil
import json
from lib.goodsCommon import goodsCommon
from lib.login import Login
from lib.contracCommon import contracCommon
from cfg import Global

force_tags = ['供应商内部端','合同相关动作']

#用于合同模块
headers = {
    "x-token": Login().login_yun(userPhone='18316321174',userPasswd='123456', url=Global.login_yun_url)
}

class a3201:
    # 测试用例名字
    name = '暂存线上合同（框架+执行单） - API-3201'

    # 测试用例步骤
    def teststeps(self):
        STEP(1, '更新数据库中的合同编号')
        contracCommon().updateContractNo()

        STEP(2, '暂存线上合同（框架+执行单）')
        testId = 'API-3201-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3202:
    name = '暂存-提交审核线上合同（框架+执行单） - API-3202'
    def teststeps(self):
        STEP(1, '暂存-提交审核线上合同（框架+执行单）')
        testId = 'API-3202-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3203:
    name = '撤回合同 - API-3203'
    def teststeps(self):
        STEP(1, '撤回合同')
        testId = 'API-3203-01'
        apiCommon().check_data(testId=testId,headers=headers)

        STEP(2, '重新提交合同')
        testId = 'API-3202-01'
        apiCommon().check_data(testId=testId, headers=headers)

class a3204:
    name = '查询当前审批节点 - API-3204'
    def teststeps(self):
        STEP(1, '查询当前审批节点')
        testId = 'API-3204-01'
        response = apiCommon().check_success(testId=testId,headers=headers)

class a3205:
    name = '催办 - API-3205'
    def teststeps(self):
        STEP(1, '催办')
        testId = 'API-3205-01'
        apiCommon().check_data(testId=testId,headers=headers)

        STEP(2, '催办-10分内重复催办')
        testId = 'API-3205-02'
        apiCommon().check_data(testId=testId, headers=headers ,isCheckSucces=False)

class a3206:
    name = '审核通过 - API-3206'
    def teststeps(self):
        STEP(1, '获取当前审批节点')
        testId = 'API-3204-01'
        response = apiCommon().check_success(testId=testId, headers=headers)
        nodeNo = response.get('data').get('nodeNo')

        STEP(2, '更新审核通过用例的审批节点')
        #获取审核通过用例的请求参数
        testId = 'API-3206-01'
        ret = mysql().getOrderUpdatedAt(testId)
        testParams = json.loads(ret[0].get('testParams'))
        testParams['nodeNo'] = nodeNo
        testParams = json.dumps(testParams)
        ret = mysql().updateSQL_interface(testId=testId,testParams=testParams)
        INFO(ret)

        STEP(3, '执行审核通过')
        apiCommon().check_data(testId=testId,headers=headers)

        STEP(4, '再次获取当前审批节点')
        testId = 'API-3204-01'
        response = apiCommon().check_success(testId=testId, headers=headers)
        nodeNo = response.get('data').get('nodeNo')

        STEP(5, '更新审核驳回用例的审批节点')
        # 获取审核通过用例的请求参数
        testId = 'API-3206-02'
        ret = mysql().getOrderUpdatedAt(testId)
        testParams = json.loads(ret[0].get('testParams'))
        testParams['nodeNo'] = nodeNo
        testParams = json.dumps(testParams)
        ret = mysql().updateSQL_interface(testId=testId,testParams=testParams)
        INFO(ret)

        STEP(6, '执行审核驳回')
        # 用于审核驳回
        headers_nixing = {
            "x-token": Login().login_yun(userPhone='13732237699',userPasswd='123456', url=Global.login_yun_url)
        }
        apiCommon().check_data(testId=testId, headers=headers_nixing)

class a3207:
    name = '删除合同 - API-3207'
    def teststeps(self):
        STEP(1, '删除合同')
        testId = 'API-3207-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3208:
    name = '申请归档 - API-3208'
    def teststeps(self):
        STEP(1, '申请归档')
        testId = 'API-3208-01'
        apiCommon().check_data(testId=testId,headers=headers)

class a3209:
    name = '驳回归档申请 - API-3209'
    def teststeps(self):
        STEP(1, '驳回归档申请')
        testId = 'API-3209-01'
        apiCommon().check_data(testId=testId,headers=headers)


if __name__ == "__main__":
    a3209().teststeps()