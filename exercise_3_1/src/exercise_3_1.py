#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('robot_velocity')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
velocity = Twist()
velocity.linear.x = 0.5
velocity.angular.z = 0.5

while not rospy.is_shutdown(): 
  pub.publish(velocity)
  rate.sleep()