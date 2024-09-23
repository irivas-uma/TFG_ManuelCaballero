#!/usr/bin/env python3

import rospy
import pyfirmata2
import time

from std_msgs.msg import Float32, Bool

def listener_activate():
    rospy.init_node('Aspirador', anonymous=True)
    rospy.Subscriber('/control_aspirado', Bool, callback)
    rospy.on_shutdown(shutdown_hook)
    rospy.spin()

def callback(data):
    pindigi = data.data;    
    #Escribe el valor en el pin digital 4
    board.digital[4].write(pindigi)
    rospy.loginfo("Recibido: %s", data.data)
    time.sleep(1)

def shutdown_hook():
    """
    Esta función se llama cuando el nodo se está apagando.
    Desactiva el pin digital del Arduino.
    """
    rospy.loginfo("Cerrando nodo, desactivando pin digital 4...")
    board.digital[4].write(0)  # Apaga el pin digital 4 (aspirador apagado)
    time.sleep(1)  # Espera para asegurarse de que la señal sea enviada correctamente


print("Arduino conectado por USB.")
#board = pyfirmata2.Arduino('COM3'): Esto es para el sistema operativo Windows
board = pyfirmata2.Arduino('/dev/ttyACM0')
if __name__ == '__main__':
    listener_activate()
