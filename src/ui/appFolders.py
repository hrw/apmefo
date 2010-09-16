# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import os
import codecs

from PyQt4.QtGui import QMainWindow,  QIcon,  QListWidgetItem
from PyQt4.QtCore import pyqtSignature,  QString, Qt

from Ui_appFolders import Ui_MainWindow
import Ui_folders

class FoldersWindow(QMainWindow, Ui_folders.Ui_MainWindow):

    def __init__(self, mainApp,  parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
#        self.setAttribute(Qt.WA_Maemo5StackedWindow)
        self.mainApp = mainApp

    @pyqtSignature("")
    def on_btnDelete_released(self):
        """
        Slot documentation goes here.
        """
        if not self.inpEditName.text():
            self.mainApp.showInfoPopup(self, "Please select a folder first!")
            return

        self.mainApp.folderlist.readFilenames()
        try:
            dirFileName = self.mainApp.folderlist.nameref[unicode (self.inpEditName.text().toUtf8(),  "utf-8")]
        except:
            self.mainApp.showInfoPopup(self, "Could not find directory!")

        folderName = dirFileName.split("/")[-1]
        folderName = folderName.split(".directory")[0]
        menuFileName = self.mainApp.folderlist.Menupath + folderName + ".menu"

        os.remove(dirFileName)
        try:
            os.remove(menuFileName)
            self.mainApp.showInfoPopup(self, "Your folder was successfully removed!")
            self.inpEditName.setText("")
        except:
            self.mainApp.showInfoPopup(self, "Your folder was removed, but could not find menu entry!")

    @pyqtSignature("")
    def on_btnEditNameSelect_released(self):
        """
        Slot documentation goes here.
        """
        self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, True)
        filename = self.mainApp.folderlist.selectFile()
        if not filename == "":
            self.inpEditName.setText(filename)
        self.inpIconName.setText("")
        self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, False)

    @pyqtSignature("")
    def on_btnIconSelect_released(self):
        """
        Slot documentation goes here.
        """
        self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, True)
        filename = self.mainApp.folderlist.selectIcon(self)
        if not filename == "":
            self.inpIcon.setText(filename)
        self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, False)

    @pyqtSignature("")
    def on_btnCreate_released(self):
        """
        Slot documentation goes here.
        """
        if not self.inpEditName.text() or not  self.inpIcon.text():
            self.mainApp.showInfoPopup(self, "Please enter both name and icon!")
            return

        self.mainApp.folderlist.readFilenames()

        isNew = True

#        displayName = QString.fromUtf8(self.inpEditName.text())
        displayString = QString.fromUtf8(self.inpEditName.text())
        displayName = unicode (self.inpEditName.text().toUtf8(),  "utf-8")

        if displayName in self.mainApp.folderlist.nameref:
            dirFileName = self.mainApp.folderlist.nameref[displayName]
            folderName = dirFileName.split("/")[-1]
            folderName = folderName.split(".directory")[0]
            isNew = False
        else:
#            try:
            folderName = self.mainApp.getFileNameFromName(str(displayString.toAscii()))
            dirFileName = self.mainApp.folderlist.DirpathLocal + folderName + ".directory"
#            except:
#                self.mainApp.showInfoPopup(self, "Please note that folder names are restricted " \
#                                          + "to letters, numbers, spaces and the following " \
#                                          + "special characters:\n - _ \\ /")
#                return

        dirFileText = QString.fromUtf8(self.mainApp.readDirectoryTemplate())
        dirFileText = dirFileText.replace('%%name%%',  displayName)
        dirFileText = dirFileText.replace('%%icon%%',  self.inpIcon.text())

        if not os.path.exists(self.mainApp.folderlist.Menupath):
            os.makedirs(self.mainApp.folderlist.Menupath)

        try:
            fcont = unicode (dirFileText.toUtf8(),  "utf-8")

            s = codecs.open(dirFileName,'w','utf-8')
            s.write(fcont)
            s.close()
#            f = open(dirFileName, 'w')
#            f.write(dirFileText)
#            f.close()

            if isNew:

                menuFileText = QString.fromUtf8(self.mainApp.readMenuTemplate())
                menuFileText = menuFileText.replace('%%name%%',  displayName)
                menuFileText = menuFileText.replace('%%path%%',  folderName)

                menuFileName = self.mainApp.folderlist.Menupath + folderName + ".menu"

                fcont = unicode (menuFileText.toUtf8(),  "utf-8")

                s = codecs.open(menuFileName,'w','utf-8')
                s.write(fcont)
                s.close()
#                f = open(menuFileName, 'w')
#                f.write(menuFileText)
#                f.close()

            self.mainApp.showInfoPopup(self, "Your folder was successfully saved!")
        except:
            self.mainApp.showInfoPopup(self, "An unknown error occured while trying to save!")


class MainWindow(QMainWindow, Ui_MainWindow):

    hildonMenuPath = "/home/user/.config/menus/hildon.menu"

    """
    Class documentation goes here.
    """
    def __init__(self, mainApp,  parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_Maemo5AutoOrientation, True)
        self.mainApp = mainApp

    @pyqtSignature("")
    def on_btnAppAdd_released(self):
        """
        Slot documentation goes here.
        """
        if not self.inpAddName.text():
            self.mainApp.showInfoPopup(self, "Please select a folder first!")
            return

        filenames = self.mainApp.foldercontent.selectApp(self)
        for filename in filenames:
            self.mainApp.foldercontent.addApp(unicode (filename.toUtf8(),  "utf-8"))
        self.refreshContent()

    @pyqtSignature("")
    def on_btnAppDelete_released(self):
        """
        Slot documentation goes here.
        """
        if not self.listApps.currentItem():
            self.mainApp.showInfoPopup(self, "Please select an application first!")
            return

        filename = self.listApps.currentItem().text()
        if not filename == "":
            self.mainApp.foldercontent.removeApp(filename)
            self.refreshContent()

    @pyqtSignature("")
    def on_btnUpdate_released(self):
        """
        Slot documentation goes here.
        """
        self.mainApp.foldercontent.folderapps = []
        for index in xrange(self.listApps.count()):
            item = self.listApps.item(index)
            self.mainApp.foldercontent.folderapps.append(unicode (item.text().toUtf8(),  "utf-8"))
        self.mainApp.foldercontent.updateFolder()
        self.mainApp.showInfoPopup(self, "Your folder was successfully saved!")

    @pyqtSignature("")
    def on_btnAddNameSelect_released(self):
        """
        Slot documentation goes here.
        """
        self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, True)
        filename = self.mainApp.folderlist.selectFile()
        if not filename == "":
            self.inpAddName.setText(filename)
        self.mainApp.foldercontent.setFolder(filename)

        self.refreshContent()
        self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, False)

    def refreshContent(self):
        self.listApps.clear()
#        self.listApps.reset()

        for app in self.mainApp.foldercontent.folderapps:
            if not self.mainApp.foldercontent.allapps[app]["icon"]  == None:
                icon = QIcon.fromTheme(self.mainApp.foldercontent.allapps[app]["icon"])
                if not icon.hasThemeIcon(self.mainApp.foldercontent.allapps[app]["icon"]):
                    icon = QIcon("/usr/share/pixmaps/" + self.mainApp.foldercontent.allapps[app]["icon"])
                listItem = QListWidgetItem(icon,  app,  self.listApps,  QListWidgetItem.UserType)
#                listItem = QListViewItem(icon,  app,  self.listApps,  QListWidgetItem.UserType)
            else:
                listItem = QListWidgetItem(app,  self.listApps,  QListWidgetItem.UserType)
#                listItem = QListViewItem(app,  self.listApps,  QListWidgetItem.UserType)

    @pyqtSignature("")
    def on_actionActivate_triggered(self):
        """
        Slot documentation goes here.
        """
        hildonMenuText = self.mainApp.readHildonMenuTemplate()
        try:
            f = open(self.hildonMenuPath, 'w')
            f.write(hildonMenuText)
            f.close()
            self.mainApp.showInfoPopup(self, "ApMeFo has been activated!")
        except:
            self.mainApp.showInfoPopup(self, "An error occured while trying to deactivate ApMeFo!")

    @pyqtSignature("")
    def on_actionDeactivate_triggered(self):
        """
        Slot documentation goes here.
        """
        try:
            os.remove(self.hildonMenuPath)
            self.mainApp.showInfoPopup(self, "ApMeFo has been deactivated!")
        except:
            self.mainApp.showInfoPopup(self, "An error occured while trying to deactivate ApMeFo!")

    @pyqtSignature("")
    def on_actionDiagnosis_Tool_triggered(self):
        """
        Slot documentation goes here.
        """
        self.mainApp.popupDiagnosis(self.hildonMenuPath)

    @pyqtSignature("")
    def on_actionFolders_triggered(self):
        """
        Slot documentation goes here.
        """
        foldersui = FoldersWindow(self.mainApp, self)
        foldersui.show()

    @pyqtSignature("")
    def on_actionReadme_triggered(self):
        """
        Slot documentation goes here.
        """
        self.mainApp.popupReadme()

    @pyqtSignature("")
    def on_btnAppUp_released(self):
        """
        Slot documentation goes here.
        """
        current = self.listApps.currentItem()
        currint = self.listApps.row(current)
        moving = self.listApps.takeItem(currint);
        self.listApps.insertItem(currint - 1, moving);
        self.listApps.setCurrentItem(moving)

    @pyqtSignature("")
    def on_btnAppDown_released(self):
        current = self.listApps.currentItem()
        currint = self.listApps.row(current)
        moving = self.listApps.takeItem(currint);
        self.listApps.insertItem(currint + 1, moving);
        self.listApps.setCurrentItem(moving)
