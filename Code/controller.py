import application as app
import database as db

class Register_user2:#客户入住
    '''
    modified by 谢祎凡
    '''
    def __init__(self, room_id, user_id, time):
        self.room_id = room_id
        self.user_id = user_id
        self.time = time #入住时为入住时间，退房时为退房时间
        self.bill = app.user_in(self.room_id, self.user_id, 0,0,0) 

    def u_in(self):#客户入住
        self.bill.in_bill(self.room_id, self.user_id, self.time)
    def u_out(self):#客户退房
        self.bill.out_bill(self.room_id, self.user_id, self.time)

class Register_user:  # 控制器0的基类
    '''
    modified by 刘峰麟 on 6.26
        增加了形参air_monitor
    '''

    def air_on(self,air_subs, services,room_id,air_monitor):#开启空调,需要送风调度
        services[room_id-1].set_air_on(air_subs[room_id-1],air_monitor)

    def air_off(self,air_subs,services,room_id,air_monitor):#关闭空调,无需送风调度
        services[room_id-1].set_air_off(air_subs[room_id-1],air_monitor)
        services[room_id-1].set_wind_off(air_subs[room_id-1],air_monitor)

    def change_wind(self,windmode,air_subs,services,room_id,air_monitor):#调节风速，需要送风调度
        services[room_id-1].wind_set=windmode
        services[room_id-1].set_windmode(air_subs[room_id-1],air_monitor)

    def change_tem(self,tem_set,air_subs,services,room_id,air_monitor):#调节温度，无需送风调度
        services[room_id-1].tem_set=tem_set
        services[room_id-1].set_tem(air_subs[room_id-1],air_monitor)

class Register_admin:#控制器1的基类
    def power_on(self):#初始化空调系统
        air_main=app.Air_main(0,0,0)#创建空调主机实例
        air_subs=air_main.create_air_sub()#创建空调子机实例
        scheduler=air_main.create_scheduler()#创建调度器实例
        services=air_main.create_service()#创建服务器实例
        return air_main,air_subs,services,scheduler

    def init_air(self,services,air_main,air_on_num,wind_on_num,wait_on_num,air_sub,tem, wind_mode, cost, if_wind, if_on):#空调子机参数初始化
        air_main.air_on_num = air_on_num
        air_main.wind_on_num=wind_on_num
        air_main.wait_on_num=wait_on_num

        for i in range(0,5):
            air_sub[i].tem = tem
            air_sub[i].wind_mode = wind_mode
            services[i].tem_set = tem
            services[i].wind_set = wind_mode
            air_sub[i].if_wind = if_wind
            air_sub[i].if_on = if_on
            air_sub[i].cost = cost

class Register_cashier:#控制器2的基类
    '''
    modified by 张佳颖
    '''
    #账单至少包含如下信息：房间号、总费用、入住时间、离店时间。
    def __init__(self, user_id, room_id):          #认为只需要从用户界面获取user_id,room_id即可定位到订单信息
        self.user_id = user_id
        self.room_id = room_id
        self.bill = app.Bill(self.user_id, self.room_id)
        self.detail = app.Details(self.user_id,room_id)

    def check_bill(self):
        b_time,e_time,cost = self.bill.check_bill()
        return b_time,e_time,cost

    def create_detail(self):
        self.detail.create()

    def update_bill(self):
        self.detail.update_bill()

    def check_detail(self):
        rows,records = self.detail.check()
        return rows,records              #可能多项

class Register_manager:#控制器3的基类
    '''
    modified by 谢祎凡
    '''
    def __init__(self, room_id, b_time, e_time):
        self.room_id = room_id
        self.b_time = b_time
        self.e_time = e_time
        self.form_id = room_id+"-"+str(b_time)+str(e_time) #自定义一种form_id的生成规则
        self.form = app.Form(self.form_id, self.room_id, self.b_time, self.e_time, 0,0,0,0,0,0,0,0) #其它设置为0等待插入form时更新

    def create_form(self):#创建报表
        air_on_times, air_off_times, use_time, schedule_times, change_tem_times, change_wind_times, details_number, cost_all = self.form.insert_data()
        return air_on_times, air_off_times, use_time, schedule_times, change_tem_times, change_wind_times, details_number, cost_all

    def print_form(self):#查看报表
        form_items = self.form.check_form_item()
        return form_items



