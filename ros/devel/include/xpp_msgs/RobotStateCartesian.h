// Generated by gencpp from file xpp_msgs/RobotStateCartesian.msg
// DO NOT EDIT!


#ifndef XPP_MSGS_MESSAGE_ROBOTSTATECARTESIAN_H
#define XPP_MSGS_MESSAGE_ROBOTSTATECARTESIAN_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <xpp_msgs/State6d.h>
#include <xpp_msgs/StateLin3d.h>
#include <geometry_msgs/Vector3.h>

namespace xpp_msgs
{
template <class ContainerAllocator>
struct RobotStateCartesian_
{
  typedef RobotStateCartesian_<ContainerAllocator> Type;

  RobotStateCartesian_()
    : time_from_start()
    , base()
    , ee_motion()
    , ee_forces()
    , ee_contact()  {
    }
  RobotStateCartesian_(const ContainerAllocator& _alloc)
    : time_from_start()
    , base(_alloc)
    , ee_motion(_alloc)
    , ee_forces(_alloc)
    , ee_contact(_alloc)  {
  (void)_alloc;
    }



   typedef ros::Duration _time_from_start_type;
  _time_from_start_type time_from_start;

   typedef  ::xpp_msgs::State6d_<ContainerAllocator>  _base_type;
  _base_type base;

   typedef std::vector< ::xpp_msgs::StateLin3d_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::xpp_msgs::StateLin3d_<ContainerAllocator> >::other >  _ee_motion_type;
  _ee_motion_type ee_motion;

   typedef std::vector< ::geometry_msgs::Vector3_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::Vector3_<ContainerAllocator> >::other >  _ee_forces_type;
  _ee_forces_type ee_forces;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _ee_contact_type;
  _ee_contact_type ee_contact;





  typedef boost::shared_ptr< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> const> ConstPtr;

}; // struct RobotStateCartesian_

typedef ::xpp_msgs::RobotStateCartesian_<std::allocator<void> > RobotStateCartesian;

typedef boost::shared_ptr< ::xpp_msgs::RobotStateCartesian > RobotStateCartesianPtr;
typedef boost::shared_ptr< ::xpp_msgs::RobotStateCartesian const> RobotStateCartesianConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace xpp_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'xpp_msgs': ['/home/toby/biped_robot/ros/src/xpp/xpp_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> >
{
  static const char* value()
  {
    return "25955243f6c682a57bfe4fb411b854bb";
  }

  static const char* value(const ::xpp_msgs::RobotStateCartesian_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x25955243f6c682a5ULL;
  static const uint64_t static_value2 = 0x7bfe4fb411b854bbULL;
};

template<class ContainerAllocator>
struct DataType< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xpp_msgs/RobotStateCartesian";
  }

  static const char* value(const ::xpp_msgs::RobotStateCartesian_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# The state of a robot expressed in the Cartesian frame\n\
\n\
duration                time_from_start   # global time along trajectory\n\
\n\
# Position, velocity and acceleration of the base expressed in world frame\n\
# The orientation quaternion maps base to world frame.\n\
State6d                 base              # base pos/vel/acc in world\n\
\n\
StateLin3d[]            ee_motion         # endeffector pos/vel/acc in world\n\
geometry_msgs/Vector3[] ee_forces         # endeffector forces expressed in world\n\
bool[]                  ee_contact        # True if the foot is touching the environment\n\
\n\
\n\
\n\
\n\
================================================================================\n\
MSG: xpp_msgs/State6d\n\
# The state of the 6D base of a system\n\
\n\
geometry_msgs/Pose     pose         # The 6D linear and angular position, orientation maps base to world\n\
geometry_msgs/Twist    twist        # The 6D linear and angular velocity \n\
geometry_msgs/Accel    accel        # The 6D linear and angular acceleration\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of position and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Twist\n\
# This expresses velocity in free space broken into its linear and angular parts.\n\
Vector3  linear\n\
Vector3  angular\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
================================================================================\n\
MSG: geometry_msgs/Accel\n\
# This expresses acceleration in free space broken into its linear and angular parts.\n\
Vector3  linear\n\
Vector3  angular\n\
\n\
================================================================================\n\
MSG: xpp_msgs/StateLin3d\n\
# This contains the 3D representation of a linear state, including:\n\
# position, velocity, acceleration\n\
\n\
geometry_msgs/Point pos\n\
geometry_msgs/Vector3 vel\n\
geometry_msgs/Vector3 acc\n\
";
  }

  static const char* value(const ::xpp_msgs::RobotStateCartesian_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.time_from_start);
      stream.next(m.base);
      stream.next(m.ee_motion);
      stream.next(m.ee_forces);
      stream.next(m.ee_contact);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RobotStateCartesian_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xpp_msgs::RobotStateCartesian_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xpp_msgs::RobotStateCartesian_<ContainerAllocator>& v)
  {
    s << indent << "time_from_start: ";
    Printer<ros::Duration>::stream(s, indent + "  ", v.time_from_start);
    s << indent << "base: ";
    s << std::endl;
    Printer< ::xpp_msgs::State6d_<ContainerAllocator> >::stream(s, indent + "  ", v.base);
    s << indent << "ee_motion[]" << std::endl;
    for (size_t i = 0; i < v.ee_motion.size(); ++i)
    {
      s << indent << "  ee_motion[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::xpp_msgs::StateLin3d_<ContainerAllocator> >::stream(s, indent + "    ", v.ee_motion[i]);
    }
    s << indent << "ee_forces[]" << std::endl;
    for (size_t i = 0; i < v.ee_forces.size(); ++i)
    {
      s << indent << "  ee_forces[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "    ", v.ee_forces[i]);
    }
    s << indent << "ee_contact[]" << std::endl;
    for (size_t i = 0; i < v.ee_contact.size(); ++i)
    {
      s << indent << "  ee_contact[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.ee_contact[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // XPP_MSGS_MESSAGE_ROBOTSTATECARTESIAN_H