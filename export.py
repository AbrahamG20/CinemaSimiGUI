from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import QUrl
from tinytag import TinyTag
import math
import time
import icons_rc
from PyQt5.QtMultimediaWidgets import QVideoWidget


class Ui_Export(object):
    actualPath = ""
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

        self.layoutPrincipal.addWidget(self.VideoPlayer)

        self.progressBar = QtWidgets.QProgressBar(self.VideoPlayer)
        self.progressBar.setGeometry(QtCore.QRect(390, 190, 300, 10))

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.VideoPlayer)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())

        self.progressBar.setSizePolicy(sizePolicy)
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

        self.lblEstimated = QtWidgets.QLabel(self.VideoPlayer)
        self.lblEstimated.setGeometry(QtCore.QRect(390, 210, 300, 20))
        self.lblEstimated.setObjectName("lblEstimated")

        self.btnCancel = QtWidgets.QPushButton(self.VideoPlayer)
        self.btnCancel.setGeometry(QtCore.QRect(445, 250, 191, 28))
        self.btnCancel.setStyleSheet("/*BUTTON */\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: #94A5C9;\n"
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
"QPushButton::pressed {  \n"
"background-color: rgb(58, 113, 154) \n"
"}\n"
"")
        self.btnCancel.setObjectName("btnCancel")

        self.layoutSecundario_ = QtWidgets.QHBoxLayout()
        self.layoutSecundario_.setObjectName("layoutSecundario_")

        self.layoutOpciones = QtWidgets.QVBoxLayout()
        self.layoutOpciones.setObjectName("layoutOpciones")

        self.layoutBtns = QtWidgets.QHBoxLayout()
        self.layoutBtns.setObjectName("layoutBtns")

        self.btnPlay = QtWidgets.QPushButton(Export)
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
"background-color:#B5B5B5;\n"
"color: #D6D6D6;\n"
"border-width: 2px;\n"
"border-radius: 4px;\n"
"font: bold ;\n"
"}\n"
                                  
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
        self.layoutOpciones.addLayout(self.layoutBtns)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

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
        self.lblLocation = QtWidgets.QLabel(Export)
        self.lblLocation.setMinimumSize(QtCore.QSize(350, 0))
        self.lblLocation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lblLocation.setObjectName("lblLocation")
        self.gridLayout.addWidget(self.lblLocation, 0, 0, 1, 1)
        self.lblTipe = QtWidgets.QLabel(Export)
        self.lblTipe.setObjectName("lblTipe")
        self.gridLayout.addWidget(self.lblTipe, 2, 0, 1, 1)
        self.lblSize = QtWidgets.QLabel(Export)
        self.lblSize.setObjectName("lblSize")
        self.gridLayout.addWidget(self.lblSize, 1, 2, 1, 1)
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
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.layoutOpciones.addLayout(self.gridLayout)
        self.layoutSecundario_.addLayout(self.layoutOpciones)
        self.btnExportar = QtWidgets.QPushButton(Export)
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
        self.lblEstimated.setText(_translate("Export", "Tiempo estimado:"))
        self.btnCancel.setText(_translate("Export", "Cancelar Exportación"))
        self.lblLenght.setText(_translate("Export", "Duración del vídeo:  00:01:20"))
        self.lblLocation.setText(_translate("Export", "C:/User/Videos/"))
        self.lblTipe.setText(_translate("Export", "Tipo de vídeo:         .mp4"))
        self.lblSize.setText(_translate("Export", "Tamaño del video: "))

        self.comboBox.setItemText(0, _translate("Export", "Seleccione la calidad de video"))
        self.comboBox.setItemText(1, _translate("Export", "360p"))
        self.comboBox.setItemText(2, _translate("Export", "480p"))
        self.comboBox.setItemText(3, _translate("Export", "720p"))
        self.comboBox.setItemText(4, _translate("Export", "1080p"))

        self.btnExportar.setText(_translate("NewProject", "Exportar"))

        self.pushButton.clicked.connect(self.pushButton_handler)

        self.btnPlay.setEnabled(False)
        self.btnPause.setEnabled(False)
        self.btnStop.setEnabled(False)

        self.btnPlay.clicked.connect(self.play_video)
        self.btnPause.clicked.connect(self.mediaPlayer.pause)
        self.btnStop.clicked.connect(self.mediaPlayer.stop)

        self.btnExportar.clicked.connect(lambda status, n_size=300: self.run(n_size))

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def run(self, n):
        if self.comboBox.currentIndex() != 0:

            self.mediaPlayer.stop()
            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
            self.btnExportar.setEnabled(False)
            self.comboBox.setEnabled(False)

            self.VideoPlayer2 = QVideoWidget(Export)
            self.VideoPlayer2.setMinimumSize(QtCore.QSize(720, 440))
            self.VideoPlayer2.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.VideoPlayer2.setStyleSheet("background-color: rgb(224, 230, 237);")
            self.VideoPlayer2.setObjectName("VideoPlayer")
            self.layoutPrincipal.addWidget(self.VideoPlayer2)

            self.progressBar.raise_()

            for i in range(n):
                time.sleep(0.01)
                self.progressBar.setValue(i+1)
        else:
            print("Seleccione la calidad de vídeo deseada.")


    def cancel(self):
        self.progressBar.setValue(0)

    def cancelHandler(self):
        self.cancel()

    def pushButton_handler(self):
        self.openVideo()

    def exportarHandler(self):
        self.exportar()

    def exportar(self):
        print('completar')

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
        self.lblLocation.setText("  " + path)
        video = TinyTag.get(path)
        self.actualPath = path
        self.lblTipe.setText("Tipo de vídeo:         " + path[len(path)-4:])
        self.lblLenght.setText("Duración del vídeo:  " + time.strftime('%H:%M:%S', time.gmtime(video.duration)))

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Export = QtWidgets.QWidget()
    ui = Ui_Export()
    ui.setupUi(Export)
    Export.show()
    sys.exit(app.exec_())
