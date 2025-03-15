#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from exercise_6_3.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse

def callback(request):
    rospy.loginfo("The Service move_bb8_in_circle_custom has been called")
    velocity.linear.x = 0.2
    velocity.angular.z = 0.2
    i = 0
    while request.duration <= 0:
        pub.publish(velocity)
        rate.sleep()
        i += 1

    velocity.linear.x = 0.0
    velocity.angular.z = 0.0
    pub.publish(velocity)
    rospy.loginfo("Finished service move_bb8_in_circle_custom")
    
    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('service_move_bb8_in_circle_custom_server') 
service = rospy.Service('/move_bb8_in_circle_custom', BB8CustomServiceMessage, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
velocity = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rospy.spin()