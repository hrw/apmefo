import os

from PyQt4.QtCore import QDir,  QStringList

class DiagnosisTool():

    hildonFromPath = ""

    def getIsSetHildonMenu(self, hildonMenuPath):
        return os.path.exists(hildonMenuPath)

    def compareHildonMenu(self,  hildonMenuPath,  hildonMenuTemplate):
        f = open(hildonMenuPath, 'r')
        self.hildonFromPath = f.read()
        f.close()

        return hildonMenuTemplate == self.hildonFromPath

    def getFilesDirectory(self,  globalPath,  localPath):
        directoryLocal = QDir(localPath)
        directoryLocal.setFilter(QDir.Files | QDir.Hidden | QDir.NoSymLinks);
        directoryLocal.setNameFilters(QStringList("*.directory"))

        directoryGlobal = QDir(globalPath)
        directoryGlobal.setFilter(QDir.Files | QDir.Hidden | QDir.NoSymLinks);
        directoryGlobal.setNameFilters(QStringList("*.directory"))

        return directoryGlobal.entryList() + directoryLocal.entryList()

    def getFilesMenu(self, localPath):
        directoryLocal = QDir(localPath)
        directoryLocal.setFilter(QDir.Files | QDir.Hidden | QDir.NoSymLinks);
        directoryLocal.setNameFilters(QStringList("*.menu"))

        return directoryLocal.entryList()
