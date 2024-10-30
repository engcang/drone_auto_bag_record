<h1 align="center"><span>Drone Auto Bag Recorder</span></h1>

+ This repository is for recording ROS bag file subscribing the arming state of a drone with `mavros`, which is based on `PX4`

<br>

## Dependencies
+ `ROS` (currently supporting only `ROS1`)
+ `Python3`


<br>

## How to install
+ Install
```bash
cd ~/<your_workspace>/src
git clone https://github.com/engcang/drone_auto_bag_record

cd ~/<your_workspace>
catkin build

. devel/setup.bash
```

<br>

## How to use
1. Setup the topics you want to record within `record.sh` file
    ```sh
    #!/bin/bash
    if [ -z "$1" ]; then
    echo "Usage: ./record.sh <output_directory>"
    exit 1
    fi

    OUTPUT_DIR=$1
    rosbag record -o "${OUTPUT_DIR}/output" /mavros/imu/data_raw /mavros/local_position/pose /mavros/vision_pose/pose /Odometry /cloud_registered __name:=recorder
    ```
2. Run as a separate node
    ```bash
    rosrun drone_auto_bag_record python_terminal_control.py /Absolute/directory/you/want/to/save/bag/file
    ```
3. Or, include this as a node within `.launch` file of your wanted program
    ```xml
    <?xml version="1.0"?>
    <launch>

        ...

        <node pkg="drone_auto_bag_record" type="python_terminal_control.py" name="any_node_name_you_want" args="/Absolute/directory/you/want/to/save/" output="screen"/>

        ...

    </launch>
    ```
4. If the drone is armed, ROS bag is recorded, and recording will be stopped when the drone is disarmed.
5. The bag file will be store in the directory