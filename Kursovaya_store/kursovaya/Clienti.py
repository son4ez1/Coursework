# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clienti.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Clienti(object):
    def setupUi(self, Clienti):
        Clienti.setObjectName("Clienti")
        Clienti.resize(559, 480)
        self.layoutWidget_2 = QtWidgets.QWidget(Clienti)
        self.layoutWidget_2.setGeometry(QtCore.QRect(390, 110, 111, 152))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineFind = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineFind.setObjectName("lineFind")
        self.verticalLayout_4.addWidget(self.lineFind)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbFind = QtWidgets.QComboBox(self.layoutWidget_2)
        self.cbFind.setObjectName("cbFind")
        self.verticalLayout_2.addWidget(self.cbFind)
        self.pbFind = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbFind.setFont(font)
        self.pbFind.setObjectName("pbFind")
        self.verticalLayout_2.addWidget(self.pbFind)
        self.lineChange = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineChange.setFont(font)
        self.lineChange.setStyleSheet("color: rgb(143, 143, 143);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 7pt \"MS Shell Dlg 2\";")
        self.lineChange.setText("")
        self.lineChange.setObjectName("lineChange")
        self.verticalLayout_2.addWidget(self.lineChange)
        self.pdChange = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pdChange.setFont(font)
        self.pdChange.setObjectName("pdChange")
        self.verticalLayout_2.addWidget(self.pdChange)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.label_5 = QtWidgets.QLabel(Clienti)
        self.label_5.setGeometry(QtCore.QRect(220, 0, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.twClient = QtWidgets.QTableWidget(Clienti)
        self.twClient.setGeometry(QtCore.QRect(10, 280, 531, 192))
        self.twClient.setObjectName("twClient")
        self.twClient.setColumnCount(0)
        self.twClient.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(Clienti)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 80, 111, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbOpen = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbOpen.setFont(font)
        self.pbOpen.setObjectName("pbOpen")
        self.verticalLayout.addWidget(self.pbOpen)
        self.pbAdd = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbAdd.setFont(font)
        self.pbAdd.setObjectName("pbAdd")
        self.verticalLayout.addWidget(self.pbAdd)
        self.pbDelet = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbDelet.setFont(font)
        self.pbDelet.setObjectName("pbDelet")
        self.verticalLayout.addWidget(self.pbDelet)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.lineID = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineID.setFont(font)
        self.lineID.setStyleSheet("color: rgb(143, 143, 143);")
        self.lineID.setText("")
        self.lineID.setObjectName("lineID")
        self.verticalLayout_3.addWidget(self.lineID)
        self.layoutWidget_3 = QtWidgets.QWidget(Clienti)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 70, 220, 299))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineName = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineName.setObjectName("lineName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineName)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineFamilia = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineFamilia.setObjectName("lineFamilia")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineFamilia)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineAdress = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineAdress.setObjectName("lineAdress")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineAdress)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.linePhone = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.linePhone.setObjectName("linePhone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.linePhone)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.linePochta = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.linePochta.setObjectName("linePochta")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.linePochta)

        self.retranslateUi(Clienti)
        QtCore.QMetaObject.connectSlotsByName(Clienti)

    def retranslateUi(self, Clienti):
        _translate = QtCore.QCoreApplication.translate
        Clienti.setWindowTitle(_translate("Clienti", "Form"))
        self.pbFind.setText(_translate("Clienti", "Найти"))
        self.lineChange.setWhatsThis(_translate("Clienti", "<html><head/><body><p>fnnnnn</p></body></html>"))
        self.pdChange.setText(_translate("Clienti", "Изменить"))
        self.label_5.setText(_translate("Clienti", "Клиенты"))
        self.pbOpen.setText(_translate("Clienti", "Открыть"))
        self.pbAdd.setText(_translate("Clienti", "Добавить"))
        self.pbDelet.setText(_translate("Clienti", "Удалить"))
        self.lineID.setWhatsThis(_translate("Clienti", "<html><head/><body><p>fnnnnn</p></body></html>"))
        self.label.setText(_translate("Clienti", "Имя"))
        self.label_2.setText(_translate("Clienti", "Фамилия "))
        self.label_4.setText(_translate("Clienti", "Адрес"))
        self.label_6.setText(_translate("Clienti", "Телефон"))
        self.label_7.setText(_translate("Clienti", "Почта"))