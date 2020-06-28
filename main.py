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
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.pwd.setFont(font)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "客户身份核验"))
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
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.pwd.setFont(font)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "选择服务类型"))
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
            rooms[room_id - 1].user_id = user_id
            users[user_id - 1].room_id = room_id
            users[user_id - 1].b_time=air_monitor.systime#获取入住时间
            print("入住成功：顾客%d->房间%d 时间:%d"%(user_id,room_id,air_monitor.systime))
            u = ctrl.Register_user2(room_id, user_id,air_monitor.systime)
            u.u_in()
            air_monitor.show()
            move_in.closewin()
            air_monitor.lcd_roomtem.display(rooms[int(room_id) - 1].tem)
            air_monitor.lcd_room_id.display(air_subs[int(room_id) - 1].room_id)
            air_monitor.lcd_if_on.display(air_subs[int(room_id) - 1].if_on)
            air_monitor.lcd_if_wind.display(air_subs[int(room_id) - 1].if_wind)
            air_monitor.tem_set.setText(str(air_subs[int(room_id) - 1].tem))
            air_monitor.wind_set.setText(str(air_subs[int(room_id) - 1].windmode))
            air_monitor.cost_now.setText(str(air_subs[int(room_id) - 1].cost))
            air_monitor.show()
            enter_room.closewin()
            air_monitor.show()
        elif(users[user_id-1].room_id!=0):
            print(rooms[room_id-1].user_id, users[user_id-1].room_id)
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
            users[user_id-1].b_time=air_monitor.systime#获取退房时间
            rooms[room_id-1].user_id=0 
            users[user_id-1].room_id=0
            u = ctrl.Register_user2(room_id, user_id,air_monitor.systime)
            u.u_out()
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
              air_monitor.lcd_room_id.display(air_subs[int(room_id) - 1].room_id)
              air_monitor.lcd_roomtem.display(rooms[int(room_id) - 1].tem)
              air_monitor.lcd_if_on.display(air_subs[int(room_id) - 1].if_on)
              air_monitor.lcd_if_wind.display(air_subs[int(room_id) - 1].if_wind)
              air_monitor.tem_set.setText(str(air_subs[int(room_id) - 1].tem))
              air_monitor.wind_set.setText(str(air_subs[int(room_id) - 1].windmode))
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
        self.air_on = QtWidgets.QPushButton(self.centralwidget)
        self.air_on.setGeometry(QtCore.QRect(580, 120, 151, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.air_on.setFont(font)
        self.air_on.setObjectName("air_on")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(40, 170, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_1.setStyleSheet("color:white");
        self.air_off = QtWidgets.QPushButton(self.centralwidget)
        self.air_off.setGeometry(QtCore.QRect(580, 190, 151, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.air_off.setFont(font)
        self.air_off.setObjectName("air_off")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(580, 470, 151, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 300, 81, 41))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 420, 81, 41))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.check_cost = QtWidgets.QPushButton(self.centralwidget)
        self.check_cost.setGeometry(QtCore.QRect(580, 400, 151, 61))
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
        self.change_tem = QtWidgets.QPushButton(self.centralwidget)
        self.change_tem.setGeometry(QtCore.QRect(580, 260, 151, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.change_tem.setFont(font)
        self.change_tem.setObjectName("change_tem")
        self.change_wind = QtWidgets.QPushButton(self.centralwidget)
        self.change_wind.setGeometry(QtCore.QRect(580, 330, 151, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.change_wind.setFont(font)
        self.change_wind.setObjectName("change_wind")
        self.tem_set = QtWidgets.QTextEdit(self.centralwidget)
        self.tem_set.setGeometry(QtCore.QRect(150, 160, 331, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.tem_set.setFont(font)
        self.tem_set.setObjectName("tem_set")
        self.wind_set = QtWidgets.QTextEdit(self.centralwidget)
        self.wind_set.setGeometry(QtCore.QRect(150, 280, 331, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.wind_set.setFont(font)
        self.wind_set.setObjectName("wind_set")
        self.cost_now = QtWidgets.QTextEdit(self.centralwidget)
        self.cost_now.setGeometry(QtCore.QRect(150, 410, 331, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.cost_now.setFont(font)
        self.cost_now.setObjectName("cost_now")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "空调控制面板"))
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
        self.change_tem.setText(_translate("MainWindow", "调温"))
        self.change_wind.setText(_translate("MainWindow", "调风"))
        #self.room_id.setDigitCount(1)
        self.lcd_room_id.display(1)
        self.air_on.clicked.connect(self.f1)
        self.air_off.clicked.connect(self.f2)
        self.tem_set.setText("25")
        self.wind_set.setText("1")
        self.systime = 0  # 系统时间,1s模拟1min,进行系统时间线的更新
        self.timer = QBasicTimer()
        self.timer.start(30000, self)  # 时间模拟，真实时间10s模拟系统时间1min
        self.change_tem.clicked.connect(self.f3)
        self.change_wind.clicked.connect(self.f4)
        self.check_cost.clicked.connect(self.f5)
        self.back.clicked.connect(self.f6)

    def timerEvent(self, event):#时间线推进
        '''
        modified by 温嘉烨 on 6.27
        时刻变化，启动调度算法，房间信息对应更新
        '''
        if event.timerId() == self.timer.timerId():
            scheduler.schedule_on(air_main, air_subs, services,air_monitor)  # 调度算法开启 更新当前服务队列和等待队列的信息
            room_id = int(self.lcd_room_id.value())
            self.lcd_if_on.display(air_subs[room_id - 1].if_on)
            self.lcd_if_wind.display(air_subs[room_id - 1].if_wind)

            # 每隔半分钟输出一次所有房间的对应信息，供测试用例填表使用,默认属性更改与系统响应有一定延迟，保持同一个时间单位
            print()
            print(
                "*********************************************************************************************************")
            print("系统时间:%d" % self.systime)
            # 送风服务队列信息
            print("当前送风服务队列:", end="")
            for i in range(0, len(scheduler.s_seq)):
                print("%d " % scheduler.s_seq[i].room_id, end="")
            print()
            # 送风等待队列信息
            print("当前送风等待队列:", end="")
            for i in range(0, len(scheduler.w_seq)):
                print("%d " % scheduler.w_seq[i].room_id, end="")
            print()
            # 各房间详细信息信息
            for i in range(0, 5):
                print("房间:%d " % (i + 1), end="")
                print("房间当前温度:%.1f " % rooms[i].tem, end="")
                print("设定温度:%d " % air_subs[i].tem, end="")
                if (air_subs[i].windmode == 0):
                    print("设定风速:低 ", end="")
                elif (air_subs[i].windmode == 1):
                    print("设定风速:中 ", end="")
                elif (air_subs[i].windmode == 2):
                    print("设定风速:高 ", end="")

                print("当前消费:%.2f " % air_subs[i].cost, end="")
                print("是否开启:%d " % air_subs[i].if_on, end="")
                print("是否送风:%d " % air_subs[i].if_wind, end="")
                print("服务时间:%d " % air_subs[i].serve_time, end="")
                print("等待时间:%d " % air_subs[i].wait_time, end="")
                print()
            print(
                "*********************************************************************************************************")
            print()

            # 更新房间状态信息，以便在写一个时刻到来的时候正确输出对应信息
            for room_id in range(1, 6):  # 更新房间状态信息，在下一时刻到来的时候做相应输出
                if (air_subs[room_id - 1] in scheduler.s_seq):  # 空调处于调度队列，送风
                    air_subs[room_id - 1].serve_time += 1
                    if (air_subs[room_id - 1].windmode == 0):  # 低风模式
                        tem_freq = 0.4
                        money_freq = 0.33
                    elif (air_subs[room_id - 1].windmode == 1):  # 中风模式
                        tem_freq = 0.5
                        money_freq = 0.5
                    elif (air_subs[room_id - 1].windmode == 2):  # 高风模式
                        tem_freq = 0.6
                        money_freq = 1
                    if (rooms[room_id - 1].tem - tem_freq >= air_subs[room_id - 1].tem):  # 空调降低室内温度
                        rooms[room_id - 1].tem -= tem_freq
                        self.lcd_roomtem.display(rooms[room_id - 1].tem)
                        air_subs[room_id - 1].cost += money_freq
                    else:  # 室内温度达到空调设定值，关闭送风
                        air_subs[room_id - 1].if_wind = 0
                        self.lcd_if_wind.display(0)
                else:
                    if (air_subs[room_id - 1] in scheduler.w_seq):  # 空调在等待队列未送风，回温算法开启
                        air_subs[room_id - 1].wait_time += 1
                        if (rooms[room_id - 1].tem < rooms[room_id - 1].ori_tem):  # 未回温到到房间的起始温度
                            rooms[room_id - 1].tem += 0.5
                        self.lcd_roomtem.display(rooms[room_id - 1].tem)
                    else:  # 空调未开机，回温算法开启
                        if (rooms[room_id - 1].tem < rooms[room_id - 1].ori_tem):  # 未回温到房间的起始温度
                            rooms[room_id - 1].tem += 0.5
                        self.lcd_roomtem.display(rooms[room_id - 1].tem)

            self.systime = self.systime + 1  # 更新系统时间


    def f1(self):#空调开启
        room_id = int(self.lcd_room_id.value())
        user.air_on(air_subs, services,room_id,air_monitor)
        print("信号——时间:%d,房间:%d,操作:空调开启" % (self.systime, room_id))
        air_main.air_on_num+=1
        air_main.wind_on_num += 1

    def f2(self):#空调关闭
        room_id = int(self.lcd_room_id.value())
        user.air_off(services,air_subs,room_id,air_monitor)
        #空调关机，一些对应的状态信息初始化
        air_subs[room_id-1].serve_time=0
        air_subs[room_id-1].wait_time=0
        air_subs[room_id-1].tem=25
        air_subs[room_id-1].windmode=1
        '''
            modified by 王博琛 on 6-28
            修改温度和风速控件内容
        '''
        # self.change_tem.setValue(air_subs[room_id-1].tem)
        # self.change_wind.setValue(air_subs[room_id-1].windmode)
        self.tem_set.setText(str(air_subs[room_id - 1].tem))
        self.wind_set.setText(str(air_subs[room_id-1].windmode))

        print("信号——时间:%d,房间:%d,操作:空调关闭"%(self.systime,room_id))
        air_main.air_on_num -= 1
        air_main.wind_on_num -= 1

    def f3(self):#调温度
        if(self.lcd_if_on.value()==1):
            room_id = int(self.lcd_room_id.value())
            user.change_tem(int(self.tem_set.toPlainText()),air_subs,services,room_id,air_monitor)
            print("信号——时间:%d,房间:%d,操作:温度调节到%d" % (self.systime, room_id, int(self.tem_set.toPlainText())))

    def f4(self):#调风速
        if(self.lcd_if_on.value()==1):
            room_id = int(self.lcd_room_id.value())
            user.change_wind(int(self.wind_set.toPlainText()),air_subs,services,room_id,air_monitor)
            if (int(self.wind_set.toPlainText()) == 0):
                print("信号——时间:%d,房间:%d,操作:风速调节到低" % (self.systime, room_id))
            elif (int(self.wind_set.toPlainText()) == 1):
                print("信号——时间:%d,房间:%d,操作:风速调节到中" % (self.systime, room_id))
            elif (int(self.wind_set.toPlainText()) == 2):
                print("信号——时间:%d,房间:%d,操作:风速调节到高" % (self.systime, room_id))

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
        MainWindow.setWindowTitle(_translate("MainWindow", "选择服务类型"))
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
        self.lcd_aironnum.display(air_main.air_on_num)
        self.lcd_windonnum.display(len(scheduler.s_seq))
        self.lcd_waitnum.display(len(scheduler.w_seq))
        print("酒店空调信息查询成功")
        print("子机开启数:%d"%air_main.air_on_num)
        print("子机送风数:%d"%len(scheduler.s_seq))
        print("子机等待数:%d"%len(scheduler.w_seq))

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
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(90, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.create.setFont(font)
        self.create.setObjectName("create")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(90, 480, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(90, 360, 171, 51))
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
        self.print.setGeometry(QtCore.QRect(90, 420, 171, 51))
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
        self.create.setText(_translate("MainWindow","创建账单"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.check.setText(_translate("MainWindow", "查询"))
        self.label_8.setText(_translate("MainWindow", "客户号"))
        self.userselect.setItemText(0, _translate("MainWindow", "1"))
        self.userselect.setItemText(1, _translate("MainWindow", "2"))
        self.userselect.setItemText(2, _translate("MainWindow", "3"))
        self.userselect.setItemText(3, _translate("MainWindow", "4"))
        self.userselect.setItemText(4, _translate("MainWindow", "5"))
        self.print.setText(_translate("MainWindow", "打印"))
        self.print.clicked.connect(self.print_bill)  # 打印键响应
        self.back.clicked.connect(self.f1)           # 返回键响应
        self.check.clicked.connect(self.checkbill)   # 查询键响应
        self.create.clicked.connect(self.createbill) # 创建账单键响应

    def print_bill(self):
            print()
            print("****账单信息****")
            print("房间号:%d" % int(self.roomselect.currentText()))
            print("客户号:%d" % int(self.userselect.currentText()))
            print("入住时间:%d" % int(self.lcd_btime.value()))
            print("退房时间:%d" % int(self.lcd_etime.value()))
            print("总消费金额:%d" % int(self.lcd_cost_all.value()))
            print("****************")

    def f1(self):
            cashier_select.show()
            check_bill.closewin()

    def checkbill(self):
            user_id = str(self.userselect.currentText())
            room_id = str(self.roomselect.currentText())
            # print('get user_id : %s , room_id : %s' % (user_id,room_id))
            b_time, e_time, cost = cashier.print_bill(user_id, room_id)
            self.lcd_btime.display(b_time)
            self.lcd_etime.display(e_time)
            self.lcd_cost_all.display(cost)

    def createbill(self):
            user_id = str(self.userselect.currentText())
            room_id = str(self.userselect.currentText())
            cashier.create_bill(user_id, room_id)
            print('账单创建成功')

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
        self.label_1.setStyleSheet("color:red")
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
        self.userselect = QtWidgets.QComboBox(self.centralwidget)
        self.userselect.setGeometry(QtCore.QRect(130, 100, 211, 41))
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 101, 81))
        self.label_2.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 101, 81))
        self.label_3.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 80, 150, 81))
        self.label_4.setStyleSheet("color:white");
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(QtCore.QRect(400, 160, 300, 350))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
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
        self.userselect.setItemText(0, _translate("MainWindow", "1"))
        self.userselect.setItemText(1, _translate("MainWindow", "2"))
        self.userselect.setItemText(2, _translate("MainWindow", "3"))
        self.userselect.setItemText(3, _translate("MainWindow", "4"))
        self.userselect.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "房间号"))
        self.label_3.setText(_translate("MainWindow", "用户号"))
        self.label_4.setText(_translate("MainWindow", "详单信息"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.check.setText(_translate("MainWindow", "查询"))
        self.print.setText(_translate("MainWindow", "打印"))
        self.print.clicked.connect(self.print_detail)  # 打印响应
        self.back.clicked.connect(self.f1)  # 返回响应
        self.check.clicked.connect(self.check_detail)

    def print_detail(self):
        print()
        print("****详单信息****")
        print("房间号:%d" % int(self.roomselect.currentText()))
        for i in range(self.rows):
            print("开始送风时间: %d" % (self.records[i][2]))
            print("结束送风时间: %d" % (self.records[i][3]))
            print("送风时长: %d" % (self.records[i][4]))
            print("风速: %d" % (self.records[i][5]))
            print("费率: %.3f" % (self.records[i][6]))
            print("费用: %.3f" % (self.records[i][7]))
        print("****************")

    def f1(self):
        cashier_select.show()
        check_detail.closewin()

    def check_detail(self):
        room_id = self.roomselect.currentText()
        user_id = self.userselect.currentText()
        self.textedit.setPlainText('房间号： %s '% (room_id))
        self.rows,self.records = cashier.print_detail(user_id,room_id)
        for i in range(self.rows):
            self.textedit.append('-----------------------')
            self.textedit.append('送风开始时间：%d' %(self.records[i][2]))
            self.textedit.append('送风结束时间：%d' %(self.records[i][3]))
            self.textedit.append('送风时长：%d' %(self.records[i][4]))
            self.textedit.append('风速：%d' %(self.records[i][5]))
            self.textedit.append('费率：%.3f' %(self.records[i][6]))
            self.textedit.append('费用：%.3f' %(self.records[i][7]))
            self.textedit.append('-----------------------')


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
        self.label_4.setText(_translate("MainWindow", "空调使用总时长"))
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
        self.check.clicked.connect(self.check_form)
        self.print.clicked.connect(self.print_form)
        self.back.clicked.connect(self.f1)

    def check_form(self): #点击查询后调用的函数
        #先创建报表，再返回查询结果
        room_id = self.roomselect.currentText()
        b_time = self.btime_select.value()
        e_time = self.etime_select.value()

        air_on_times, air_off_times, use_time, schedule_times, change_tem_times, change_wind_times, details_number, cost_all = manager.create_form(room_id, b_time, e_time)
        self.lcd_airon_times.display(air_on_times)
        self.lcd_airoff_times.display(air_off_times)
        self.lcd_temreach_times.display(use_time)
        self.lcd_schedule_times.display(schedule_times)
        self.lcd_changetem_times.display(change_tem_times)
        self.lcd_changewind_times.display(change_wind_times)
        self.lcd_detail_times.display(details_number)
        self.lcd_cost_all.display(cost_all)

    def print_form(self): #点击打印后调用的函数
        room_id = self.roomselect.currentText()
        b_time = self.btime_select.value()
        e_time = self.etime_select.value()
        manager.print_form(room_id, b_time, e_time)
        

    def f1(self):
        manager_select.show()
        check_form.closewin()

    def closewin(self):
        self.close()


class Cashier:  # 酒店前台的基类
    def __init__(self):
        self.if_login = 0  # 是否登录
        self.pwd = 20  # 酒店前台登录密码

    def login(self):  # 登录系统
        if self.if_login == 0:
            self.if_login = 1

    def print_bill(self, user_id, room_id):
        register_cashier = ctrl.Register_cashier(user_id, room_id)
        return register_cashier.check_bill()

    def print_detail(self, user_id, room_id):
        register_cashier = ctrl.Register_cashier(user_id, room_id)
        return register_cashier.check_detail()

    def create_bill(self,user_id,room_id):
        register_cashier = ctrl.Register_cashier(user_id,room_id)
        register_cashier.create_detail()
        register_cashier.update_bill()

    def logoff(self):
        if self.if_login == 1:
            self.if_login = 0

class Manager:  # 酒店经理的基类
    def __init__(self):
        self.if_login = 0#是否登录
        self.pwd=30#酒店经理登录密码

    def create_form(self, room_id, b_time, e_time): #创建报表
        r3 = ctrl.Register_manager(room_id, b_time, e_time)
        air_on_times, air_off_times, use_time, schedule_times, change_tem_times, change_wind_times, details_number, cost_all = r3.create_form()
        return air_on_times, air_off_times, use_time, schedule_times, change_tem_times, change_wind_times, details_number, cost_all

    def print_form(self, room_id, b_time, e_time):  #打印报表
        r3 = ctrl.Register_manager(room_id, b_time, e_time)
        form_items = r3.print_form()    
        print()
        print("******报表信息*******")
        print("房间号:%d" %int(form_items[1]))
        print("起始时间:%d" %int(form_items[2]))
        print("结束时间:%d" %int(form_items[3]))
        print("空调开启次数:%d" %int(form_items[4]))
        print("空调关闭次数:%d" %int(form_items[5]))
        print("空调使用时长:%d" %int(form_items[6]))
        print("被调度次数:%d" %int(form_items[7]))
        print("调温次数:%d" %int(form_items[8]))
        print("调风次数:%d" %int(form_items[9]))
        print("详单数:%d" %int(form_items[10]))
        print("总消费金额:%d" %float(form_items[11]))
        print("*********************")
    

class Room:  # 房间的基类
    def __init__(self, room_id):
        self.room_id = room_id
        self.tem = 0
        self.ori_tem=0
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

    '''
    modified by 刘峰麟 on 6.26
    增加形参air_monitor
    '''

    def air_on(self,air_subs,services,room_id,air_monitor):#启动空调
        register_user.air_on(air_subs, services,room_id,air_monitor)#启动空调

    def air_off(self, services, air_subs,room_id,air_monitor):#关闭空调
        register_user.air_off(air_subs, services,room_id,air_monitor)

    def change_wind(self,windmode,air_subs,services,room_id,air_monitor):#调节风速
        register_user.change_wind(windmode,air_subs,services,room_id,air_monitor)

    def change_tem(self,tem_set,air_subs,services,room_id,air_monitor):  #调节温度
        register_user.change_tem(tem_set,air_subs,services,room_id,air_monitor)

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


#设置一些全局变量并将系统start-up
b_time=0
e_time=0
users=[]
rooms=[]
temp=0
for i in range(1,6):
    room=Room(i)
    rooms.append(room)
print("房间实例创建成功...")

#设置房间初始温度
rooms[0].tem=32
rooms[1].tem=28
rooms[2].tem=30
rooms[3].tem=29
rooms[4].tem=35

rooms[0].ori_tem=32
rooms[1].ori_tem=28
rooms[2].ori_tem=30
rooms[3].ori_tem=29
rooms[4].ori_tem=35
#创建5个用户实例
for i in range(1,6):
    user =User(i,i)
    users.append(user)
print("用户实例创建成功...")

#创建实例并输出初始化信息
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
print("空调子机创建成功")
print("当前子机开启数:%d"%air_main.air_on_num)
print("当前子机送风数:%d"%air_main.wind_on_num)
print()
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



