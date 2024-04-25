#/usr/bin/env python3
import rospy

from random import randint
from message_gen_check.msg import Custom

publisher = None

def cb(event):
    global publisher
    msg = Custom()
    msg.header.stamp = rospy.Time.now()
    msg.text = str(randint(0,10))
    msg.flag = True

    publisher.publish(msg)


def main():
    global publisher
    rospy.init_node('message_custom_publisher')
    publisher = rospy.Publisher('custom_message', Custom, queue_size=10)
    rospy.Timer(rospy.Duration(secs=1), cb)
    rospy.spin()

if __name__ == '__main__':
    main()