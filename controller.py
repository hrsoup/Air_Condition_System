class Register_user:#控制器0的基类
    def air_on(self):#开启空调
    def air_off(self):#关闭空调
    def change_wind(self):#调节风速
    def change_tem(self):#调节温度


class Register_admin:#控制器1的基类
    def create_air_main(self):#创建空调主机实例
    def power_on(self):#初始化空调系统
    def init_air(self):#空调子机参数初始化
    def print_hotel(self):#查看酒店空调运行状态
    def print_room(self):#查看房间空调运行状态


class Register_cashier:#控制器2的基类
    def create_bill(self):#创建账单详单
    def print_bill(self):#查看账单详单
    def get_begin(self):#获取用户入住时间
    def get_end(self):#获取用户退房时间


class Register_manager:#控制器3的基类
    def create_form(self):#创建报表
    def print_form(self):#查看报表