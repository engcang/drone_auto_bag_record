#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: ./record.sh <output_directory>"
  exit 1
fi

OUTPUT_DIR=$1
rosbag record -o "${OUTPUT_DIR}/output" /mavros/imu/data_raw /mavros/local_position/pose /mavros/vision_pose/pose /Odometry /cloud_registered __name:=recorder
