# cyberdog_remote

## Dependencies
```sh
pip install pyserial
sudo apt remove brltty
```

## Permissions
```sh
# enable all connected USB devices
sudo chmod a+rw /dev/ttyUSB*
```

## Installation

```sh
# cd to your ROS 2 Workspace
cd colcon_ws/src
git clone https://github.com/AIR-HCI-Demonstration-2023/cyberdog_remote.git
cd ..
colcon build
source install setup.bash
```

## How to Use

```sh
# Terminal 1, Launch the Service
cd colcon_ws
source install/setup.bash
ros2 run cyberdog_remote service 

# Terminal 2, Call the Service
cd colcon_ws
source install/setup.bash
ros2 run cyberdog_remote client 0 # Open the Gripper
ros2 run cyberdog_remote client 1 # Close the Gripper
```