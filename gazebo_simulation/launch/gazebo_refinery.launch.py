"""
ROS 2 & GAZEBO CO-SIMULATION LAUNCH SCRIPT: VIRTUAL REFINERY COMPLEX
Author: Sourish Senapati (Jadavpur University, Chemical Engineering)
Launches Gazebo with physics-accurate refinery world and starts the ROS 2 Digital Twin bridge.
"""

import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    pkg_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    world_path = os.path.join(pkg_dir, 'worlds', 'refinery_complex.world')

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=world_path,
            description='Path to the Gazebo refinery world file'
        ),
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', LaunchConfiguration('world')],
            output='screen'
        )
    ])
