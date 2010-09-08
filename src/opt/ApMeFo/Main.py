import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from classes.mainApp import *

if __name__ == '__main__':

    #Creating Qt application
    app = QtGui.QApplication(sys.argv)

    mainApp = MainApp()
    mainApp.folderlist.readFilenames()

#    readme = mainApp.readReadme()
#    warning = mainApp.readWarning()

    ui = MainWindow(mainApp)
#    ui.txtReadme.setText(readme)
#    ui.txtWarning.setHtml(warning)
    ui.show()

    #Initing application
    sys.exit(app.exec_())
