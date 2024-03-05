#!/usr/bin/env python3

import rospy
import time
import subprocess
import os, sys, signal
from mavros_msgs.msg import State

import sys
import signal

def signal_handler(signal, frame): # ctrl + c -> exit program
    print('You pressed Ctrl+C!')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def terminate_process_and_children(p):
    ps_command = subprocess.Popen("ps -o pid --ppid %d --noheaders" % p.pid, shell=True, stdout=subprocess.PIPE)
    ps_output = ps_command.stdout.read()
    retcode = ps_command.wait()
    assert retcode == 0, "ps command returned %d" % retcode
    for pid_str in ps_output.decode().split("\n")[:-1]:
        os.kill(int(pid_str), signal.SIGINT)
    p.terminate()

''' class '''
class robot():
    def __init__(self):
        rospy.init_node('record_python_node', anonymous=True)
        self.state_sub = rospy.Subscriber('/mavros/state', State, self.signal_cb)
        self.switch_flag = False
        self.rate = rospy.Rate(1)

    def signal_cb(self, msg):
        if not self.switch_flag and msg.armed:
            self.switch_flag = True
            self.process1 = subprocess.Popen(['rosrun', 'drone_auto_bag_record', 'record.sh'])
            print("Record start!")
        elif self.switch_flag and not msg.armed:
            terminate_process_and_children(self.process1)
            self.switch_flag = False
            print("Record stop!")


if __name__ == '__main__':
    record_ = robot()
    time.sleep(0.5)
    while 1:
        try:
            record_.rate.sleep()
        except (rospy.ROSInterruptException, SystemExit, KeyboardInterrupt) :
            sys.exit(0)
    sys.exit(0)
