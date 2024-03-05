cmake_minimum_required(VERSION 3.10.0)
project(drone_auto_bag_record)

### Get packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  mavros_msgs
)

### Get packages headers
include_directories(
  ${catkin_INCLUDE_DIRS}
)

### Set catkin package
catkin_package()