# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/DataServer/FilesBen/Work/WIP/ApplicationMenuFolders/ui/dialogDisplayText.ui'
#
# Created: Sat Jun 26 00:37:50 2010
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
        self.btnCopy = QtGui.QPushButton(self.layoutWidget)
        self.btnCopy.setObjectName("btnCopy")
        self.hboxlayout.addWidget(self.btnCopy)
        self.btnOkay = QtGui.QPushButton(self.layoutWidget)
        self.btnOkay.setObjectName("btnOkay")
        self.hboxlayout.addWidget(self.btnOkay)
        self.gridLayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.txtDisplay = QtGui.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDisplay.setFont(font)
        self.txtDisplay.setOpenExternalLinks(True)
        self.txtDisplay.setObjectName("txtDisplay")
        self.gridLayout.addWidget(self.txtDisplay, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnOkay, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCopy.setText(QtGui.QApplication.translate("Dialog", "Copy to Clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOkay.setText(QtGui.QApplication.translate("Dialog", "&OK", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

