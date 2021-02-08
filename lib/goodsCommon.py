from ywyrobot.common import *
from tools.mysql import mysql
from lib.login import Login
from cfg import Global
import json
from tools.HttpUtil import HttpUtil

class goodsCommon():
    def get_itemNo(self,itemName):
        url = 'https://api-srm-supplier.ywwl.com/admin/supplier/item/list/page'
        data = {"index":1,"size":10,"itemName":itemName,"categoryNoPath":"","updateStartTime":None,"updateEndTime":None}
        data = json.dumps(data)
        response = HttpUtil().post_request(url=url,postdata=data,headers=Global.Headers_yun)
        # print(response)
        item_list = response.get('data').get('list')
        itemNo_list = []
        for item in item_list:
            itemNo = item.get('itemNo')
            itemNo_list.append(itemNo)
        return itemNo_list

    def del_item(self,itemNo):
        url = 'https://api-srm-supplier.ywwl.com/admin/supplier/item/delete'
        data = {"no":itemNo}
        data = json.dumps(data)
        response = HttpUtil().post_request(url=url,postdata=data,headers=Global.Headers_yun)
        # print(response)
        return response

    def for_del_item(self,itemName):
        itemNo_list = self.get_itemNo(itemName)
        ret_list = []
        for itemNo in itemNo_list:
            ret = self.del_item(itemNo)
            ret_list.append(ret)
        return ret_list


    def get_submitUniqueNo(self,itemName):
        url = 'https://api-srm-supplier.ywwl.com/admin/supply/submit/daily/list/page'
        data = {"index":1,"size":10,"isDailyOnly":True,"submitBatchNo":"","spuName":itemName,"spuNo":"","supplyType":"","submitStatus":"","submitTimeStart":"","submitTimeEnd":""}
        data = json.dumps(data)
        response = HttpUtil().post_request(url=url, postdata=data, headers=Global.Headers_yun)
        # print(response)
        item_list = response.get('data').get('list')
        submitUniqueNo_list = []
        for item in item_list:
            submitUniqueNo = item.get('submitUniqueNo')
            submitUniqueNo_list.append(submitUniqueNo)
        return submitUniqueNo_list

    def return_submit(self,submitUniqueNo):
        url = 'https://api-srm-supplier.ywwl.com/admin/supply/submit/undo'
        data = 'submitUniqueNo=' + submitUniqueNo
        url = url + '?' + data
        response = HttpUtil().get_request(url=url,headers=Global.Headers_yun)
        # print(response)
        return response

    def del_submit(self,submitUniqueNo):
        url = 'https://api-srm-supplier.ywwl.com/admin/supply/submit/delete'
        data = 'submitUniqueNo=' + submitUniqueNo
        url = url + '?' + data
        response = HttpUtil().get_request(url=url,headers=Global.Headers_yun)
        # print(response)
        return response

    def for_del_submit(self,itemName):
        submitUniqueNo_list = self.get_submitUniqueNo(itemName)
        ret_list = []
        for submitUniqueNo in submitUniqueNo_list:
            ret_return = self.return_submit(submitUniqueNo)
            ret_list.append(ret_return)
            ret_del = self.del_submit(submitUniqueNo)
            ret_list.append(ret_del)
        return ret_list

if __name__ == "__main__":

    goodsCommon().for_del_submit('自动化导入创建商品00')
    goodsCommon().for_del_item('自动化导入创建商品00')