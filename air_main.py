class Air_main:  # 空调主机的基类
    def __init__(self, air_on_num, wind_on_num, login_mode):
        self.air_on_num = air_on_num
        self.wind_on_num = wind_on_num
        self.login_mode = login_mode

    def tem_ctrl(self):  #温控平衡
    def set_if_on(self): #设置对应空调子机开启
    def cost_on(self):   #计费开启
    def cost_off(self):  #计费关闭
    def create_rs(self): #创建调度服务接收器实例
    def create_as(self): #创建空调子机实例
    def init_air(self):  #初始化空调子机参数
    def create_has(self):#创建酒店空调状态实例
    def get_begin(self): #获得用户入住时间
    def get_end(self):   #获得用户退房时间









