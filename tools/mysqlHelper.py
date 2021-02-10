import logging
import pymysql
import sys
from cfg import Global

logger = logging.getLogger("baseSpider")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s\%(levelname)-8s:%(message)s')
# 文件日志
# file_handler = logging.FileHandler("baseSpider.log")
# file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logge添加具体的日志处理器
# logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)

# class mysqlConn(object):
#     def __init__(self, host, user,password,database):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
MYSQL = {
    'host': '192.168.122.208',
    'user': 'root',
    'password': '123456',
    'database': 'ywwl_python_rd'
}
class mysqlHelper:
    def __init__(self,mysql=Global.mysq_local,charset='utf8'):
        # if mysql is None:
        #     import index
        #     mysql = index.app.config['MYSQL']
        self.host = mysql.get('host')
        self.user = mysql.get('user')
        self.password = mysql.get('password')
        self.database = mysql.get('database')
        self.connectDatabase()

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(self.host, self.user,
                                        self.password, self.database, charset='utf8')
        except:
            logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        return self.cur

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 回滚数据库
    def rollback(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.conn.rollback()
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None):
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql, params)
                self.conn.commit()
        except Exception as e:
            logger.error("execute failed: " + sql)
            logger.error("params: " + str(params))
            logger.error("Exception: " + str(e))
            raise e
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def executeMany(self, sql, params):
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.executemany(sql, params)
                self.conn.commit()
        except Exception as e:
            logger.error("execute failed: " + sql)
            logger.error("params: " + str(params))
            logger.error("Exception: " + str(e))
            raise e
        return True

    # 用来查询所有表数据
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        result = self.mysql2json(self.cur.fetchall(),self.cur.description)
        return result

    # 用来查询单条表数据
    def fetchone(self, sql, params=None):
        self.execute(sql, params)
        result = self.mysql2json(self.cur.fetchone(),self.cur.description)
        return result

    def fetchDesciption(self, sql, params=None):
        self.execute(sql, params)
        return self.cur.description

    # 用来查询条数数据
    def fetchCount(self, sql, params=None):
        self.cur.execute(sql, params)
        result = self.cur.fetchall()
        return result

    def mysql2json(self,data,des):
        keys = []
        for column in des:
            keys.append(column[0])
        key_number = len(keys)
        json_data = []
        if not data :
            return {}
        if tuple != type(data[0]) :
            data = [data]
        for row in data:
            item = dict()
            for q in range(key_number):
                if keys[q] == 'createTime':
                    item[keys[q]] = str(row[q])
                # else:
                elif None == row[q]:
                    item[keys[q]] = ''
                elif isinstance(row[q],bytes):
                    item[keys[q]] = str(row[q], encoding = "utf-8")
                else:
                    item[keys[q]] = row[q]
            json_data.append(item)
        return json_data

if __name__ == '__main__':
    db = mysqlHelper(host='172.16.5.208',user='root',password='123456',database='ywwl_python_test')
    sql = "select * from xmind limit 1;"
    print(db.fetchall(sql))
    # data = db.fetchDesciption(sql)
    # print(data)
    # print(des)
    # json2mysql.json2mysql(conn,sql)
    # from com.ywwl.utils import xls2Json




