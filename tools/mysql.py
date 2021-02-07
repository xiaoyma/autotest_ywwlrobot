import pymysql
from ywyrobot.common import *

class mysql():
    def getOrderUpdatedAt(self,testId):
        host = 'localhost'
        user = 'root'
        password = '123456'
        database = 'test'
        sql = "SELECT id,testId,`module`, `function`, interface, testPath, method, testParams, testResp, check_point, remark, `status` FROM `test_supply` WHERE `status` = 0 and"
        params = []
        sql += " testId = %s "
        params.append(testId)
        conn = pymysql.connect(host, user, password, database, charset='utf8')
        cur = conn.cursor()
        cur.execute(sql,params)
        result = self.mysql2json(cur.fetchall(),cur.description)
        # print("sql执行结果：" ,result)
        cur.close()
        conn.close()
        return result

    #结果转为json格式
    def mysql2json(self,data, des):
        keys = []
        for column in des:
            keys.append(column[0])
        key_number = len(keys)
        json_data = []
        if not data:
            return {}
        if tuple != type(data[0]):
            data = [data]
        for row in data:
            item = dict()
            for q in range(key_number):
                if keys[q] == 'createTime':
                    item[keys[q]] = str(row[q])
                # else:
                elif None == row[q]:
                    item[keys[q]] = ''
                elif isinstance(row[q], bytes):
                    item[keys[q]] = str(row[q], encoding="utf-8")
                else:
                    item[keys[q]] = row[q]
            json_data.append(item)
        return json_data

    def updateSQL_interface(self, testId, interface=None, testParams=None):
        host = 'localhost'
        user = 'root'
        password = '123456'
        database = 'test'
        params = []
        if interface != None and testParams == None:
            sql = "UPDATE test_supply SET interface = %s WHERE testId = %s"
            params.append(interface)
        elif interface == None and testParams != None:
            sql = "UPDATE test_supply SET testParams = %s WHERE testId = %s"
            params.append(testParams)
        else:
            INFO('updateSQL_interface 是传参错误，请检查')
            sql = ''
        params.append(testId)
        conn = pymysql.connect(host, user, password, database, charset='utf8')
        cur = conn.cursor()
        ret = cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return ret

if __name__ == '__main__':
    mysql().getOrderUpdatedAt('API-1101')