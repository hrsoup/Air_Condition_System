'''
import controller as ctrl
import application as app
import database as db

'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Welcome(QMainWindow):#��ʼ������
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(130, 70, 561, 101))
        self.label_1.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(30)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(280, 340, 241, 61))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(12)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")
        self.roleselect = QtWidgets.QComboBox(self.centralwidget)
        self.roleselect.setGeometry(QtCore.QRect(280, 240, 241, 61))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(12)
        self.roleselect.setFont(font)
        self.roleselect.setObjectName("roleselect")
        self.roleselect.addItem("")
        self.roleselect.addItem("")
        self.roleselect.addItem("")
        self.roleselect.addItem("")
        self.roleselect.currentIndexChanged.connect(self.selectionchange)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "�ֲ�ʽ�¿�ϵͳ"))
        self.label_1.setText(_translate("MainWindow", "��ӭʹ�÷ֲ�ʽ�¿�ϵͳ"))
        self.enter.setText(_translate("MainWindow", "����ϵͳ"))
        self.roleselect.setItemText(0, _translate("MainWindow", "�ͻ�"))
        self.roleselect.setItemText(1, _translate("MainWindow", "�յ�����Ա"))
        self.roleselect.setItemText(2, _translate("MainWindow", "�Ƶ�ǰ̨"))
        self.roleselect.setItemText(3, _translate("MainWindow", "�Ƶ꾭��"))

    def selectionchange(self):
        if (welcome.roleselect.currentText() == '�ͻ�'):
            # �ͻ���·��ת�߼�
            welcome.enter.clicked.connect(move_select.show)
            welcome.enter.clicked.connect(welcome.closewin)
            welcome.enter.clicked.connect(admin_select.closewin)
            welcome.enter.clicked.connect(cashier_select.closewin)
            welcome.enter.clicked.connect(manager_select.closewin)

        elif (welcome.roleselect.currentText() == '�յ�����Ա'):
            # �յ�����Ա��·��ת�߼�
            welcome.enter.clicked.connect(admin_select.show)
            welcome.enter.clicked.connect(welcome.closewin)
            welcome.enter.clicked.connect(cashier_select.closewin)
            welcome.enter.clicked.connect(manager_select.closewin)
            welcome.enter.clicked.connect(move_select.closewin)

        elif (welcome.roleselect.currentText() == '�Ƶ�ǰ̨'):
            # �Ƶ�ǰ̨��·��ת�߼�
            welcome.enter.clicked.connect(cashier_select.show)
            welcome.enter.clicked.connect(welcome.closewin)
            welcome.enter.clicked.connect(admin_select.closewin)
            welcome.enter.clicked.connect(manager_select.closewin)
            welcome.enter.clicked.connect(move_select.closewin)

        elif (welcome.roleselect.currentText() == '�Ƶ꾭��'):
            # �Ƶ꾭����ת�߼�
            welcome.enter.clicked.connect(manager_select.show)
            welcome.enter.clicked.connect(welcome.closewin)
            welcome.enter.clicked.connect(cashier_select.closewin)
            welcome.enter.clicked.connect(admin_select.closewin)
            welcome.enter.clicked.connect(move_select.closewin)

    def closewin(self):
        self.close()

class Move_select(QMainWindow):#�û�ѡ�����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(290, 90, 231, 91))
        self.label_1.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.movein = QtWidgets.QPushButton(self.centralwidget)
        self.movein.setGeometry(QtCore.QRect(270, 200, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.movein.setFont(font)
        self.movein.setObjectName("movein")
        self.moveout = QtWidgets.QPushButton(self.centralwidget)
        self.moveout.setGeometry(QtCore.QRect(270, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.moveout.setFont(font)
        self.moveout.setObjectName("moveout")
        self.enterroom = QtWidgets.QPushButton(self.centralwidget)
        self.enterroom.setGeometry(QtCore.QRect(270, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.enterroom.setFont(font)
        self.enterroom.setObjectName("enterroom")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(270, 350, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "��ӭ����"))
        self.label_1.setText(_translate("MainWindow", "��ѡ���������"))
        self.movein.setText(_translate("MainWindow", "������ס"))
        self.moveout.setText(_translate("MainWindow", "�����˷�"))
        self.enterroom.setText(_translate("MainWindow", "���뷿��"))
        self.exit.setText(_translate("MainWindow", "�˳�ϵͳ"))

    def closewin(self):
        self.close()

class Move_in(QMainWindow):#ȷ����ס����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(170, 50, 461, 111))
        self.label_1.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(280, 220, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(16)
        self.roomselect.setFont(font)
        self.roomselect.setObjectName("roomselect")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.movein_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.movein_confirm.setGeometry(QtCore.QRect(280, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.movein_confirm.setFont(font)
        self.movein_confirm.setObjectName("movein_confirm")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(280, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "������ס"))
        self.label_1.setText(_translate("MainWindow", "���ã���ѡ�񷿼�Ű�����ס����"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.movein_confirm.setText(_translate("MainWindow", "ȷ����ס"))
        self.back.setText(_translate("MainWindow", "����"))

    def closewin(self):
        self.close()

class Move_out(QMainWindow):#ȷ���˷�����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(170, 50, 621, 141))
        self.label_1.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(280, 210, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(16)
        self.roomselect.setFont(font)
        self.roomselect.setObjectName("roomselect")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.moveout_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.moveout_confirm.setGeometry(QtCore.QRect(280, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.moveout_confirm.setFont(font)
        self.moveout_confirm.setObjectName("moveout_confirm")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(280, 390, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "�����˷�"))
        self.label_1.setText(_translate("MainWindow", "���ã���ѡ�񷿼�Ű����˷�����"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.moveout_confirm.setText(_translate("MainWindow", "ȷ���˷�"))
        self.back.setText(_translate("MainWindow", "����"))

    def closewin(self):
        self.close()

class Enter_room(QMainWindow):#���뷿�����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.setObjectName("MainWindow")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./corridor.jpg")))
        self.setPalette(window_pale)
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(220, 70, 371, 91))
        self.label_1.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(280, 220, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(16)
        self.roomselect.setFont(font)
        self.roomselect.setObjectName("roomselect")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.movein_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.movein_confirm.setGeometry(QtCore.QRect(280, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.movein_confirm.setFont(font)
        self.movein_confirm.setObjectName("movein_confirm")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(280, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "���뷿��"))
        self.label_1.setText(_translate("MainWindow", "���ã���ѡ�������ڵķ���"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.movein_confirm.setText(_translate("MainWindow", "���뷿��"))
        self.back.setText(_translate("MainWindow", "����"))

    def closewin(self):
        self.close()

class Air_monitor(QMainWindow):#�յ�����������
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./room.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.change_tem = QtWidgets.QSpinBox(self.centralwidget)
        self.change_tem.setGeometry(QtCore.QRect(130, 100, 381, 91))
        font = QtGui.QFont()
        font.setFamily("����")
        font.setPointSize(32)
        self.change_tem.setFont(font)
        self.change_tem.setObjectName("change_tem")
        self.change_wind = QtWidgets.QSpinBox(self.centralwidget)
        self.change_wind.setGeometry(QtCore.QRect(130, 220, 381, 91))
        font = QtGui.QFont()
        font.setFamily("����")
        font.setPointSize(32)
        self.change_wind.setFont(font)
        self.change_wind.setObjectName("change_wind")
        self.air_on = QtWidgets.QPushButton(self.centralwidget)
        self.air_on.setGeometry(QtCore.QRect(580, 110, 151, 61))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(12)
        self.air_on.setFont(font)
        self.air_on.setObjectName("air_on")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 120, 81, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_1.setStyleSheet("color:white");
        self.cost_now = QtWidgets.QTextBrowser(self.centralwidget)
        self.cost_now.setGeometry(QtCore.QRect(140, 360, 371, 91))
        self.cost_now.setObjectName("cost_now")
        self.air_off = QtWidgets.QPushButton(self.centralwidget)
        self.air_off.setGeometry(QtCore.QRect(580, 210, 151, 61))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(12)
        self.air_off.setFont(font)
        self.air_off.setObjectName("air_off")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(580, 390, 151, 61))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 81, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color:white");
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 390, 81, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color:white");
        self.check_cost = QtWidgets.QPushButton(self.centralwidget)
        self.check_cost.setGeometry(QtCore.QRect(580, 300, 151, 61))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(12)
        self.check_cost.setFont(font)
        self.check_cost.setObjectName("check_cost")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "�յ��ӻ��������"))
        self.air_on.setText(_translate("MainWindow", "����"))
        self.label_1.setText(_translate("MainWindow", "�¶�"))
        self.air_off.setText(_translate("MainWindow", "�ػ�"))
        self.back.setText(_translate("MainWindow", "����"))
        self.label_3.setText(_translate("MainWindow", "����"))
        self.label_4.setText(_translate("MainWindow", "����"))
        self.check_cost.setText(_translate("MainWindow", "�鿴��ǰ����"))

    def closewin(self):
        self.close()

class Admin_select(QMainWindow):#����Աѡ�����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome1 = QtWidgets.QLabel(self.centralwidget)
        self.welcome1.setGeometry(QtCore.QRect(280, 80, 241, 101))
        self.welcome1.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.welcome1.setFont(font)
        self.welcome1.setObjectName("welcome1")
        self.check_has = QtWidgets.QPushButton(self.centralwidget)
        self.check_has.setGeometry(QtCore.QRect(270, 210, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.check_has.setFont(font)
        self.check_has.setObjectName("check_has")
        self.check_ras = QtWidgets.QPushButton(self.centralwidget)
        self.check_ras.setGeometry(QtCore.QRect(270, 280, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.check_ras.setFont(font)
        self.check_ras.setObjectName("check_ras")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(270, 350, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "���ã�����Ա"))
        self.welcome1.setText(_translate("MainWindow", "��ѡ���������"))
        self.check_has.setText(_translate("MainWindow", "�鿴�Ƶ�յ�״̬"))
        self.check_ras.setText(_translate("MainWindow", "�鿴����յ�״̬"))
        self.exit.setText(_translate("MainWindow", "�˳�ϵͳ"))

    def closewin(self):
        self.close()

class Hotel_air_state(QMainWindow):#��ѯ�Ƶ�յ�״̬����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(290, 20, 191, 121))
        self.label_1.setStyleSheet("color:red");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lcd_aironnum = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_aironnum.setGeometry(QtCore.QRect(440, 160, 171, 61))
        self.lcd_aironnum.setObjectName("lcd_aironnum")
        self.lcd_windonnum = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_windonnum.setGeometry(QtCore.QRect(440, 260, 171, 61))
        self.lcd_windonnum.setObjectName("lcd_windonnum")
        self.lcd_waitnum = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_waitnum.setGeometry(QtCore.QRect(440, 360, 171, 61))
        self.lcd_waitnum.setObjectName("lcd_waitnum")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 140, 191, 101))
        self.label_2.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 240, 191, 101))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 340, 191, 101))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(190, 470, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(400, 470, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "��ѯ�Ƶ�յ�״̬"))
        self.label_1.setText(_translate("MainWindow", "�Ƶ�յ���Ϣ"))
        self.label_2.setText(_translate("MainWindow", "�����յ���"))
        self.label_3.setText(_translate("MainWindow", "�ͷ�յ���"))
        self.label_4.setText(_translate("MainWindow", "�ȴ�������"))
        self.check.setText(_translate("MainWindow", "��ѯ"))
        self.back.setText(_translate("MainWindow", "����"))

    def closewin(self):
        self.close()

class Room_air_state(QMainWindow):#��ѯ����յ�״̬����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./room.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(260, -10, 271, 131))
        self.label1.setStyleSheet("color:red");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.lcd_ifair = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_ifair.setGeometry(QtCore.QRect(580, 110, 171, 61))
        self.lcd_ifair.setObjectName("lcd_ifair")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(70, 190, 211, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.roomselect.setFont(font)
        self.roomselect.setObjectName("roomselect")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 100, 101, 81))
        self.label_2.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcd_ifwind = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_ifwind.setGeometry(QtCore.QRect(580, 180, 171, 61))
        self.lcd_ifwind.setObjectName("lcd_ifwind")
        self.lcd_tem = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_tem.setGeometry(QtCore.QRect(580, 250, 171, 61))
        self.lcd_tem.setObjectName("lcd_tem")
        self.lcd_windmode = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_windmode.setGeometry(QtCore.QRect(580, 320, 171, 61))
        self.lcd_windmode.setObjectName("lcd_windmode")
        self.lcd_cost = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_cost.setGeometry(QtCore.QRect(580, 390, 171, 61))
        self.lcd_cost.setObjectName("lcd_cost")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 80, 191, 121))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 150, 191, 121))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 220, 191, 121))
        self.label_5.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 360, 191, 121))
        self.label_7.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 290, 191, 121))
        self.label_6.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(90, 380, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(90, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "��ѯ����յ�״̬"))
        self.label1.setText(_translate("MainWindow", "����յ���Ϣ��ѯ"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "�����"))
        self.label_3.setText(_translate("MainWindow", "�Ƿ���"))
        self.label_4.setText(_translate("MainWindow", "�Ƿ��ͷ�"))
        self.label_5.setText(_translate("MainWindow", "�趨�¶�"))
        self.label_7.setText(_translate("MainWindow", "��ǰ����"))
        self.label_6.setText(_translate("MainWindow", "�趨����"))
        self.back.setText(_translate("MainWindow", "����"))
        self.check.setText(_translate("MainWindow", "��ѯ"))

    def closewin(self):
        self.close()

class Cashier_select(QMainWindow):#�Ƶ�ǰ̨ѡ�����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(290, 130, 221, 71))
        self.label_1.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.check_bill = QtWidgets.QPushButton(self.centralwidget)
        self.check_bill.setGeometry(QtCore.QRect(270, 240, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.check_bill.setFont(font)
        self.check_bill.setObjectName("check_bill")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(270, 310, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "���ã��Ƶ�ǰ̨"))
        self.label_1.setText(_translate("MainWindow", "��ѡ���������"))
        self.check_bill.setText(_translate("MainWindow", "�鿴����ӡ�˵�"))
        self.exit.setText(_translate("MainWindow", "�˳�ϵͳ"))

    def closewin(self):
        self.close()

class Check_bill(QMainWindow):#�˵���ѯ����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./room.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(340, 10, 141, 111))
        self.label_1.setStyleSheet("color:red");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lcd_btime = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_btime.setGeometry(QtCore.QRect(570, 140, 171, 61))
        self.lcd_btime.setObjectName("lcd_btime")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(130, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.roomselect.setFont(font)
        self.roomselect.setObjectName("roomselect")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 101, 81))
        self.label_2.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcd_etime = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_etime.setGeometry(QtCore.QRect(570, 240, 171, 61))
        self.lcd_etime.setObjectName("lcd_etime")
        self.lcd_cost_all = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_cost_all.setGeometry(QtCore.QRect(570, 350, 171, 61))
        self.lcd_cost_all.setObjectName("lcd_cost_all")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 110, 191, 121))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 210, 191, 121))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 320, 191, 121))
        self.label_5.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(90, 420, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(90, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 101, 81))
        self.label_8.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.userselect = QtWidgets.QComboBox(self.centralwidget)
        self.userselect.setGeometry(QtCore.QRect(130, 200, 211, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.userselect.setFont(font)
        self.userselect.setObjectName("userselect")
        self.userselect.addItem("")
        self.userselect.addItem("")
        self.userselect.addItem("")
        self.userselect.addItem("")
        self.userselect.addItem("")
        self.print = QtWidgets.QPushButton(self.centralwidget)
        self.print.setGeometry(QtCore.QRect(90, 360, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.print.setFont(font)
        self.print.setObjectName("print")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "�˵���ѯ"))
        self.label_1.setText(_translate("MainWindow", "�˵���ѯ"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "�����"))
        self.label_3.setText(_translate("MainWindow", "��סʱ��"))
        self.label_4.setText(_translate("MainWindow", "�˷�ʱ��"))
        self.label_5.setText(_translate("MainWindow", "�����ѽ��"))
        self.back.setText(_translate("MainWindow", "����"))
        self.check.setText(_translate("MainWindow", "��ѯ"))
        self.label_8.setText(_translate("MainWindow", "�ͻ���"))
        self.userselect.setItemText(0, _translate("MainWindow", "1"))
        self.userselect.setItemText(1, _translate("MainWindow", "2"))
        self.userselect.setItemText(2, _translate("MainWindow", "3"))
        self.userselect.setItemText(3, _translate("MainWindow", "4"))
        self.userselect.setItemText(4, _translate("MainWindow", "5"))
        self.print.setText(_translate("MainWindow", "��ӡ"))

    def closewin(self):
        self.close()

class Manager_select(QMainWindow):#����ѡ�����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(290, 120, 231, 91))
        self.label_1.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.check_form = QtWidgets.QPushButton(self.centralwidget)
        self.check_form.setGeometry(QtCore.QRect(270, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.check_form.setFont(font)
        self.check_form.setObjectName("check_form")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(270, 320, 251, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "���ã��Ƶ꾭��"))
        self.label_1.setText(_translate("MainWindow", "��ѡ���������"))
        self.check_form.setText(_translate("MainWindow", "�鿴����ӡ����"))
        self.exit.setText(_translate("MainWindow", "�˳�ϵͳ"))

    def closewin(self):
        self.close()

class Check_form(QMainWindow):#�����ѯ����
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./room.jpg")))
        self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(310, 10, 271, 131))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_1.setStyleSheet("color:red");
        self.lcd_airontimes = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_airontimes.setGeometry(QtCore.QRect(560, 120, 171, 61))
        self.lcd_airontimes.setObjectName("lcd_airontimes")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(160, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.roomselect.setFont(font)
        self.roomselect.setObjectName("roomselect")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 101, 81))
        self.label_2.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:white");
        self.lcd_airofftimes = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_airofftimes.setGeometry(QtCore.QRect(560, 200, 171, 61))
        self.lcd_airofftimes.setObjectName("lcd_airofftimes")
        self.lcd_tem_reach_times = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_tem_reach_times.setGeometry(QtCore.QRect(560, 280, 171, 61))
        self.lcd_tem_reach_times.setObjectName("lcd_tem_reach_times")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 90, 191, 121))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 250, 191, 121))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 170, 191, 121))
        self.label_7.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(70, 460, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(70, 340, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 151, 71))
        self.label_8.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btime_select = QtWidgets.QSpinBox(self.centralwidget)
        self.btime_select.setGeometry(QtCore.QRect(160, 190, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btime_select.setFont(font)
        self.btime_select.setObjectName("btime_select")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 240, 151, 71))
        self.label_9.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.etime_select = QtWidgets.QSpinBox(self.centralwidget)
        self.etime_select.setGeometry(QtCore.QRect(160, 250, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.etime_select.setFont(font)
        self.etime_select.setObjectName("etime_select")
        self.lcd_schedule_times = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_schedule_times.setGeometry(QtCore.QRect(560, 360, 171, 61))
        self.lcd_schedule_times.setObjectName("lcd_schedule_times")
        self.lcd_cost_all = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_cost_all.setGeometry(QtCore.QRect(560, 430, 171, 61))
        self.lcd_cost_all.setObjectName("lcd_cost_all")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 330, 191, 121))
        self.label_5.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 400, 191, 121))
        self.label_6.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.print = QtWidgets.QPushButton(self.centralwidget)
        self.print.setGeometry(QtCore.QRect(70, 400, 171, 51))
        font = QtGui.QFont()
        font.setFamily("΢���ź� Light")
        font.setPointSize(14)
        self.print.setFont(font)
        self.print.setObjectName("print")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "�����ѯ"))
        self.label_1.setText(_translate("MainWindow", "�����ѯ"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "�����"))
        self.label_3.setText(_translate("MainWindow", "�յ���������"))
        self.label_4.setText(_translate("MainWindow", "��Ŀ���¶ȴ���"))
        self.label_7.setText(_translate("MainWindow", "�յ��رմ���"))
        self.back.setText(_translate("MainWindow", "����"))
        self.check.setText(_translate("MainWindow", "��ѯ"))
        self.label_8.setText(_translate("MainWindow", "��ʼʱ��"))
        self.label_9.setText(_translate("MainWindow", "����ʱ��"))
        self.label_5.setText(_translate("MainWindow", "�����ȴ���"))
        self.label_6.setText(_translate("MainWindow", "�����ѽ��"))
        self.print.setText(_translate("MainWindow", "��ӡ"))

    def closewin(self):
        self.close()

'''
class User:#�ͻ��Ļ���
    def __init__(self,user_id,room_id,b_time,e_time ):
        self.user_id =user_id#�ͻ���
        self.room_id = room_id#��ס�����
        self.b_time=b_time#��סʱ��
        self.e_time=e_time#�˷�ʱ��

    def login(self):#��ס����¼ϵͳ
    def air_on(self):#�����յ�
    def air_off(self):#�رտյ�
    def change_wind(self):#���ڷ���
    def change_tem(self):#�����¶�
    def logout(self):#�˷�,�˳�ϵͳ

class Air_admin:  #�յ�����Ա�Ļ���
    def __init__(self, admin_id, if_login, status):
        self.admin_id = admin_id#����Ա���
        self.if_login = if_login#�Ƿ��¼
        self.status = status#��ݱ�ʶ

    def login(self):  # ��¼ϵͳ
    def power_on(self):  #��ʼ���յ�ϵͳ
    def init_air(self):  # ��ʼ���յ�����
    def print_hotel(self):  # �鿴�Ƶ�յ�����״̬
    def print_room(self):  # �鿴����յ�����״̬
    def logout(self):  # �˳�ϵͳ

class Cashier:  # �Ƶ�ǰ̨�Ļ��ࡪ����Ƽܹ�����
     def __init__(self, cashier_id, if_login, status):
         self.cashier_id = cashier_id#�Ƶ�ǰ̨���
         self.if_login = if_login#�Ƿ��¼
         self.status = status#��ݱ�ʶ

     def login(self):  # ��¼ϵͳ
         if self.if_login != 0:
             self.if_login = 1
             return 1
         else:
             return 0           #error��������Ҫ��һЩ�쳣������δ��¼���˳����ѵ�¼�ٵ�¼

     def create_bill(self):  # �����˵�
         user_id = 1                #���û������ȡuser_id��room_id,������ʱ��д
         room_id = 1
         register = Register_cashier(user_id,room_id)
         register.create_bill()

     def print_bill(self):  # �鿴�˵�
         user_id = 1
         room_id = 0
         register = Register_cashier(user_id,room_id)
         record = register.print_bill()                  #record�Ǵ����ݿ��в���������������Ҫ����Ҫ�з�����ʾ��������


     def logout(self):  # �˳�ϵͳ
         if self.if_login == 1:
             self.if_login = 0;
             return 1
         else:
             return 0           #error


class Manager:  # �Ƶ꾭��Ļ���
    def __init__(self, manager_id, if_login, status):
        self.manager_id = manager_id#������
        self.if_login = if_login#�Ƿ��¼
        self.status = status#��ݱ�ʶ

    def login(self):  #��¼ϵͳ
    def create_form(self): #��������
    def print_form(self):  #�鿴����
    def logout(self):  #�˳�ϵͳ
'''

if __name__ == '__main__':#�򵥲���һ��ҳ����ת
    #����ҳ��������ʵ��
    app = QApplication(sys.argv)
    welcome = Welcome()
    move_select = Move_select()
    move_in=Move_in()
    move_out=Move_out()
    enter_room=Enter_room()
    air_monitor=Air_monitor()
    admin_select=Admin_select()
    hotel_air_state=Hotel_air_state()
    room_air_state=Room_air_state()
    cashier_select=Cashier_select()
    check_bill=Check_bill()
    manager_select=Manager_select()
    check_form=Check_form()

    #ҳ������ת�¼�
    welcome.show()
    #�û���·��ת�߼�
    welcome.enter.clicked.connect(move_select.show)
    welcome.enter.clicked.connect(welcome.closewin)

    # �û���·������ת
    move_select.movein.clicked.connect(move_in.show)
    move_select.movein.clicked.connect(move_select.closewin)
    move_select.moveout.clicked.connect(move_out.show)
    move_select.moveout.clicked.connect(move_select.closewin)
    move_select.enterroom.clicked.connect(enter_room.show)
    move_select.enterroom.clicked.connect(move_select.closewin)
    move_select.exit.clicked.connect(welcome.show)
    move_select.exit.clicked.connect(move_select.closewin)

    move_in.movein_confirm.clicked.connect(air_monitor.show)
    move_in.movein_confirm.clicked.connect(move_in.closewin)
    move_in.back.clicked.connect(move_select.show)
    move_in.back.clicked.connect(move_in.closewin)

    move_out.moveout_confirm.clicked.connect(welcome.show)
    move_out.moveout_confirm.clicked.connect(move_out.closewin)
    move_out.back.clicked.connect(move_select.show)
    move_out.back.clicked.connect(move_out.closewin)

    enter_room.movein_confirm.clicked.connect(air_monitor.show)
    enter_room.movein_confirm.clicked.connect(enter_room.closewin)
    enter_room.back.clicked.connect(move_select.show)
    enter_room.back.clicked.connect(enter_room.closewin)

    air_monitor.back.clicked.connect(move_select.show)
    air_monitor.back.clicked.connect(air_monitor.close)

    #�յ�����Ա��·������ת
    admin_select.check_has.clicked.connect(hotel_air_state.show)
    admin_select.check_has.clicked.connect(admin_select.closewin)
    admin_select.check_ras.clicked.connect(room_air_state.show)
    admin_select.check_ras.clicked.connect(admin_select.closewin)
    admin_select.exit.clicked.connect(welcome.show)
    admin_select.exit.clicked.connect(admin_select.closewin)

    hotel_air_state.back.clicked.connect(admin_select.show)
    hotel_air_state.back.clicked.connect(hotel_air_state.closewin)
    room_air_state.back.clicked.connect(admin_select.show)
    room_air_state.back.clicked.connect(room_air_state.closewin)


    #�Ƶ�ǰ̨��·������ת
    cashier_select.check_bill.clicked.connect(check_bill.show)
    cashier_select.check_bill.clicked.connect(cashier_select.closewin)
    cashier_select.exit.clicked.connect(welcome.show)
    cashier_select.exit.clicked.connect(cashier_select.closewin)

    check_bill.back.clicked.connect(cashier_select.show)
    check_bill.back.clicked.connect(check_bill.closewin)

    #�Ƶ꾭����·������ת
    manager_select.check_form.clicked.connect(check_form.show)
    manager_select.check_form.clicked.connect(manager_select.closewin)
    manager_select.exit.clicked.connect(welcome.show)
    manager_select.exit.clicked.connect(manager_select.closewin)

    check_form.back.clicked.connect(manager_select.show)
    check_form.back.clicked.connect(check_form.closewin)
    sys.exit(app.exec_())
