#!/usr/bin/env python
import rospy
import math

from std_msgs.msg import Float64
from gazebo_msgs.msg import ContactsState
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Vector3
from sensor_msgs.msg import JointState

from gazebo_connection import GazeboConnection
from biped_inverse_kinematics import BipedKinematics


class BipedRobot(object):
    def __init__(self):
        self.gazebo = GazeboConnection

        # publisher
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

        # subscriber
        self.base_position = Point()
        self.base_orientation = Quaternion()
        self.base_angular_velocity = Vector3()
        self.base_linear_acceleration = Vector3()
        self.L_contact_force = Vector3()
        self.R_contact_force = Vector3()
        self.joints_state = JointState()

        rospy.Subscriber("/odom", Odometry, self.odom_callback)
        rospy.Subscriber("/biped/imu/data", Imu, self.imu_callback)
        rospy.Subscriber("/L_lowerleg_contactsensor_state",
                         ContactsState, self.L_contact_callback)
        rospy.Subscriber("/R_lowerleg_contactsensor_state",
                         ContactsState, self.R_contact_callback)
        rospy.Subscriber("/biped/joint_states", JointState,
                         self.joints_state_callback)

        self.initial_pos()

    def initial_pos(self):
        pos = [-0.8, 1.57, -1.57, 0.8, 1.57, -1.57]
        pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.move_joints(pos)

    def odom_callback(self, msg):
        self.base_position = msg.pose.pose.position

    def imu_callback(self, msg):
        self.base_orientation = msg.orientation
        self.base_angular_velocity = msg.angular_velocity
        self.base_linear_acceleration = msg.linear_acceleration

    def L_contact_callback(self, msg):
        for state in msg.states:
            self.L_contact_force = state.total_wrench.force

    def R_contact_callback(self, msg):
        for state in msg.states:
            self.R_contact_force = state.total_wrench.force

    def joints_state_callback(self, msg):
        self.joints_state = msg

    def move_joints(self, joints_array):

        for i, publisher_object in enumerate(self.publishers):
            joint_value = Float64()
            joint_value.data = joints_array[i]
            rospy.loginfo(str(joint_value))
            publisher_object.publish(joint_value)

    def start_loop(self, rate_value=0.5):
        rospy.loginfo("Start Loop")
        pos1 = [-0.0, 0.8, -0.0, 0.0, 0.8, -0.0]
        pos2 = [0.0, -0.8, 0.0, 0.0, -0.8, 0.0]
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

    # def move_leg(self, x_pos, y_pos, z_pos):

def clip(value, max_value = 0.5):
    if(value>max_value):
        return max_value
    elif(value<-1*max_value):
        return -1*max_value
    else:
        return value

if __name__ == "__main__":
    rospy.init_node('joint_publisher_node')
    my_robot = BipedRobot()
    rate_value = 50
    rate = rospy.Rate(rate_value)
    # my_robot.start_loop()

    target_angle = 0
    kp = 10
    kd = 1
    angle_diff = 0
    pre_angle_diff = 0
    leg_angle = 0
    while not rospy.is_shutdown():
        
        # pos = [0.0, -0.5, 0.0, 0.0, -0.5, 0.0]

        # my_robot.move_joints(pos)

        body_angle = my_robot.base_position.x/(my_robot.base_position.z+10e-8)
        body_angle = math.atan(body_angle)
        # angle = math.degrees(angle)
        angle_diff = body_angle-target_angle
        
        # if(my_robot.L_contact_force.z < 0 or my_robot.R_contact_force.z < 0):
        #     leg_angle = -1 * (kp*angle_diff - kd*(angle_diff-pre_angle_diff))
        #     leg_angle = clip(leg_angle, 0.8)
        #     pos = [0.0, leg_angle, 0.0, 0.0, leg_angle, 0.0]
        #     my_robot.move_joints(pos)
        # else:
        #     my_robot.initial_pos()
        leg_angle = 1 * (kp*angle_diff - kd*(angle_diff-pre_angle_diff))
        leg_angle = clip(leg_angle, 1.0)
        pos = [0.0, leg_angle, 0.0, 0.0, leg_angle, 0.0]
        my_robot.move_joints(pos)
        
        pre_angle_diff = angle_diff
        print(angle_diff)
        print(leg_angle)
        
        rate.sleep()
    # my_robot.start_loop(rate_value)
