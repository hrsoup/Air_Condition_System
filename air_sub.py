class Air_sub:  # 空调子机的基类
    def __init__(self, room_id, tem, wind_mode, cost):
        self.room_id = room_id
        self.tem = tem
        self.wind_mode = wind_mode
        self.cost = cost

    def tem_ctrl(self):   # 温控平衡
    def get_btime(self):  # 获取开始送风时间
    def get_etime(self):  # 获取停止送风时间
    def create_ras(self): # 创建房间空调状态对象
    def check_ras(self):  # 获得房间空调状态信息
    def update_ras(self): # 更新房间空调状态信息








