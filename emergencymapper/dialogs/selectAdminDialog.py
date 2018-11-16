# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/selectAdminDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectAdminDialog(object):
    def setupUi(self, selectAdminDialog):
        selectAdminDialog.setObjectName("selectAdminDialog")
        selectAdminDialog.resize(563, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(selectAdminDialog)
        self.buttonBox.setGeometry(QtCore.QRect(395, 260, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(selectAdminDialog)
        self.label.setGeometry(QtCore.QRect(341, 10, 144, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(selectAdminDialog)
        self.pushButton.setGeometry(QtCore.QRect(484, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(selectAdminDialog)
        self.buttonBox.accepted.connect(selectAdminDialog.accept)
        self.buttonBox.rejected.connect(selectAdminDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(selectAdminDialog)

    def retranslateUi(self, selectAdminDialog):
        _translate = QtCore.QCoreApplication.translate
        selectAdminDialog.setWindowTitle(_translate("selectAdminDialog", "Dialog"))
        self.label.setText(_translate("selectAdminDialog", "Select Administrative Layer :) "))
        self.pushButton.setText(_translate("selectAdminDialog", "PushButton"))

