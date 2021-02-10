from ywyrobot.common import *
from tools.mysql import mysql
from lib.login import Login
from cfg import Global
import json, random, time, string
from tools.HttpUtil import HttpUtil


class contracCommon():
    def updateContractNo(self):
        #获取新的合同编号
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 2))
        createtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        new_contractNo = 'TEST' + createtime + ran_str

        #获取老的合同编号
        testId_old = 'API-3207-01'
        ret = mysql().getOrderUpdatedAt(testId=testId_old)
        old_testParams = json.loads(ret[0].get('testParams'))
        old_contractNo = old_testParams.get('contractNo')

        #获取合同动作相关的用例数据
        ret_list = mysql().getOrderUpdatedAt(module='合同动作')
        testId_list = []
        for ret in ret_list:
            testParams = ret.get('testParams')
            testId = ret.get('testId')
            functionName = ret.get('function')
            #判断testParams字符串中不包含老的合同编号
            if testParams.find(old_contractNo) == -1:
                INFO(testId + functionName + '  未更新***该用例请求参数不包含该编号：' + old_contractNo)
            else:
                #替换掉老的合同编号
                INFO(testId + functionName + '  该用例请求参数的合同更新为新编号： ' + new_contractNo)
                testParams = testParams.replace(old_contractNo,new_contractNo)
                #更新数据库数据为新合同编号
                result = mysql().updateSQL_interface(testId=testId,testParams=testParams)
                testId_list.append(testId)
        check_testId_list = ['API-3207-01', 'API-3206-02', 'API-3206-01', 'API-3204-01', 'API-3203-01', 'API-3202-01', 'API-3201-01']
        CHECK_POINT('检查此次更新新合同编号的用例，此次更新了合同编号的用例有： ' + str(testId_list), testId_list == check_testId_list)
        return '此次进行更新合同编号的用例有： ' + str(testId_list)
if __name__ == "__main__":
    print(contracCommon().updateContractNo())