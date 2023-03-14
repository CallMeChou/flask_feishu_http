import pymysql
import os
class Mysql(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host=os.environ.get('MYSQLHOST'),port=int(os.environ.get('MYSQLPORT')),user=os.environ.get('MYSQLUSER'),password=os.environ.get('MYSQLPASSWORD'),database=os.environ.get('MYSQLDATABASE'))
            #游标对象
            self.cursor = self.db.cursor()
            print("连接成功！")
        except:
            print("连接失败！")
 	#查询数据函数
    def getdata(self):
        sql = "select * from test"
        #执行sql语句
        self.cursor.execute(sql)
        #获取所有的记录
        results = self.cursor.fetchall()
        return results
    #关闭
    def __del__(self):
        self.db.close()
Mysql.getdata(self)