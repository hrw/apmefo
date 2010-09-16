# -*- coding: utf-8 -*-

"""
Module implementing DialogDisplayText.
"""
from PyQt4 import QtGui

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_dialogDisplayText import Ui_Dialog

class DialogDisplayText(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_btnCopy_released(self):
        """
        Slot documentation goes here.
        """
        clip = QtGui.QApplication.clipboard()
        text = self.txtDisplay.toPlainText()
        clip.setText(text)
