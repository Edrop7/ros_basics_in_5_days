#! /usr/bin/env python

# this is a Server

import rospy
import actionlib
from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgResult, CustomActionMsgFeedback
from std_msgs.msg import Empty

class DroneActionServer:

    # create messages that are used to publish feedback/result
    _feedback = CustomActionMsgFeedback()
    _result   = CustomActionMsgResult()

    def __init__(self):
        self._as = actionlib.SimpleActionServer("action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
        self._as.start()
        self.takeoff_pub = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self.land_pub = rospy.Publisher('/drone/land', Empty, queue_size=1)
        self.takeoff_msg = Empty()
        self.land_msg = Empty()
        self.rate = rospy.Rate(1)
        self.ctrl_c = False

    def goal_callback(self, goal):
        # helper variable
        success = False

        rospy.loginfo(f"Received {goal.goal} process from user as intended action for drone")

        if goal.goal == "TAKEOFF":
            rospy.loginfo(f"Initiating {goal.goal} process of drone")
            self.takeoff()
            success = True
        elif goal.goal == "LAND":
            rospy.loginfo(f"Initiating {goal.goal} process of drone")
            self.land()
            success = True
        else:
            rospy.loginfo(f"User submitted {goal.goal} process is not valid")

        if success:
            self._feedback.feedback = (f"Accomplished {goal.goal} process!")
            rospy.loginfo(f"Succeeded at {goal.goal} process of drone")
            self._as.set_succeeded(self._feedback)

    def takeoff(self):
        rospy.loginfo('Taking off...')

        while not self.ctrl_c:
            connections = self.takeoff_pub.get_num_connections()
            if connections > 0:
                self.takeoff_pub.publish(self.takeoff_msg)
                rospy.loginfo("Takeoff Published")
                break
            else:
                self.rate.sleep()

    def land(self):
        rospy.loginfo('Landing...')

        while not self.ctrl_c:
            connections = self.land_pub.get_num_connections()
            if connections > 0:
                self.land_pub.publish(self.land_msg)
                rospy.loginfo("Land Published")
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        self.ctrl_c = True

if __name__ == '__main__':
  rospy.init_node('my_script')
  DroneActionServer()
  rospy.spin()