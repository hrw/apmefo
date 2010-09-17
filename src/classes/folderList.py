# -*- coding: utf-8 -*-
import string
import locale
import gettext

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QIcon,  QListWidgetItem,  QProgressDialog
from PyQt4.QtCore import QDir,  QStringList,  QString

from ui.dialogSelectFile import DialogSelectFile

import ConfigParser

class FolderList():

    IconpathLocal = "home/user/.local/share/icons/hicolor/48x48/hildon/"
    IconpathGlobal = "/usr/share/icons/hicolor/48x48/hildon/"
    DirpathLocal = "/home/user/.local/share/applications/hildon/"
    DirpathGlobal = "/usr/share/applications/hildon/"
    Menupath = "/home/user/.config/menus/submenus/"

    def __init__(self):
        self.nameref = {}
        self.selFile = ""
        self.langs = []
        loc = locale.getdefaultlocale()[0]
        self.langs = [loc, "en_UK", "en_US"]

    def setFileName(self,  filename):
        self.selFile= filename

    def selectFile(self):

        dialog = DialogSelectFile(self)

        self.readFilenames()
        for index in self.nameref:
#            dialog.listFile.addItem(QString.fromUtf8(index))
            listItem = QListWidgetItem(index,  dialog.listFile,  QListWidgetItem.UserType)

        dialog.listFile.sortItems()

        dialog.show()
        dialog.exec_()

        selected = self.selFile
        self.selFile = ""
        return selected

    def selectIcon(self,  parent = None):

        dialog = DialogSelectFile(self)
        dialog.setWindowTitle("Select Icon")

        progress = QtGui.QProgressDialog("Please wait while loading icons", "Hide", 0, 100, parent)
        progress.setWindowModality(QtCore.Qt.WindowModal)
        progress.setAutoReset(True)
        progress.setAutoClose(True)
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.setWindowTitle("Loading...")
        progress.show()

        progress.setValue(0)

        directoryLocal = QDir(self.IconpathLocal)
        directoryLocal.setFilter(QDir.Files | QDir.Hidden | QDir.NoSymLinks);
        directoryLocal.setNameFilters(QStringList("*.png"))

        directoryGlobal = QDir(self.IconpathGlobal)
        directoryGlobal.setFilter(QDir.Files | QDir.Hidden | QDir.NoSymLinks);
        directoryGlobal.setNameFilters(QStringList("*.png"))

        for file in directoryLocal.entryList():
            icon = QIcon(self.IconpathLocal + file)
            part = string.split(file, '.png')[0]
            listItem = QListWidgetItem(icon,  part,  dialog.listFile,  QListWidgetItem.UserType)

        progress.setValue(50)

        for file in directoryGlobal.entryList():
            icon = QIcon(self.IconpathGlobal + file)
            part = string.split(file, '.png')[0]
            listItem = QListWidgetItem(icon,  part,   dialog.listFile,  QListWidgetItem.UserType)


        dialog.listFile.sortItems()
        progress.setValue(100)
#        progress.hide()

        dialog.show()
        dialog.exec_()

        selected = self.selFile
        self.selFile = ""
        return selected

    def getNameFromDirFile(self, input):
        desktop = ConfigParser.ConfigParser()
        try:
            desktop.readfp(open(input))
            try:
                filetxt = desktop.get('Desktop Entry', 'Name')
            except:
                filetxt = "";
            try:
                domain = desktop.get('Desktop Entry', 'X-Text-Domain')
            except:
                domain = "maemo-af-desktop"
        except ConfigParser.ParsingError:
            #show note which .desktop file is wrong?
            inputFile = open(input)
            filecontent= inputFile.read()
            try:
                filetxt = filecontent.split("Name=")[1]
            except:
                filetxt = filecontent.split("Name =")[1]

            filetxt = filetxt.split("\n")[0].split("\r")[0].lstrip()

            try:
                domain = filecontent.split("X-Text-Domain")[1]
                domain = domain.lstrip(' =')
            except:
                domain = "maemo-af-desktop"

        if  filetxt == "":
            part = string.split(input,  '/')[-1]
            part = string.split(part, '.directory')[0]
            part = string.split(part, '.desktop')[0]
        else:
            gettext.textdomain(domain)
            lang = gettext.translation(domain, "/usr/share/locale",  languages= self.langs, fallback = True)
            part = unicode(QString.fromUtf8(lang.gettext(filetxt)).toUtf8(),  "utf-8")
        return part

    def getIconFromDirFile(self, input):
        desktop = ConfigParser.ConfigParser()
        try:
            desktop.readfp(open(input))
            try:
                return desktop.get('Desktop Entry', 'Icon')
            except:
                return
        except ConfigParser.ParsingError:
            #show note which .desktop file is wrong?
            inputFile = open(input)
            filecontent= inputFile.read()
            try:
                filetxt = filecontent.split("Icon")[1]
                return domain.lstrip(' =')
            except:
                return

    def readFilenames(self):
        self.nameref.clear()

        directoryLocal = QDir(self.DirpathLocal)
        directoryLocal.setFilter(QDir.Files | QDir.Hidden | QDir.NoSymLinks);
        directoryLocal.setNameFilters(QStringList("*.directory"))

        directoryGlobal = QDir(self.DirpathGlobal)
        directoryGlobal.setFilter(QDir.Files | QDir.Hidden | QDir.NoSymLinks);
        directoryGlobal.setNameFilters(QStringList("*.directory"))

        for file in directoryGlobal.entryList():
            part = self.getNameFromDirFile(self.DirpathGlobal + file)
            self.nameref[part] = self.DirpathGlobal + file
        for file in directoryLocal.entryList():
            part = self.getNameFromDirFile(self.DirpathLocal + file)
            self.nameref[part] = self.DirpathLocal + file
