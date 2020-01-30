# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\lenovo\Desktop\操作系统课设\GUI\logins.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-70, 180, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 130, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.user_lineEdit = QtWidgets.QLabel(Dialog)
        self.user_lineEdit.setGeometry(QtCore.QRect(80, 90, 54, 12))
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.pwd_lineEdit = QtWidgets.QLabel(Dialog)
        self.pwd_lineEdit.setGeometry(QtCore.QRect(80, 140, 54, 12))
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 54, 12))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.user_lineEdit.setText(_translate("Dialog", "用户名"))
        self.pwd_lineEdit.setText(_translate("Dialog", "密码"))
        self.label_3.setText(_translate("Dialog", "登录"))

