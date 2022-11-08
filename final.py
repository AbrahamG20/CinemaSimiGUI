from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc

class Ui_Final(object):
    def setupUi(self, Final):
        Final.setObjectName("Final")
        Final.resize(1080, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Final.setWindowIcon(icon)
        Final.setStyleSheet("background-color: rgb(255, 234, 212);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Final)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lytCabezera = QtWidgets.QHBoxLayout()
        self.lytCabezera.setObjectName("lytCabezera")
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lytCabezera.addItem(spacerItem)
        self.lblUPC = QtWidgets.QLabel(Final)
        self.lblUPC.setMaximumSize(QtCore.QSize(90, 90))
        self.lblUPC.setText("")
        self.lblUPC.setPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"))
        self.lblUPC.setScaledContents(True)
        self.lblUPC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblUPC.setObjectName("lblUPC")
        self.lytCabezera.addWidget(self.lblUPC)
        self.verticalLayout.addLayout(self.lytCabezera)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.lytLogo = QtWidgets.QHBoxLayout()
        self.lytLogo.setObjectName("lytLogo")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lytLogo.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Final)
        self.label.setMinimumSize(QtCore.QSize(0, 350))
        self.label.setBaseSize(QtCore.QSize(0, 500))
        self.label.setStyleSheet("/*BUTTON */\n"
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
"}")
        self.label.setObjectName("label")
        self.lytLogo.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lytLogo.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.lytLogo)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.lytBotones = QtWidgets.QHBoxLayout()
        self.lytBotones.setObjectName("lytBotones")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lytBotones.addItem(spacerItem5)
        self.btnInicio = QtWidgets.QPushButton(Final)
        self.btnInicio.setMinimumSize(QtCore.QSize(200, 45))
        self.btnInicio.setStyleSheet("/*BUTTON */\n"
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
"}")
        self.btnInicio.setObjectName("btnInicio")
        self.lytBotones.addWidget(self.btnInicio)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lytBotones.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.lytBotones)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)

        self.retranslateUi(Final)
        QtCore.QMetaObject.connectSlotsByName(Final)

    def retranslateUi(self, Final):
        _translate = QtCore.QCoreApplication.translate
        Final.setWindowTitle(_translate("Final", "CinemaSimi "))
        self.label.setText(_translate("Final", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">!Su vídeo ha sido subtitulado </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">y exportado con éxito!</span></p></body></html>"))
        self.btnInicio.setText(_translate("Final", "Ir al Inicio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Final = QtWidgets.QWidget()
    ui = Ui_Final()
    ui.setupUi(Final)
    Final.show()
    sys.exit(app.exec_())
