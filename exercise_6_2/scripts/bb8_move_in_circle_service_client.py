#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node('service_move_bb8_in_circle_client')
rospy.wait_for_service('/move_bb8_in_circle')
move_bb8_in_circle_service_client = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
move_bb8_in_circle_request_object = EmptyRequest()

result = move_bb8_in_circle_service_client(move_bb8_in_circle_request_object)
print(result)