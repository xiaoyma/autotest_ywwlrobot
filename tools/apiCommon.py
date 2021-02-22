from ywyrobot.common import *
from tools.mysql import mysql
from lib.login import Login
from cfg import Global
import json
from tools.HttpUtil import HttpUtil

class apiCommon():
    def get_response(self, testId, headers=Global.Headers_yun):
        '''
        获取接口返回结果，然后取出其中的各类参数，去请求接口，这里顺带校验了下接口返回的success值
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

        response = self.reponse(method,url,testParams,remark,headers)

        paramdict = {}
        paramdict['response'] = response
        paramdict['testResp'] = testResp
        paramdict['check_point_list'] = check_point_list

        # self.check_common(response,isCheckSucces)
        #
        # paramdict = {}
        # paramdict['resData'] = response.get('data')
        # paramdict['testData'] = testResp.get('data')
        # paramdict['check_point_list'] = check_point_list
        return paramdict

    def getResponse(self,testId,headers=Global.Headers_yun):
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
        response = self.reponse(method,url,testParams,remark,headers)
        return response

    def reponse(self, method, url, testParams, remark, headers=Global.Headers_yun):
        '''
        传入相关的url,请求方式，token等等参数，去请求接口，并返回response
        :param method:
        :param url:
        :param testParams:
        :param remark:
        :param headers:
        :return:
        '''
        if method == 'get':
            url = url + '?' + testParams
            response = HttpUtil().get_request(url=url, headers=headers)
        elif method == 'post':
            testParams = testParams.encode()
            response = HttpUtil().post_request(url=url,postdata=testParams, headers=headers)
        elif method == 'post+file':
            response = HttpUtil().post_upload(url=url, postdata=testParams, headers=headers)
        else:
            response = '请检查下method字段:  ' + method
            pass
        return response

    def get_respDict(self,testId,headers=Global.Headers_yun):
        '''
        取数据库的参数去请求接口，并把整个response和数据库存的testResp统一放在一个字典内，并return
        :param testId:
        :param headers:
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

        response = self.reponse(method,url,testParams,remark,headers)

        paramdict = {}
        paramdict['resp'] = response
        paramdict['testResp'] = testResp
        return paramdict

    def check_all(self,testId,headers=Global.Headers_yun):
        '''
        校验整个response与数据库中的testResp是否相等，适用于接口返回值固定的接口
        :param testId:
        :param headers:
        :return:
        '''
        respDict = apiCommon().get_respDict(testId, headers)
        resp = respDict.get('resp')
        testResp = respDict.get('testResp')
        CHECK_POINT('检查两边的response相等', resp == testResp)
        return resp

    def check_common(self,response,isCheckSucces=True):
        '''
        根据传入的isCheckSucces判断，校验response中succese的值为True还是False
        :param response:
        :param isCheckSucces: 传True,或者传False
        :return:
        '''
        success = response.get('success')
        if isCheckSucces == True:
            CHECK_POINT('检查接口的success，数据返回：' + str(response), success == True)
        elif isCheckSucces == False:
            CHECK_POINT('检查接口的success，数据返回：' + str(response), success == False)
        else:
            INFO('isCheckSucces发生异常，数据返回：' + str(response))


    def check_success(self,testId,headers=Global.Headers_yun):
        '''
        仅校验response的success为Ture
        :param testId:
        :param headers:
        :return:
        '''
        response = self.getResponse(testId,headers)
        success = response.get('success')
        CHECK_POINT('检查接口的success，数据返回：' + str(response), success == True)
        return response

    def check_false(self,testId,headers=Global.Headers_yun):
        '''
        仅校验response的success为False
        :param testId:
        :param headers:
        :return:
        '''
        response = self.getResponse(testId,headers)
        success = response.get('success')
        CHECK_POINT('检查接口的success，数据返回：' + str(response), success == False)



    def check_data(self,testId,isCheckSucces=True,headers=Global.Headers_yun):
        '''
        校验response和testParams中的data部分数据是否相等
        :param testId:
        :param isCheckSucces:默认校验接口的success == True ,传False则校验success == False
        :param headers:
        :return:
        '''
        paramdict = apiCommon().get_response(testId,headers)
        response = paramdict.get('response')
        testResp = paramdict.get('testResp')
        check_point_list = paramdict.get('check_point_list')
        #先校验下succsess
        self.check_common(response, isCheckSucces)
        if check_point_list == '':
            #校验整个response与testResp相等
            CHECK_POINT('检查点： ' + str(testResp) + '\n****** 返回的数据  ******： ' + str(response), response == testResp)
        else:
            #校验整个response与testResp内的Data部分内容
            resData = response.get('data')
            testData = testResp.get('data')
            check_point_list = eval(check_point_list)
            for check_point in check_point_list:
                # check_point = {
                #     'first_param__name': 'list',
                #     'second_param__name': 0,
                #     'third_param__name': 'name'
                # }
                apiCommon().check_branch(resData, testData, check_point=check_point)

    def check_branch(self,resData,testData,check_point=None):
        '''
        根据check_point中的值，判断是校验整个data数据，还是校验data下的一级字段，还是校验data下的二级字段
        :param resData: respoonse中的整个data数据
        :param testData: testResp中的整个data数据
        :param check_point: 可传入srt， dict，srt 则校验resData和testData中的一级字段，dict  则校验resData和testData中的二级或三级字段
        :return:
        '''
        param_type = type(check_point)
        if param_type == dict:

            # print('是字典')
            first_param__name = check_point.get('first_param__name')
            second_param__name = check_point.get('second_param__name')
            if type(second_param__name) == str:
                '''
                    实例：
                    数据库存的check_point = [{'first_param__name': 'fileDetail','second_param__name': 'uploadFileName'},{'first_param__name': 'list','second_param__name': 'FileUrl'}]，分别取出的值均为dict,但只有二级字段
                    会分别校验resData和testData中data['fileDetail']['uploadFileName']字段和data['fileDetail']['FileUrl']的值是否相等
                '''
                res_param = resData.get(first_param__name).get(second_param__name)
                test_param = testData.get(first_param__name).get(second_param__name)
            elif type(second_param__name) == int:
                '''
                    实例：
                    数据库存的check_point = [{'first_param__name': 'list','second_param__name': 0,'third_param__name': 'uploadFileName'},{'first_param__name': 'list','second_param__name': 0,'third_param__name': 'FileUrl'}]，分别取出的值均为dict，且有三级字段
                    会分别校验resData和testData中data['list'][0]['uploadFileName']字段和data['list'][0]['FileUrl']的值是否相等
                '''
                third_param__name = check_point.get('third_param__name')
                res_param = resData.get(first_param__name)[second_param__name].get(third_param__name)
                test_param = testData.get(first_param__name)[second_param__name].get(third_param__name)
            else:
                res_param = 'res_param参数异常：  second_param__name传值错误  当前类型为  ' + type(second_param__name)
                test_param = 'test_param参数异常：  second_param__name传值错误  当前类型为  ' + type(second_param__name)
        elif param_type == str:
            '''
                实例：
                数据库存的check_point = ['errorInfo','failNum','importSuccess','successNum']，分别取出的值均为str
                会分别校验resData和testData中errorInfo，failNum...等字段的值是否相等
            '''
            # print('是字符串')
            res_param = resData.get(check_point)
            test_param = testData.get(check_point)
        else:
            res_param = 'res_param参数异常：  check_point传值错误  当前类型为  ' + param_type
            test_param = 'test_param参数异常：  check_point传值错误  当前类型为  ' + param_type
            # print('异常')

        #检查最终的res_param == test_param
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