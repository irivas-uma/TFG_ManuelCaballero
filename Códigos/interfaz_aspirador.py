#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
import tkinter as tk

class BoolPublisherGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz aspirador")

        self.pub = rospy.Publisher('/aspirator/activate', Bool, queue_size=10)
        rospy.init_node('bool_publisher_gui', anonymous=True)

        self.true_button = tk.Button(master, text="Activate aspirator", command=self.publish_true)
        self.true_button.pack()

        self.false_button = tk.Button(master, text="Deactivate aspirator", command=self.publish_false)
        self.false_button.pack()

    def publish_true(self):
        self.pub.publish(True)
        rospy.loginfo("Publicado: True")

    def publish_false(self):
        self.pub.publish(False)
        rospy.loginfo("Publicado: False")

if __name__ == '__main__':
    root = tk.Tk()
    gui = BoolPublisherGUI(root)
    root.mainloop()