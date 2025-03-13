#! /usr/bin/env python

import rospy
from my_subscriber_example_pkg.msg import Age

rospy.init_node('age_publisher')
pub = rospy.Publisher('/age', Age, queue_size=1)
rate = rospy.Rate(2)
age = Age()
age.years = 23
age.months = 5
age.days = 27

while not rospy.is_shutdown(): 
  pub.publish(age)
  rate.sleep()