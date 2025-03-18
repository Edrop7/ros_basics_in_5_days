#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse

global service
global pub
global velocity

def callback(request):
    rate = rospy.Rate(10)
    rospy.loginfo("The Service move_bb8_in_square_custom has been called")
    num_of_squares_completed = 0
    sides_completed = 0
    iterations = request.side * 400000
    counter = 0
    while num_of_squares_completed < request.repetitions:
        while sides_completed < 4:
            while counter < iterations:
                velocity.linear.x = 0.2
                pub.publish(velocity)
                counter += 1
            velocity.linear.x = 0.0
            pub.publish(velocity)
            counter = 0
            rate.sleep()
            for i in range(100):
                velocity.angular.z = 0.15707963267
                pub.publish(velocity)
                rate.sleep()
            velocity.angular.z = 0
            pub.publish(velocity)
            sides_completed += 1
        num_of_squares_completed += 1
    velocity.linear.x = 0.0
    velocity.angular.z = 0.0
    pub.publish(velocity)

    rospy.loginfo("Finished service move_bb8_in_square_custom")
    
    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('service_move_bb8_in_square_custom_server') 
service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
velocity = Twist()
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rospy.spin()