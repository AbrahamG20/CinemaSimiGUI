from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout
from home import Ui_CinemaSimi
from newProject import Ui_NewProject
import sys
import icons_rc

#class MainWindow(QMainWindow):
#    def __init__(self):
#        super(MainWindow, self).__init__()
#        self.startMainWindow()

#    def startMainWindow(self):
#        self.ui = Ui_CinemaSimi()
#        self.ui.setupUi(self)
#        self.ui.btnAdd.clicked.connect(self.startNewProject)

#    def startNewProject(self):
#        self.ui = Ui_NewProject()
#        self.ui.setupUi(self)

class Home(QWidget):
    def __init__(self):
        super(Home, self).__init__()
        self.ui = Ui_CinemaSimi()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.goNewProject)

class NewProject(QWidget):
    def __init__(self):
        super(NewProject,self).__init__()
        self.ui = Ui_NewProject()
        self.ui.setupUi(self)

def goNewProject():
    widget.setCurrentIndex(widget.currentIndex()+1)

def goHome():
    widget.setCurrentIndex(widget.currentIndex()-1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    CinemaSimi = QtWidgets.QWidget()
    ui = Ui_CinemaSimi()
    ui.setupUi(CinemaSimi)
    ui.btnAdd.clicked.connect(goNewProject)

    newProject = QtWidgets.QWidget()
    ui1 = Ui_NewProject()
    ui1.setupUi(newProject)
    ui1.btnProcesar.clicked.connect(goHome)

    widget.addWidget(CinemaSimi)
    widget.addWidget(newProject)
    widget.setFixedWidth(1080)
    widget.setFixedHeight(720)

    widget.setWindowIcon(icon)
    widget.setWindowTitle("CinemaSimi")

    widget.show()

    #CinemaSimi.show()
    sys.exit(app.exec_())


 #   def startMainWindow(self):
 #       self.ui = Ui_CinemaSimi()
 #       self.ui.setupUi(self)
 #       self.ui.btnAdd.clicked.connect(self.startNewProject)

 #   def startNewProject(self):
 #       print('test')
 #       self.ui = Ui_NewProject()
 #       self.ui.setupUi(self)