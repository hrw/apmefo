# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/DataServer/FilesBen/Work/WIP/ApplicationMenuFolders/ui/dialogSelectFile.ui'
#
# Created: Fri Jun 25 23:32:13 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 380)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 761, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtGui.QSpacerItem(131, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.btnOkay = QtGui.QPushButton(self.layoutWidget)
        self.btnOkay.setObjectName("btnOkay")
        self.hboxlayout.addWidget(self.btnOkay)
        self.btnCancel = QtGui.QPushButton(self.layoutWidget)
        self.btnCancel.setObjectName("btnCancel")
        self.hboxlayout.addWidget(self.btnCancel)
        self.gridLayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.listFile = QtGui.QListWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listFile.setFont(font)
        self.listFile.setObjectName("listFile")
        self.gridLayout.addWidget(self.listFile, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnOkay, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Select Existing Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOkay.setText(QtGui.QApplication.translate("Dialog", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Dialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

