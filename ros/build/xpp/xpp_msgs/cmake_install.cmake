# Install script for directory: /home/toby/biped_robot/ros/src/xpp/xpp_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/toby/biped_robot/ros/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xpp_msgs/msg" TYPE FILE FILES
    "/home/toby/biped_robot/ros/src/xpp/xpp_msgs/msg/StateLin3d.msg"
    "/home/toby/biped_robot/ros/src/xpp/xpp_msgs/msg/State6d.msg"
    "/home/toby/biped_robot/ros/src/xpp/xpp_msgs/msg/RobotStateCartesianTrajectory.msg"
    "/home/toby/biped_robot/ros/src/xpp/xpp_msgs/msg/RobotStateCartesian.msg"
    "/home/toby/biped_robot/ros/src/xpp/xpp_msgs/msg/RobotStateJoint.msg"
    "/home/toby/biped_robot/ros/src/xpp/xpp_msgs/msg/RobotParameters.msg"
    "/home/toby/biped_robot/ros/src/xpp/xpp_msgs/msg/TerrainInfo.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xpp_msgs/cmake" TYPE FILE FILES "/home/toby/biped_robot/ros/build/xpp/xpp_msgs/catkin_generated/installspace/xpp_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/toby/biped_robot/ros/devel/include/xpp_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/toby/biped_robot/ros/devel/share/roseus/ros/xpp_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/toby/biped_robot/ros/devel/share/common-lisp/ros/xpp_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/toby/biped_robot/ros/devel/share/gennodejs/ros/xpp_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/toby/biped_robot/ros/devel/lib/python2.7/dist-packages/xpp_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/toby/biped_robot/ros/devel/lib/python2.7/dist-packages/xpp_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/toby/biped_robot/ros/build/xpp/xpp_msgs/catkin_generated/installspace/xpp_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xpp_msgs/cmake" TYPE FILE FILES "/home/toby/biped_robot/ros/build/xpp/xpp_msgs/catkin_generated/installspace/xpp_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xpp_msgs/cmake" TYPE FILE FILES
    "/home/toby/biped_robot/ros/build/xpp/xpp_msgs/catkin_generated/installspace/xpp_msgsConfig.cmake"
    "/home/toby/biped_robot/ros/build/xpp/xpp_msgs/catkin_generated/installspace/xpp_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xpp_msgs" TYPE FILE FILES "/home/toby/biped_robot/ros/src/xpp/xpp_msgs/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/xpp_msgs" TYPE DIRECTORY FILES "/home/toby/biped_robot/ros/src/xpp/xpp_msgs/include/xpp_msgs/" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()

