# -- coding: UTF-8 --
from lib.login import Login
import time, os
'''
created_by: 
created_At: 2020-04-17
params: 配置信息
'''

evn_path = os.path.dirname(os.path.abspath(__file__))
evn_path = evn_path.split(r"\cfg")[0]
evn_path = os.path.join(evn_path, "ywyrobot\evn.txt")
f = open(evn_path,mode="r",encoding='utf-8')
evn = f.read()
f.close()

print("*********************************************************************************************")
print(evn)
print("*********************************************************************************************")


if evn == 'TEST':
    host_supplier = "http://test-api-srm-supplier.ywwl.com"
    login_yun_url = 'http://test-api-auth.ywwl.com/user/login'
    login_yun_account = '18316321174'
    login_yun_password = '123456'
    force_tags = ['供应商接口用例总数（TEST）']
else:
    host_supplier = "https://api-srm-supplier.ywwl.com"
    login_yun_url = 'https://api-auth.ywwl.com/user/login'
    login_yun_account = '18800000000'
    login_yun_password = '123456'
    force_tags = ['供应商接口用例总数（PRD）']


tonken_yun = Login().login_yun(userPhone=login_yun_account, userPasswd=login_yun_password, url=login_yun_url)
print(tonken_yun)

#线上域名
# baseUrl = "https://api-srm-supplier.ywwl.com"

#获取tonken
# tonken_yun = Login().login_yun()

Headers_yun = {
    "x-token": tonken_yun
}

# 获取当前时间
locatime = time.strftime("%Y-%m-%d", time.localtime())

Headers_yun_all ={
    "Host": "api-srm-supplier.ywwl.com",
    "Connection": "keep-alive",
    "Content-Length": "154",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://srm-manage-revision.ywwl.com",
    "X-TOKEN": tonken_yun,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Sec-Fetch-Mode": "cors",
    "Content-Type": "application/json;charset=UTF-8",
    "Sec-Fetch-Site": "cross-site",
    "Referer": "https://srm-manage-revision.ywwl.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}



#测试库208
mysql208 = {
    'DBHost_208_test' : 'localhost',
    'DBUser_208_test' : 'root',
    'DBPwd_208_test' : '123456',
    'DBbase_208_test_order' : 'ywwl_order_test',
    'DBbase_208_test_trial' : 'ywwl_trial_test',
    'DBbase_208_test_fans' : 'ywwl_zhibo_fans_test',
    'DBbase_208_test_supply' : 'ywwl_supply_chain_test',
    'DBbase_208_test' : 'test'
}

#本地测试库
mysq_local = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'test'
}



