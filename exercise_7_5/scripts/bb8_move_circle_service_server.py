#! /usr/bin/env python

import rospy
from exercise_7_5.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from bb8_move_circle_class import MoveBB8


def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    movebb8_object = MoveBB8()
    movebb8_object.move_bb8()

    i = 0
    while i < request.duration:
        rate.sleep()
        i += 1
    movebb8_object.stop_bb8()

    rospy.loginfo("Finished service move_bb8_in_circle")
    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('service_move_bb8_in_circle_server') 
my_service = rospy.Service('/move_bb8_in_circle', BB8CustomServiceMessage, my_callback)
rospy.loginfo("Service /move_bb8_in_circle Ready")
rate = rospy.Rate(1) #1 hz
rospy.spin() # keep the service open.