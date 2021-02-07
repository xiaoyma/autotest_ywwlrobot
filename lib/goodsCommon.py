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


if __name__ == "__main__":
    goodsCommon().for_del_item('自动化导入创建商品00')
