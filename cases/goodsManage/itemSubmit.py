from ywyrobot.common import *
from tools.apiCommon import apiCommon
from tools.mysql import mysql
from tools.HttpUtil import HttpUtil
import json
from lib.goodsCommon import goodsCommon

force_tags = ['供应商内部端','商品提报']

class a2201:
    # 测试用例名字
    name = 'SPU申请提报 - API-2201'

    # 测试用例步骤
    def teststeps(self):
        STEP(1, 'SPU编号申请提报-SPU编号不存在')
        testId = 'API-2201-01'
        apiCommon().check_data(testId=testId,isCheckSucces=False)

        STEP(2, '国际码申请提报-国际码不存在')
        testId = 'API-2201-02'
        apiCommon().check_data(testId=testId,isCheckSucces=False)

        STEP(3, 'SPU编号申请提报-SPU编号存在')
        testId = 'API-2201-03'
        apiCommon().check_data(testId)

        STEP(4, '国际码申请提报-国际码存在')
        testId = 'API-2201-04'
        apiCommon().check_data(testId)

        STEP(5, '申请提报失败-重复提报')
        testId = 'API-2201-05'
        apiCommon().check_data(testId=testId,isCheckSucces=False)

class  a2202:
    name = '查询不可销售平台 - API-2202'
    def teststeps(self):
        STEP(1,'查询不可销售平台')
        testId = 'API-2202-01'
        apiCommon().check_data(testId)

class  a2203:
    name = '查询sku优惠方式 - API-2203'
    def teststeps(self):
        STEP(1,'查询sku优惠方式')
        testId = 'API-2203-01'
        apiCommon().check_data(testId)

class  a2204:
    name = '检查非寄售 - API-2204'
    def teststeps(self):
        STEP(1,'检查非寄售')
        testId = 'API-2204-01'
        apiCommon().check_data(testId)

class  a2205:
    name = '创建提报-成功创建 - API-2205'
    def teststeps(self):
        STEP(1, '检查测试数据纯净，若有脏数据，删之')
        ret = goodsCommon().for_del_submit('自动化商品提报2021-02-07（勿动）')
        INFO(ret)

        STEP(2,'创建提报-成功创建')
        testId = 'API-2205-01'
        apiCommon().check_data(testId)

class  a2206:
    name = '撤回提报 - API-2206'
    def teststeps(self):
        STEP(1,'获取待撤回的提报记录')
        testId = 'API-2206-01'
        submitUniqueNo_list = goodsCommon().get_submitUniqueNo('自动化商品提报2021-02-07（勿动）')

        STEP(2,'更新用例的testParams')
        testParams = 'submitUniqueNo=' + submitUniqueNo_list[0]
        mysql().updateSQL_interface(testId=testId,testParams=testParams)

        STEP(3,'执行用例，撤回提报')
        apiCommon().check_data(testId)

        STEP(4,'撤回提报失败（已选品通过）')
        testId = 'API-2206-02'
        apiCommon().check_data(testId=testId,isCheckSucces=False)

class  a2207:
    name = '删除提报 - API-2207'
    def teststeps(self):
        STEP(1,'获取待删除的提报记录')
        testId = 'API-2207-01'
        submitUniqueNo_list = goodsCommon().get_submitUniqueNo('自动化商品提报2021-02-07（勿动）')

        STEP(2, '更新用例的testParams')
        testParams = 'submitUniqueNo=' + submitUniqueNo_list[0]
        mysql().updateSQL_interface(testId=testId, testParams=testParams)

        STEP(3,'执行用例，删除提报')
        apiCommon().check_data(testId)

class  a2208:
    name = '查询提报列表 - API-2208'
    def teststeps(self):
        STEP(1,'查询提报列表')
        testId = 'API-2208-01'
        apiCommon().check_data(testId)

class  a2209:
    name = '查询提报详情 - API-2209'
    def teststeps(self):
        STEP(1,'查询提报详情')
        testId = 'API-2209-01'
        apiCommon().check_data(testId)

class  a2210:
    name = '提报-编辑详情页 - API-2210'
    def teststeps(self):
        STEP(1,'提报-编辑详情页')
        testId = 'API-2210-01'
        apiCommon().check_data(testId)

class  a2211:
    name = '商品链接解析店铺上架编码 - API-2211'
    def teststeps(self):
        STEP(1,'商品链接解析店铺上架编码')
        testId = 'API-2211-01'
        apiCommon().check_data(testId)

class  a2212:
    name = '导入创建+提报模板 - API-2212'
    def teststeps(self):
        STEP(1,'导入创建+提报模板')
        testId = 'API-2212-01'
        apiCommon().check_data(testId)

        STEP(2,'撤回并删除提报记录')
        ret = goodsCommon().for_del_submit('自动化导入创建商品00')
        INFO(ret)

        STEP(3, '导入提报模板')
        testId = 'API-2212-02'
        apiCommon().check_data(testId)

        STEP(4, '撤回并删除提报记录')
        ret = goodsCommon().for_del_submit('自动化导入创建商品00')
        INFO(ret)

        STEP(5, '删除商品')
        ret = goodsCommon().for_del_item('自动化导入创建商品00')
        INFO(ret)

if __name__ == "__main__":
    a2201().teststeps()