#!/bin/env bash


gnome-terminal --title="gazeebo" -e "bash -c \"cd ~/my_ws ; source devel/setup.bash ; export TURTLEBOT3_MODEL=burger ; sed -e 's/\(<real_time_update_rate>\).*\(<\/real_time_update_rate>\)/<real_time_update_rate>1000000<\/real_time_update_rate>/g' src/MRS_236609/worlds/closed_room.world ;  roslaunch MRS_236609 multi_turtlebot3.launch ; $SHELL\""
gnome-terminal --title="Rviz" -e "bash -c \"cd ~/my_ws ; source devel/setup.bash ; export TURTLEBOT3_MODEL=burger ; sleep 10 ; roslaunch MRS_236609 multi_turtlebot3_navigation.launch
map_file:=$HOME/my_ws/src/MRS_236609/maps/closed_room.yaml ; $SHELL\""


gnome-terminal --title="python" -e "bash -c \"cd ~/my_ws ; source devel/setup.bash ; export TURTLEBOT3_MODEL=burger ; sleep 10 ; echo roslaunch MRS_236609 $1 $2  ; $SHELL\""



