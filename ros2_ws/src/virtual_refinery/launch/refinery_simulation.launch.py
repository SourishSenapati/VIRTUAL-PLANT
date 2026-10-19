"""
ROS 2 REFINERY DIGITAL TWIN LAUNCH FILE
Author: Sourish Senapati (Department of Chemical Engineering, Jadavpur University)
Launches the full suite of nodes: CDU/VDU simulator, Conversion units, Stream router, SIS safety, and Orchestrator.
"""

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='virtual_refinery',
            executable='cdu_vdu_simulator',
            name='cdu_vdu_simulator_node',
            output='screen',
        ),
        Node(
            package='virtual_refinery',
            executable='conversion_units',
            name='conversion_units_node',
            output='screen',
        ),
        Node(
            package='virtual_refinery',
            executable='stream_router',
            name='stream_router_node',
            output='screen',
        ),
        Node(
            package='virtual_refinery',
            executable='process_safety_sis',
            name='process_safety_sis_node',
            output='screen',
        ),
        Node(
            package='virtual_refinery',
            executable='gazebo_bridge',
            name='gazebo_bridge_node',
            output='screen',
        ),
        Node(
            package='virtual_refinery',
            executable='refinery_orchestrator',
            name='refinery_orchestrator_node',
            output='screen',
        ),
    ])
