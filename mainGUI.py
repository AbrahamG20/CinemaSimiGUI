from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QDesktopWidget
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtMultimedia import QMediaContent
from home import Ui_CinemaSimi
from newProject import Ui_NewProject
from newExport import Ui_Export
from final import Ui_Final
from subtitle import subtitle, subtitle2
import sys
import os

actWidg = ''
exportt = 'no'
exportFVal = 0


class CinemaSimi(QWidget):
    def __init__(self):
        super(CinemaSimi, self).__init__()
        self.ui = Ui_CinemaSimi()
        self.ui.setupUi(self)

class NewProject(QWidget):
    def __init__(self):
        super(NewProject,self).__init__()
        self.ui = Ui_NewProject()
        self.ui.setupUi(self)

class NewExport(QWidget):
    def __init__(self):
        super(NewExport,self).__init__()
        self.ui = Ui_Export()
        self.ui.setupUi(self)

class Final(QWidget):
    def __init__(self):
        super(Final,self).__init__()
        self.ui = Ui_Final()
        self.ui.setupUi(self)

def goFinal():
    global actWidg

    if actWidg == 'newExport':
        if uiNE.progressBar.value() == 100:

            base = os.path.basename(uiNE.upload)
            newPath = uiNE.exportFolder + "\[SUB] " + base
            uiNE.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(newPath)))


            widget.addWidget(final)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.removeWidget(newExport)

            actWidg = 'final'

            os.remove(uiNE.actual)

        else:
            QTimer.singleShot(1000, lambda: goFinal())

    else:
        print("Se canceló la exportación")


def goHomeNP():
    global actWidg

    widget.addWidget(home)
    widget.setCurrentIndex(widget.currentIndex() + 1)
    widget.removeWidget(newProject)

    actWidg = 'home'

def goHomeF():
    global actWidg

    widget.addWidget(home)
    widget.setCurrentIndex(widget.currentIndex() + 1)
    widget.removeWidget(final)

    actWidg = 'home'

def goNewProject():
    global actWidg

    widget.addWidget(newProject)
    widget.setCurrentIndex(widget.currentIndex() + 1)
    widget.removeWidget(home)

    actWidg = 'newProject'

def goExport():
    global actWidg

    if actWidg == 'newProject':
        if uiNP.progressBar.value() == 100:
            widget.addWidget(newExport)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.removeWidget(newProject)

            actWidg = 'newExport'
        else:
            QTimer.singleShot(1000, lambda : goExport())
    else:
        print("Se canceló el proceso")


def updatePath(tmp, proc):
    uiNE.gpath = tmp
    uiNE.upload = proc

def recognition():
    uiNP.mediaPlayer.stop()
    uiNP.btnPlay.setEnabled(False)
    uiNP.btnPause.setEnabled(False)
    uiNP.btnStop.setEnabled(False)
    uiNP.btnProcesar.setEnabled(False)
    uiNP.lblEstimated.setText("          Inicializando, espere por favor ...")

    uiNP.progressBar.setValue(0)
    uiNP.progressBar.show()
    uiNP.btnCancel.setEnabled(True)
    uiNP.btnCancel.show()
    uiNP.lblEstimated.show()

    QTimer.singleShot(10, lambda : subtitle(uiNP.tmpPath))  #Subtitulado

    folder = os.path.dirname(uiNP.tmpPath) + "/tempOutput.mp4"
    updatePath(folder, uiNP.tmpPath)                            #Actualizar path temporal

def checkFolderNP():
    uiNP.increase()                                         #Incrementar barra de carga
    uiNP.lblEstimated.setText("          Procesando ...")
    QTimer.singleShot(10000, lambda : goExport())           #Dirigir a la ventana de Exportación

def processHandler():
    recognition()                                       #Procesamiento
    QTimer.singleShot(5000, lambda: checkFolderNP())    #Cambio de ventana

def cancelProgress():
    uiNP.cancelHandler()
    goHomeNP()

def export():
    global exportt
    global exportFVal

    if len(str(uiNE.exportFolder)) > 1:
        exportFVal = 1

    if uiNE.comboBox.currentIndex() != 0 and exportFVal > 0:
        uiNE.mediaPlayer.stop()
        uiNE.btnPlay.setEnabled(False)
        uiNE.btnPause.setEnabled(False)
        uiNE.btnStop.setEnabled(False)
        uiNE.btnExportar.setEnabled(False)
        uiNE.comboBox.setEnabled(False)

        uiNE.progressBar.setValue(0)
        uiNE.progressBar.show()
        uiNE.btnCancel.setEnabled(True)
        uiNE.btnCancel.show()
        uiNE.lblEstimated.setText("            Inicializando, espere por favor ...")
        uiNE.lblEstimated.show()

        QTimer.singleShot(10, lambda : subtitle2(uiNE.upload,uiNE.exportFolder,0))

        exportt = 'si'
        #base = os.path.basename(upload)
        #newPath = uiNE.exportFolder + "\[SUB] " + base

    else:
        exportt = 'no'
        uiNE.lblEstimated.setText("  Por favor, seleccione la calidad y ubicación de exportación deseada.")
        uiNE.lblEstimated.show()

def checkFolderNE():
    uiNE.increase()                                         #Incrementar barra de carga
    uiNE.lblEstimated.setText("          Exportando ...")
    QTimer.singleShot(10000, lambda : goFinal())           #Dirigir a la ventana de Exportación

def exportHandler():
    global exportt
    export()                                                #Procesamiento
    if exportt == 'si':
        QTimer.singleShot(5000, lambda: checkFolderNE())    #Cambio de ventana

def cancelExport():
    uiNE.cancelHandler()
    goNewProject()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    home = QtWidgets.QWidget()
    uiHome = Ui_CinemaSimi()
    uiHome.setupUi(home)
    uiHome.btnAdd.clicked.connect(goNewProject)

    newProject = QtWidgets.QWidget()
    uiNP = Ui_NewProject()
    uiNP.setupUi(newProject)
    uiNP.btnProcesar.clicked.connect(processHandler)
    uiNP.btnCancel.clicked.connect(cancelProgress)

    newExport = QtWidgets.QWidget()
    uiNE = Ui_Export()
    uiNE.setupUi(newExport)
    uiNE.btnExportar.clicked.connect(exportHandler)
    uiNE.btnCancel.clicked.connect(cancelExport)

    final = QtWidgets.QWidget()
    uiFinal = Ui_Final()
    uiFinal.setupUi(final)
    uiFinal.btnInicio.clicked.connect(goHomeF)

    widget.addWidget(home)

    widget.setFixedWidth(1080)
    widget.setFixedHeight(720)

    qtRectangle = widget.frameGeometry()
    centerpoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerpoint)
    widget.move(qtRectangle.topLeft())

    widget.setWindowIcon(icon)
    widget.setWindowTitle("CinemaSimi")
    widget.show()

    sys.exit(app.exec_())

