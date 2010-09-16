# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/dialogSelectFile.ui'
#
# Created: Thu Sep 16 13:44:02 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(803, 393)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listFile = QtGui.QListWidget(Dialog)
        self.listFile.setObjectName("listFile")
        self.gridLayout.addWidget(self.listFile, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnOkay = QtGui.QPushButton(Dialog)
        self.btnOkay.setObjectName("btnOkay")
        self.verticalLayout.addWidget(self.btnOkay)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnOkay, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Select folder", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOkay.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

