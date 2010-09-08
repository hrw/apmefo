# -*- coding: utf-8 -*-
import os
import codecs
from xml.dom.minidom import parse, parseString,  Node

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QIcon,  QListWidgetItem,  QProgressDialog,  QAbstractItemView
from PyQt4.QtCore import QDir,  QStringList,  QString,  Qt

from ui.dialogSelectFile import DialogSelectFile

class FolderContent():

    def __init__(self,  folderlist):
        self.folderlist = folderlist
        self.foldername = ""
        self.folderapps = []
        self.allapps = {}
        self.selFile = ""
        self.selFiles = {}
        self.xmlTree = None

    def setFileName(self,  filename):
        self.selFile= filename

    def setFileNames(self,  filenames):
        self.selFiles = filenames

    def setFolder(self,  folder):
        self.foldername = unicode (folder.toUtf8(),  "utf-8")

        self.readAllApps()

        dirFileName = self.folderlist.nameref[unicode (folder.toUtf8(),  "utf-8")]
        folderName = dirFileName.split("/")[-1]
        folderName = folderName.split(".directory")[0]
        menuFileName = self.folderlist.Menupath + folderName + ".menu"

        menuFile = open(menuFileName,  "r")

#        self.folderapps.clear()
        self.folderapps = []

        self.xmlTree = parse(menuFile)

        parentInclude = self.xmlTree.getElementsByTagName("Include")[0]

        filenames = parentInclude.getElementsByTagName("Filename")

        for filenode in filenames:
            rc = []
            for node in filenode.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    rc.append(node.data)
            nodeText = "".join(rc)
            try:
                appName = self.folderlist.getNameFromDirFile(self.folderlist.DirpathLocal + nodeText)
            except:
                try:
                    appName = self.folderlist.getNameFromDirFile(self.folderlist.DirpathGlobal + nodeText)
                except:
                    appName = ""
            if not appName == "":
#                self.folderapps[appName] = {}
                self.folderapps.append(appName)
            filenode.parentNode.removeChild(filenode)
            filenode.unlink()

        parentLayout = self.xmlTree.getElementsByTagName("Layout")
        for layout in parentLayout:
            layout.parentNode.removeChild(layout)
            layout.unlink()

        menuFile.close()

#        print self.xmlTree.toxml()

    def updateFolder(self):
        backupxml = self.xmlTree.cloneNode(True)
        includeNode = self.xmlTree.getElementsByTagName("Include")[0]
        includeNode.normalize()
        layoutNode = self.xmlTree.createElement("Layout")

#        includeNode.parentNode.insertBefore(layoutNode, includeNode)
        includeNode.parentNode.appendChild(layoutNode)

        for app in self.folderapps:
            newNode = self.xmlTree.createElement("Filename")
            newNode.appendChild(self.xmlTree.createTextNode(str(self.allapps[app]["path"].split("/")[-1])))
            includeNode.appendChild(newNode)
            newNode = self.xmlTree.createElement("Filename")
            newNode.appendChild(self.xmlTree.createTextNode(str(self.allapps[app]["path"].split("/")[-1])))
            layoutNode.appendChild(newNode)

        dirFileName = self.folderlist.nameref[self.foldername]
        folderName = dirFileName.split("/")[-1]
        folderName = folderName.split(".directory")[0]
        menuFileName = self.folderlist.Menupath + folderName + ".menu"

#        print self.xmlTree.toxml()

        fcont = self.xmlTree.toxml()

        s = codecs.open(menuFileName,'w','utf-8')
        s.write(fcont)
        s.close()
#        menuFile = open(menuFileName,  "w")
#        menuFile.write(self.xmlTree.toxml())
#        menuFile.close

        self.xmlTree = backupxml

    def addApp(self,  filename):
#        self.folderapps[filename] = {}
        self.folderapps.append(filename)

    def removeApp(self,  filename):
#        del self.folderapps[filename]
        self.folderapps.remove(filename)

    def selectApp(self,  parent = None):
        self.readAllApps()
        dialog = DialogSelectFile(self)
        dialog.setWindowTitle("Select Application")
        dialog.listFile.setSelectionMode(QAbstractItemView.MultiSelection)

        progress = QtGui.QProgressDialog("Please wait while loading icons", "Hide", 0, 100, parent)
        progress.setWindowModality(QtCore.Qt.WindowModal)
        progress.setAutoReset(True)
        progress.setAutoClose(True)
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.setWindowTitle("Loading...")
        progress.show()

        progress.setValue(0)

        for app in self.allapps:
            if not self.allapps[app]["icon"]  == None:
                icon = QIcon.fromTheme(self.allapps[app]["icon"])
                if not icon.hasThemeIcon(self.allapps[app]["icon"]):
                    icon = QIcon("/usr/share/pixmaps/" + self.allapps[app]["icon"])
                listItem = QListWidgetItem(icon,  app,  dialog.listFile,  QListWidgetItem.UserType)
            else:
                listItem = QListWidgetItem(app,  dialog.listFile,  QListWidgetItem.UserType)

        dialog.listFile.sortItems()

        progress.setValue(100)

        dialog.show()
        dialog.exec_()

        selected = self.selFiles
        self.selFiles = {}
        return selected

    def getAppIsNoDisplay(self,  input):
        inputFile = open(input)
        filetxt = inputFile.read()

        filetxt = QString(filetxt)

        splitAppl = filetxt.split("Type=Appl", QString.KeepEmptyParts,  Qt.CaseInsensitive)
        if len(splitAppl) <= 1:
            return True

        splitDisplay = filetxt.split("NoDisplay=", QString.KeepEmptyParts,  Qt.CaseInsensitive)
        if  len(splitDisplay) <= 1:
            return False

        filetxt = splitDisplay[1]
        filetxt = filetxt.split("\n")[0]

        filetxt = QString(filetxt)
        filetxt = filetxt.toLower()

        if filetxt == "true":
            return True
        else:
            return False

    def readAllApps(self):
        self.allapps.clear()

        directoryLocal = QDir(self.folderlist.DirpathLocal)
        directoryLocal.setFilter(QDir.Files | QDir.Hidden);
        directoryLocal.setNameFilters(QStringList("*.desktop"))

        directoryGlobal = QDir(self.folderlist.DirpathGlobal)
        directoryGlobal.setFilter(QDir.Files | QDir.Hidden);
        directoryGlobal.setNameFilters(QStringList("*.desktop"))

        for file in directoryGlobal.entryList():
            if not self.getAppIsNoDisplay(self.folderlist.DirpathGlobal + file):
                part = self.folderlist.getNameFromDirFile(self.folderlist.DirpathGlobal + file)
                icon = self.folderlist.getIconFromDirFile(self.folderlist.DirpathGlobal + file)
                self.allapps[part] = {}
                self.allapps[part]["path"] = self.folderlist.DirpathGlobal + file
                self.allapps[part]["icon"] = icon
        for file in directoryLocal.entryList():
            if not self.getAppIsNoDisplay(self.folderlist.DirpathLocal + file):
                part = self.folderlist.getNameFromDirFile(self.folderlist.DirpathLocal + file)
                icon = self.folderlist.getIconFromDirFile(self.folderlist.DirpathLocal + file)
                self.allapps[part] = {}
                self.allapps[part]["path"] = self.folderlist.DirpathLocal + file
                self.allapps[part]["icon"] = icon


