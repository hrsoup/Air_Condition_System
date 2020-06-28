import pymysql as py

db = py.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123456",
    database="hotel",
    charset="utf8"
)
            
class DBMapper:#数据库接口基类
    def insert_detail(self,id,room_id,b_time,e_time,wind_duration,wind,money_ratio,cost):        #插入detail表中的数据
        '''
    modified by 张佳颖
        '''
        cursor = db.cursor()
        sql = 'insert into detail(detail_id,room_id,b_time,e_time,wind_duration,wind,money_ratio,cost) value (%s,%s,%d,%d,%d,%d,%f,%d)' \
              %(id,room_id,b_time,e_time,wind_duration,wind,money_ratio,cost)
        isok = cursor.execute(sql)      # if isok==1 the insert succeed
        if(isok):
            db.commit()   #提交数据
        cursor.close()
        return isok       #返回1说明插入成功

    def query_detail(self,sql):  #根据sql查询详单内容
        '''
    modified by 张佳颖
        '''
        cursor = db.cursor()
        rows = cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        return rows,records #返回数目和查询结果（列表格式）

    def query_bill(self,user_id,room_id):#根据user_id,room_id查询账单数据
        '''
    modified by 张佳颖
        '''
        cursor = db.cursor()
        sql = "select * from user_in where user_id='%s' and room_id='%s'" % (user_id,room_id)
        cursor.execute(sql)
        records = cursor.fetchall()      #query results
        return records                #返回全部查询结果（列表格式）

    def update(self,sql):
        '''
            modified by 张佳颖
                '''
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

    def insert_air(self, sql):
        '''
    modified by 刘峰麟 on 6-26
    传入了sql语句执行
        '''
        # 创建游标，并且执行对应sql语句
        cursor = db.cursor()
        print(sql)
        cursor.execute(sql)
        cursor.connection.commit()  # 执行commit操作，插入语句才能生效
        cursor.close()

    def insert_bill(self, room_id, user_id, intime, outime, total_cost):
        '''
    modified by 谢祎凡
        '''
        cursor = db.cursor()
        cursor.execute("insert into user_in values \
                        (%s,%s,%s,%s,%s)", [room_id, user_id, intime, outime, total_cost]) 
        db.commit()

    def insert_form(self,form_id, room_id, b_time, e_time, air_on_times, air_off_times, use_time,
                         schedule_times, change_tem_times, change_wind_times, details_number, cost_all):#插入数据
        '''
    modified by 谢祎凡
        '''
        cursor = db.cursor()
        cursor.execute("insert into form \
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                [form_id, room_id, b_time, e_time, air_on_times, air_off_times, use_time,
                         schedule_times, change_tem_times, change_wind_times, details_number, cost_all])
        db.commit()

    def query_air_switch(self, room_id, b_time, e_time): #查询空调开关次数、空调运行总时长
        '''
    modified by 谢祎凡
        '''
        cursor = db.cursor()
        cursor.execute("select count(room_id) from switch_air \
                        where now_time >= %s and \
                        now_time <= %s and \
                        room_id = %s and \
                        on_off = 1",[b_time, e_time, room_id]) 
        result = cursor.fetchone()
        on = result[0]

        cursor = db.cursor()
        cursor.execute("select count(room_id) from switch_air \
                        where now_time >= %s and \
                        now_time <= %s and \
                        room_id = %s and \
                        on_off = 0",[b_time, e_time, room_id]) 
        result = cursor.fetchone()  
        off = result[0]         

        cursor = db.cursor()
        cursor.execute("select now_time, on_off from switch_air \
                        where now_time >= %s and \
                        now_time <= %s and \
                        room_id = %s",[b_time, e_time, room_id]) 
        result = cursor.fetchall() 

        on_time = 0 #开机时间
        off_time = 0 #关机时间
        time = 0 #总时长
        on_off = 0 #控制开关，初始为关
        for item in result:
            if item[1] == 1: #如果空调开启
                on_time = item[0]
                on_off = 1
            if item[1] == 0: #如果空调关闭
                off_time = item[0] 
                on_off = 0
                temp = off_time - on_time
                time = time + temp
        if on_off == 1: #如果查询的结束时间仍然没有关闭空调
            temp = e_time - on_time
            time = time + temp

        return on,off,time

    def query_air_tem(self, room_id, b_time, e_time): #查询调温次数
        '''
    modified by 谢祎凡
        '''
        cursor = db.cursor()
        cursor.execute("select count(room_id) from change_temperature \
                         where now_time >= %s and \
                        now_time <= %s and \
                        room_id = %s",[b_time, e_time, room_id]) 
        result = cursor.fetchone()
        changeing = result[0]
    
        return changeing

    def query_air_wind(self, room_id, b_time, e_time): #查询调风、被调度次数
        '''
    modified by 谢祎凡
        '''
        cursor = db.cursor()
        cursor.execute("select count(room_id) from change_windmode \
                        where now_time >= %s and \
                        now_time <= %s and \
                        room_id = %s",[b_time, e_time, room_id]) 
        result = cursor.fetchone()
        changeing = result[0]

        cursor = db.cursor()
        cursor.execute("select count(room_id) from schedule \
                        where now_time >= %s and \
                            now_time <= %s and \
                            room_id = %s",[b_time, e_time, room_id]) 
        result = cursor.fetchone()  
        schedule = result[0] 
        print(changeing,schedule)          
        return changeing,schedule

    def query_details(self, room_id, b_time, e_time):   #获取详单数量及总消费金额 
        '''
    modified by 谢祎凡
        '''
        cursor = db.cursor()
        cursor.execute("select count(detail_id) from detail \
                        where room_id = %s and \
                            b_time >= %s and \
                            e_time <= %s ",[room_id, b_time, e_time]) 
        result = cursor.fetchone()
        datails_number = result[0] 

        cursor = db.cursor()
        cursor.execute("select sum(cost) from detail \
                      where room_id = %s and \
                            b_time >= %s and \
                            e_time <= %s ",[room_id, b_time, e_time]) 
        result = cursor.fetchone()
        cost_all = result[0]
        if cost_all == None:
            cost_all = 0
        return datails_number, cost_all 

    def query_form(self, form_id):#查询报表
        '''
    modified by 谢祎凡
        '''
        cursor = db.cursor()
        cursor.execute("select * from form \
                        where form_id = %s",[form_id]) 
        result = cursor.fetchone()
        return result