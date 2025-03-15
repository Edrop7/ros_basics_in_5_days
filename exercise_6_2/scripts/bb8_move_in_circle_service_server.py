#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty, EmptyResponse

def callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    velocity.linear.x = 0.2
    velocity.angular.z = 0.2
    pub.publish(velocity)
    rospy.loginfo("Finished service move_bb8_in_circle")
    return EmptyResponse()

rospy.init_node('service_move_bb8_in_circle_server') 
service = rospy.Service('/move_bb8_in_circle', Empty , callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
velocity = Twist()
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin()