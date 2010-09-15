# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogDisplayText.ui'
#
# Created: Tue Sep 14 15:47:04 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(849, 562)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.txtDisplay = QtGui.QTextBrowser(Dialog)
        self.txtDisplay.setObjectName("txtDisplay")
        self.gridLayout.addWidget(self.txtDisplay, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnCopy = QtGui.QPushButton(Dialog)
        self.btnCopy.setObjectName("btnCopy")
        self.horizontalLayout.addWidget(self.btnCopy)
        self.btnOkay = QtGui.QPushButton(Dialog)
        self.btnOkay.setObjectName("btnOkay")
        self.horizontalLayout.addWidget(self.btnOkay)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnOkay, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCopy.setText(QtGui.QApplication.translate("Dialog", "Copy to clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOkay.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

