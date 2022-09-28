from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Instrucciones(object):
    def setupUi(self, Instrucciones):
        Instrucciones.setObjectName("Instrucciones")
        Instrucciones.resize(800, 600)
        Instrucciones.setMinimumSize(QtCore.QSize(800, 600))
        Instrucciones.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Instrucciones.setWindowIcon(icon)
        Instrucciones.setStyleSheet("background-color: rgb(255, 234, 212);")
        Instrucciones.setAnimated(False)
        Instrucciones.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Instrucciones)
        self.centralwidget.setStyleSheet("/* VERTICAL SCROLLBAR*/\n"
"\n"
"QScrollBar:vertical{\n"
"    bolder: none;\n"
"    background-color: rgb(229, 233, 242);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* HANDLEBAR VERTICAL*/\n"
"\n"
"QScrollBar::handle::vertical{\n"
"    \n"
"    background-color: rgb(132, 146, 166);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle::vertical:hover{\n"
"    background-color: rgb(73, 136, 175);\n"
"}\n"
"\n"
"QScrollBar::handle::vertical:pressed{\n"
"    background-color: rgb(58, 113, 154);\n"
"}\n"
"\n"
"/*BIN TOP - SCROLLBAR*/\n"
"QScrollBar::sub-line:vertical{\n"
"    border: none;\n"
"    background-color: rgb(229, 233, 242);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover{\n"
"    background-color: rgb(73, 136, 175);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover:pressed{\n"
"    background-color: rgb(58, 113, 154);\n"
"}\n"
"\n"
"/*BIN BOTTOM - SCROLLBAR*/\n"
"QScrollBar::add-line:vertical{\n"
"    border: none;\n"
"    background-color: rgb(229, 233, 242);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"    background-color: rgb(73, 136, 175);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover:pressed{\n"
"    background-color: rgb(58, 113, 154);\n"
"}\n"
"\n"
"/*RESET ARROW*/\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"    background: none;\n"
"}\n"
"\n"
"/*CLOSE BUTTON */\n"
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
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLogo.sizePolicy().hasHeightForWidth())
        self.lblLogo.setSizePolicy(sizePolicy)
        self.lblLogo.setMinimumSize(QtCore.QSize(0, 0))
        self.lblLogo.setMaximumSize(QtCore.QSize(220, 80))
        self.lblLogo.setSizeIncrement(QtCore.QSize(0, 0))
        self.lblLogo.setBaseSize(QtCore.QSize(0, 0))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/icons/recursos/cinemaSimi.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblLogo.setObjectName("lblLogo")
        self.verticalLayout.addWidget(self.lblLogo)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 764, 1822))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameInstruccioens = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frameInstruccioens.setMinimumSize(QtCore.QSize(0, 1800))
        self.frameInstruccioens.setStyleSheet("background-color: rgb(255, 254, 248);")
        self.frameInstruccioens.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInstruccioens.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInstruccioens.setObjectName("frameInstruccioens")
        self.label = QtWidgets.QLabel(self.frameInstruccioens)
        self.label.setGeometry(QtCore.QRect(10, 30, 721, 361))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.frameInstruccioens)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.clicked.connect(Instrucciones.close)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setMinimumSize(QtCore.QSize(100, 40))
        self.btnClose.setStyleSheet("")
        self.btnClose.setCheckable(False)
        self.btnClose.setAutoDefault(False)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Instrucciones.setCentralWidget(self.centralwidget)

        self.retranslateUi(Instrucciones)
        QtCore.QMetaObject.connectSlotsByName(Instrucciones)

    def retranslateUi(self, Instrucciones):
        _translate = QtCore.QCoreApplication.translate
        Instrucciones.setWindowTitle(_translate("Instrucciones", "Instrucciones"))
        self.label.setText(_translate("Instrucciones", "<html><head/><body><p><span style=\" font-size:12pt;\">Bienvenido a </span><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">CinemaSimi</span></p><p><span style=\" font-size:12pt;\">En esta aplicación podrás traducir tu vídeo favorito del español al quechua. A continuación te daremos instrucciones para que puedas traducir tu video de manera satisfactoria.</span></p></body></html>"))
        self.btnClose.setText(_translate("Instrucciones", "Cerrar"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Instrucciones = QtWidgets.QMainWindow()
    ui = Ui_Instrucciones()
    ui.setupUi(Instrucciones)
    Instrucciones.show()
    sys.exit(app.exec_())
