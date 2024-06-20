import pyfirmata2
import time
import rospy
from std_msgs.msg import Float32, Bool

def callback(data):
    rospy.loginfo("Recibido: %f", data.data)

def listener_activate():
    rospy.init_node('aspirator_node', anonymous=True)
    rospy.Subscriber('/aspirator/activate', Bool, callback)
    rospy.spin()

def callback(data):
    pindigi = data.data;    
    #Escribe el valor en el pin digital 13
    board.digital[4].write(pindigi)
    time.sleep(1)

print("Arduino conectado por USB.")
board = pyfirmata2.Arduino('COM3')
if __name__ == '__main__':
    listener_activate()
