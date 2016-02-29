#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16
from geometry_msgs.msg import Twist

steering = 90
velocity = Twist()

def move_emaxx():
    steering_pub = rospy.Publisher('/servo', UInt16, queue_size=10)
    rospy.init_node('move_emaxx_teleop', anonymous=True)
    rospy.Subscriber('/turtle1/command_velocity', Twist, callback)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        steering = 90 + (velocity.angular.z * 10) 
        steering_pub.publish(steering)
        rate.sleep()

def callback(data):
    velocity = data

if __name__ == '__main__':
    move_emaxx()
