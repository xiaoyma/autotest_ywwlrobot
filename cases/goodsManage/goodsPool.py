from ywyrobot.common import *
from tools.apiCommon import apiCommon
from tools.mysql import mysql
from tools.HttpUtil import HttpUtil
import json
from lib.goodsCommon import goodsCommon

force_tags = ['供应商内部端','商家商品池']


class a2101:
    # 测试用例名字
    name = '查询商品列表 - API-2101'

    # 测试用例步骤
    def teststeps(self):
        STEP(1, '查询商品列表')
        testId = 'API-2101-01'
        apiCommon().check_data(testId)

class  a2102:
    name = '查询商品名称为不重复 - API-2102'
    def teststeps(self):
        STEP(1, '检查环境数据，存在脏数据删之')
        ret = goodsCommon().for_del_item('自动化测试-商品创建与删除')
        INFO(ret)

        STEP(2,'查询商品名称为不重复')
        testId = 'API-2102-01'
        apiCommon().check_data(testId)

        STEP(3, '查询商品名称为重复')
        testId = 'API-2102-02'
        apiCommon().check_data(testId)

class  a2103:
    name = '创建商品-查询供应商 - API-2103'
    def teststeps(self):
        STEP(1,'创建商品-查询供应商')
        testId = 'API-2103-01'
        apiCommon().check_data(testId)

class  a2104:
    name = '创建商品-校验国际码为不重复 - API-2104'
    def teststeps(self):
        STEP(1, '检查环境数据，存在脏数据删之')
        ret = goodsCommon().for_del_item('自动化测试-商品创建与删除')
        INFO(ret)

        STEP(2,'创建商品-校验国际码为不重复')
        testId = 'API-2104-01'
        apiCommon().check_data(testId)

        STEP(3, '创建商品-校验国际码为重复')
        testId = 'API-2104-02'
        apiCommon().check_data(testId)

class  a2105:
    name = '创建商品 - API-2105'
    def teststeps(self):
        STEP(1, '检查环境数据，存在脏数据删之')
        ret = goodsCommon().for_del_item('自动化测试-商品创建与删除')
        INFO(ret)

        STEP(2,'创建商品')
        testId = 'API-2105-01'
        response = apiCommon().check_success(testId)

        STEP(3, '将创建的商品编号存进删除用例的testParams中')
        itemNo = response.get('data').get('itemNo')
        testParams = json.dumps({"no": itemNo})
        testId = 'API-2106-01'
        ret = mysql().updateSQL_interface(testId=testId, testParams=testParams)
        INFO(ret)

class  a2106:
    name = '删除商品 - API-2106'
    def teststeps(self):
        STEP(1,'删除商品')
        testId = 'API-2106-01'
        apiCommon().check_data(testId)

class  a2107:
    name = '类目品牌查询 - API-2107'
    def teststeps(self):
        STEP(1,'类目品牌查询')
        testId = 'API-2107-01'
        apiCommon().check_data(testId)

class  a2108:
    name = '查询商品详情 - API-2108'
    def teststeps(self):
        STEP(1,'查询商品详情')
        testId = 'API-2108-01'
        apiCommon().check_data(testId)

class  a2109:
    name = '商品导出 - API-2109'
    def teststeps(self):
        STEP(1,'商品导出')
        testId = 'API-2109-01'
        apiCommon().check_success(testId)

class  a2110:
    name = '查询批量创建模板下载地址 - API-2110'
    def teststeps(self):
        STEP(1,'查询批量创建模板下载地址')
        testId = 'API-2110-01'
        apiCommon().check_data(testId)

        STEP(2, '查询批量提报模板下载地址')
        testId = 'API-2110-02'
        apiCommon().check_data(testId)

        STEP(3, '查询批量创建+提报模板下载地址')
        testId = 'API-2110-03'
        apiCommon().check_data(testId)

class  a2111:
    name = '商品创建-模板导入成功 - API-2111'
    def teststeps(self):
        STEP(1,'商品创建-模板导入成功')
        testId = 'API-2111-01'
        apiCommon().check_data(testId)

        STEP(2, '商品创建-模板导入失败（重复导入）')
        testId = 'API-2111-02'
        apiCommon().check_data(testId)

        STEP(3, '删除创建的商品')
        ret = goodsCommon().for_del_item('自动化导入创建商品00')
        INFO(ret)

class  a2112:
    name = '商品创建-图片上传 - API-2112'
    def teststeps(self):
        STEP(1,'商品创建-图片上传')
        testId = 'API-2112-01'
        apiCommon().check_data(testId)

if __name__ == "__main__":
    a2105().teststeps()