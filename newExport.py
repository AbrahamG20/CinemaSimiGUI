import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import QUrl, QTimer
from tinytag import TinyTag
import math
import time
from subtitle import subtitle2
from PyQt5.QtMultimediaWidgets import QVideoWidget

gpath = ''
upload = ''

def updatePath(tmp, proc):
    global gpath
    global upload

    gpath = tmp
    upload = proc

class Ui_Export(object):

    def setupUi(self, Export):
        Export.setObjectName("Export")
        Export.resize(1080, 741)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Export.sizePolicy().hasHeightForWidth())
        Export.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Export.setWindowIcon(icon)
        Export.setStyleSheet("background-color: rgb(255, 234, 212);\n"
"\n"
"")

        self.exportPath = ""

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Export)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.encabezado = QtWidgets.QHBoxLayout()
        self.encabezado.setObjectName("encabezado")

        self.lblLogo = QtWidgets.QLabel(Export)
        self.lblLogo.setMaximumSize(QtCore.QSize(280, 100))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/icons/recursos/cinemaSimi.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setObjectName("lblLogo")

        self.encabezado.addWidget(self.lblLogo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.encabezado.addItem(spacerItem)

        self.lblUPC = QtWidgets.QLabel(Export)
        self.lblUPC.setMinimumSize(QtCore.QSize(100, 100))
        self.lblUPC.setMaximumSize(QtCore.QSize(100, 100))
        self.lblUPC.setText("")
        self.lblUPC.setPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"))
        self.lblUPC.setScaledContents(True)
        self.lblUPC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblUPC.setObjectName("lblUPC")

        self.encabezado.addWidget(self.lblUPC)

        self.verticalLayout_2.addLayout(self.encabezado)

        self.layoutPrincipal = QtWidgets.QVBoxLayout()
        self.layoutPrincipal.setObjectName("layoutPrincipal")

        self.VideoPlayer = QVideoWidget(Export)
        self.VideoPlayer.setMinimumSize(QtCore.QSize(720, 440))
        self.VideoPlayer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.VideoPlayer.setStyleSheet("background-color: rgb(224, 230, 237);")
        self.VideoPlayer.setObjectName("VideoPlayer")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.VideoPlayer)

        self.layoutPrincipal.addWidget(self.VideoPlayer)

        self.layoutSecundario_ = QtWidgets.QHBoxLayout()
        self.layoutSecundario_.setObjectName("layoutSecundario_")

        self.layoutOpciones = QtWidgets.QVBoxLayout()

        self.layoutOpciones.setObjectName("layoutOpciones")
        self.layoutBtns = QtWidgets.QHBoxLayout()
        self.layoutBtns.setObjectName("layoutBtns")

        self.btnPlay = QtWidgets.QPushButton(Export)
        self.btnPlay.setEnabled(True)
        self.btnPlay.setMinimumSize(QtCore.QSize(50, 50))
        self.btnPlay.setMaximumSize(QtCore.QSize(50, 50))
        self.btnPlay.setAutoFillBackground(False)
        self.btnPlay.setStyleSheet("/*BUTTON */\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(132, 146, 166);\n"
"    color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(73, 136, 175);\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"    background-color:#B5B5B5;\n"
"    color: #D6D6D6;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"QPushButton::pressed {  \n"
"background-color: rgb(58, 113, 154) \n"
"}\n"
"")
        self.btnPlay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/recursos/play_ic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon1)
        self.btnPlay.setIconSize(QtCore.QSize(40, 40))
        self.btnPlay.setObjectName("btnPlay")

        self.layoutBtns.addWidget(self.btnPlay)

        self.btnPause = QtWidgets.QPushButton(Export)
        self.btnPause.setMinimumSize(QtCore.QSize(50, 50))
        self.btnPause.setMaximumSize(QtCore.QSize(50, 50))
        self.btnPause.setStyleSheet("/*BUTTON */\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(132, 146, 166);\n"
"    color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(73, 136, 175);\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"    background-color:#B5B5B5;\n"
"    color: #D6D6D6;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"QPushButton::pressed {  \n"
"background-color: rgb(58, 113, 154) \n"
"}\n"
"")
        self.btnPause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/recursos/pause_ic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon2)
        self.btnPause.setIconSize(QtCore.QSize(40, 40))
        self.btnPause.setObjectName("btnPause")

        self.layoutBtns.addWidget(self.btnPause)

        self.btnStop = QtWidgets.QPushButton(Export)
        self.btnStop.setMinimumSize(QtCore.QSize(50, 50))
        self.btnStop.setMaximumSize(QtCore.QSize(50, 50))
        self.btnStop.setStyleSheet("/*BUTTON */\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(132, 146, 166);\n"
"    color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(73, 136, 175);\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"    background-color:#B5B5B5;\n"
"    color: #D6D6D6;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"QPushButton::pressed {  \n"
"background-color: rgb(58, 113, 154) \n"
"}\n"
"")
        self.btnStop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/recursos/stop_ic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon3)
        self.btnStop.setIconSize(QtCore.QSize(40, 40))
        self.btnStop.setObjectName("btnStop")

        self.layoutBtns.addWidget(self.btnStop)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutBtns.addItem(spacerItem1)

        self.progressBar = QtWidgets.QProgressBar(Export)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(400, 10))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 13))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 0.5px;\n"
"\n"
"    border-color: #8492A6;\n"
"    border-radius: 9px;\n"
"    background-color: #ffffff;\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"    background-color: #94A5C9;\n"
"}   ")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")

        self.progressBar.hide()

        self.timer = QTimer(Export)

        self.layoutBtns.addWidget(self.progressBar)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutBtns.addItem(spacerItem2)
        self.btnCancel = QtWidgets.QPushButton(Export)
        self.btnCancel.setEnabled(True)
        self.btnCancel.setMinimumSize(QtCore.QSize(180, 30))
        self.btnCancel.setStyleSheet("/*BUTTON */\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color:rgb(132, 146, 166);\n"
"    color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"    background-color:#B5B5B5;\n"
"    color: #D6D6D6;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(73, 136, 175);\n"
"}\n"
"\n"
"QPushButton::pressed {  \n"
"background-color: rgb(58, 113, 154) \n"
"}\n"
"")
        self.btnCancel.setObjectName("btnCancel")

        self.btnCancel.hide()

        self.layoutBtns.addWidget(self.btnCancel)
        self.layoutOpciones.addLayout(self.layoutBtns)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.lblLocation = QtWidgets.QLabel(Export)
        self.lblLocation.setMinimumSize(QtCore.QSize(350, 0))
        self.lblLocation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lblLocation.setObjectName("lblLocation")
        self.gridLayout.addWidget(self.lblLocation, 0, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(Export)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton.setStyleSheet("background-image: url(:/icons/recursos/upload.png);\n"
"QPushButton{\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/recursos/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.lblLenght = QtWidgets.QLabel(Export)
        self.lblLenght.setObjectName("lblLenght")
        self.gridLayout.addWidget(self.lblLenght, 1, 0, 1, 1)

        self.lblTipe = QtWidgets.QLabel(Export)
        self.lblTipe.setObjectName("lblTipe")
        self.gridLayout.addWidget(self.lblTipe, 2, 0, 1, 1)

        self.lblSize = QtWidgets.QLabel(Export)
        self.lblSize.setObjectName("lblSize")
        self.gridLayout.addWidget(self.lblSize, 2, 3, 1, 1)

        self.comboBox = QtWidgets.QComboBox(Export)
        self.comboBox.setStyleSheet("/*style for the QComboBox*/\n"
"\n"
"#comboBox{\n"
"    border: 1px solid rgb(132, 146, 166);\n"
"    border-radius: 1px;\n"
"    padding-left: 10px;\n"
"    background-color:     rgb(255,255,255);\n"
"    height: 28px;\n"
"}\n"
"\n"
"/*style for dropdown area*/\n"
"\n"
"#comboBox::drop-down{\n"
"    border: 0px;\n"
"}\n"
"\n"
"/*style for drop down arrow*/\n"
"#comboBox::down-arrow{\n"
"    image: url(:/icons/recursos/down.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 15px;\n"
"}\n"
"\n"
"/*style for QComboBox after open select menu*/\n"
"\n"
"#comboBox::on{\n"
"    border: 2px solid #c2dbfe;\n"
"}\n"
"\n"
"/*style for list menu*/\n"
"\n"
"#comboBox QListView{\n"
"    font-size: 12px;\n"
"    border: 1px solid rgba(0,0,0,10%);\n"
"    padding: 5px;\n"
"    background-color:     rgb(255,255,255);\n"
"    outline: 0px;\n"
"}\n"
"\n"
"\n"
"/*style for list items*/\n"
" \n"
"#comboBox QListView:item{\n"
"    padding-left: 10px;\n"
"    background-color:     rgb(255,255,255);\n"
"}\n"
"\n"
"#comboBox QListView:item:hover{\n"
"    background-color:  rgb(73, 136, 175);\n"
"}\n"
"\n"
"#comboBox QListView:item:selected{\n"
"    background-color: rgb(73, 136, 175);\n"
"}\n"
"\n"
"\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)

        self.lblEstimated = QtWidgets.QLabel(Export)
        self.lblEstimated.setObjectName("lblEstimated")
        self.gridLayout.addWidget(self.lblEstimated, 0, 3, 1, 1)

        self.lblEstimated.hide()

        self.layoutOpciones.addLayout(self.gridLayout)
        self.layoutSecundario_.addLayout(self.layoutOpciones)
        self.btnExportar = QtWidgets.QPushButton(Export)
        self.btnExportar.setEnabled(True)
        self.btnExportar.setMinimumSize(QtCore.QSize(150, 40))
        self.btnExportar.setStyleSheet("/*BUTTON */\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(132, 146, 166);\n"
"    color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"    background-color:#B5B5B5;\n"
"    color: #D6D6D6;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    font: bold ;\n"
"}\n"
"\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(73, 136, 175);\n"
"}\n"
"\n"
"QPushButton::pressed {  \n"
"background-color: rgb(58, 113, 154) \n"
"}\n"
"")
        self.btnExportar.setObjectName("btnExportar")

        self.layoutSecundario_.addWidget(self.btnExportar)
        self.layoutPrincipal.addLayout(self.layoutSecundario_)
        self.verticalLayout_2.addLayout(self.layoutPrincipal)

        self.retranslateUi(Export)
        QtCore.QMetaObject.connectSlotsByName(Export)

    def retranslateUi(self, Export):

        _translate = QtCore.QCoreApplication.translate
        Export.setWindowTitle(_translate("Export", "CinemaSimi - Exportar"))

        self.btnCancel.setText(_translate("Export", "Cancelar Exportación"))
        self.lblLocation.setText(_translate("Export", " Seleccionar carpeta..."))
        self.lblLenght.setText(_translate("Export", "Duración del vídeo:  "))
        self.lblTipe.setText(_translate("Export", "Tipo de vídeo:         "))
        self.lblSize.setText(_translate("Export", " Tamaño del video: "))

        self.comboBox.setItemText(0, _translate("Export", "Seleccione la calidad de video"))
        self.comboBox.setItemText(1, _translate("Export", "360p"))
        self.comboBox.setItemText(2, _translate("Export", "480p"))
        self.comboBox.setItemText(3, _translate("Export", "720p"))
        self.comboBox.setItemText(4, _translate("Export", "1080p"))

        self.lblEstimated.setText(_translate("Export", " Tiempo estimado:"))
        self.btnExportar.setText(_translate("Export", "Exportar"))

        self.pushButton.clicked.connect(self.pushButton_handler)

        self.btnPlay.setEnabled(True)
        self.btnPause.setEnabled(True)
        self.btnStop.setEnabled(True)
        self.btnCancel.setEnabled(False)

        #self.btnExportar.setEnabled(False)

        self.btnPlay.clicked.connect(self.play_video)
        self.btnPause.clicked.connect(self.mediaPlayer.pause)
        self.btnStop.clicked.connect(self.mediaPlayer.stop)

        self.btnExportar.clicked.connect(self.run)
        self.btnCancel.clicked.connect(self.cancelHandler)

        self.actual = ""
        self.folder = ""
        self.exportFolder = ""

    def play_video(self):
        if len(self.actual) < 1:
            global gpath
            self.update(gpath)

        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def increase_step(self):
        self.progressBar.setValue(self.progressBar.value()+1)

    def run(self):

        if self.comboBox.currentIndex() != 0:
            self.mediaPlayer.stop()
            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
            self.btnExportar.setEnabled(False)
            self.comboBox.setEnabled(False)

            self.progressBar.show()
            self.btnCancel.setEnabled(True)
            self.btnCancel.show()
            self.lblEstimated.show()

            self.timer.start(100)
            self.timer.timeout.connect(self.increase_step)

            global upload

            subtitle2(upload,self.exportFolder,0)

            base = os.path.basename(upload)
            newPath = self.exportFolder + "\SUB_" + base

            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(newPath)))

        else:
            print("Seleccione la calidad de vídeo deseada.")

    def cancel(self):
        if self.timer.isActive() :
            self.timer.stop()
        self.progressBar.setValue(0)

        self.btnPlay.setEnabled(True)
        self.btnPause.setEnabled(True)
        self.btnStop.setEnabled(True)
        self.btnExportar.setEnabled(True)
        self.comboBox.setEnabled(True)

        self.progressBar.hide()
        self.btnCancel.setEnabled(False)
        self.btnCancel.hide()
        self.lblEstimated.hide()
        os.remove(self.actual)

        self.pushButton.setEnabled(False)
        self.comboBox.setEnabled(False)

    def cancelHandler(self):
        self.cancel()

    def pushButton_handler(self):
        self.selectFolder()

    def selectFolder(self):
        def convert_size(size_bytes):
            if size_bytes == 0:
                return "0B"
            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            i = int(math.floor(math.log(size_bytes, 1024)))
            p = math.pow(1024, i)
            s = round(size_bytes / p, 2)
            return "%s %s" % (s, size_name[i])
        print(self.actual)

        if len(self.actual) < 1:
            global gpath
            self.update(gpath)

        filename = QFileDialog.getExistingDirectory(None,'Seleccionar Carpeta')

        path = filename

        self.exportFolder = path

        if path == "":
            return

        self.lblLocation.setText("  " + path)
        video = TinyTag.get(self.actual)

        self.lblTipe.setText("Tipo de vídeo:         " + self.actual[len(self.actual)-4:])
        self.lblLenght.setText("Duración del vídeo:  " + time.strftime('%H:%M:%S', time.gmtime(video.duration)))

    def update(self, path):
        self.actual = path
        self.folder = os.path.dirname(path)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Export = QtWidgets.QWidget()
    ui = Ui_Export()
    ui.setupUi(Export)
    Export.show()
    sys.exit(app.exec_())
