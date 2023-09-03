# cyberdog_hci
HCI铁蛋2代的配置流程
## 1. 铁蛋开启多播模式
```sh
# 在铁蛋的Jetson NX板上执行这些命令
cd /etc/mi
sudo nano cyclonedds.xml
# 将文件里的内容照着下面这个例子修改：
# <?xml version="1.0" encoding="UTF-8" ?>
# <CycloneDDS xmlns="https://cdds.io/config" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"    xsi:schemaLocation="https://cdds.io/config https://raw.githubusercontent.com/eclipse-cyc$
#     <Domain id="42">
#         <General>
#             <NetworkInterfaceAddress>wlan0</NetworkInterfaceAddress>
#             <AllowMulticast>true</AllowMulticast>
#         </General>
#         <Discovery>
#             <ParticipantIndex>auto</ParticipantIndex>
#             <MaxAutoParticipantIndex>100</MaxAutoParticipantIndex>
#             <Peers>
#                 <Peer address="localhost"/>
#             </Peers>
#         </Discovery>
#     </Domain>
# </CycloneDDS>

# 重启铁蛋，让配置生效
sudo reboot
```

## 2. PC端ROS2远程连接配置
在PC端配置ROS_DOMAIN_ID，这样就能在同一局域网内收到铁蛋的ROS 2消息了
```sh
# 在你自己的电脑上执行这些命令
sudo gedit ~/.bashrc
# 在~/.bashrc这个文件里加两行：
export ROS_DOMAIN_ID=42
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
# 然后保存退出，执行该命令让配置生效：
source ~/.bashrc
# 然后安装依赖（我用的是ROS 2 Humble版本，根据你自己的ROS 2版本修改）
sudo apt install ros-humble-rmw-cyclonedds-cpp
```

## 3. PC端部署这个功能包
```sh
cd ~
mkdir -p hci_ws/src
cd hci_ws/src
git clone https://github.com/0nhc/cyberdog_hci.git
cd ..
colcon build
source install/setup.bash
```

## 4. 运行这个功能包
```sh
source ~/hci_ws/install/setup.bash
ros2 run cyberdog_remote client # 默认运行这个是站立
```