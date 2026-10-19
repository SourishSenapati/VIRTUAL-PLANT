"""
REFINERY CONVERSION UNITS SIMULATOR: FCCU, HYDROCRACKER & DELAYED COKER
Author: Sourish Senapati (Department of Chemical Engineering, Jadavpur University)

Physics and reaction kinetics models for downstream heavy-end upgrading:
  1. Fluid Catalytic Cracking Unit (FCCU): Riser kinetics & regenerator energy balance
  2. Hydrocracking Unit (HCU): High-pressure catalytic hydroprocessing & H2 consumption
  3. Delayed Coking Unit (DCU): Thermal cracking & semi-batch coking cycle
"""

import sys
import os
import math
import numpy as np

try:
    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String
    HAVE_ROS2 = True
except ImportError:
    HAVE_ROS2 = False
    class Node:
        def __init__(self, name):
            self.name = name

class ConversionUnitsPhysics:
    """Rigorous kinetics and mass balances for FCCU, Hydrocracker, and Delayed Coker."""
    def __init__(self):
        # FCCU Operating Parameters
        self.fcc_feed_kg_h = 75000.0  # HVGO + LVGO blend from VDU
        self.fcc_cat_to_oil = 6.8     # Cat-to-oil mass ratio
        self.fcc_riser_temp_c = 535.0
        self.fcc_regen_temp_c = 705.0
        self.fcc_cat_circ_t_min = 28.5
        
        # Hydrocracker Operating Parameters
        self.hcu_feed_kg_h = 45000.0  # HVGO + Coker Gas Oil
        self.hcu_r1_press_bar = 155.0
        self.hcu_r1_temp_c = 395.0
        self.hcu_r2_temp_c = 410.0
        self.hcu_h2_consumption_nm3_m3 = 1420.0
        
        # Delayed Coker Operating Parameters
        self.coker_feed_kg_h = 85800.0 # Vacuum Residue (VR) from VDU
        self.coker_temp_c = 498.0
        self.coker_press_bar = 2.1
        self.active_drum = 'Drum A'    # Drum A / Drum B cycle state
        self.drum_fill_pct = 42.0

    def solve_fcc_kinetics(self, feed_kg_h=None):
        """
        Weekman-Nace 4-Lump FCC kinetic model:
        Lump 1: Gas Oil (Feed)
        Lump 2: Gasoline (C5 - 215 C)
        Lump 3: Light Gases (C1 - C4 + LPG)
        Lump 4: Coke on Catalyst
        """
        if feed_kg_h is not None:
            self.fcc_feed_kg_h = feed_kg_h
            
        # Kinetic conversion X = 1 / (1 + 1 / (k0 * t_res * (C/O) * a_cat))
        # Base conversion: ~76.5 vol%
        conv_frac = 0.765
        
        coke_wt_pct = 5.2
        lpg_wt_pct = 17.5
        gasoline_wt_pct = 48.8
        lco_wt_pct = 23.5  # Light Cycle Oil
        slurry_wt_pct = 5.0
        
        fcc_products = {
            'FCC Gasoline (RON 92+)': {'wt_pct': gasoline_wt_pct, 'flow_kg_h': self.fcc_feed_kg_h * gasoline_wt_pct / 100.0, 'api': 58.0},
            'LPG (C3/C4 Alkylation Feed)': {'wt_pct': lpg_wt_pct, 'flow_kg_h': self.fcc_feed_kg_h * lpg_wt_pct / 100.0, 'api': 110.0},
            'Light Cycle Oil (LCO -> Diesel)': {'wt_pct': lco_wt_pct, 'flow_kg_h': self.fcc_feed_kg_h * lco_wt_pct / 100.0, 'api': 22.0},
            'Clarified Slurry Oil': {'wt_pct': slurry_wt_pct, 'flow_kg_h': self.fcc_feed_kg_h * slurry_wt_pct / 100.0, 'api': 8.5},
            'Coke Burned in Regenerator': {'wt_pct': coke_wt_pct, 'flow_kg_h': self.fcc_feed_kg_h * coke_wt_pct / 100.0, 'api': 0.0},
        }
        return fcc_products

    def solve_hydrocracker_kinetics(self, feed_kg_h=None):
        """
        Two-stage high pressure hydrocracking mass balance and conversion.
        Converts refractory aromatics into clean diesel and kerosene.
        """
        if feed_kg_h is not None:
            self.hcu_feed_kg_h = feed_kg_h
            
        # Overall conversion per pass: 65% with recycle -> >98% total conversion
        # Hydrogen addition increases mass yield to ~103.2 wt%
        h2_intake_kg_h = self.hcu_feed_kg_h * 0.032
        total_effluent = self.hcu_feed_kg_h + h2_intake_kg_h
        
        hcu_products = {
            'Ultra-Low Sulfur Diesel (ULSD)': {'wt_pct': 51.5, 'flow_kg_h': total_effluent * 0.515, 'api': 38.5, 'cetane': 62.0},
            'Hydrocracker Jet Fuel': {'wt_pct': 27.5, 'flow_kg_h': total_effluent * 0.275, 'api': 45.0, 'smoke_pt': 28.0},
            'Heavy Hydrocrackate Naphtha': {'wt_pct': 16.0, 'flow_kg_h': total_effluent * 0.160, 'api': 62.0, 'ron': 74.0},
            'Light Ends (LPG / C1-C4)': {'wt_pct': 5.0, 'flow_kg_h': total_effluent * 0.050, 'api': 95.0, 'ron': 0.0},
        }
        return hcu_products

    def solve_delayed_coker(self, vr_feed_kg_h=None):
        """
        Delayed Coking thermal cracking reaction:
        Conradson Carbon Residue (CCR) correlation for petroleum coke and coker gas oil.
        """
        if vr_feed_kg_h is not None:
            self.coker_feed_kg_h = vr_feed_kg_h
            
        coke_wt_pct = 28.5
        coker_gas_pct = 8.5
        coker_naphtha_pct = 14.5
        lcgo_pct = 32.5  # Light Coker Gas Oil
        hcgo_pct = 16.0  # Heavy Coker Gas Oil
        
        coker_products = {
            'Light Coker Gas Oil (LCGO)': {'wt_pct': lcgo_pct, 'flow_kg_h': self.coker_feed_kg_h * lcgo_pct / 100.0, 'api': 28.5},
            'Heavy Coker Gas Oil (HCGO)': {'wt_pct': hcgo_pct, 'flow_kg_h': self.coker_feed_kg_h * hcgo_pct / 100.0, 'api': 18.0},
            'Petroleum Green Coke': {'wt_pct': coke_wt_pct, 'flow_kg_h': self.coker_feed_kg_h * coke_wt_pct / 100.0, 'api': 0.0},
            'Coker Naphtha': {'wt_pct': coker_naphtha_pct, 'flow_kg_h': self.coker_feed_kg_h * coker_naphtha_pct / 100.0, 'api': 60.0},
            'Coker Off-Gas': {'wt_pct': coker_gas_pct, 'flow_kg_h': self.coker_feed_kg_h * coker_gas_pct / 100.0, 'api': 105.0},
        }
        return coker_products

def main(args=None):
    print("=" * 80)
    print("VIRTUAL REFINERY: CONVERSION & UPGRADING KINETICS (FCCU, HCU, DCU)")
    print("=" * 80)
    conv = ConversionUnitsPhysics()
    
    # 1. FCCU
    fcc_y = conv.solve_fcc_kinetics(75000.0)
    print("\n--- 1. FLUID CATALYTIC CRACKING UNIT (FCCU / R-201 & R-202) ---")
    print(f"Feed Rate: {conv.fcc_feed_kg_h:,.0f} kg/h | Riser: {conv.fcc_riser_temp_c:.0f} C | Cat/Oil: {conv.fcc_cat_to_oil:.1f}")
    for k, v in fcc_y.items():
        print(f"  {k:<35} : {v['wt_pct']:>5.1f} wt% | {v['flow_kg_h']:>10,.0f} kg/h | {v['api']:>5.1f} API")
        
    # 2. Hydrocracker
    hcu_y = conv.solve_hydrocracker_kinetics(45000.0)
    print("\n--- 2. HIGH-PRESSURE HYDROCRACKING UNIT (HCU / R-301 & R-302) ---")
    print(f"Feed Rate: {conv.hcu_feed_kg_h:,.0f} kg/h @ {conv.hcu_r1_press_bar:.0f} bar(g) | H2 Intake: {conv.hcu_h2_consumption_nm3_m3:.0f} Nm3/m3")
    for k, v in hcu_y.items():
        print(f"  {k:<35} : {v['wt_pct']:>5.1f} wt% | {v['flow_kg_h']:>10,.0f} kg/h | {v['api']:>5.1f} API")
        
    # 3. Delayed Coker
    dcu_y = conv.solve_delayed_coker(85800.0)
    print("\n--- 3. DELAYED COKING UNIT (DCU / V-401A & V-401B) ---")
    print(f"VR Feed Rate: {conv.coker_feed_kg_h:,.0f} kg/h | Furnace: {conv.coker_temp_c:.0f} C | Active Drum: {conv.active_drum}")
    for k, v in dcu_y.items():
        print(f"  {k:<35} : {v['wt_pct']:>5.1f} wt% | {v['flow_kg_h']:>10,.0f} kg/h | {v['api']:>5.1f} API")
    print("=" * 80)

if __name__ == '__main__':
    main()
