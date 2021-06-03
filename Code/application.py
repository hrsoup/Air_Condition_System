import database as db

class Air_main:  # 空调主机的基类
    def __init__(self, air_on_num, wind_on_num,wait_on_num):
        self.air_on_num = air_on_num   #当前开启子机数
        self.wind_on_num = wind_on_num #当前送风子机数
        self.wait_on_num =wait_on_num  #当前等待送风调度子机数

    def create_service(self):#创建服务对象
        services=[]
        for i in range(1,6):
            service=Service(i,25,1)
            services.append(service)
        return services

    def create_scheduler(self):  #创建调度对象
        scheduler = Scheduler()
        return scheduler

    def create_air_sub(self):  # 创建空调子机对象
        air_subs=[]
        for i in range(1,6):
            air_sub = Air_sub(i, 0, 0, 25, 1, 0)
            air_subs.append(air_sub)
        return air_subs

class Air_sub:  # 空调子机的基类_
    def __init__(self, room_id, if_wind, if_on,tem, windmode, cost):
        self.room_id = room_id  # 房间号
        self.tem = tem  # 设定温度
        self.windmode = windmode  # 设定风速
        self.cost = cost  # 当前计费
        self.if_wind = if_wind  # 是否送风
        self.if_on = if_on  # 是否开启
        self.if_wait = 0  # 是否在送风队列等待，初始化设置为0、
        self.wait_time = 0 #等待时间
        self.serve_time = 0 #服务时间
    '''
    modified by 刘峰麟 on 6.26
        增加了传入持久化层的操作和形参table_name和data(列表)
    '''
    def insert_data(self, table_name, data):  #向数据库插入数据
        dbmapper = db.DBMapper()  # 创建DBMapper
        # 根据表名确定属性列表
        if(table_name == 'switch_air'):#开关机表
            attributes_list = ["room_id", "now_time", "on_off"]
        elif (table_name == 'change_temperature'):#调温表
            attributes_list = ["room_id", "now_time", "tem_change","if_reach"]
        elif(table_name == "change_windmode"):#改变风速表
            attributes_list = ["room_id", "now_time", "wind_change"]
        elif(table_name == "schedule"):#调度表
            attributes_list = ["room_id", "now_time", "if_schedule","wind_mode"]
        #拼接表名，属性列表，data生成sql语句
        sql = "insert into " + table_name + "(" + ",".join(attributes_list) + ") values(" + ",".join(data) + ")"
        # sql语句传入持久化层
        dbmapper.insert_air(sql)
        return True

class Service:
    def __init__(self, room_id, tem_set, wind_set):
        self.room_id = room_id  # 房间号
        self.tem_set = tem_set  # 目标温度
        self.wind_set = wind_set  # 目标风速

    def send_request(self):  # 发送送风请求
        return self.room_id, self.tem_set, self.wind_set

    '''
    modified by 刘峰麟 on 6-26
        增加了对switch_air的插入数据操作
        update_data修改为insert_data
        增加了形参air_monitor
    '''
    def set_air_on(self, air_sub, air_monitor):  # 开启空调
        air_sub.if_on = 1
        air_sub.insert_data("switch_air", [str(self.room_id), str(air_monitor.systime), "1"])
        print("空调开启..")

    def set_air_off(self, air_sub, air_monitor):  # 关闭空调
        air_sub.if_on = 0
        air_sub.insert_data("switch_air", [str(self.room_id), str(air_monitor.systime), "0"])
        print("空调关闭..")

    def set_wind_on(self, air_sub, air_monitor):  #开启送风
        air_sub.if_wind = 1
        air_sub.insert_data("schedule", [str(self.room_id), str(air_monitor.systime),"1",str(air_sub.windmode)])
        print("送风开启..")

    def set_wind_off(self, air_sub, air_monitor):  # 关闭送风
        air_sub.if_wind = 0
        '''
            modified by 王博琛 on 6-28
            修改了部分参数
        '''
        '''
         modified by 温嘉烨 on 6-28
            修改了处于等待队列关机算调度的情况
        '''
        air_sub.insert_data("schedule", [str(self.room_id), str(air_monitor.systime), "0", "1"])
        print("送风关闭..")

    '''
    modified by 刘峰麟 on 6-26
        增加了对change_temperature的插入数据操作
        update_data修改为insert_data
        增加了形参air_monitor
    '''

    def set_tem(self, air_sub, air_monitor):  #设定温度
        air_sub.tem = self.tem_set
        air_sub.insert_data("change_temperature", [str(self.room_id), str(air_monitor.systime), str(self.tem_set),'0'])
        print("温度调节成功..")

    def set_windmode(self, air_sub, air_monitor):  #设定风速
         air_sub.windmode = self.wind_set
         air_sub.insert_data("change_windmode", [str(self.room_id), str(air_monitor.systime), str(self.wind_set)])
         print("风速调节成功..")

class Scheduler:  # 调度对象的基类
    def __init__(self):
        self.w_seq = []  # 等待队列
        self.s_seq = []  # 服务队列

    '''
     modified by 温嘉烨 on 6-27
        增加了调度算法
    '''
    def schedule_on(self, air_main, air_subs, services,air_monitor):#执行调度算法,满足调度条件则让服务器直接修改对应空调子机的参数,这里的air_sub是一个对象列表
        if (air_main.air_on_num in [1, 2, 3]):#不用判断可以直接调度
            for room_id in range(1, 6):
                if (air_subs[room_id - 1].if_on == 1 and air_subs[room_id - 1] not in self.s_seq):
                    self.s_seq.append(air_subs[room_id - 1])
                    services[room_id - 1].set_wind_on(air_subs[room_id - 1],air_monitor)
                    '''
                        modified by 温嘉烨 on 6-28
                        修改了在服务队列有空或者开机的时候会调节风速的情况 开机不算调风速只可能算调度
                    '''
                    #services[room_id - 1].set_windmode(air_subs[room_id - 1],air_monitor)
                    air_main.wind_on_num += 1
                    if (air_subs[room_id - 1] in self.w_seq):
                        self.w_seq.remove(air_subs[room_id - 1])
                if (air_subs[room_id - 1].if_on == 0 and air_subs[room_id - 1] in self.s_seq):
                    self.s_seq.remove(air_subs[room_id - 1])
                    print("房间%d关机，直接被调出服务队列" % room_id)

        else:  # 有超过4台空调处于开机状态 需要判断是否进行调度
            wind_now = []  # 现在在服务队列里的，可能要被替换的
            change_ready = []  # 现在不在服务队列里的，可能要去替换的
            if_prior = 0
            if_timestamp = 0
            for room_id in range(1, 6):
                if (air_subs[room_id - 1].if_on == 0 and air_subs[room_id - 1] in self.s_seq):
                    self.s_seq.remove(air_subs[room_id - 1])
                    print("房间%d关机，直接被调出服务队列" % room_id)
                if (air_subs[room_id - 1].if_on == 0 and air_subs[room_id - 1] in self.w_seq):
                    self.w_seq.remove(air_subs[room_id - 1])
                    print("房间%d关机，直接被调出等待队列" % room_id)
                if (air_subs[room_id - 1].if_on == 1 and air_subs[room_id - 1] in self.s_seq):
                    wind_now.append(air_subs[room_id - 1])
                if (air_subs[room_id - 1].if_on == 1 and air_subs[room_id - 1] not in self.s_seq):
                    change_ready.append(air_subs[room_id - 1])

            print("有可能被调出服务队列的房间")
            for i in range(0, len(wind_now)):
                print("%d " % wind_now[i].room_id, end="")
            print()
            print("有可能被调入服务队列的房间")
            for i in range(0, len(change_ready)):
                print("%d " % change_ready[i].room_id, end="")

            # 判断是否需要调度调度的情况
            for i in range(0, len(change_ready)):
                for j in range(0, len(wind_now)):
                    if (change_ready[i].windmode == wind_now[j].windmode):
                        if_timestamp = 1  # 有可能需要时间片调度
                    if (change_ready[i].windmode > wind_now[j].windmode):
                        if_prior = 1  # 有可能需要优先级调度

            if (if_prior == 1):  # 需要优先级调度的情况
                for air1 in change_ready:
                    for air2 in wind_now:
                        if (air1.windmode > air2.windmode):
                            # 优先级低的出队
                            self.w_seq.append(air2)
                            self.s_seq.remove(air2)
                            wind_now.remove(air2)
                            air2.serve_time = 0
                            services[air2.room_id-1].set_wind_off(air2,air_monitor)
                            # 优先级高的入队
                            if (air1 in self.w_seq):
                                self.w_seq.remove(air1)
                            self.s_seq.append(air1)
                            air_main.wind_on_num += 1
                            change_ready.remove(air1)
                            services[air1.room_id - 1].set_wind_on(air1,air_monitor)
                            break

            if (if_timestamp == 1):  #可能需要时间片调度的情况
                change_list = []
                for air1 in change_ready:
                    if (air1 in self.w_seq):  # 在等待队列
                        if (air1.wait_time >= 2):  # 请求调度
                            if (len(self.s_seq) <= 2):
                                self.w_seq.remove(air1)
                                self.s_seq.append(air1)
                                air1.wait_time = 0
                                services[air1.room_id - 1].set_wind_on(air1,air_monitor)
                                change_ready.remove(air1)
                            else:
                                for air2 in wind_now:
                                    if (air2.windmode == air1.windmode):
                                        change_list.append(air2)

                                max_serve_time = change_list[0].serve_time
                                for temp in change_list:
                                    if temp.serve_time > max_serve_time:
                                        max_serve_time = temp.serve_time  # 更新有可能被调度的里面的最大服务时间

                                for air in wind_now:
                                    if (air.serve_time == max_serve_time and air in change_list):
                                        # 服务时间最长的同优先级的出队
                                        self.w_seq.append(air)
                                        self.s_seq.remove(air)
                                        air.serve_time = 0
                                        services[air.room_id - 1].set_wind_off(air,air_monitor)
                                        wind_now.remove(air)

                                        # 等待时间满足条件的同优先级的入队
                                        self.w_seq.remove(air1)
                                        self.s_seq.append(air1)
                                        air1.wait_time = 0
                                        services[air1.room_id - 1].set_wind_on(air1,air_monitor)
                                        change_ready.remove(air1)

                    else:  # 将其添加到等待队列中
                        self.w_seq.append(air1)

            # 临时变量赋初始值
            if_prior = 0
            if_timestamp = 0
            # 临时队列清空
            change_ready.clear()
            wind_now.clear()


class Bill:  # 账单的基类
    '''
    modified by 张佳颖
    '''
    def __init__(self, user_id, room_id):
        self.user_id = user_id  # 账单编号
        self.room_id = room_id  # 空调送风房间数
        self.dbs = db.DBMapper()

    def check_bill(self):
        records = self.dbs.query_bill(self.user_id,self.room_id)
        b_time = records[0][2]
        e_time = records[0][3]
        cost = records[0][4]
        return b_time,e_time,cost


class Details:        #详单基类，只记录信息，考虑客户退房后才需要打印详单，所以默认查询表项都已插入到表中
    '''
    modified by 张佳颖
    '''
    #详单至少需要包含如下信息：房间号、开始送风时间、结束送风时间、送风时长、风速、费率、费用
    def __init__(self,user_id,room_id):
        self.user_id = user_id
        self.room_id = room_id
        self.dbs = db.DBMapper()

    def create(self):#插入
        sql = 'select * from (select min(now_time),sum(now_time),wind_mode from schedule ' \
              'where if_schedule=1 and room_id = %s group by wind_mode)as a join (select max(now_time),' \
              'sum(now_time),wind_mode from schedule where if_schedule=0 and room_id = %s group by wind_mode) as b where a.wind_mode = b.wind_mode' % (
              self.room_id, self.room_id)
        # 查询得到了开始送风时间、结束送风时间、送风总时长、送风模式——schedule的计数即为送风总时长
        rows, records = self.dbs.query_detail(sql)
        for row in range(rows):
            start_time = records[row][0];
            stop_time = records[row][3];
            wind = records[row][2];
            wind_duration = records[row][4] - records[row][1];
            if (wind == 2):  # 根据模式得到费率——0代表低风，1代表中风，2代表高风
                ratio = 1
            elif (wind == 1):
                ratio = 0.5
            else:
                ratio = 1 / 3
            cost = int(wind_duration) * ratio  # 计算费用
            detail_id = self.user_id + self.room_id + str(wind)  #
            # print(detail_id, self.room_id, start_time, stop_time, wind_duration, wind, ratio, cost)
            self.dbs.insert_detail(detail_id, self.room_id, start_time, stop_time, wind_duration, wind, ratio, cost)

    def update_bill(self):
        sql = 'select min(b_time),max(e_time),sum(cost) from detail where room_id=%s' %(self.room_id)
        rows,records = self.dbs.query_detail(sql)
        b_time = int(records[0][0])
        e_time = int(records[0][1])
        total_cost = float(records[0][2])
        sql = 'update user_in set cost_all=%f,b_time = %d,e_time=%d where user_id=%s and room_id=%s' %(total_cost,b_time,e_time,self.user_id,self.room_id)
        print(sql)
        self.dbs.update(sql)

    def check(self):
        sql = 'select * from detail where room_id = %s' %(self.room_id) #详单信息针对某个风速模式设定而言，因此无法确定一个用户一个房间会有几种送风设置，采用user_id 和room_id 查
        rows,records = self.dbs.query_detail(sql)
        return rows,records

class Form:  # 报表的基类
    '''
    modified by 谢祎凡
    '''
    def __init__(self, form_id, room_id, b_time, e_time, air_on_times, air_off_times, use_time,
                         schedule_times, change_tem_times, change_wind_times, details_number, cost_all):
        self.form_id = form_id  # 报表号
        self.room_id = room_id  # 房间号
        self.b_time = b_time  # 开始时间
        self.e_time = e_time  # 结束时间
        self.air_on_times = air_on_times  # 子机开启次数
        self.air_off_times = air_off_times  # 子机关闭次数
        self.use_time = use_time  # 空调使用时长
        self.schedule_times = schedule_times  # 调度次数
        self.change_tem_times = change_tem_times  # 调温次数
        self.change_wind_times = change_wind_times  # 调风次数
        self.details_number =  details_number # 详单数
        self.cost_all = cost_all  # 总消费金额

    def insert_data(self):  # 向数据库中插入表单数据
        dbm = db.DBMapper()
        self.air_on_times, self.air_off_times, self.use_time = dbm.query_air_switch(self.room_id, self.b_time, self.e_time)
        self.change_tem_times = dbm.query_air_tem(self.room_id, self.b_time, self.e_time)
        self.change_wind_times, self.schedule_times = dbm.query_air_wind(self.room_id, self.b_time, self.e_time)
        self.details_number, self.cost_all = dbm.query_details(self.room_id, self.b_time, self.e_time)
        dbm.insert_form(self.form_id, self.room_id, self.b_time, self.e_time, self.air_on_times, 
                        self.air_off_times, self.use_time, self.schedule_times, 
                        self.change_tem_times, self.change_wind_times, self.details_number, self.cost_all)
        return self.air_on_times, self.air_off_times, self.use_time, self.schedule_times, self.change_tem_times, self.change_wind_times, self.details_number, self.cost_all

    def check_form_item(self):  # 获得报表表项信息
        dbm = db.DBMapper()
        result = dbm.query_form(self.form_id)#查询报表
        return result

class user_in:        
    '''
    modified by 谢祎凡
    '''
    def __init__(self, room_id, user_id, intime, outime, total_cost):
        self.room_id = room_id
        self.user_id = user_id
        self.intime = intime
        self.outime = outime
        self.total_cost = total_cost
        
    def in_bill(self, room_id, user_id, time):
        self.intime = time

    def out_bill(self, room_id, user_id, time):
        self.outime = time
        dbm = db.DBMapper()
        _, total_cost = dbm.query_details(room_id, self.intime, self.outime)
        self.total_cost = total_cost
        dbm.insert_bill(self.room_id, self.user_id, self.intime, self.outime, self.total_cost)
