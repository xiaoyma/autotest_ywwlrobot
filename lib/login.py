
import json,requests
from tools.HttpUtil import HttpUtil


'''
created_by: 
created_At: 2020-04-17
params: 获取tonken
'''

class Login():
    def login_yun(self,userPhone='18800000000',userPasswd='123456'):
        headers = {
            "Host": "api-auth.ywwl.com",
            "Connection": "keep-alive",
            "Content-Length": "73",
            "X-TOKEN": "wvdxtc1bre1jtl8wljm0mjywnda5mje2mzmxndq0xzgwmdg3mze0mzgzodizotq1",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "*/*",
            "Origin": "https://yun.ywwl.com",
            "Referer": "https://yun.ywwl.com/",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        }
        params = {"userPhone": userPhone, "userPasswd": userPasswd, "projectId": "PROSUPPLIER"}
        url = "https://api-auth.ywwl.com/user/login"
        x = HttpUtil()
        response = x.post_requestCookies(url,params,headers)
        return response

    # def login_yun(self,userPhone='18316321174',userPasswd='123456'):
    #     headers = {
    #         "Host": "test-api-auth.ywwl.com",
    #         "Connection": "keep-alive",
    #         "Content-Length": "73",
    #         "Content-Type": "application/json;charset=UTF-8",
    #         "Accept": "*/*",
    #         "Origin": "http://framework.test.ywwl.com",
    #         "Referer": "http://framework.test.ywwl.com/",
    #         "Accept-Language": "zh-CN,zh;q=0.9",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    #     }
    #     params = {"userPhone": userPhone, "userPasswd": userPasswd, "projectId": "PROSUPPLIER"}
    #     # url = "https://api-auth.ywwl.com/user/login"
    #     url = 'http://test-api-auth.ywwl.com/user/login'
    #     x = HttpUtil()
    #     response = x.post_requestCookies(url,params,headers)
    #     return response

    # def login_sso(self):
    #     operUrl = "http://oper.98u.com/sso/login.html"
    #     operHeaders = {
    #         "Host": "oper.98u.com",
    #         "Connection": "keep-alive",
    #         "Accept": "*/*",
    #         "Origin": "http://oper.98u.com",
    #         "token": "",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    #         "Referer": "http://oper.98u.com/sso/tologin.html?loginAuto=true&sourceUrl=http%3A%2F%2Foper.39ysj.com%2F%23%2FvideoOrders%3FloginAuto%3Dtrue%26%253FloginAuto%3Dtrue%26%253FloginAuto%3Dtrue%26%253FloginAuto%3Dtrue%26",
    #         "Accept-Encoding": "gzip, deflate",
    #         "Accept-Language": "zh-CN,zh;q=0.9",
    #     }
    #     operParams = {
    #         "username": "董承",
    #         "password": "18c5fc794c06b1b1b432da361bf08005"
    #     }
    #     response = HttpUtil.HttpUtil.post_getToken(operUrl,operParams,operHeaders)
    #     return response

    def loginout(self):
        pass


if __name__ == "__main__":
    login = Login()
    print(login.login_yun())
    # print(login.login_dh())
    # print(login.login_sso())