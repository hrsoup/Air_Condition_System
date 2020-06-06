from database import DBMapper
from application import Bill

class Register_user:#������0�Ļ���
    def air_on(self):#�����յ�
    def air_off(self):#�رտյ�
    def change_wind(self):#���ڷ���
    def change_tem(self):#�����¶�


class Register_admin:#������1�Ļ���
    def create_air_main(self):#�����յ�����ʵ��
    def power_on(self):#��ʼ���յ�ϵͳ
    def init_air(self):#�յ��ӻ�������ʼ��
    def print_hotel(self):#�鿴�Ƶ�յ�����״̬
    def print_room(self):#�鿴����յ�����״̬

class Register_cashier:#������2�Ļ���
    def __init__(self, user_id, room_id):          #��Ϊֻ��Ҫ���û������ȡuser_id,room_id���ɶ�λ
        self.user_id = user_id
        self.room_id = room_id
        self.bill_id = user_id+"-"+room_id         #�Զ���һ��bill_id�����ɹ���
        self.bill = Bill(bill_id=self.bill_id, room_id=self.room_id, b_time=0, e_time=0,cost_all=0)

    def create_bill(self):#�����˵��굥
        self.bill.insert_data(self.bill_id)

    def print_bill(self):#�鿴�˵��굥
        record = self.bill.check_bill_item(self.bill_id)
        return record

    def get_begin(self):#��ȡ�û���סʱ��
        query_b = "select b_time from User_item where user_id="+self.user_id
        st = DBMapper.query(query_b)
        if st.count() != 0:                     #���ز�Ϊ��
            return st
        else:
            return -1


    def get_end(self):#��ȡ�û��˷�ʱ��
        query_e ="select e_time from User_item where user_id="+self.user_id
        et = DBMapper.query(query_e)
        if et.count() != 0:
            return et
        else:
            return -1


class Register_manager:#������3�Ļ���
    def create_form(self):#��������
    def print_form(self):#�鿴����
