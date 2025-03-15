#! /usr/bin/env python

import rospy
from exercise_6_3.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('service_move_bb8_custom_client')
rospy.wait_for_service('/move_bb8_in_circle_custom')
move_bb8_custom_service_client = rospy.ServiceProxy('/move_bb8_in_circle_custom', BB8CustomServiceMessage)
move_bb8_custom_request_object = BB8CustomServiceMessageRequest()


result = move_bb8_custom_service_client(move_bb8_custom_request_object)
print(result)