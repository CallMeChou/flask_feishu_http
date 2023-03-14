import pymysql
import os
class Mysql_con(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host=os.environ.get('MYSQLHOST'),port=int(os.environ.get('MYSQLPORT')),user=os.environ.get('MYSQLUSER'),password=os.environ.get('MYSQLPASSWORD'),database=os.environ.get('MYSQLDATABASE'))
            #游标对象
            self.cursor = self.db.cursor()
            print("连接成功！")
        except:
            print("连接失败！")
 	#查询数据函数
    def get_data(self):
        sql = "select * from test"
        #执行sql语句
        self.cursor.execute(sql)
        #获取所有的记录
        results = self.cursor.fetchall()
        return results
    #插入
    def insertdata(self,results):
        sql = "insert into test(name,age)values('%s','%s')" % (results['name'],results['age'])
        sql1 = "ALTER TABLE test DROP id"
        sql2 = "ALTER TABLE test ADD id int NOT NULL FIRST"
        sql3 = "ALTER TABLE test MODIFY COLUMN id int NOT NULL AUTO_INCREMENT,ADD PRIMARY KEY(id)"
        try:
            self.cursor.execute(sql)
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.cursor.execute(sql3)
            self.db.commit()
        except:
            # 如果发生错误就回滚，建议使用这样发生错误就不会对表数据有影响
            self.db.rollback()
        return

    #关闭
    def __del__(self):
        self.db.close()
