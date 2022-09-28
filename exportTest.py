from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
import icons_rc
import time

class Ui_NewProject(object):
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

        self.progressBar = QtWidgets.QProgressBar(self.VideoPlayer)
        self.progressBar.setGeometry(QtCore.QRect(390, 190, 300, 10))

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

        n = 300

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(n)

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
        icon4.addPixmap(QtGui.QPixmap(":/icons/recursos/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.lblLenght = QtWidgets.QLabel(NewProject)
        self.lblLenght.setObjectName("lblLenght")
        self.gridLayout.addWidget(self.lblLenght, 1, 0, 1, 1)
        self.lblLocation = QtWidgets.QLabel(NewProject)
        self.lblLocation.setMinimumSize(QtCore.QSize(350, 0))
        self.lblLocation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lblLocation.setObjectName("lblLocation")
        self.gridLayout.addWidget(self.lblLocation, 0, 0, 1, 1)
        self.lblTipe = QtWidgets.QLabel(NewProject)
        self.lblTipe.setObjectName("lblTipe")
        self.gridLayout.addWidget(self.lblTipe, 2, 0, 1, 1)
        self.lblSize = QtWidgets.QLabel(NewProject)
        self.lblSize.setObjectName("lblSize")
        self.gridLayout.addWidget(self.lblSize, 1, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(NewProject)
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
        self.btnExportar = QtWidgets.QPushButton(NewProject)
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

        self.retranslateUi(NewProject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

    def retranslateUi(self, NewProject):
        n = 300

        _translate = QtCore.QCoreApplication.translate

        NewProject.setWindowTitle(_translate("NewProject", "CinemaSimi - Nuevo Proyecto"))
        self.lblEstimated.setText(_translate("NewProject", "Tiempo estimado:"))
        self.btnCancel.setText(_translate("NewProject", "Cancelar Exportación"))
        self.lblLenght.setText(_translate("NewProject", "Duración del vídeo:  00:01:20"))
        self.lblLocation.setText(_translate("NewProject", "C:/User/Videos/"))
        self.lblTipe.setText(_translate("NewProject", "Tipo de vídeo:         .mp4"))
        self.lblSize.setText(_translate("NewProject", "Tamaño del video: "))

        self.comboBox.setItemText(0, _translate("NewProject", "Seleccione la calidad de video"))
        self.comboBox.setItemText(1, _translate("NewProject", "360p"))
        self.comboBox.setItemText(2, _translate("NewProject", "480p"))
        self.comboBox.setItemText(3, _translate("NewProject", "720p"))
        self.comboBox.setItemText(4, _translate("NewProject", "1080p"))

        self.btnExportar.setText(_translate("NewProject", "Exportar"))

        self.btnExportar.clicked.connect(lambda status, n_size=n: self.run(n_size))
        self.btnCancel.clicked.connect(self.cancelHandler)


    def run(self, n):
        for i in range(n):
            time.sleep(0.01)
            self.progressBar.setValue(i+1)

    def cancel(self):
        self.progressBar.setValue(0)

    def cancelHandler(self):
        self.cancel()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewProject = QtWidgets.QWidget()
    ui = Ui_NewProject()
    ui.setupUi(NewProject)
    NewProject.show()
    sys.exit(app.exec_())
