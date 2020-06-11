from database import DBMapper

class Hotel:  # �Ƶ�Ļ���
    def __init__(self, livein_num):
        self.livein_num = livein_num  # ��ǰ��ס�ܷ�����
    def change_livein(self):  #��ס�������仯

class Room:#����Ļ���
    def __init__(self, room_id, livein_times, tem):
        self.room_id = room_id
        self.livein_times = livein_times
        self.tem = tem

    def Change_tem(self):#�����¶ȸı�

class Air_main:  # �յ������Ļ���
    def __init__(self, air_on_num, wind_on_num, login_mode):
        self.air_on_num = air_on_num #�����ӻ���
        self.wind_on_num = wind_on_num #�ͷ��ӻ���
        self.login_mode = login_mode #��¼ģʽ

    def create_service(self):  # �����������
    def create_scheduler(self):  # �������ȶ���
    def create_air_sub(self):  # �����յ��ӻ�����
    def check_has(self):  # �鿴�Ƶ�յ�״̬

class Air_sub:  # �յ��ӻ��Ļ���_
    def __init__(self, room_id, tem, wind_mode, cost, if_wind, if_on):
        self.room_id = room_id  # �����
        self.tem = tem  # �趨�¶�
        self.wind_mode = wind_mode  # �趨����
        self.cost = cost  # ��ǰ�Ʒ�
        self.if_wind = if_wind  # �Ƿ��ͷ�
        self.if_on = if_on  # �Ƿ���

    def insert_data(self):  # �����ݿ��������
    def update_data(self):  # �������ݿ�����
    def check_ras(self):  # �鿴�Ƶ�յ�״̬


class Service:  # �������Ļ���
    def __init__(self, room_id, tem_set, wind_set):
        self.room_id = room_id  # �����
        self.tem_set = tem_set  # Ŀ���¶�
        self.wind_set = wind_set  # Ŀ�����

    def send_request(self):  # �����ͷ�����
    def set_air_on(self):  # �����յ�
    def set_air_off(self):  # �رտյ�
    def set_wind_on(self):  # �����ͷ�
    def set_wind_off(self):  # �ر��ͷ�
    def cost_on(self):  # �����Ʒ�
    def cost_off(self):  # �رռƷ�
    def set_tem(self):  # �趨�¶�
    def set_windmode(self):  # �趨����


class Scheduler:  # ���ȶ���Ļ���
    def __init__(self, wait_num, success_num):
        self.wait_num = wait_num  # �ͷ�ȴ���
        self.success_num = success_num  # �ɹ��ͷ���

    def schedule_on(self):  # ִ�е����㷨


class Bill:  # �˵��Ļ���
    def __init__(self, bill_id, room_id, b_time, e_time, cost_all):
        self.bill_id = bill_id  # �˵����
        self.room_id = room_id  # �յ��ͷ緿����
        self.b_time = b_time  # ��סʱ��
        self.e_time = e_time  # ���ʱ��
        self.cost_all = cost_all

    def insert_data(self):  # �����ݿ��в����˵�����
        values = self.bill_id+","+self.room_id+","+self.b_time+","+self.e_time+","+self.cost_all
        DBMapper.insert("Bill_item",values)            #cost_all��ҪAir_sub�ڿյ��ػ�ʱupdate

    def check_bill_item(self,bill_id):  # ����˵��굥������Ϣ
        record = DBMapper.query("select * from Bill_item where bill_id = "+bill_id)
        return record

    # insert(table_name,values)
    # query(sql���)

class Details:        #�굥���ֻ࣬��¼��Ϣ�����ǿͻ��˷������Ҫ��ӡ�굥������Ĭ�ϲ�ѯ����Ѳ��뵽����
    #�굥������Ҫ����������Ϣ������š���ʼ�ͷ�ʱ�䡢�����ͷ�ʱ�䡢�ͷ�ʱ�������١����ʡ�����
    def __init__(self,bill_id,room_id,user_id):
        self.bill_id = bill_id
        self.room_id = room_id
        self.user_id = user_id
        #����������Ϣֱ�Ӵ�Air_sub���        ��Ҫ�ٽ�һЩϸ����ӵ�Air_sub����
        self.on_time = DBMapper.query("select on_time from Air_sub where room_id = "+self.bill_id+" and id = "+self.user_id)   #id??
        self.off_time = DBMapper.query("select off_time from Air_sub where room_id = "+self.bill_id+" and id = "+self.user_id)
        self.total_time = self.off_time - self.on_time
        self.wind_mode = DBMapper.query("select wind_mode from Air_sub where room_id = "+self.bill_id+" and id = "+self.user_id)
        self.cost_interest = DBMapper.query("select cost_interest from Air_sub where room_id = "+self.bill_id+" and id = "+self.user_id)
        #���Ӧ����Air_sub������¶Ⱥͷ��ټ������һ�����ʣ����Ǳ���û����,Ӧ��ҲҪ�����
        self.total_cost = DBMapper.query("select coat from Air_sub where bill_id = "+self.bill_id+" and id = "+self.user_id)



class Form:  # ����Ļ���
    def __init__(self, form_id, room_id, b_time, e_time, air_on_times, air_off_times, tem_reach_times,
                         schedule_times, cost_all):
        self.form_id = form_id  # �����
        self.room_id = room_id  # �����
        self.b_time = b_time  # ��ʼʱ��
        self.e_time = e_time  # ����ʱ��
        self.air_on_times = air_on_times  # �ӻ���������
        self.air_off_times = air_off_times  # �ӻ��رմ���
        self.tem_reach_times = tem_reach_times  # �¶ȵ������
        self.schedule_times = schedule_times  # ���ȴ���
        self.cost_all = cost_all  # �����ѽ��

    def insert_data(self):  # �����ݿ��в��������
    def check_form_item(self):  # ��ñ��������Ϣ




































































