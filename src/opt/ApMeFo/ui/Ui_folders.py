# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'folders.ui'
#
# Created: Wed Sep  8 21:46:30 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 656)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setSizeIncrement(QtCore.QSize(4, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.inpEditName = QtGui.QLineEdit(self.centralwidget)
        self.inpEditName.setObjectName("inpEditName")
        self.horizontalLayout.addWidget(self.inpEditName)
        self.btnEditNameSelect = QtGui.QPushButton(self.centralwidget)
        self.btnEditNameSelect.setObjectName("btnEditNameSelect")
        self.horizontalLayout.addWidget(self.btnEditNameSelect)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setSizeIncrement(QtCore.QSize(14, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.inpIcon = QtGui.QLineEdit(self.centralwidget)
        self.inpIcon.setObjectName("inpIcon")
        self.horizontalLayout_4.addWidget(self.inpIcon)
        self.btnIconSelect = QtGui.QPushButton(self.centralwidget)
        self.btnIconSelect.setObjectName("btnIconSelect")
        self.horizontalLayout_4.addWidget(self.btnIconSelect)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btnDelete = QtGui.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_5.addWidget(self.btnDelete)
        self.btnCreate = QtGui.QPushButton(self.centralwidget)
        self.btnCreate.setObjectName("btnCreate")
        self.horizontalLayout_5.addWidget(self.btnCreate)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Folders", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEditNameSelect.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Icon", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIconSelect.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCreate.setText(QtGui.QApplication.translate("MainWindow", "Create/Edit", None, QtGui.QApplication.UnicodeUTF8))

