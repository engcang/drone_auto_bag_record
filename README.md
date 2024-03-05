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
    rosbag record -o output /mavros/vision_pose/pose /Odometry /cloud_registered __name:=recorder
    ```
2. Run as a separate node
    ```bash
    rosrun drone_auto_bag_record python_terminal_control.py
    ```
3. Or, include this as a node within `.launch` file of your wanted program
    ```xml
    <?xml version="1.0"?>
    <launch>

        ...

        <node pkg="drone_auto_bag_record" type="python_terminal_control.py" name="any_node_name_you_want" output="screen"/>

        ...

    </launch>
    ```
4. If the drone is armed, ROS bag is recorded, and recording will be stopped when the drone is disarmed.
5. Directory
    + If you ran this as a separate node, you can find the bag file in the directory where you ran the command `rosrun`.
    + You can find the `output_DATE_TIME.bag` file in `~/.ros` directory, if you include this repository as a node within `.launch` file