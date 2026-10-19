"""
GAZEBO & ROS 2 CO-SIMULATION BRIDGE
Author: Sourish Senapati (Department of Chemical Engineering, Jadavpur University)

Synchronizes chemical process telemetry to 3D visual and physical entities in Gazebo:
  - Flare stack flame length & emissive radiation intensity
  - Fired heater chimney exhaust particle markers
  - Tank farm liquid level indicators
  - Catalyst slide valve stroke positions
"""

import sys
import os

try:
    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String, Float64
    from geometry_msgs.msg import Pose, Point, Quaternion
    HAVE_ROS2 = True
except ImportError:
    HAVE_ROS2 = False
    class Node:
        def __init__(self, name):
            self.name = name

class GazeboRefineryBridge(Node):
    """Bridges ROS 2 topics to Gazebo simulation models."""
    def __init__(self):
        super().__init__('gazebo_refinery_bridge_node')
        if HAVE_ROS2:
            self.pub_flare_scale = self.create_publisher(Float64, '/gazebo/flare_stack/flame_scale', 10)
            self.pub_cdu_level = self.create_publisher(Float64, '/gazebo/cdu_tower/liquid_level', 10)
            self.sub_telemetry = self.create_subscription(String, '/refinery/cdu_vdu/telemetry', self.telemetry_cb, 10)
            self.get_logger().info("Gazebo-ROS 2 Co-Simulation Bridge initialized.")

    def telemetry_cb(self, msg):
        pass

    def compute_visual_states(self, flare_load_kg_h, cdu_level_pct, fcc_cat_circ_t_min):
        """Computes 3D visual properties for Gazebo world rendering."""
        # Flare flame vertical scale factor (1.0 = base pilot, 5.0 = full relief emergency)
        flame_scale = max(1.0, min(6.0, flare_load_kg_h / 45000.0))
        flame_lumens = 1000.0 + flame_scale * 15000.0
        
        # Tank level height in meters (max 18.0 m)
        tank_height_m = (cdu_level_pct / 100.0) * 18.0
        
        # Slide valve displacement (0.0 to 0.85 m stroke)
        valve_stroke_m = (fcc_cat_circ_t_min / 35.0) * 0.85
        
        return {
            'flare_flame_scale_z': flame_scale,
            'flare_light_lumens': flame_lumens,
            'cdu_sump_liquid_height_m': tank_height_m,
            'fcc_slide_valve_stroke_m': valve_stroke_m,
        }

def main(args=None):
    bridge = GazeboRefineryBridge()
    print("=" * 80)
    print("VIRTUAL REFINERY: ROS 2 <-> GAZEBO CO-SIMULATION BRIDGE")
    print("=" * 80)
    normal_vis = bridge.compute_visual_states(12500.0, 52.0, 28.5)
    print("--- NORMAL CO-SIMULATION STATES ---")
    for k, v in normal_vis.items():
        print(f"  {k:<30} : {v:.3f}")
        
    emergency_vis = bridge.compute_visual_states(265000.0, 15.0, 34.0)
    print("\n--- EMERGENCY DEPRESSURING CO-SIMULATION STATES ---")
    for k, v in emergency_vis.items():
        print(f"  {k:<30} : {v:.3f}")
    print("=" * 80)

if __name__ == '__main__':
    main()
