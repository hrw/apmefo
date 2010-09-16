# -*- coding: utf-8 -*-

"""
Module implementing DialogSelectFile.
"""

from PyQt4.QtGui import QDialog,  QAbstractItemView
from PyQt4.QtCore import pyqtSignature

from Ui_dialogSelectFile import Ui_Dialog

class DialogSelectFile(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mainApp,  parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.mainApp = mainApp

    @pyqtSignature("")
    def on_btnOkay_released(self):
        """
        Slot documentation goes here.
        """
        if self.listFile.selectionMode() == QAbstractItemView.MultiSelection:
            items = []
            for index in xrange(self.listFile.count()):
                item = self.listFile.item(index)
                if item.isSelected():
                    items.append(item.text())
            self.mainApp.setFileNames(items)
        else:
            self.mainApp.setFileName(self.listFile.currentItem().text())
