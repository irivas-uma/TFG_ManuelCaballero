# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comprobaciones.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_comprobaciones(object):
    def setupUi(self, comprobaciones):
        comprobaciones.setObjectName("comprobaciones")
        comprobaciones.resize(577, 293)
        self.centralwidget = QtWidgets.QWidget(comprobaciones)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout.addWidget(self.checkBox_8)
        comprobaciones.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(comprobaciones)
        self.statusbar.setObjectName("statusbar")
        comprobaciones.setStatusBar(self.statusbar)

        self.retranslateUi(comprobaciones)
        QtCore.QMetaObject.connectSlotsByName(comprobaciones)

    def retranslateUi(self, comprobaciones):
        _translate = QtCore.QCoreApplication.translate
        comprobaciones.setWindowTitle(_translate("comprobaciones", "MainWindow"))
        self.checkBox_2.setText(_translate("comprobaciones", "Conexionado electroválvula."))
        self.checkBox_5.setText(_translate("comprobaciones", "Conexionado Relay Shield."))
        self.checkBox_6.setText(_translate("comprobaciones", "Conexionado de los tubos del aspirador"))
        self.checkBox_4.setText(_translate("comprobaciones", "Arduino conectado."))
        self.checkBox_3.setText(_translate("comprobaciones", "Fuente de tensión a +/-24V."))
        self.checkBox.setText(_translate("comprobaciones", "Aspirador encendido."))
        self.checkBox_7.setText(_translate("comprobaciones", "Código cargado."))
        self.checkBox_8.setText(_translate("comprobaciones", "Comprobación del vacío en el aspirador tras operación."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    comprobaciones = QtWidgets.QMainWindow()
    ui = Ui_comprobaciones()
    ui.setupUi(comprobaciones)
    comprobaciones.show()
    sys.exit(app.exec_())
