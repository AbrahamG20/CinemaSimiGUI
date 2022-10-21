from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget
from home import Ui_CinemaSimi
from newProject import Ui_NewProject
from newExport import Ui_Export
import sys


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
        #self.ui.btnCancel.clicked.connect(self.goExport)

class NewExport(QWidget):
    def __init__(self):
        super(NewExport,self).__init__()
        self.ui = Ui_Export()
        self.ui.setupUi(self)

def goHome():
    widget.setCurrentIndex(0)

def goNewProject():
    widget.setCurrentIndex(1)

def goExport():
    widget.setCurrentIndex(2)

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
    ui1.btnCancel.clicked.connect(goExport)

    newExport = QtWidgets.QWidget()
    ui2 = Ui_Export()
    ui2.setupUi(newExport)


    widget.addWidget(CinemaSimi)
    widget.addWidget(newProject)
    widget.addWidget(newExport)

    widget.setFixedWidth(1080)
    widget.setFixedHeight(720)

    widget.setWindowIcon(icon)
    widget.setWindowTitle("CinemaSimi")

    widget.show()

    #while ui1.timer.isActive():
    #    print(ui1.progressBar.value())
    #    if ui1.progressBar.value() == 100:
    #        widget.setCurrentIndex(2)

    sys.exit(app.exec_())

