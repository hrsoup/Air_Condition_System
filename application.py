class Air_main:  # 空调主机的基类
    def __init__(self, air_on_num, wind_on_num,wait_on_num):
        self.air_on_num = air_on_num  #当前开启子机数
        self.wind_on_num = wind_on_num #当前送风子机数
        self.wait_on_num =wait_on_num  #当前等待送风调度子机数

    def create_service(self):#创建服务对象
        services=[]
        for i in range(1,6):
            service=Service(i,18,0)
            services.append(service)
        return services

    def create_scheduler(self):  #创建调度对象
        scheduler = Scheduler(0,0)
        return scheduler

    def create_air_sub(self):  # 创建空调子机对象
        air_subs=[]
        for i in range(1,6):
            air_sub = Air_sub(i, 0, 0, 18, 0, 0)
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

'''
 def insert_data(self):#向数据库插入数据
    dbmapper.insert_air()
    def update_data(self):#更新数据库数据
    dbmapper.update_air()
'''

class Service:  # 服务对象的基类
    def __init__(self, room_id, tem_set, wind_set):
        self.room_id = room_id  # 房间号
        self.tem_set = tem_set  # 目标温度
        self.wind_set = wind_set  # 目标风速

    def send_request(self):  # 发送送风请求
        return self.room_id, self.tem_set, self.wind_set

    def set_air_on(self, air_sub):#开启空调
        air_sub.if_on = 1
        print("空调开启..")

    def set_air_off(self, air_sub):#关闭空调
        air_sub.if_on = 0
        print("空调关闭..")

    def set_wind_on(self, air_sub):#开启送风
        air_sub.if_wind = 1
        print("送风开启..")

    def set_wind_off(self, air_sub):#关闭送风
        air_sub.if_wind = 0
        print("送风关闭..")

    def set_tem(self, air_sub):  # 设定温度
        if(self.tem_set>=18 and self.tem_set<=30):#合理的温度区间
            air_sub.tem = self.tem_set
            print("温度调节成功..")

    def set_windmode(self, air_sub):  # 设定风速
        if (self.wind_set == 0 or self.wind_set == 1 or self.wind_set == 2):#合理的风速区间
            air_sub.windmode = self.wind_set
            print("风速调节成功..")

    # def cost_on(self):  # 开启计费
    # def cost_off(self):  # 关闭计费


class Scheduler:  # 调度对象的基类
    def __init__(self, wait_num, success_num):
        self.wait_num = wait_num  # 送风等待数
        self.success_num = success_num  # 成功送风数

    def schedule_on(self, air_subs,services,room_id):#执行调度算法,满足调度条件则让服务器直接修改对应空调子机的参数,这里的air_sub是一个对象列表
        room_id, tem_set, wind_set = services[room_id-1].send_request()
        if((tem_set>=18 and tem_set<=30) and (wind_set==0 or wind_set==1 or wind_set==2)):
            '''
            判断这个请求是否可以执行,送风调度的过程
            '''
            # 执行请求内容,这两个请求是要通过调度器调度的，服务器不能直接给出对应服务
            services[room_id-1].set_wind_on(air_subs[room_id-1])
            services[room_id-1].set_windmode(air_subs[room_id-1])

'''
class Bill:  # 账单的基类
    def __init__(self, bill_id, room_id, b_time, e_time, cost_all):
        self.bill_id = bill_id  # 账单编号
        self.room_id = room_id  # 空调送风房间数
        self.b_time = b_time  # 入住时间
        self.e_time = e_time  # 离店时间
        self.cost_all = cost_all

    def insert_data(self):  # 向数据库中插入账单数据
        values = self.bill_id+","+self.room_id+","+self.b_time+","+self.e_time+","+self.cost_all
        DBMapper.insert("Bill_item",values)            #cost_all需要Air_sub在空调关机时update

    def check_bill_item(self,bill_id):  # 获得账单详单表项信息
        record = DBMapper.query("select * from Bill_item where bill_id = "+bill_id)
        return record

    # insert(table_name,values)
    # query(sql语句)

class Details:        #详单基类，只记录信息，考虑客户退房后才需要打印详单，所以默认查询表项都已插入到表中
    #详单至少需要包含如下信息：房间号、开始送风时间、结束送风时间、送风时长、风速、费率、费用
    def __init__(self,bill_id,room_id,user_id):
        self.bill_id = bill_id
        self.room_id = room_id
        self.user_id = user_id
        #其他所有信息直接从Air_sub里查        需要再将一些细节项加到Air_sub表中
        self.on_time = DBMapper.query("select on_time from Air_sub where room_id = "+self.bill_id+" and id = "+self.user_id)   #id??
        self.off_time = DBMapper.query("select off_time from Air_sub where room_id = "+self.bill_id+" and id = "+self.user_id)
        self.total_time = self.off_time - self.on_time
        self.wind_mode = DBMapper.query("select wind_mode from Air_sub where room_id = "+self.bill_id+" and id = "+self.user_id)
        self.cost_interest = DBMapper.query("select cost_interest from Air_sub where room_id = "+self.bill_id+" and id = "+self.user_id)
        #这个应该在Air_sub里根据温度和风速计算出了一个费率，但是表单里没这项,应该也要加入吧
        self.total_cost = DBMapper.query("select coat from Air_sub where bill_id = "+self.bill_id+" and id = "+self.user_id)



class Form:  # 报表的基类
    def __init__(self, form_id, room_id, b_time, e_time, air_on_times, air_off_times, tem_reach_times,
                         schedule_times, cost_all):
        self.form_id = form_id  # 报表号
        self.room_id = room_id  # 房间号
        self.b_time = b_time  # 开始时间
        self.e_time = e_time  # 结束时间
        self.air_on_times = air_on_times  # 子机开启次数
        self.air_off_times = air_off_times  # 子机关闭次数
        self.tem_reach_times = tem_reach_times  # 温度到达次数
        self.schedule_times = schedule_times  # 调度次数
        self.cost_all = cost_all  # 总消费金额

    def insert_data(self):  # 向数据库中插入表单数据
    def check_form_item(self):  # 获得报表表项信息
'''





































































