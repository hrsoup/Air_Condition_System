# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 663)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(100, 70, 841, 141))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(30)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(400, 370, 241, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "           欢迎使用分布式温控系统"))
        self.enter.setText(_translate("MainWindow", "进入系统"))
        self.comboBox.setItemText(0, _translate("MainWindow", "客户"))
        self.comboBox.setItemText(1, _translate("MainWindow", "空调管理员"))
        self.comboBox.setItemText(2, _translate("MainWindow", "酒店前台"))
        self.comboBox.setItemText(3, _translate("MainWindow", "酒店经理"))



if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

