#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests, json
from testFiles.filesCommon import filesCommon

'''
created_by: 
created_At: 2020-04-17
params: httpResponse http报文响应
function: 对http报文的response进行解析，并返回一个类，包含解析后的结果、状态、及text属性
return: 如果一个类的对象，类中有result、statusLine及text三个属性
'''

class HttpUtil():

    def post_request(self, url=None, postdata=None, headers=None):
        request = requests.Session()
        response = request.post(url, data=postdata, headers=headers)
        json = response.json()
        if response.status_code == 200:
            data = json['data']
            return json
        else:
            return json['error']

    def get_request(self, url=None, params=None, headers=None):
        response = requests.get(url, params=params, headers=headers)
        json = response.json()
        if response.status_code == 200:
            data = json['data']
            return json
        else:
            return json['error']

    def post_requestCookies(self, url=None, postdata=None, headers=None, cookies=None):
        request = requests.Session()
        response = request.post(url, json=postdata, headers=headers, cookies=cookies)
        ret = response.json()
        # token = ret['data']['userToken']
        token = ret.get('data').get('userToken')
        return token

    # post 请求中获取token
    def post_getToken(self, url=None, postdata=None, headers=None):
        request = requests.Session()
        response = request.post(url, data=postdata, headers=headers)
        ret = response.json()
        token = ret['data']['userToken']
        return token

    #post 请求上传文件
    def post_upload(self, url=None, postdata=None, headers=None):
        path = filesCommon().getFilePath()
        postdata_dict = json.loads(postdata)
        filesParamName = postdata_dict.get('filesParamName')
        fileName = postdata_dict.get('fileName')
        files = {
            filesParamName: (open(path + '\\' + fileName, 'rb'))
        }
        response = requests.post(url, data=postdata_dict, files=files, headers=headers)
        json_resp = response.json()
        if response.status_code == 200:
            data = json_resp.get('data')
            return json_resp
        else:
            return json_resp.get('error')