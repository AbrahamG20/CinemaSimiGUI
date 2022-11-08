from PyQt5 import QtCore, QtGui, QtWidgets
from instr import Ui_Instrucciones
import icons_rc
import sys

class Ui_CinemaSimi(object):

    def openInstrucciones(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Instrucciones()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, CinemaSimi):
        CinemaSimi.setObjectName("CinemaSimi")
        CinemaSimi.resize(1080, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CinemaSimi.setWindowIcon(icon)
        CinemaSimi.setStyleSheet("background-color: rgb(255, 234, 212);")
        self.verticalLayout = QtWidgets.QVBoxLayout(CinemaSimi)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lytCabezera = QtWidgets.QHBoxLayout()
        self.lytCabezera.setObjectName("lytCabezera")
        self.btnQuestion = QtWidgets.QToolButton(CinemaSimi, clicked=lambda: self.openInstrucciones())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnQuestion.sizePolicy().hasHeightForWidth())
        self.btnQuestion.setSizePolicy(sizePolicy)
        self.btnQuestion.setMaximumSize(QtCore.QSize(110, 90))
        self.btnQuestion.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/recursos/question_red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnQuestion.setIcon(icon1)
        self.btnQuestion.setIconSize(QtCore.QSize(70, 70))
        self.btnQuestion.setAutoRaise(True)
        self.btnQuestion.setObjectName("btnQuestion")
        self.lytCabezera.addWidget(self.btnQuestion)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lytCabezera.addItem(spacerItem)
        self.lblUPC = QtWidgets.QLabel(CinemaSimi)
        self.lblUPC.setMaximumSize(QtCore.QSize(90, 90))
        self.lblUPC.setText("")
        self.lblUPC.setPixmap(QtGui.QPixmap(":/icons/recursos/upc_logo.png"))
        self.lblUPC.setScaledContents(True)
        self.lblUPC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblUPC.setObjectName("lblUPC")
        self.lytCabezera.addWidget(self.lblUPC)
        self.verticalLayout.addLayout(self.lytCabezera)
        self.lytLogo = QtWidgets.QHBoxLayout()
        self.lytLogo.setObjectName("lytLogo")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lytLogo.addItem(spacerItem1)
        self.lblLogo = QtWidgets.QLabel(CinemaSimi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLogo.sizePolicy().hasHeightForWidth())
        self.lblLogo.setSizePolicy(sizePolicy)
        self.lblLogo.setMaximumSize(QtCore.QSize(580, 200))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/icons/recursos/cinemaSimi.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setObjectName("lblLogo")
        self.lytLogo.addWidget(self.lblLogo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lytLogo.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.lytLogo)
        self.lytPrincipal = QtWidgets.QGridLayout()
        self.lytPrincipal.setObjectName("lytPrincipal")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.lytPrincipal.addItem(spacerItem3, 2, 0, 1, 1)
        self.btnAdd = QtWidgets.QToolButton(CinemaSimi)
        self.btnAdd.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/recursos/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon2)
        self.btnAdd.setIconSize(QtCore.QSize(260, 260))
        self.btnAdd.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnAdd.setAutoRaise(True)
        self.btnAdd.setArrowType(QtCore.Qt.NoArrow)
        self.btnAdd.setObjectName("btnAdd")

        self.lytPrincipal.addWidget(self.btnAdd, 0, 0, 1, 1)
        self.lblNew = QtWidgets.QLabel(CinemaSimi)
        self.lblNew.setObjectName("lblNew")
        self.lytPrincipal.addWidget(self.lblNew, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.lytPrincipal)

        self.retranslateUi(CinemaSimi)
        QtCore.QMetaObject.connectSlotsByName(CinemaSimi)


    def retranslateUi(self, CinemaSimi):
        _translate = QtCore.QCoreApplication.translate
        CinemaSimi.setWindowTitle(_translate("CinemaSimi", "CinemaSimi - Inicio"))
        self.lblNew.setText(_translate("CinemaSimi", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Crear nuevo proyecto</span></p></body></html>"))

"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    CinemaSimi = QtWidgets.QWidget()
    ui = Ui_CinemaSimi()
    ui.setupUi(CinemaSimi)
    CinemaSimi.show()
    sys.exit(app.exec_())
"""