class Manager:  # 酒店经理的基类
    def __init__(self, manager_id, if_login, status):
        self.manager_id = manager_id#经理编号
        self.if_login = if_login#是否登录
        self.status = status#身份标识

    def login(self):  #登录系统
        #后端写好再写

    def create_form(self): #创建报表
        room_id = 0 #获取自前端的参数
        b_time = 0 #获取自前端的参数
        e_time = 0 #获取自前端的参数
        r3 = Register_manager(room_id, b_time, e_time) 
        r3.create_form()

    def print_form(self):  #查看报表
        room_id = 0 #获取自前端的参数
        b_time = 0 #获取自前端的参数
        e_time = 0 #获取自前端的参数
        r3 = Register_manager(room_id, b_time, e_time)
        form_items = r3.print_form()

    def logout(self):  #退出系统、
        #后端写好再写

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
        #(1)首先从数据库中查询出其他信息，等后端确定后再写
        #(1)get air_on_times, air_off_times, tem_reach_times, schedule_times, cost_all
        #(2) 将所有信息插入数据库：insert into form values(...)
        #(3) 利用查询出的信息，更新当前Form类的值

    def check_form_item(self):  # 获得报表表项信息
        #根据form_id 从数据库中查询form即可
        return form_items
