# Install script for directory: /home/toby/biped_robot/ros/src/xpp/robots/xpp_quadrotor

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/toby/biped_robot/ros/build/xpp/robots/xpp_quadrotor/catkin_generated/installspace/xpp_quadrotor.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xpp_quadrotor/cmake" TYPE FILE FILES
    "/home/toby/biped_robot/ros/build/xpp/robots/xpp_quadrotor/catkin_generated/installspace/xpp_quadrotorConfig.cmake"
    "/home/toby/biped_robot/ros/build/xpp/robots/xpp_quadrotor/catkin_generated/installspace/xpp_quadrotorConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xpp_quadrotor" TYPE FILE FILES "/home/toby/biped_robot/ros/src/xpp/robots/xpp_quadrotor/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/xpp_quadrotor/urdf_visualizer_quadrotor" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/xpp_quadrotor/urdf_visualizer_quadrotor")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/xpp_quadrotor/urdf_visualizer_quadrotor"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/xpp_quadrotor" TYPE EXECUTABLE FILES "/home/toby/biped_robot/ros/devel/lib/xpp_quadrotor/urdf_visualizer_quadrotor")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/xpp_quadrotor/urdf_visualizer_quadrotor" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/xpp_quadrotor/urdf_visualizer_quadrotor")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/xpp_quadrotor/urdf_visualizer_quadrotor"
         OLD_RPATH "/home/toby/biped_robot/ros/devel/lib:/opt/ros/kinetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/xpp_quadrotor/urdf_visualizer_quadrotor")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/xpp_quadrotor" TYPE DIRECTORY FILES
    "/home/toby/biped_robot/ros/src/xpp/robots/xpp_quadrotor/launch"
    "/home/toby/biped_robot/ros/src/xpp/robots/xpp_quadrotor/meshes"
    "/home/toby/biped_robot/ros/src/xpp/robots/xpp_quadrotor/urdf"
    )
endif()

