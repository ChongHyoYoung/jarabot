from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='nav2_bt_navigator',
            name='bt_navigator',
            executable='bt_navigator',
            output="screen"
        )
    ])


# <launch>
#   <node pkg="move_base" type="move_base" respawn="false" name="move_base" output="screen">
#     <param name="base_local_planner" value="dwa_local_planner/DWAPlannerROS" />
#     <rosparam file="$(find dronebot23)/config/move_base/costmap_common_params.yaml" command="load" ns="global_costmap" />
#     <rosparam file="$(find dronebot23)/config/move_base/costmap_common_params.yaml" command="load" ns="local_costmap" />
#     <rosparam file="$(find dronebot23)/config/move_base/local_costmap_params.yaml" command="load" />
#     <rosparam file="$(find dronebot23)/config/move_base/global_costmap_params.yaml" command="load" />
#     <rosparam file="$(find dronebot23)/config/move_base/move_base_params.yaml" command="load" />
#     <rosparam file="$(find dronebot23)/config/move_base/dwa_local_planner_params.yaml" command="load" />
#     <remap from="cmd_vel" to="/movebase/cmd_vel" />
#   </node>
# </launch>
