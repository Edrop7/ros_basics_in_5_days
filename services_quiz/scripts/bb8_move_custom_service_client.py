#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('service_move_bb8_custom_client')
rospy.wait_for_service('/move_bb8_in_square_custom')
move_bb8_custom_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)

small_square_request = BB8CustomServiceMessageRequest()
small_square_request.side = 1.1
small_square_request.repetitions = 2

large_square_request = BB8CustomServiceMessageRequest()
large_square_request.side = 2.2
large_square_request.repetitions = 1

result = move_bb8_custom_service_client(small_square_request)
print(result)
result = move_bb8_custom_service_client(large_square_request)
print(result)