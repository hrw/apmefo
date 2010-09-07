# -*- coding: utf-8 -*-
import curses.ascii
import urllib

from PyQt4 import QtGui
from PyQt4 import QtCore

from PyQt4.QtCore import QFile,  QIODevice
from PyQt4.QtMaemo5 import QMaemo5InformationBox

from ui.appFolders import MainWindow
from ui.dialogDisplayText import DialogDisplayText

from classes.folderContent import FolderContent
from classes.folderList import FolderList
from classes.diagnosisTool import DiagnosisTool

import resources_rc

class FolderName(Exception):
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)

class MainApp():
    
    def __init__ (self,  parent = None):
        
        self.folderlist = FolderList()
        self.foldercontent = FolderContent(self.folderlist)
    
    def getFileNameFromName(self,  input):
#        try:
#            input = unicode(input)
#            input = input.encode("ascii")
#        except:
#            raise FolderName("Not Ascii")
        
        output = ""
        for j in input:
                if curses.ascii.isalnum(j) or j == "-" or j =="_":
                   output = output + j
                elif j == " " or j == "\\" or j == "/":
                   output = output + "_"
                else:
                    output = output + "-"
#                else:
#                    raise FolderName("Special")
        
        output = urllib.quote_plus(output)
        return output
        
    def readDirectoryTemplate(self):
        templateFile = QFile(":/resources/dirFolder.txt")
        templateFile.open(QIODevice.ReadOnly)
        template = templateFile.readData(templateFile.size())
        templateFile.close()
        return template
        
    def readMenuTemplate(self):
        templateFile = QFile(":/resources/menuFolder.txt")
        templateFile.open(QIODevice.ReadOnly)
        template = templateFile.readData(templateFile.size())
        templateFile.close()
        return template
        
    def readHildonMenuTemplate(self):
        templateFile = QFile(":/resources/hildonMenu.txt")
        templateFile.open(QIODevice.ReadOnly)
        template = templateFile.readData(templateFile.size())
        templateFile.close()
        return template
        
    def readReadme(self):
        readmeFile = QFile(":/resources/readme.txt")
        readmeFile.open(QIODevice.ReadOnly)
        readme = readmeFile.readData(readmeFile.size())
        readmeFile.close()
        return readme
        
    def readWarning(self):
        readmeFile = QFile(":/resources/warning.txt")
        readmeFile.open(QIODevice.ReadOnly)
        readme = readmeFile.readData(readmeFile.size())
        readmeFile.close()
        return readme
        
    def showInfoPopup(self,  target,  text):
        QMaemo5InformationBox.information(target, text)
        
    def popupReadme(self):
        dialog = DialogDisplayText()
        dialog.setWindowTitle("Readme")

        dialog.txtDisplay.setHtml(self.readReadme())
        
        dialog.show()
        dialog.exec_()
        
    def popupDiagnosis(self,  hildonMenuPath):
        dialog = DialogDisplayText()
        dialog.setWindowTitle("Diagnosis Tool")

        diagTool = DiagnosisTool()
        
        exists = diagTool.getIsSetHildonMenu(hildonMenuPath)
        diag = "hildon.menu set: " + str(exists) +"\n"
        if exists:
            template = self.readHildonMenuTemplate()
            matches = diagTool.compareHildonMenu(hildonMenuPath,  template)
            diag += "hildon.menu matches: " + str(matches) + "\n"
            if  not matches:
                diag += "\n"
                diag += diagTool.hildonFromPath
                diag += "\n\n"
                
        diag += "\nDirectory Files:\n"
        list = diagTool.getFilesDirectory(self.folderlist.DirpathGlobal,  self.folderlist.DirpathLocal)
        for file in list:
            diag += file + "\n"
        diag += "\n"
        
        diag += "\nMenu Files:\n"
        list = diagTool.getFilesMenu(self.folderlist.Menupath)
        for file in list:
            diag += file + "\n"
        diag += "\n"
            
        dialog.txtDisplay.setText(diag)
        
        dialog.show()
        dialog.exec_()
