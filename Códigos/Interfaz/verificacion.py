# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verificacion.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_verificacion(object):
    def setupUi(self, verificacion):
        verificacion.setObjectName("verificacion")
        verificacion.resize(577, 293)
        self.centralwidget = QtWidgets.QWidget(verificacion)
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
        verificacion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(verificacion)
        self.statusbar.setObjectName("statusbar")
        verificacion.setStatusBar(self.statusbar)

        self.retranslateUi(verificacion)
        QtCore.QMetaObject.connectSlotsByName(verificacion)

    def retranslateUi(self, verificacion):
        _translate = QtCore.QCoreApplication.translate
        verificacion.setWindowTitle(_translate("verificacion", "Verificación de puesta en marcha"))
        self.checkBox_2.setText(_translate("verificacion", "Conexionado electroválvula."))
        self.checkBox_5.setText(_translate("verificacion", "Conexionado Relay Shield."))
        self.checkBox_6.setText(_translate("verificacion", "Conexionado de los tubos del aspirador"))
        self.checkBox_4.setText(_translate("verificacion", "Arduino conectado."))
        self.checkBox_3.setText(_translate("verificacion", "Fuente de tensión a +/-24V."))
        self.checkBox.setText(_translate("verificacion", "Aspirador encendido."))
        self.checkBox_7.setText(_translate("verificacion", "Código cargado."))
        self.checkBox_8.setText(_translate("verificacion", "Comprobación del vacío en el aspirador tras operación."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verificacion = QtWidgets.QMainWindow()
    ui = Ui_verificacion()
    ui.setupUi(verificacion)
    verificacion.show()
    sys.exit(app.exec_())
