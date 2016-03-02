# EE487
Code examples for the Embedded Systems Course

### Traxxas Emaxx vehicle
1. Configure your Arduino according to these [instructions] (http://wiki.ros.org/rosserial_arduino/Tutorials/Servo%20Controller).
2. Create a new package or clone the [EE487 repo] (https://github.com/westpoint-robotics/EE487.git).
  - `$ cd ~/catkin_ws/src`
  - `$ git clone https://github.com/westpoint-robotics/EE487.git`
  - `$ cd..`
  - `$ catkin_make`
3. Follow this [tutorial] (http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics) on ROS Nodes to launch turtlesim and teleop. In new terminal windows:
  - `$ roscore`
  - `$ rosrun turtlesim turtlesim_node`
  - `$ rosrun turtlesim turtle_teleop_key`
4. You should have a turtlesim controllable using the arrow keys.  
5. Check to make sure that the cmd_vel topic is being published.
  - `$ rostopic echo /turtle1/cmd_vel` 
6. The emaxx_driver subscribes to the velocity topic and then publishes a scaled servo message to the Arduino.
7. Launch the rosserial node to allow your Arduino to connect to the ROS environment.  Your tty port may be different (i.e. ttyACM0).  Check using:
  - `ls /dev/tty*`
  - `$ rosrun rosserial_python serial_node.py /dev/ttyUSB0`
8. The emaxx_driver is based on this publisher/subscriber [tutorial] (http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
  - `$ rosrun emaxx_driver move_emaxx_teleop.py`
