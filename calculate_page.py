# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")

        Form.resize(560, 800)
        Form.setMinimumSize(QtCore.QSize(560, 800))
        Form.setMaximumSize(QtCore.QSize(560, 800))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 541, 161))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.Percent_Button = QtWidgets.QPushButton(Form)
        self.Percent_Button.setGeometry(QtCore.QRect(10, 170, 120, 80))
        self.Percent_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.Percent_Button.setMaximumSize(QtCore.QSize(160, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.Percent_Button.setFont(font)
        self.Percent_Button.setStyleSheet("QPushButton#Percent_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Percent_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Percent_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Percent_Button.setObjectName("Percent_Button")
        self.AC_Button = QtWidgets.QPushButton(Form)
        self.AC_Button.setGeometry(QtCore.QRect(150, 170, 120, 80))
        self.AC_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.AC_Button.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.AC_Button.setFont(font)
        self.AC_Button.setStyleSheet("QPushButton#AC_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#AC_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#AC_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.AC_Button.setObjectName("AC_Button")
        self.Arrow_Button = QtWidgets.QPushButton(Form)
        self.Arrow_Button.setGeometry(QtCore.QRect(290, 170, 120, 80))
        self.Arrow_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.Arrow_Button.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Arrow_Button.setFont(font)
        self.Arrow_Button.setStyleSheet("QPushButton#Arrow_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Arrow_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Arrow_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Arrow_Button.setObjectName("Arrow_Button")
        self.Div_Button = QtWidgets.QPushButton(Form)
        self.Div_Button.setGeometry(QtCore.QRect(430, 170, 120, 80))
        self.Div_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.Div_Button.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Div_Button.setFont(font)
        self.Div_Button.setStyleSheet("QPushButton#Div_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Div_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Div_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Div_Button.setObjectName("Div_Button")
        self.Number7 = QtWidgets.QPushButton(Form)
        self.Number7.setGeometry(QtCore.QRect(10, 270, 120, 80))
        self.Number7.setMinimumSize(QtCore.QSize(120, 80))
        self.Number7.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number7.setFont(font)
        self.Number7.setStyleSheet("QPushButton#Number7{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number7:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number7:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number7.setObjectName("Number7")
        self.Number4 = QtWidgets.QPushButton(Form)
        self.Number4.setGeometry(QtCore.QRect(10, 370, 120, 80))
        self.Number4.setMinimumSize(QtCore.QSize(120, 80))
        self.Number4.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number4.setFont(font)
        self.Number4.setStyleSheet("QPushButton#Number4{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number4:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number4:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number4.setObjectName("Number4")
        self.Number1 = QtWidgets.QPushButton(Form)
        self.Number1.setGeometry(QtCore.QRect(10, 470, 120, 80))
        self.Number1.setMinimumSize(QtCore.QSize(120, 80))
        self.Number1.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number1.setFont(font)
        self.Number1.setStyleSheet("QPushButton#Number1{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number1:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number1:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number1.setObjectName("Number1")
        self.Number8 = QtWidgets.QPushButton(Form)
        self.Number8.setGeometry(QtCore.QRect(150, 270, 120, 80))
        self.Number8.setMinimumSize(QtCore.QSize(120, 80))
        self.Number8.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number8.setFont(font)
        self.Number8.setStyleSheet("QPushButton#Number8{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number8:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number8:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number8.setObjectName("Number8")
        self.Number9 = QtWidgets.QPushButton(Form)
        self.Number9.setGeometry(QtCore.QRect(290, 270, 120, 80))
        self.Number9.setMinimumSize(QtCore.QSize(120, 80))
        self.Number9.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number9.setFont(font)
        self.Number9.setStyleSheet("QPushButton#Number9{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number9:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number9:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number9.setObjectName("Number9")
        self.Multiply_Button = QtWidgets.QPushButton(Form)
        self.Multiply_Button.setGeometry(QtCore.QRect(430, 270, 120, 80))
        self.Multiply_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.Multiply_Button.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Multiply_Button.setFont(font)
        self.Multiply_Button.setStyleSheet("QPushButton#Multiply_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Multiply_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Multiply_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Multiply_Button.setObjectName("Multiply_Button")
        self.Number5 = QtWidgets.QPushButton(Form)
        self.Number5.setGeometry(QtCore.QRect(150, 370, 120, 80))
        self.Number5.setMinimumSize(QtCore.QSize(120, 80))
        self.Number5.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number5.setFont(font)
        self.Number5.setStyleSheet("QPushButton#Number5{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number5:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number5:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number5.setObjectName("Number5")
        self.Number6 = QtWidgets.QPushButton(Form)
        self.Number6.setGeometry(QtCore.QRect(290, 370, 120, 80))
        self.Number6.setMinimumSize(QtCore.QSize(120, 80))
        self.Number6.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number6.setFont(font)
        self.Number6.setStyleSheet("QPushButton#Number6{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number6:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number6:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number6.setObjectName("Number6")
        self.Minus_Button = QtWidgets.QPushButton(Form)
        self.Minus_Button.setGeometry(QtCore.QRect(430, 370, 120, 80))
        self.Minus_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.Minus_Button.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Minus_Button.setFont(font)
        self.Minus_Button.setStyleSheet("QPushButton#Minus_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Minus_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Minus_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Minus_Button.setObjectName("Minus_Button")
        self.Number2 = QtWidgets.QPushButton(Form)
        self.Number2.setGeometry(QtCore.QRect(150, 470, 120, 80))
        self.Number2.setMinimumSize(QtCore.QSize(120, 80))
        self.Number2.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number2.setFont(font)
        self.Number2.setStyleSheet("QPushButton#Number2{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number2:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number2:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number2.setObjectName("Number2")
        self.Number3 = QtWidgets.QPushButton(Form)
        self.Number3.setGeometry(QtCore.QRect(290, 470, 120, 80))
        self.Number3.setMinimumSize(QtCore.QSize(120, 80))
        self.Number3.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number3.setFont(font)
        self.Number3.setStyleSheet("QPushButton#Number3{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number3:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number3:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number3.setObjectName("Number3")
        self.Add_Button = QtWidgets.QPushButton(Form)
        self.Add_Button.setGeometry(QtCore.QRect(430, 470, 120, 80))
        self.Add_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.Add_Button.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Add_Button.setFont(font)
        self.Add_Button.setStyleSheet("QPushButton#Add_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Add_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Add_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Add_Button.setObjectName("Add_Button")
        self.Change_Button = QtWidgets.QPushButton(Form)
        self.Change_Button.setGeometry(QtCore.QRect(10, 570, 120, 80))
        self.Change_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.Change_Button.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Change_Button.setFont(font)
        self.Change_Button.setStyleSheet("QPushButton#Change_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Change_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Change_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Change_Button.setObjectName("Change_Button")
        self.Number0 = QtWidgets.QPushButton(Form)
        self.Number0.setGeometry(QtCore.QRect(150, 570, 120, 80))
        self.Number0.setMinimumSize(QtCore.QSize(120, 80))
        self.Number0.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Number0.setFont(font)
        self.Number0.setStyleSheet("QPushButton#Number0{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Number0:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Number0:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Number0.setObjectName("Number0")
        self.Dot_Button = QtWidgets.QPushButton(Form)
        self.Dot_Button.setGeometry(QtCore.QRect(290, 570, 120, 80))
        self.Dot_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.Dot_Button.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Dot_Button.setFont(font)
        self.Dot_Button.setStyleSheet("QPushButton#Dot_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Dot_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Dot_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Dot_Button.setObjectName("Dot_Button")
        self.Equal_Button = QtWidgets.QPushButton(Form)
        self.Equal_Button.setGeometry(QtCore.QRect(10, 670, 541, 111))
        self.Equal_Button.setMinimumSize(QtCore.QSize(80, 80))
        self.Equal_Button.setMaximumSize(QtCore.QSize(9999, 9999))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Equal_Button.setFont(font)
        self.Equal_Button.setStyleSheet("QPushButton#Equal_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Equal_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Equal_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Equal_Button.setObjectName("Equal_Button")
        self.Exit_Button = QtWidgets.QPushButton(Form)
        self.Exit_Button.setGeometry(QtCore.QRect(430, 570, 120, 80))
        self.Exit_Button.setMinimumSize(QtCore.QSize(120, 80))
        self.Exit_Button.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Exit_Button.setFont(font)
        self.Exit_Button.setStyleSheet("QPushButton#Exit_Button{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Exit_Button:hover{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"QPushButton#Exit_Button:pressed{\n"
"    \n"
"    background-color: rgb(143, 143, 143);\n"
"}")
        self.Exit_Button.setObjectName("Exit_Button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Máy tính - Ứng dụng hỗ trợ học tập"))
        self.label.setText(_translate("Form", "0"))
        self.Percent_Button.setText(_translate("Form", "%"))
        self.AC_Button.setText(_translate("Form", "AC"))
        self.Arrow_Button.setText(_translate("Form", "Del"))
        self.Div_Button.setText(_translate("Form", "/"))
        self.Number7.setText(_translate("Form", "7"))
        self.Number4.setText(_translate("Form", "4"))
        self.Number1.setText(_translate("Form", "1"))
        self.Number8.setText(_translate("Form", "8"))
        self.Number9.setText(_translate("Form", "9"))
        self.Multiply_Button.setText(_translate("Form", "x"))
        self.Number5.setText(_translate("Form", "5"))
        self.Number6.setText(_translate("Form", "6"))
        self.Minus_Button.setText(_translate("Form", "-"))
        self.Number2.setText(_translate("Form", "2"))
        self.Number3.setText(_translate("Form", "3"))
        self.Add_Button.setText(_translate("Form", "+"))
        self.Change_Button.setText(_translate("Form", "+/-"))
        self.Number0.setText(_translate("Form", "0"))
        self.Dot_Button.setText(_translate("Form", "."))
        self.Equal_Button.setText(_translate("Form", "="))
        self.Exit_Button.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
