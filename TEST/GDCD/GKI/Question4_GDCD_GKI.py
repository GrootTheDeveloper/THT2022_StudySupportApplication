# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Question4_GDCD_GKI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 702)
        MainWindow.setMinimumSize(QtCore.QSize(1081, 702))
        MainWindow.setMaximumSize(QtCore.QSize(1081, 702))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.D_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.D_Button.setGeometry(QtCore.QRect(20, 450, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.D_Button.setFont(font)
        self.D_Button.setObjectName("D_Button")
        self.Time = QtWidgets.QLineEdit(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(700, 20, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.Time.setFont(font)
        self.Time.setObjectName("Time")
        self.C_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.C_Button.setGeometry(QtCore.QRect(20, 370, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.C_Button.setFont(font)
        self.C_Button.setObjectName("C_Button")
        self.Next_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Next_Button.setGeometry(QtCore.QRect(270, 550, 551, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        self.Next_Button.setFont(font)
        self.Next_Button.setObjectName("Next_Button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(80, 20, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.B_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.B_Button.setGeometry(QtCore.QRect(20, 290, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.B_Button.setFont(font)
        self.B_Button.setObjectName("B_Button")
        self.A_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.A_Button.setGeometry(QtCore.QRect(20, 210, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.A_Button.setFont(font)
        self.A_Button.setObjectName("A_Button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 1071, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 21))
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
        self.D_Button.setText(_translate("MainWindow", "D."))
        self.C_Button.setText(_translate("MainWindow", "C."))
        self.Next_Button.setText(_translate("MainWindow", "PushButton"))
        self.label_4.setText(_translate("MainWindow", "Thời gian còn lại:"))
        self.B_Button.setText(_translate("MainWindow", "B."))
        self.A_Button.setText(_translate("MainWindow", "A."))
        self.label_3.setText(_translate("MainWindow", "Tên:"))
        self.label_2.setText(_translate("MainWindow", "Câu 4."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
