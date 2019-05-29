#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from gazebo_msgs.msg import ContactsState
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Vector3
from sensor_msgs.msg import JointState

from gazebo_connection import GazeboConnection

class BipedRobot(object):
    def __init__(self):
        self.gazebo = GazeboConnection

        #publisher
        self.publishers = []
        self._L_haa_joint_pub = rospy.Publisher(
            '/biped/L_haa_joint_position_controller/command', Float64, queue_size=1)
        self._L_hfe_joint_pub = rospy.Publisher(
            '/biped/L_hfe_joint_position_controller/command', Float64, queue_size=1)
        self._L_kfe_joint_pub = rospy.Publisher(
            '/biped/L_kfe_joint_position_controller/command', Float64, queue_size=1)
        self._R_haa_joint_pub = rospy.Publisher(
            '/biped/R_haa_joint_position_controller/command', Float64, queue_size=1)
        self._R_hfe_joint_pub = rospy.Publisher(
            '/biped/R_hfe_joint_position_controller/command', Float64, queue_size=1)
        self._R_kfe_joint_pub = rospy.Publisher(
            '/biped/R_kfe_joint_position_controller/command', Float64, queue_size=1)

        self.publishers.append(self._L_haa_joint_pub)
        self.publishers.append(self._L_hfe_joint_pub)
        self.publishers.append(self._L_kfe_joint_pub)
        self.publishers.append(self._R_haa_joint_pub)
        self.publishers.append(self._R_hfe_joint_pub)
        self.publishers.append(self._R_kfe_joint_pub)

        #subscriber
        self.base_position = Point()
        self.base_orientation = Quaternion()
        self.base_angular_velocity = Vector3()
        self.base_linear_acceleration = Vector3()
        self.L_contact_force = Vector3()
        self.R_contact_force = Vector3()
        self.joints_state = JointState()

        rospy.Subscriber("/odom", Odometry, self.odom_callback)
        rospy.Subscriber("/biped/imu/data", Imu, self.imu_callback)
        rospy.Subscriber("/lowerleg_contactsensor_state", ContactsState, self.L_contact_callback)
        rospy.Subscriber("/biped/joint_states", JointState, self.joints_state_callback)

    def odom_callback(self,msg):
        self.base_position = msg.pose.pose.position

    def imu_callback(self,msg):
        self.base_orientation = msg.orientation
        self.base_angular_velocity = msg.angular_velocity
        self.base_linear_acceleration = msg.linear_acceleration

    def contact_callback(self,msg):
        for state in msg.states:
            self.contact_force = state.total_wrench.force

    def joints_state_callback(self,msg):
        self.joints_state = msg

    def move_joints(self, joints_array):

        i = 0
        for publisher_object in self.publishers:
            joint_value = Float64()
            joint_value.data = joints_array[i]
            rospy.loginfo(str(joint_value))
            publisher_object.publish(joint_value)
            i += 1

    def start_loop(self, rate_value=2.0):
        rospy.loginfo("Start Loop")
        pos1 = [-0.8, 1.57, -1.57, 0.8, 1.57, -1.57]
        pos2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        position = "pos1"
        rate = rospy.Rate(rate_value)
        while not rospy.is_shutdown():
            if position == "pos1":
                self.move_joints(pos1)
                position = "pos2"
            else:
                self.move_joints(pos2)
                position = "pos1"
            rate.sleep()


if __name__ == "__main__":
    rospy.init_node('joint_publisher_node')
    my_robot = BipedRobot()
    rate_value = 1

    my_robot.start_loop(rate_value)
