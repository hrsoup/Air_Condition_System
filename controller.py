import application as app
#import database as db

class Register_user:  # 控制器0的基类
    def air_on(self, air_subs, services,scheduler,room_id):#开启空调,需要送风调度
        services[room_id-1].set_air_on(air_subs[room_id-1])
        scheduler.schedule_on(air_subs,services,room_id)

    def air_off(self,air_subs,services,room_id):#关闭空调,无需送风调度
        services[room_id-1].set_air_off(air_subs[room_id-1])
        services[room_id].set_wind_off(air_subs[room_id-1])

    def change_wind(self,windmode,air_subs,services,scheduler,room_id):#调节风速，需要送风调度
        services[room_id-1].tem_set=air_subs[room_id-1].tem
        services[room_id-1].wind_set=windmode
        scheduler.schedule_on(air_subs,services,room_id)

    def change_tem(self,tem_set,air_subs,services,room_id):#调节温度，无需送风调度
        services[room_id-1].tem_set=tem_set
        services[room_id-1].set_tem(air_subs[room_id-1])

class Register_admin:#控制器1的基类
    def power_on(self):#初始化空调系统
        air_main=app.Air_main(0,0,0)#创建空调主机实例
        air_subs=air_main.create_air_sub()#创建空调子机实例
        scheduler=air_main.create_scheduler()#创建调度器实例
        services=air_main.create_service()#创建服务器实例
        return air_main,air_subs,services,scheduler

    def init_air(self,air_main,air_on_num,wind_on_num,wait_on_num,air_sub,tem, wind_mode, cost, if_wind, if_on):#空调子机参数初始化
        air_main.air_on_num = air_on_num
        air_main.wind_on_num=wind_on_num
        air_main.wait_on_num=wait_on_num
        for i in range(0,5):
            air_sub[i].tem = tem
            air_sub[i].wind_mode = wind_mode
            air_sub[i].if_wind = if_wind
            air_sub[i].if_on = if_on
            air_sub[i].cost = cost



class Register_cashier:#控制器2的基类
    #账单至少包含如下信息：房间号、总费用、入住时间、离店时间。
    def __init__(self, user_id, room_id):          #认为只需要从用户界面获取user_id,room_id即可定位到订单信息
        self.user_id = user_id
        self.room_id = room_id
        self.bill_id = user_id+"-"+room_id         #自定义一种bill_id的生成规则
        self.bill = Bill(bill_id=self.bill_id, room_id=self.room_id, b_time=self.get_begin(), e_time=self.get_end(),cost_all=0)
        self.detail = Details(self.bill_id,self.room_id,self.user_id)         #详单，只有属性值供输出

    def create_bill(self):#创建账单详单
        self.bill.insert_data(self.bill_id)

    def print_bill(self):#查看账单
        record = self.bill.check_bill_item(self.bill_id)
        return record

    def get_begin(self):#获取用户入住时间——直接从User_item表中查
        sql_b = "select b_time from User_item where user_id="+self.user_id
        st = DBMapper.query(sql_b)
        if st.count() != 0:
            return st
        else:
            return -1                           #用户尚未入住的情况


    def get_end(self):#获取用户退房时间
        query_e ="select e_time from User_item where user_id="+self.user_id
        et = DBMapper.query(query_e)
        if et.count() != 0:
            return et
        else:
            return -1                            #用户尚未入住

class Register_manager:#控制器3的基类
    def __init__(self, room_id, b_time, e_time):
        self.room_id = room_id
        self.b_time = b_time
        self.e_time = e_time
        self.form_id = room_id+"-"+b_time #自定义一种form_id的生成规则
        self.form = Form(self.form_id, self.room_id, self.b_time, self.e_time, 0,0,0,0,0) #其它设置为0等待插入form时更新

    def create_form(self):#创建报表
        self.form.insert_data(self.form_id, self.room_id, self.b_time, self.e_time)

    def print_form(self):#查看报表
        form_items = self.form.check_form_item(self.form_id)
        return form_items



