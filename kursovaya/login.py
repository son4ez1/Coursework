# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(416, 354)
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(90, 240, 221, 41))
        self.pushButton.setStyleSheet("background-color: rgb(185, 198, 241);\n"
"background-color: rgb(170, 255, 127);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(login)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 290, 221, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(185, 198, 241);\n"
"background-color: rgb(170, 255, 127);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(login)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 401, 73))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(login)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 180, 261, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(login)
        self.lineEdit.setGeometry(QtCore.QRect(70, 120, 261, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.pushButton.setText(_translate("login", "Зарегестрироваться"))
        self.pushButton_2.setText(_translate("login", "Войти"))
        self.label.setText(_translate("login", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Регистрация</span></p></body></html>"))
        self.label_2.setText(_translate("login", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
