class Hotel:  # 酒店的基类
    def __init__(self, livein_num):
        self.livein_num = livein_num  # 当前入住总房间数
    def change_livein(self):  #入住房间数变化

class Room:#房间的基类
    def __init__(self, room_id, livein_times, tem):
        self.room_id = room_id
        self.livein_times = livein_times
        self.tem = tem

    def Change_tem(self):#环境温度改变


class User:#客户的基类
    def __init__(self,user_id,room_id,b_time,e_time ):
        self.user_id =user_id#客户号
        self.room_id = room_id#入住房间号
        self.b_time=b_time#入住时间
        self.e_time=e_time#退房时间

    def login(self):#入住，登录系统
    def air_on(self):#启动空调
    def air_off(self):#关闭空调
    def change_wind(self):#调节风速
    def change_tem(self):#调节温度
    def logout(self):#退房,退出系统


class Air_admin:  #空调管理员的基类
    def __init__(self, admin_id, if_login, status):
        self.admin_id = admin_id#管理员编号
        self.if_login = if_login#是否登录
        self.status = status#身份标识

    def login(self):  # 登录系统
    def power_on(self):  #初始化空调系统
    def init_air(self):  # 初始化空调参数
    def print_hotel(self):  # 查看酒店空调运行状态
    def print_room(self):  # 查看房间空调运行状态
    def logout(self):  # 退出系统


class Cashier:  # 酒店前台的基类
    def __init__(self, cashier_id, if_login, status):
        self.cashier_id = cashier_id#酒店前台编号
        self.if_login = if_login#是否登录
        self.status = status#身份标识

    def login(self):  # 登录系统
    def create_bill(self):  # 创建账单
    def print_bill(self):  # 查看账单
    def logout(self):  # 退出系统


class Manager:  # 酒店经理的基类
    def __init__(self, manager_id, if_login, status):
        self.manager_id = manager_id#经理编号
        self.if_login = if_login#是否登录
        self.status = status#身份标识

    def login(self):  #登录系统
    def create_form(self): #创建报表
    def print_form(self):  #查看报表
    def logout(self):  #退出系统


class Air_main:  # 空调主机的基类
    def __init__(self, air_on_num, wind_on_num, login_mode):
        self.air_on_num = air_on_num  # 开启子机数
        self.wind_on_num = wind_on_num  # 送风子机数
        self.login_mode = login_mode  # 登录模式

    def create_service(self):  # 创建服务对象
    def create_scheduler(self):  # 创建调度对象
    def create_air_sub(self):  # 创建空调子机对象
    def check_has(self):  # 查看酒店空调状态


class Air_sub:  # 空调子机的基类_
    def __init__(self, room_id, tem, wind_mode, cost, if_wind, if_on):
        self.room_id = room_id  # 房间号
        self.tem = tem  # 设定温度
        self.wind_mode = wind_mode  # 设定风速
        self.cost = cost  # 当前计费
        self.if_wind = if_wind  # 是否送风
        self.if_on = if_on  # 是否开启

    def insert_data(self):  # 向数据库插入数据
    def update_data(self):  # 更新数据库数据
    def check_ras(self):  # 查看酒店空调状态


class Service:  # 服务对象的基类
    def __init__(self, room_id, tem_set, wind_set):
        self.room_id = room_id  # 房间号
        self.tem_set = tem_set  # 目标温度
        self.wind_set = wind_set  # 目标风速

    def send_request(self):  # 发送送风请求
    def set_air_on(self):  # 开启空调
    def set_air_off(self):  # 关闭空调
    def set_wind_on(self):  # 开启送风
    def set_wind_off(self):  # 关闭送风
    def cost_on(self):  # 开启计费
    def cost_off(self):  # 关闭计费
    def set_tem(self):  # 设定温度
    def set_windmode(self):  # 设定风速


class Scheduler:  # 调度对象的基类
    def __init__(self, wait_num, success_num):
        self.wait_num = wait_num  # 送风等待数
        self.success_num = success_num  # 成功送风数

    def schedule_on(self):  # 执行调度算法


class Bill:  # 账单的基类
    def __init__(self, bill_id, room_id, b_time, e_time, cost_all):
        self.bill_id = bill_id  # 空调开启房间数
        self.room_id = room_id  # 空调送风房间数
        self.b_time = b_time  # 开始时间
        self.e_time = e_time  # 结束时间

    def insert_data(self):  # 向数据库中插入账单数据
    def check_bill_item(self):  # 获得账单详单表项信息


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




































































