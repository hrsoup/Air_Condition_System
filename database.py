import pymysql as py
class DBMapper:#数据库接口基类
    def __init__(self):
    def insert_air(self):
        db = py.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="123456",
            database="用户注册",
            charset="utf8"
        )
        # 创建游标，并且执行对应sql语句
        cursor = db.cursor()
        sql = 'select * from 用户信息'
        cursor.execute(sql)

    def delete_air(self):
    def update_air(self):
    def insert_air(self):
    def insert_bill(self):#插入数据
        db = py.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="123456",
            database="用户注册",
            charset="utf8"
        )
        # 创建游标，并且执行对应sql语句
        cursor = db.cursor()
        sql = 'select * from 用户信息'
        cursor.execute(sql)

    def delete_bill(self):#删除数据
    def update_bill(self):#更新数据
    def query_bill(self):#查询数据
    def insert_form(self):#插入数据
            db = py.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="123456",
                database="用户注册",
                charset="utf8"
            )
            # 创建游标，并且执行对应sql语句
            cursor = db.cursor()
            sql = 'select * from 用户信息'
            cursor.execute(sql)

    def delete_form(self):#删除数据
    def update_form(self):#更新数据
    def query_form(self):#查询数据






