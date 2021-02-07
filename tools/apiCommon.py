from ywyrobot.common import *
from tools.mysql import mysql
from lib.login import Login
from cfg import Global
import json
from tools.HttpUtil import HttpUtil

class apiCommon():
    def get_response(self, testId, isCheckSucces=True):
        '''
        获取接口返回结果，然后取出其中的data并返回；
        获取testid的数据库数据，然后去除其中data并返回
        :param testId:
        :return:
        '''
        ret = mysql().getOrderUpdatedAt(testId)
        testPath = ret[0].get('testPath')
        interface = ret[0].get('interface')
        testParams = ret[0].get('testParams')
        method = ret[0].get('method')
        testResp = ret[0].get('testResp')
        check_point_list = ret[0].get('check_point')
        remark = ret[0].get('remark')
        url = testPath + interface
        testResp = json.loads(testResp)

        response = self.reponse(method,url,testParams,remark)

        if isCheckSucces == True:
            self.check_common(response, isCheckSucces)
        elif isCheckSucces == False:
            self.check_common(response, isCheckSucces)
        else:
            INFO('isCheckSucces  传值异常')

        paramdict = {}
        paramdict['resData'] = response.get('data')
        paramdict['testData'] = testResp.get('data')
        paramdict['check_point_list'] = check_point_list
        return paramdict

    def getResponse(self,testId):
        '''
        获取接口返回的数据，并直接返回response
        :return:
        '''
        ret = mysql().getOrderUpdatedAt(testId)
        testPath = ret[0].get('testPath')
        interface = ret[0].get('interface')
        testParams = ret[0].get('testParams')
        method = ret[0].get('method')
        remark = ret[0].get('remark')
        url = testPath + interface
        response = self.reponse(method,url,testParams,remark)
        return response

    def reponse(self, method, url, testParams, remark):
        if method == 'get':
            url = url + '?' + testParams
            response = HttpUtil().get_request(url=url, headers=Global.Headers_yun)
        elif method == 'post':
            testParams = testParams.encode()
            response = HttpUtil().post_request(url=url,postdata=testParams, headers=Global.Headers_yun)
        elif method == 'post+file':
            response = HttpUtil().post_upload(url=url, postdata=testParams, headers=Global.Headers_yun)
        else:
            response = '请检查下method字段:  ' + method
            pass
        return response

    def get_respDict(self,testId):
        ret = mysql().getOrderUpdatedAt(testId)
        testPath = ret[0].get('testPath')
        interface = ret[0].get('interface')
        testParams = ret[0].get('testParams')
        method = ret[0].get('method')
        testResp = ret[0].get('testResp')
        check_point_list = ret[0].get('check_point')
        remark = ret[0].get('remark')
        url = testPath + interface
        testResp = json.loads(testResp)

        response = self.reponse(method,url,testParams,remark)

        paramdict = {}
        paramdict['resp'] = response
        paramdict['testResp'] = testResp
        return paramdict

    def check_all(self,testId):
        respDict = apiCommon().get_respDict(testId)
        resp = respDict.get('resp')
        testResp = respDict.get('testResp')
        CHECK_POINT('检查两边的response相等', resp == testResp)
        return resp

    def check_common(self,response,isCheckSucces=True):
        success = response.get('success')
        if isCheckSucces == True:
            CHECK_POINT('检查接口的success', success == True)
        elif isCheckSucces == False:
            CHECK_POINT('检查接口的success', success == False)
        else:
            INFO('isCheckSucces发生异常')


    def check_success(self,testId):
        response = self.getResponse(testId)
        success = response.get('success')
        CHECK_POINT('检查接口的success', success == True)
        return response

    def check_false(self,testId):
        response = self.getResponse(testId)
        success = response.get('success')
        CHECK_POINT('检查接口的success', success == False)



    def check_data(self,testId,isCheckSucces=True):
        paramdict = apiCommon().get_response(testId, isCheckSucces)
        resData = paramdict.get('resData')
        testData = paramdict.get('testData')
        check_point_list = paramdict.get('check_point_list')
        if check_point_list == '':
            CHECK_POINT('检查点： ' + str(testData) + '返回的数据： ' + str(resData), resData == testData)
        else:
            check_point_list = eval(check_point_list)
            for check_point in check_point_list:
                # check_point = {
                #     'first_param__name': 'list',
                #     'second_param__name': 0,
                #     'third_param__name': 'name'
                # }
                apiCommon().check_branch(resData, testData, check_point=check_point)

    def check_branch(self,resData,testData,check_point=None):
        param_type = type(check_point)
        if param_type == dict:
            # print('是字典')
            first_param__name = check_point.get('first_param__name')
            second_param__name = check_point.get('second_param__name')
            if type(second_param__name) == str:
                res_param = testData.get(first_param__name).get(second_param__name)
                test_param = testData.get(first_param__name).get(second_param__name)
            elif type(second_param__name) == int:
                third_param__name = check_point.get('third_param__name')
                res_param = testData.get(first_param__name)[second_param__name].get(third_param__name)
                test_param = testData.get(first_param__name)[second_param__name].get(third_param__name)
            else:
                res_param = 'res_param参数异常：  second_param__name传值错误  当前类型为  ' + type(second_param__name)
                test_param = 'test_param参数异常：  second_param__name传值错误  当前类型为  ' + type(second_param__name)
        elif param_type == str:
            # print('是字符串')
            res_param = testData.get(check_point)
            test_param = testData.get(check_point)
        else:
            res_param = 'res_param参数异常：  check_point传值错误  当前类型为  ' + param_type
            test_param = 'test_param参数异常：  check_point传值错误  当前类型为  ' + param_type
            # print('异常')

        CHECK_POINT('检查点： ' + str(check_point) + '返回的数据： ' + str(res_param), res_param == test_param)
if __name__ == "__main__":
    check_point = {
        'a': '1',
        'b': '2'
    }
    # check_point = []
    # check_point = ''
    print(type(check_point))
    apiCommon().check_data(check_point)