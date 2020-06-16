import time
import controller as ctrl
import application as app
#import database as db

import sys
import time
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Welcome(QMainWindow):#初始化界面
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(130, 70, 561, 101))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(30)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_1.setStyleSheet("color:white");
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(280, 340, 241, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")
        self.roleselect = QtWidgets.QComboBox(self.centralwidget)
        self.roleselect.setGeometry(QtCore.QRect(280, 240, 241, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.roleselect.setFont(font)
        self.roleselect.setObjectName("roleselect")
        self.roleselect.addItem("")
        self.roleselect.addItem("")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "分布式温控系统"))
        self.label_1.setText(_translate("MainWindow", "欢迎使用分布式温控系统"))
        self.enter.setText(_translate("MainWindow", "进入系统"))
        self.roleselect.setItemText(0, _translate("MainWindow", "酒店客户"))
        self.roleselect.setItemText(1, _translate("MainWindow", "酒店员工"))
        self.roleselect.currentIndexChanged.connect(self.selectionchange)

    def selectionchange(self):
        if (self.roleselect.currentText() == '酒店客户'):
            self.enter.clicked.connect(user_confirm.show)
            self.enter.clicked.connect(self.closewin)
            self.enter.clicked.connect(staff_confirm.closewin)

        elif (self.roleselect.currentText() == '酒店员工'):
            self.enter.clicked.connect(staff_confirm.show)
            self.enter.clicked.connect(self.closewin)
            self.enter.clicked.connect(user_confirm.closewin)

    def closewin(self):
        self.close()

class User_confirm(QMainWindow):#用户身份核验界面
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(310, 100, 251, 91))
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_1.setStyleSheet("color:red");
        self.user_id = QtWidgets.QComboBox(self.centralwidget)
        self.user_id.setGeometry(QtCore.QRect(290, 220, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.user_id.setFont(font)
        self.user_id.setObjectName("user_id")
        self.user_id.addItem("")
        self.user_id.addItem("")
        self.user_id.addItem("")
        self.user_id.addItem("")
        self.user_id.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd.setGeometry(QtCore.QRect(290, 290, 251, 41))
        self.pwd.setObjectName("pwd")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(270, 380, 131, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(420, 380, 131, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "客户身份核验"))
        self.user_id.setItemText(0, _translate("MainWindow", "1"))
        self.user_id.setItemText(1, _translate("MainWindow", "2"))
        self.user_id.setItemText(2, _translate("MainWindow", "3"))
        self.user_id.setItemText(3, _translate("MainWindow", "4"))
        self.user_id.setItemText(4, _translate("MainWindow", "5"))
        self.label.setText(_translate("MainWindow", "客户号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.enter.setText(_translate("MainWindow", "登录"))
        self.enter.clicked.connect(self.f1)
        self.back.setText(_translate("MainWindow", "返回"))
        self.back.clicked.connect(self.f2)

    def f1(self):
        user_id=int(self.user_id.currentText())
        pwd_true=users[user_id-1].pwd
        pwd_input=int(self.pwd.text())
        if(pwd_true==pwd_input):
            print("客户登录成功")
            move_select.show()
            self.closewin()
        else:
            print("客户号与密码不一致，登录失败！")

    def f2(self):
        welcome.show()
        self.closewin()

    def closewin(self):
        self.close()

class Staff_confirm(QMainWindow):#员工身份核验界面
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(290, 90, 251, 91))
        self.label_1.setStyleSheet("color:red");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.staff_role = QtWidgets.QComboBox(self.centralwidget)
        self.staff_role.setGeometry(QtCore.QRect(290, 220, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.staff_role.setFont(font)
        self.staff_role.setObjectName("staff_role")
        self.staff_role.addItem("")
        self.staff_role.addItem("")
        self.staff_role.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd.setGeometry(QtCore.QRect(290, 290, 251, 41))
        self.pwd.setObjectName("pwd")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(270, 370, 131, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(420, 370, 131, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "酒店人员身份核验"))
        self.staff_role.setItemText(0, _translate("MainWindow", "空调管理员"))
        self.staff_role.setItemText(1, _translate("MainWindow", "酒店前台"))
        self.staff_role.setItemText(2, _translate("MainWindow", "酒店经理"))
        self.label.setText(_translate("MainWindow", "身份"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.enter.setText(_translate("MainWindow", "登录"))
        self.enter.clicked.connect(self.f1)
        self.back.setText(_translate("MainWindow", "返回"))
        self.back.clicked.connect(self.f2)

    def f1(self):
        if (self.staff_role.currentText() == '空调管理员'):
            pwd_true = admin.pwd
            pwd_input = int(self.pwd.text())
            if (pwd_true == pwd_input):
                print("酒店人员登录成功——身份:空调管理员")
                admin_select.show()
                self.closewin()
            else:
                print("酒店人员身份与密码不一致，登录失败！")

        elif (self.staff_role.currentText() == '酒店前台'):
            pwd_true = cashier.pwd
            pwd_input = int(self.pwd.text())
            if (pwd_true == pwd_input):
                print("酒店人员登录成功——身份:酒店前台")
                cashier_select.show()
                self.closewin()
            else:
                print("酒店人员身份与密码不一致，登录失败！")

        elif (self.staff_role.currentText() == '酒店经理'):
            pwd_true = manager.pwd
            pwd_input = int(self.pwd.text())
            if (pwd_true == pwd_input):
                print("酒店人员登录成功——身份:酒店经理")
                manager_select.show()
                self.closewin()
            else:
                print("酒店人员身份与密码不一致，登录失败！")

    def f2(self):
        welcome.show()
        self.closewin()

    def closewin(self):
        self.close()

class Move_select(QMainWindow):#用户选择界面
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(290, 60, 231, 91))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.movein = QtWidgets.QPushButton(self.centralwidget)
        self.movein.setGeometry(QtCore.QRect(130, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.movein.setFont(font)
        self.movein.setObjectName("movein")
        self.moveout = QtWidgets.QPushButton(self.centralwidget)
        self.moveout.setGeometry(QtCore.QRect(130, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.moveout.setFont(font)
        self.moveout.setObjectName("moveout")
        self.enterroom = QtWidgets.QPushButton(self.centralwidget)
        self.enterroom.setGeometry(QtCore.QRect(410, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.enterroom.setFont(font)
        self.enterroom.setObjectName("enterroom")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(410, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.user_id = QtWidgets.QComboBox(self.centralwidget)
        self.user_id.setGeometry(QtCore.QRect(280, 170, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.user_id.setFont(font)
        self.user_id.setObjectName("user_id")
        self.user_id.addItem("")
        self.user_id.addItem("")
        self.user_id.addItem("")
        self.user_id.addItem("")
        self.user_id.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "请选择服务类型"))
        self.movein.setText(_translate("MainWindow", "办理入住"))
        self.moveout.setText(_translate("MainWindow", "办理退房"))
        self.enterroom.setText(_translate("MainWindow", "进入房间"))
        self.exit.setText(_translate("MainWindow", "退出系统"))
        self.user_id.setItemText(0, _translate("MainWindow", "1"))
        self.user_id.setItemText(1, _translate("MainWindow", "2"))
        self.user_id.setItemText(2, _translate("MainWindow", "3"))
        self.user_id.setItemText(3, _translate("MainWindow", "4"))
        self.user_id.setItemText(4, _translate("MainWindow", "5"))
        self.label.setText(_translate("MainWindow", "客户号"))
        self.movein.clicked.connect(self.f1)
        self.moveout.clicked.connect(self.f2)
        self.enterroom.clicked.connect(self.f3)
        self.exit.clicked.connect(self.f4)

    def f1(self):
        air_monitor.lcd_if_on.display(0)
        air_monitor.lcd_if_wind.display(0)
        move_in.show()
        self.closewin()

    def f2(self):
        move_out.show()
        self.closewin()

    def f3(self):
        enter_room.show()
        self.closewin()

    def f4(self):
        welcome.show()
        self.closewin()
    def closewin(self):
        self.close()

class Move_in(QMainWindow):#确认入住界面
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(280, 220, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.movein_confirm.setFont(font)
        self.movein_confirm.setObjectName("movein_confirm")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(280, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "办理入住"))
        self.label_1.setText(_translate("MainWindow", "您好，请选择房间号办理入住手续"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.movein_confirm.setText(_translate("MainWindow", "确定入住"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.movein_confirm.clicked.connect(self.room_choice)
        self.back.clicked.connect(self.f1)

    def room_choice(self):
        room_id=int(self.roomselect.currentText())
        user_id=int(move_select.user_id.currentText())
        if(rooms[room_id-1].user_id==0 and users[user_id-1].room_id==0):
            rooms[room_id - 1].user_id = room_id
            users[user_id - 1].room_id = user_id
            users[user_id - 1].b_time=air_monitor.systime#获取入住时间
            print("入住成功：顾客%d->房间%d 时间:%d"%(user_id,room_id,air_monitor.systime))
            air_monitor.show()
            move_in.closewin()
            air_monitor.lcd_roomtem.display(rooms[int(room_id) - 1].tem)
            air_monitor.lcd_room_id.display(air_subs[int(room_id) - 1].room_id)
            air_monitor.lcd_if_on.display(air_subs[int(room_id) - 1].if_on)
            air_monitor.lcd_if_wind.display(air_subs[int(room_id) - 1].if_wind)
            air_monitor.change_tem.setValue(air_subs[int(room_id) - 1].tem)
            air_monitor.change_wind.setValue(air_subs[int(room_id) - 1].windmode)
            air_monitor.cost_now.setText(str(air_subs[int(room_id) - 1].cost))
            air_monitor.show()
            enter_room.closewin()
            air_monitor.show()
        elif(users[user_id-1].room_id!=0):
            print("对不起，客户不可以重复定两个房间，请先退房")
        else:
            print("对不起，该房间已经有用户入住，请选择其他房间")

    def f1(self):
        move_select.show()
        move_in.closewin()

    def closewin(self):
        self.close()

class Move_out(QMainWindow):#确认退房界面
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(280, 210, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.moveout_confirm.setFont(font)
        self.moveout_confirm.setObjectName("moveout_confirm")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(280, 390, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "办理退房"))
        self.label_1.setText(_translate("MainWindow", "您好，请选择房间号办理退房手续"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.moveout_confirm.setText(_translate("MainWindow", "确定退房"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.moveout_confirm.clicked.connect(self.f1)
        self.back.clicked.connect(self.f2)

    def f1(self):
        room_id = int(self.roomselect.currentText())
        user_id = int(move_select.user_id.currentText())
        if (users[user_id-1].room_id!=room_id ):
            print("对不起，该房间您没有办理入住，您重新确认")
        else:
            users[user_id-1].b_time=air_monitor.time#获取退房时间
            print("退房成功:顾客%d->房间%d 时间:%d" % (user_id, room_id,air_monitor.systime))
        welcome.show()
        move_out.closewin()

    def f2(self):
        move_select.show()
        move_out.closewin()

    def closewin(self):
        self.close()

class Enter_room(QMainWindow):#进入房间界面
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(280, 220, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.movein_confirm.setFont(font)
        self.movein_confirm.setObjectName("movein_confirm")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(280, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "进入房间"))
        self.label_1.setText(_translate("MainWindow", "您好，请选择您所在的房间"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.movein_confirm.setText(_translate("MainWindow", "进入房间"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.movein_confirm.clicked.connect(self.room_choice)
        self.back.clicked.connect(self.f1)

    def room_choice(self):#选择不同的房间来做状态的查询
        room_id = int(self.roomselect.currentText())
        user_id = int(move_select.user_id.currentText())
        if(users[user_id-1].room_id!=room_id):
              print("对不起，该房间您没有办理入住，您重新确认")
        else:
              print("进入房间：顾客:%d->房间:%d" % (int(move_select.user_id.currentText()), room_id))
              air_monitor.lcd_roomtem.display(rooms[int(room_id)-1].tem)
              air_monitor.lcd_room_id.display(air_subs[int(room_id) - 1].room_id)
              air_monitor.lcd_if_on.display(air_subs[int(room_id) - 1].if_on)
              air_monitor.lcd_if_wind.display(air_subs[int(room_id) - 1].if_wind)
              air_monitor.change_tem.setValue(air_subs[int(room_id) - 1].tem)
              air_monitor.change_wind.setValue(air_subs[int(room_id) - 1].windmode)
              air_monitor.cost_now.setText(str(round(air_subs[int(room_id) - 1].cost,2)))
              air_monitor.show()
              enter_room.closewin()

    def f1(self):
        move_select.show()
        enter_room.closewin()

    def closewin(self):
        self.close()

class Air_monitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./room.jpg")))
        self.setPalette(window_pale)
        self.change_tem = QtWidgets.QSpinBox(self.centralwidget)
        self.change_tem.setGeometry(QtCore.QRect(130, 130, 381, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        self.change_tem.setFont(font)
        self.change_tem.setObjectName("change_tem")
        self.change_wind = QtWidgets.QSpinBox(self.centralwidget)
        self.change_wind.setGeometry(QtCore.QRect(130, 270, 381, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        self.change_wind.setFont(font)
        self.change_wind.setObjectName("change_wind")
        self.air_on = QtWidgets.QPushButton(self.centralwidget)
        self.air_on.setGeometry(QtCore.QRect(580, 130, 151, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.air_on.setFont(font)
        self.air_on.setObjectName("air_on")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 150, 81, 41))
        self.label_1.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.cost_now = QtWidgets.QTextBrowser(self.centralwidget)
        self.cost_now.setGeometry(QtCore.QRect(130, 400, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.cost_now.setFont(font)
        self.cost_now.setObjectName("cost_now")
        self.air_off = QtWidgets.QPushButton(self.centralwidget)
        self.air_off.setGeometry(QtCore.QRect(580, 230, 151, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.air_off.setFont(font)
        self.air_off.setObjectName("air_off")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(580, 430, 151, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 81, 41))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 420, 81, 41))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.check_cost = QtWidgets.QPushButton(self.centralwidget)
        self.check_cost.setGeometry(QtCore.QRect(580, 330, 151, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.check_cost.setFont(font)
        self.check_cost.setObjectName("check_cost")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lcd_if_wind = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_if_wind.setGeometry(QtCore.QRect(520, 70, 101, 41))
        self.lcd_if_wind.setObjectName("lcd_ifwind")
        self.lcd_if_on = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_if_on.setGeometry(QtCore.QRect(520, 20, 101, 41))
        self.lcd_if_on.setObjectName("lcd_ifon")
        self.lcd_room_id = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_room_id.setGeometry(QtCore.QRect(220, 20, 101, 41))
        self.lcd_room_id.setObjectName("lcd_roomid")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lcd_roomtem = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_roomtem.setGeometry(QtCore.QRect(220, 70, 101, 41))
        self.lcd_roomtem.setObjectName("lcd_roomtem")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.systime = 0  # 系统时间,1s模拟1min,进行系统时间线的更新
        self.timer = QBasicTimer()
        self.timer.start(10000, self)#时间模拟，真实时间10s模拟系统时间1min
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "空调面板"))
        self.air_on.setText(_translate("MainWindow", "开机"))
        self.label_1.setText(_translate("MainWindow", "温度"))
        self.air_off.setText(_translate("MainWindow", "关机"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.label_3.setText(_translate("MainWindow", "风速"))
        self.label_4.setText(_translate("MainWindow", "消费"))
        self.check_cost.setText(_translate("MainWindow", "查看当前消费"))
        self.label_5.setText(_translate("MainWindow", "开关状态"))
        self.label_6.setText(_translate("MainWindow", "送风状态"))
        self.label_7.setText(_translate("MainWindow", "房间号"))
        self.label_8.setText(_translate("MainWindow", "房间温度"))
        #self.room_id.setDigitCount(1)
        self.lcd_room_id.display(1)
        self.air_on.clicked.connect(self.f1)
        self.air_off.clicked.connect(self.f2)
        self.change_tem.setRange(18,30)
        self.change_tem.setValue(26)
        self.change_wind.setRange(0,2)
        self.change_wind.setValue(0)
        self.change_tem.valueChanged.connect(self.f3)
        self.change_wind.valueChanged.connect(self.f4)
        self.check_cost.clicked.connect(self.f5)
        self.back.clicked.connect(self.f6)

    def timerEvent(self, event):#时间线推进
        if event.timerId() == self.timer.timerId():
            self.systime = self.systime + 1
            room_id=int(self.lcd_room_id.value())
            #print(air_subs[room_id-1].if_on)
            #print(air_subs[room_id-1].if_wind)
            if(air_subs[room_id-1].if_on==1):#空调开机
                if(air_subs[room_id-1].if_wind==1):#空调开机且送风
                    if (air_subs[room_id - 1].windmode == 0):#低风模式
                        tem_freq = 0.4
                        money_freq = 0.33
                    elif (air_subs[room_id - 1].windmode == 1):#中风模式
                        tem_freq = 0.5
                        money_freq = 0.5
                    elif (air_subs[room_id - 1].windmode == 2):  #高风模式
                        tem_freq = 0.6
                        money_freq = 1
                    if (int(rooms[room_id - 1].tem) > air_subs[room_id - 1].tem):#空调降低室内温度
                        rooms[room_id - 1].tem -= tem_freq
                        #print(rooms[room_id - 1].tem)
                        #print(air_subs[room_id - 1].tem)
                        self.lcd_roomtem.display(rooms[room_id - 1].tem)
                        air_subs[room_id - 1].cost += money_freq
                    elif (int(rooms[room_id - 1].tem) < air_subs[room_id - 1].tem):#空调升高室内温度
                        rooms[room_id - 1].tem += tem_freq
                        self.lcd_roomtem.display(rooms[room_id - 1].tem)
                        air_subs[room_id - 1].cost += money_freq
                    else:#室内温度达到空调设定值，关闭送风
                        air_subs[room_id - 1].if_wind = 0
                        self.lcd_if_wind.display(0)

                else:#空调开机不送风
                    if (rooms[room_id - 1].tem < 30):
                        rooms[room_id - 1].tem += 0.5
                        self.lcd_roomtem.display(rooms[room_id - 1].tem)
                        if (rooms[room_id - 1].tem - air_subs[room_id - 1].tem > 1):#室温超过设定温度5度再次开启送风
                            air_subs[room_id - 1].if_wind = 1
                            self.lcd_if_wind.display(1)

            else:#空调关机
                if (rooms[room_id - 1].tem < 30):
                    rooms[room_id - 1].tem += 0.5
                    self.lcd_roomtem.display(rooms[room_id - 1].tem)


    def f1(self):#空调开启
        room_id = int(self.lcd_room_id.value())
        user.air_on(air_subs,services,scheduler,room_id)
        print("房间%d空调开启"%room_id)
        self.lcd_if_on.display(1)
        self.lcd_if_wind.display(1)
        air_main.air_on_num+=1
        air_main.wind_on_num+=1

    def f2(self):#空调关闭
        room_id = int(self.lcd_room_id.value())
        user.air_off(services,air_subs,room_id)
        print("房间%d空调关闭" %room_id)
        self.lcd_if_on.display(0)
        self.lcd_if_wind.display(0)
        air_main.air_on_num -= 1
        air_main.wind_on_num -= 1

    def f3(self):#调温度
        if(self.lcd_if_on.value()==1):
            room_id = int(self.lcd_room_id.value())
            user.change_tem(self.change_tem.value(),air_subs,services,room_id)
            print("房间%d空调温度调节成功->%d度" %(room_id,self.change_tem.value()))
            print(air_subs[int(self.lcd_room_id.value())-1].tem)

    def f4(self):#调风速
        if(self.lcd_if_on.value()==1):
            room_id = int(self.lcd_room_id.value())
            user.change_wind(self.change_wind.value(),air_subs,services,scheduler,room_id)
            print("房间%d空调风速调节成功->%d裆" %(room_id,self.change_wind.value()))
            print(air_subs[room_id-1].windmode)

    def f5(self):#查询当前消费
        room_id = int(self.lcd_room_id.value())
        self.cost_now.setText(str(air_subs[room_id-1].cost))

    def f6(self):
        move_select.show()
        air_monitor.close()

    def closewin(self):
        self.close()


class Admin_select(QMainWindow):#管理员选择界面
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 557)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./hall.jpg")))
        self.setPalette(window_pale)
        self.welcome1 = QtWidgets.QLabel(self.centralwidget)
        self.welcome1.setGeometry(QtCore.QRect(280, 80, 241, 101))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.welcome1.setFont(font)
        self.welcome1.setObjectName("welcome1")
        self.check_has = QtWidgets.QPushButton(self.centralwidget)
        self.check_has.setGeometry(QtCore.QRect(270, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check_has.setFont(font)
        self.check_has.setObjectName("check_has")
        self.check_ras = QtWidgets.QPushButton(self.centralwidget)
        self.check_ras.setGeometry(QtCore.QRect(270, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check_ras.setFont(font)
        self.check_ras.setObjectName("check_ras")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(270, 350, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.initair = QtWidgets.QPushButton(self.centralwidget)
        self.initair.setGeometry(QtCore.QRect(270, 200, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.initair.setFont(font)
        self.initair.setObjectName("initair")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome1.setText(_translate("MainWindow", "请选择服务类型"))
        self.check_has.setText(_translate("MainWindow", "查看酒店空调状态"))
        self.check_ras.setText(_translate("MainWindow", "查看房间空调状态"))
        self.exit.setText(_translate("MainWindow", "退出系统"))
        self.initair.setText(_translate("MainWindow", "初始化空调"))
        self.initair.clicked.connect(self.f1)
        self.check_has.clicked.connect(self.f2)
        self.check_ras.clicked.connect(self.f3)
        self.exit.clicked.connect(self.f4)

    def f1(self):
        for i in range(0,5):
            admin.init_air(air_main, 0, 0, 0, air_subs, 26, 1, 0, 0, 0)

        print("init...")
        print("空调主机初始化成功")
        print("当前子机开启数:%d" % air_main.air_on_num)
        print("当前子机送风数:%d" % air_main.wind_on_num)
        print("当前子机等待数:%d" % air_main.wait_on_num)
        print()

        for i in range(0,5):
            print("空调子机初始化成功")
            print("子机对应房间号:%d" % air_subs[i].room_id)
            print("子机是否开启:%d" % air_subs[i].if_on)
            print("子机是否送风:%d" % air_subs[i].if_wind)
            print("子机设定温度:%d" % air_subs[i].tem)
            print("子机设定风速:%d" % air_subs[i].windmode)
            print("子机当前计费:%d" % air_subs[i].cost)
            print()

        return air_main,air_subs

    def f2(self):
        hotel_air_state.show()
        admin_select.closewin()

    def f3(self):
        room_air_state.show()
        admin_select.closewin()

    def f4(self):
        welcome.show()
        admin_select.closewin()

    def closewin(self):
        self.close()

class Hotel_air_state(QMainWindow):#查询酒店空调状态界面
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
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 240, 191, 101))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 340, 191, 101))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(190, 470, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(400, 470, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "查询酒店空调状态"))
        self.label_1.setText(_translate("MainWindow", "酒店空调信息"))
        self.label_2.setText(_translate("MainWindow", "开启空调数"))
        self.label_3.setText(_translate("MainWindow", "送风空调数"))
        self.label_4.setText(_translate("MainWindow", "等待调度数"))
        self.check.setText(_translate("MainWindow", "查询"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.check.clicked.connect(self.print_hotel_air)
        self.back.clicked.connect(self.f1)

    def print_hotel_air(self):
        self.lcd_windonnum.display(air_main.wind_on_num)
        self.lcd_aironnum.display(air_main.air_on_num)
        self.lcd_waitnum.display(air_main.wait_on_num)
        print("酒店空调信息查询成功")
        print("子机开启数:%d"%air_main.air_on_num)
        print("子机送风数:%d"%air_main.wind_on_num)
        print("子机等待数:%d"%air_main.wait_on_num)

    def f1(self):
        admin_select.show()
        hotel_air_state.closewin()

    def closewin(self):
        self.close()

class Room_air_state(QMainWindow):#查询房间空调状态界面
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.lcd_ifair = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_ifair.setGeometry(QtCore.QRect(580, 110, 171, 61))
        self.lcd_ifair.setObjectName("lcd_ifair")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(70, 190, 211, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 150, 191, 121))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 220, 191, 121))
        self.label_5.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 360, 191, 121))
        self.label_7.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 290, 191, 121))
        self.label_6.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(90, 380, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(90, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "查询房间空调状态"))
        self.label1.setText(_translate("MainWindow", "房间空调信息"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "房间号"))
        self.label_3.setText(_translate("MainWindow", "是否开启"))
        self.label_4.setText(_translate("MainWindow", "是否送风"))
        self.label_5.setText(_translate("MainWindow", "设定温度"))
        self.label_7.setText(_translate("MainWindow", "当前消费"))
        self.label_6.setText(_translate("MainWindow", "设定风速"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.check.setText(_translate("MainWindow", "查询"))
        self.check.clicked.connect(self.room_choice)
        self.back.clicked.connect(self.f1)

    def room_choice(self):#选择不同的房间来做状态的查询
        room_id=self.roomselect.currentText()
        self.lcd_ifair.display(air_subs[int(room_id)-1].if_on)
        self.lcd_ifwind.display(air_subs[int(room_id)-1].if_wind)
        self.lcd_tem.display(air_subs[int(room_id)-1].tem)
        self.lcd_windmode.display(air_subs[int(room_id)-1].windmode)
        self.lcd_cost.display(air_subs[int(room_id)-1].cost)
        print("房间%d空调信息查询成功" %int(room_id))
        print("子机对应房间号:%d" % air_subs[int(room_id)-1].room_id)
        print("子机是否开启:%d" % air_subs[int(room_id)-1].if_on)
        print("子机是否送风:%d" % air_subs[int(room_id)-1].if_wind)
        print("子机设定温度:%d" % air_subs[int(room_id)-1].tem)
        print("子机设定风速:%d" % air_subs[int(room_id)-1].windmode)
        print("子机当前计费:%d" % air_subs[int(room_id)-1].cost)
        print()

    def f1(self):
        admin_select.show()
        room_air_state.closewin()


    def closewin(self):
        self.close()

class Cashier_select(QMainWindow):#酒店前台选择界面
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.check_bill = QtWidgets.QPushButton(self.centralwidget)
        self.check_bill.setGeometry(QtCore.QRect(270, 240, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check_bill.setFont(font)
        self.check_bill.setObjectName("check_bill")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(270, 340, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.check_detail = QtWidgets.QPushButton(self.centralwidget)
        self.check_detail.setGeometry(QtCore.QRect(270, 290, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check_detail.setFont(font)
        self.check_detail.setObjectName("check_detail")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "您好，酒店前台"))
        self.label_1.setText(_translate("MainWindow", "请选择服务类型"))
        self.check_bill.setText(_translate("MainWindow", "查看并打印账单"))
        self.check_detail.setText(_translate("MainWindow", "查看并打印详单"))
        self.exit.setText(_translate("MainWindow", "退出系统"))
        self.check_bill.clicked.connect(self.f1)
        self.check_detail.clicked.connect(self.f2)
        self.exit.clicked.connect(self.f3)

    def f1(self):
        check_bill.show()
        cashier_select.closewin()

    def f2(self):
        check_detail.show()
        cashier_select.closewin()

    def f3(self):
        welcome.show()
        cashier_select.closewin()

    def closewin(self):
        self.close()

class Check_bill(QMainWindow):#账单查询界面
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lcd_btime = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_btime.setGeometry(QtCore.QRect(570, 140, 171, 61))
        self.lcd_btime.setObjectName("lcd_btime")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(130, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 210, 191, 121))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 320, 191, 121))
        self.label_5.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(90, 420, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(90, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 101, 81))
        self.label_8.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.userselect = QtWidgets.QComboBox(self.centralwidget)
        self.userselect.setGeometry(QtCore.QRect(130, 200, 211, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.print.setFont(font)
        self.print.setObjectName("print")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "账单查询"))
        self.label_1.setText(_translate("MainWindow", "账单查询"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "房间号"))
        self.label_3.setText(_translate("MainWindow", "入住时间"))
        self.label_4.setText(_translate("MainWindow", "退房时间"))
        self.label_5.setText(_translate("MainWindow", "总消费金额"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.check.setText(_translate("MainWindow", "查询"))
        self.label_8.setText(_translate("MainWindow", "客户号"))
        self.userselect.setItemText(0, _translate("MainWindow", "1"))
        self.userselect.setItemText(1, _translate("MainWindow", "2"))
        self.userselect.setItemText(2, _translate("MainWindow", "3"))
        self.userselect.setItemText(3, _translate("MainWindow", "4"))
        self.userselect.setItemText(4, _translate("MainWindow", "5"))
        self.print.setText(_translate("MainWindow", "打印"))
        self.print.clicked.connect(self.print_bill)
        self.back.clicked.connect(self.f1)

    def print_bill(self):
        print()
        print("****账单信息****")
        print("房间号:%d" %int(self.roomselect.currentText()))
        print("客户号:%d" % int(self.userselect.currentText()))
        print("入住时间:%d"%int(self.lcd_btime.value()))
        print("退房时间:%d"%int(self.lcd_etime.value()))
        print("总消费金额:%d"%int(self.lcd_cost_all.value()))
        print("****************")

    def f1(self):
        cashier_select.show()
        check_bill.closewin()

    def closewin(self):
        self.close()

class Check_detail(QMainWindow):#详单查询界面
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
        self.label_1.setGeometry(QtCore.QRect(310, 0, 141, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_1.setStyleSheet("color:red");
        self.lcd_beginwind = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_beginwind.setGeometry(QtCore.QRect(570, 90, 171, 61))
        self.lcd_beginwind.setObjectName("lcd_beginwind")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(130, 170, 211, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.roomselect.setFont(font)
        self.roomselect.setObjectName("roomselect")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.roomselect.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 101, 81))
        self.label_2.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcd_endwind = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_endwind.setGeometry(QtCore.QRect(570, 170, 171, 61))
        self.lcd_endwind.setObjectName("lcd_endwind")
        self.lcd_windtime = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_windtime.setGeometry(QtCore.QRect(570, 240, 171, 61))
        self.lcd_windtime.setObjectName("lcd_windtime")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 60, 191, 121))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 140, 191, 121))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 280, 191, 121))
        self.label_5.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(90, 420, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(90, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.print = QtWidgets.QPushButton(self.centralwidget)
        self.print.setGeometry(QtCore.QRect(90, 360, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.print.setFont(font)
        self.print.setObjectName("print")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 210, 191, 121))
        self.label_6.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 350, 191, 121))
        self.label_7.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 420, 191, 121))
        self.label_8.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lcd_windmode = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_windmode.setGeometry(QtCore.QRect(570, 310, 171, 61))
        self.lcd_windmode.setObjectName("lcd_windmode")
        self.lcd_costrate = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_costrate.setGeometry(QtCore.QRect(570, 380, 171, 61))
        self.lcd_costrate.setObjectName("lcd_costrate")
        self.lcd_cost = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_cost.setGeometry(QtCore.QRect(570, 450, 171, 61))
        self.lcd_cost.setObjectName("lcd_cost")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "详单查询"))
        self.label_1.setText(_translate("MainWindow", "详单查询"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "房间号"))
        self.label_3.setText(_translate("MainWindow", "开始送风时间"))
        self.label_4.setText(_translate("MainWindow", "结束送风时间"))
        self.label_5.setText(_translate("MainWindow", "风速"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.check.setText(_translate("MainWindow", "查询"))
        self.print.setText(_translate("MainWindow", "打印"))
        self.label_6.setText(_translate("MainWindow", "送风时长"))
        self.label_7.setText(_translate("MainWindow", "费率"))
        self.label_8.setText(_translate("MainWindow", "费用"))
        self.print.clicked.connect(self.print_detail)
        self.back.clicked.connect(self.f1)

    def print_detail(self):
        print()
        print("****详单信息****")
        print("房间号:%d" %int(self.roomselect.currentText()))
        print("开始送风时间:%d" %int(self.lcd_beginwind.value()))
        print("结束送风时间:%d"%int(self.lcd_endwind.value()))
        print("送风时长:%d"%int(self.lcd_windtime.value()))
        print("风速:%d"%int(self.lcd_windmode.value()))
        print("费率:%d"%int(self.lcd_costrate.value()))
        print("费用:%d"%int(self.lcd_cost.value()))
        print("****************")

    def f1(self):
        cashier_select.show()
        check_detail.closewin()


    def closewin(self):
        self.close()

class Manager_select(QMainWindow):#经理选择界面
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.check_form = QtWidgets.QPushButton(self.centralwidget)
        self.check_form.setGeometry(QtCore.QRect(270, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check_form.setFont(font)
        self.check_form.setObjectName("check_form")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(270, 320, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "您好，酒店经理"))
        self.label_1.setText(_translate("MainWindow", "请选择服务类型"))
        self.check_form.setText(_translate("MainWindow", "查看并打印报表"))
        self.exit.setText(_translate("MainWindow", "退出系统"))

        self.check_form.clicked.connect(self.f1)
        self.exit.clicked.connect(self.f2)

    def f1(self):
        check_form.show()
        manager_select.closewin()

    def f2(self):
        welcome.show()
        manager_select.closewin()

    def closewin(self):
        self.close()

class Check_form(QMainWindow):#报表查询界面
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
        self.label_1.setGeometry(QtCore.QRect(310, -30, 271, 131))
        self.label_1.setStyleSheet("color:red");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lcd_airon_times = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_airon_times.setGeometry(QtCore.QRect(560, 60, 171, 61))
        self.lcd_airon_times.setObjectName("lcd_airon_times")
        self.roomselect = QtWidgets.QComboBox(self.centralwidget)
        self.roomselect.setGeometry(QtCore.QRect(160, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcd_airoff_times = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_airoff_times.setGeometry(QtCore.QRect(560, 120, 171, 61))
        self.lcd_airoff_times.setObjectName("lcd_airoff_times")
        self.lcd_temreach_times = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_temreach_times.setGeometry(QtCore.QRect(560, 180, 171, 61))
        self.lcd_temreach_times.setObjectName("lcd_temreach_times")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 50, 141, 71))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 170, 171, 71))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 110, 151, 81))
        self.label_7.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(70, 460, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(70, 340, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 151, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("color:white");
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
        font.setFamily("微软雅黑 Light")
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
        self.lcd_schedule_times.setGeometry(QtCore.QRect(560, 240, 171, 61))
        self.lcd_schedule_times.setObjectName("lcd_schedule_times")
        self.lcd_cost_all = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_cost_all.setGeometry(QtCore.QRect(560, 480, 171, 61))
        self.lcd_cost_all.setObjectName("lcd_cost_all")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 230, 131, 81))
        self.label_5.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 470, 121, 71))
        self.label_6.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.print = QtWidgets.QPushButton(self.centralwidget)
        self.print.setGeometry(QtCore.QRect(70, 400, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.print.setFont(font)
        self.print.setObjectName("print")
        self.lcd_changetem_times = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_changetem_times.setGeometry(QtCore.QRect(560, 300, 171, 61))
        self.lcd_changetem_times.setObjectName("lcd_changetem_times_2")
        self.lcd_changewind_times = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_changewind_times.setGeometry(QtCore.QRect(560, 360, 171, 61))
        self.lcd_changewind_times.setObjectName("lcd_changewind_times_3")
        self.lcd_detail_times = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_detail_times.setGeometry(QtCore.QRect(560, 420, 171, 61))
        self.lcd_detail_times.setObjectName("lcd_detail_times")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(440, 290, 101, 71))
        self.label_10.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440, 350, 111, 71))
        self.label_11.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(450, 410, 111, 71))
        self.label_12.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "报表查询"))
        self.label_1.setText(_translate("MainWindow", "报表查询"))
        self.roomselect.setItemText(0, _translate("MainWindow", "1"))
        self.roomselect.setItemText(1, _translate("MainWindow", "2"))
        self.roomselect.setItemText(2, _translate("MainWindow", "3"))
        self.roomselect.setItemText(3, _translate("MainWindow", "4"))
        self.roomselect.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "房间号"))
        self.label_3.setText(_translate("MainWindow", "空调开启次数"))
        self.label_4.setText(_translate("MainWindow", "达目标温度次数"))
        self.label_7.setText(_translate("MainWindow", "空调关闭次数"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.check.setText(_translate("MainWindow", "查询"))
        self.label_8.setText(_translate("MainWindow", "起始时间"))
        self.label_9.setText(_translate("MainWindow", "结束时间"))
        self.label_5.setText(_translate("MainWindow", "被调度次数"))
        self.label_6.setText(_translate("MainWindow", "总消费金额"))
        self.print.setText(_translate("MainWindow", "打印"))
        self.label_10.setText(_translate("MainWindow", "调温次数"))
        self.label_11.setText(_translate("MainWindow", "调风次数"))
        self.label_12.setText(_translate("MainWindow", "详单数"))
        self.print.clicked.connect(self.print_form)
        self.back.clicked.connect(self.f1)

    def print_form(self):
        print()
        print("******报表信息*******")
        print("房间号:%d" %int(self.roomselect.currentText()))
        print("起始时间:%d" % int(self.btime_select.value()))
        print("结束时间:%d" % int(self.etime_select.value()))
        print("空调开启次数:%d" % int(self.lcd_airon_times.value()))
        print("空调关闭次数:%d" % int(self.lcd_airoff_times.value()))
        print("达目标温度次数:%d" % int(self.lcd_temreach_times.value()))
        print("被调度次数:%d" % int(self.lcd_schedule_times.value()))
        print("调温次数:%d" % int(self.lcd_changetem_times.value()))
        print("调风次数:%d" % int(self.lcd_changewind_times.value()))
        print("详单数:%d" % int(self.lcd_detail_times.value()))
        print("总消费金额:%d" % int(self.lcd_cost_all.value()))
        print("*********************")

    def f1(self):
        manager_select.show()
        check_form.closewin()

    def closewin(self):
        self.close()


class Cashier:#酒店前台的基类
     def __init__(self):
         self.if_login =0#是否登录
         self.pwd =20#酒店前台登录密码
     '''
          def login(self):#登录系统
         if self.if_login != 0:
             self.if_login = 1
             return 1
         else:
             return 0#error，后续需要做一些异常处理——未登录而退出，已登录再登录

     def create_bill(self):  # 创建账单
         user_id = 1                #从用户界面获取user_id，room_id,这里暂时简写
         room_id = 1
         register = Register_cashier(user_id,room_id)
         register.create_bill()

     def print_bill(self):  # 查看账单
         user_id = 1
         room_id = 0
         register = Register_cashier(user_id,room_id)
         record = register.print_bill()#record是从数据库中查出的完整表项，后续要按需要切分再显示到界面上


     def logout(self):  # 退出系统
         if self.if_login == 1:
             self.if_login = 0;
             return 1
         else:
             return 0#error
     '''

class Manager:  # 酒店经理的基类
    def __init__(self):
        self.if_login = 0#是否登录
        self.pwd=30#酒店经理登录密码

    '''
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
    
    '''

class Room:  # 房间的基类
    def __init__(self, room_id):
        self.room_id = room_id
        self.tem = 30
        self.user_id=0#入住的房客，为0表示闲置
        self.rate_of_tem_change = -0.5  # 温度变化率

class User:  # 客户的基类
    def __init__(self, user_id,pwd):
        self.user_id = user_id  # 客户号
        self.pwd=pwd#客户登录密码，和客户号对应
        self.room_id = 0  # 入住房间号,为0表示还没有入住
        self.b_time = 0  # 入住时间
        self.e_time = 0  # 退房时间

    def login(self):  # 入住，登录系统
        self.if_login=1

    def air_on(self,air_subs,services,scheduler,room_id):#启动空调
        register_user.air_on(air_subs, services,scheduler,room_id)#启动空调

    def air_off(self, services, air_subs,room_id):#关闭空调
        register_user.air_off(air_subs, services,room_id)

    def change_wind(self,windmode,air_subs,services,scheduler,room_id):#调节风速
        register_user.change_wind(windmode,air_subs,services,scheduler,room_id)

    def change_tem(self,tem_set,air_subs,services,room_id):  #调节温度
        register_user.change_tem(tem_set,air_subs,services,room_id)

    def logout(self):  # 退房,退出系统
        self.if_login=0

class Air_admin:  #空调管理员的基类
    def __init__(self):
        self.if_login = 0#初始登录状态为0
        self.pwd = 10#管理员的密码

    def login(self):  #登录系统
        self.if_login=1

    def power_on(self):  #初始化空调系统
        air_main,air_sub,service,scheduler=register_admin.power_on()
        return air_main,air_sub,service,scheduler#返回创建的空调主机，空调子机，服务对象，调度对象

    def init_air(self,air_main,air_on_num,wind_on_num,wait_on_num,air_subs,tem, windmode, cost, if_wind, if_on):  #初始化空调参数
        register_admin.init_air(air_main,air_on_num,wind_on_num,wait_on_num,air_subs,tem, windmode, cost, if_wind, if_on)

    def logout(self):  #退出系统
        self.if_login=0


#设置一些全局变量并将系统初始化
b_time=0
e_time=0
users=[]
rooms=[]

for i in range(1,6):
    room=Room(i)
    rooms.append(room)
print("房间实例创建成功...")

for i in range(1,6):
    user =User(i,i)
    users.append(user)
print("用户实例创建成功...")

admin = Air_admin()
cashier=Cashier()
manager=Manager()
register_user=ctrl.Register_user()
register_admin = ctrl.Register_admin()
print("空调管理员创建成功...")
print("空调管理员用例控制器创建成功...")
air_main, air_subs, services, scheduler = admin.power_on()
print("power_on...")
print("空调主机创建成功...")
print("当前子机开启数:%d"%air_main.air_on_num)
print("当前子机送风数:%d"%air_main.wind_on_num)
print()
print("空调子机创建成功")
for i in range(0,5):
    print("房间号:%d" % air_subs[i].room_id)
    print("房间温度:%d" %rooms[i].tem)
    print("子机是否开启:%d" % air_subs[i].if_on)
    print("子机是否送风:%d" % air_subs[i].if_wind)
    print("子机设定温度:%d" % air_subs[i].tem)
    print("子机设定风速:%d" % air_subs[i].windmode)
    print("子机当前计费:%d" % air_subs[i].cost)
    print()
print("服务对象创建成功...")
print("调度对象创建成功...")

if __name__ == '__main__':#主函数，用来生成并且初始化各个界面
    #构造页面对象类的实例
    app = QApplication(sys.argv)
    welcome = Welcome()
    user_confirm=User_confirm()
    staff_confirm=Staff_confirm()
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
    check_detail=Check_detail()
    manager_select=Manager_select()
    check_form=Check_form()
    #显示初始化登录界面
    welcome.show()
    welcome.enter.clicked.connect(user_confirm.show)
    welcome.enter.clicked.connect(welcome.closewin)
    sys.exit(app.exec_())



