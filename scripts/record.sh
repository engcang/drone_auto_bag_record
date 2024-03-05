#!/bin/bash
rosbag record -o output /mavros/imu/data_raw /mavros/local_position/pose /mavros/vision_pose/pose /Odometry /cloud_registered __name:=recorder
