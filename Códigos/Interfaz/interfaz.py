#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool

from PyQt5 import QtCore, QtGui, QtWidgets
from comprobaciones import Ui_comprobaciones

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Inicializar la clase base QMainWindow
        super(Ui_MainWindow, self).__init__()
        
        # Iniciar el nodo de ROS
        rospy.init_node('Interfaz', anonymous=True)
        self.pub = rospy.Publisher('/control_aspirado', Bool, queue_size=10)
        self.is_active = False
        
        # Configurar la UI
        self.setupUi(self)

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_comprobaciones()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 479)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Botón para ROS
        self.pushbutton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton1.setEnabled(True)
        self.pushbutton1.setGeometry(QtCore.QRect(339, 200, 122, 122))
        self.pushbutton1.setMinimumSize(QtCore.QSize(0, 0))
        self.pushbutton1.setMaximumSize(QtCore.QSize(300, 300))
        self.pushbutton1.setAutoFillBackground(False)
        self.pushbutton1.setStyleSheet("")
        self.pushbutton1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbutton1.setIcon(icon)
        self.pushbutton1.setIconSize(QtCore.QSize(100, 100))
        self.pushbutton1.setObjectName("pushbutton1")

        # Se conecta el botón a la función designada para controlar el aspirado
        self.pushbutton1.clicked.connect(self.toggle_aspirator)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 350, 231, 111))
        self.label_4.setObjectName("label_4")

        # Botón para comprobaciones
        self.pushbutton2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow())
        self.pushbutton2.setGeometry(QtCore.QRect(20, 430, 151, 25))
        self.pushbutton2.setAutoDefault(False)
        self.pushbutton2.setDefault(False)
        self.pushbutton2.setFlat(False)
        self.pushbutton2.setObjectName("pushbutton2")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 741, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("image: url(:/interfaz/logouma.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("image: url(:/interfaz/logoeii.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interfaz Aspirador"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Autor: Manuel Caballero Roldán</span></p><p><span style=\" font-size:9pt;\">Tutoras:</span></p><p><span style=\" font-size:9pt;\">- Irene Rivas Blanco</span></p><p><span style=\" font-size:9pt;\">- Eva María Góngora Rodríguez</span></p></body></html>"))
        self.pushbutton2.setText(_translate("MainWindow", "Comprobaciones"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">AUTOMATIZACIÓN DE UN ASPIRADOR QUIRÚRGICO </span></p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">INTEGRADO EN UN SISTEMA ROBÓTICO</span></p><p align=\"center\"><br/></p></body></html>"))

    def toggle_aspirator(self):
        """
        Cambia el estado del aspirador entre activo/inactivo y publica el valor correspondiente.
        """
        if not self.is_active:
            # Publica True (se enciende el aspirador)
            self.pub.publish(True)
            rospy.loginfo("Aspirador activado")
        else:
            # Publica False (se desactiva el aspirador)
            self.pub.publish(False)
            rospy.loginfo("Aspirador desactivado")
        # Cambiar el estado del aspirador
        self.is_active = not self.is_active

    def closeEvent(self, event):
        if self.is_active:
            rospy.loginfo("Cerrando ventana, desactivando aspirador...")
            self.pub.publish(False)  # Envía False al cerrar para apagar el aspirador
            rospy.sleep(1)  # Espera para asegurar que el mensaje se publique
        event.accept()  # Acepta el evento de cierre y cierra la ventana

import imagenes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()  # Cambiado a Ui_MainWindow
    MainWindow.show()
    sys.exit(app.exec_())