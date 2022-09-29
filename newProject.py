from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import QUrl, QTimer
from tinytag import TinyTag
import math
import time
import speechRecognition
from PyQt5.QtWidgets import QVBoxLayout
import icons_rc

class Ui_NewProject(object):
    actualPath = ""
    def setupUi(self, NewProject):
        NewProject.setObjectName("NewProject")
        NewProject.resize(1080, 741)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewProject.sizePolicy().hasHeightForWidth())
        NewProject.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewProject.setWindowIcon(icon)
        NewProject.setStyleSheet("background-color: rgb(255, 234, 212);\n"
"\n"
"")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(NewProject)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.encabezado = QtWidgets.QHBoxLayout()
        self.encabezado.setObjectName("encabezado")
        self.lblLogo = QtWidgets.QLabel(NewProject)
        self.lblLogo.setMaximumSize(QtCore.QSize(280, 100))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/icons/recursos/cinemaSimi.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setObjectName("lblLogo")
        self.encabezado.addWidget(self.lblLogo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.encabezado.addItem(spacerItem)

        self.lblUPC = QtWidgets.QLabel(NewProject)
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

        self.VideoPlayer = QVideoWidget(NewProject)
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

        self.btnPlay = QtWidgets.QPushButton(NewProject)
        self.btnPlay.setMinimumSize(QtCore.QSize(50, 50))
        self.btnPlay.setMaximumSize(QtCore.QSize(50, 50))
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

        self.btnPause = QtWidgets.QPushButton(NewProject)
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

        self.btnStop = QtWidgets.QPushButton(NewProject)
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

        self.progressBar = QtWidgets.QProgressBar(NewProject)
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
        self.layoutBtns.addWidget(self.progressBar)

        self.progressBar.hide()

        self.timer = QTimer(NewProject)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutBtns.addItem(spacerItem2)
        self.btnCancel = QtWidgets.QPushButton(NewProject)
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
        self.layoutBtns.addWidget(self.btnCancel)

        self.btnCancel.hide()

        self.layoutOpciones.addLayout(self.layoutBtns)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(NewProject)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label = QtWidgets.QLabel(NewProject)
        self.label.setMinimumSize(QtCore.QSize(350, 0))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(NewProject)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton.setStyleSheet("background-image: url(:/icons/recursos/upload.png);\n"
"QPushButton{\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/recursos/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.label_8 = QtWidgets.QLabel(NewProject)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.lblEstimated = QtWidgets.QLabel(NewProject)
        self.lblEstimated.setObjectName("lblEstimated")
        self.gridLayout.addWidget(self.lblEstimated, 0, 2, 1, 1)

        self.lblEstimated.hide()

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)

        self.layoutOpciones.addLayout(self.gridLayout)
        self.layoutSecundario_.addLayout(self.layoutOpciones)

        self.btnProcesar = QtWidgets.QPushButton(NewProject)
        self.btnProcesar.setMinimumSize(QtCore.QSize(150, 40))
        self.btnProcesar.setStyleSheet("/*BUTTON */\n"
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
"QPushButton::hover{\n"
"background-color: rgb(73, 136, 175);\n"
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
"QPushButton::pressed {  \n"
"background-color: rgb(58, 113, 154) \n"
"}\n"
"")
        self.btnProcesar.setObjectName("btnProcesar")
        self.layoutSecundario_.addWidget(self.btnProcesar)

        self.layoutPrincipal.addLayout(self.layoutSecundario_)
        self.verticalLayout_2.addLayout(self.layoutPrincipal)

        self.retranslateUi(NewProject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

    def retranslateUi(self, NewProject):
        _translate = QtCore.QCoreApplication.translate
        NewProject.setWindowTitle(_translate("NewProject", "CinemaSimi - Nuevo Proyecto"))

        self.btnCancel.setText(_translate("NewProject", "Cancelar Exportación"))
        self.label_9.setText(_translate("NewProject", "Tipo de vídeo:         .mp4"))
        self.label.setText(_translate("NewProject", " Seleccione su vídeo ..."))
        self.label_8.setText(_translate("NewProject", "Duración del vídeo:  00:01:20"))
        self.lblEstimated.setText(_translate("NewProject", " Tiempo estimado:"))
        self.btnProcesar.setText(_translate("NewProject", "Procesar"))

        self.pushButton.clicked.connect(self.pushButton_handler)

        self.btnPlay.setEnabled(False)
        self.btnPause.setEnabled(False)
        self.btnStop.setEnabled(False)
        self.btnCancel.setEnabled(False)
        self.btnProcesar.setEnabled(False)

        self.btnPlay.clicked.connect(self.play_video)
        self.btnPause.clicked.connect(self.mediaPlayer.pause)
        self.btnStop.clicked.connect(self.mediaPlayer.stop)

        self.btnProcesar.clicked.connect(self.procesarHandler)

        self.btnCancel.clicked.connect(self.cancelHandler)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def pushButton_handler(self):
        self.openVideo()

    def increase_step(self):
        self.progressBar.setValue(self.progressBar.value()+1)


    def procesarHandler(self):
        self.recognition()


    def recognition(self):
        self.mediaPlayer.stop()
        self.btnPlay.setEnabled(False)
        self.btnPause.setEnabled(False)
        self.btnStop.setEnabled(False)
        self.btnProcesar.setEnabled(False)

        self.progressBar.show()
        self.btnCancel.setEnabled(True)
        self.btnCancel.show()
        self.lblEstimated.show()

        self.timer.start(100)
        self.timer.timeout.connect(self.increase_step)

        speechRecognition.recognize(self.actualPath)

    def cancel(self):
        if self.timer.isActive() :
            self.timer.stop()

        self.progressBar.setValue(0)

        self.btnPlay.setEnabled(True)
        self.btnPause.setEnabled(True)
        self.btnStop.setEnabled(True)
        self.btnProcesar.setEnabled(True)

        self.progressBar.hide()
        self.btnCancel.setEnabled(False)
        self.btnCancel.hide()
        self.lblEstimated.hide()

    def cancelHandler(self):
        self.cancel()

    def openVideo(self):

        def convert_size(size_bytes):
            if size_bytes == 0:
                return "0B"
            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            i = int(math.floor(math.log(size_bytes, 1024)))
            p = math.pow(1024, i)
            s = round(size_bytes / p, 2)
            return "%s %s" % (s, size_name[i])

        filename = QFileDialog.getOpenFileName(None,'Seleccionar Video', r"C:\\Users\\Abraham\\Videos\\","Archivos de Video(*.mp4 *.mkv *.wmv)")
        path = filename[0]
        if path == "":
            return

        self.btnPlay.setEnabled(True)
        self.btnPause.setEnabled(True)
        self.btnStop.setEnabled(True)
        self.label.setText("  " + path)
        video = TinyTag.get(path)
        self.actualPath = path
        self.label_9.setText("Tipo de vídeo:         " + path[len(path)-4:])
        self.label_8.setText("Duración del vídeo:  " + time.strftime('%H:%M:%S', time.gmtime(video.duration)))

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))

        self.btnProcesar.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewProject = QtWidgets.QWidget()
    ui = Ui_NewProject()
    ui.setupUi(NewProject)
    NewProject.show()
    sys.exit(app.exec_())
