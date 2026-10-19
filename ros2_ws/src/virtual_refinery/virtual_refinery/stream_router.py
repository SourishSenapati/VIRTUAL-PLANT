"""
REFINERY-WIDE STREAM ROUTER & PRODUCT BLENDING SOLVER
Author: Sourish Senapati (Department of Chemical Engineering, Jadavpur University)

Solves interconnected material balance across separation and downstream conversion units:
  - Atmospheric Residue to VDU
  - HVGO routing between FCCU and Hydrocracker
  - Vacuum Residue to Delayed Coker
  - Blending algorithms for Gasoline (RON), Diesel (Cetane & Sulfur), Jet Fuel, and Fuel Oil
"""

import sys
import os

from cdu_vdu_simulator import CDUVDUPhysicsModel
from conversion_units import ConversionUnitsPhysics

class RefineryStreamNetwork:
    """Refinery-wide flowsheet routing, intermediate inventory, and finished product pools."""
    def __init__(self, crude_rate_bpd=100000.0):
        self.cdu_vdu = CDUVDUPhysicsModel(crude_rate_bpd)
        self.conv = ConversionUnitsPhysics()

    def solve_refinery_balance(self):
        # 1. Primary Fractionation (CDU & VDU)
        cdu_yields = self.cdu_vdu.calculate_cdu_yields()
        atm_residue = cdu_yields['Atmospheric Residue']['flow_kg_h']
        vdu_yields = self.cdu_vdu.calculate_vdu_yields(atm_residue)
        
        # 2. Feedstock Routing to Downstream Conversion
        hvgo_flow = vdu_yields['Heavy Vacuum Gas Oil (HVGO)']['flow_kg_h']
        vr_flow = vdu_yields['Vacuum Residue (VR)']['flow_kg_h']
        
        # Split HVGO: 60% to FCCU, 40% to Hydrocracker
        fcc_feed = hvgo_flow * 0.60 + vdu_yields['Light Vacuum Gas Oil (LVGO)']['flow_kg_h'] * 0.35
        hcu_feed = hvgo_flow * 0.40 + vdu_yields['Light Vacuum Gas Oil (LVGO)']['flow_kg_h'] * 0.65
        coker_feed = vr_flow
        
        # 3. Conversion Units Execution
        fcc_out = self.conv.solve_fcc_kinetics(fcc_feed)
        hcu_out = self.conv.solve_hydrocracker_kinetics(hcu_feed)
        coker_out = self.conv.solve_delayed_coker(coker_feed)
        
        # 4. Finished Product Pool Blending
        # Gasoline Pool: CDU Light Naphtha + FCC Gasoline + Hydrocrackate + Coker Naphtha
        gasoline_components = [
            ('CDU Light Naphtha', cdu_yields['Light Naphtha']['flow_kg_h'], 68.0),
            ('FCC Gasoline', fcc_out['FCC Gasoline (RON 92+)']['flow_kg_h'], 92.5),
            ('HCU Naphtha', hcu_out['Heavy Hydrocrackate Naphtha']['flow_kg_h'], 74.0),
            ('Coker Naphtha', coker_out['Coker Naphtha']['flow_kg_h'], 62.0),
        ]
        total_gasoline_kg_h = sum(c[1] for c in gasoline_components)
        blended_ron = sum(c[1] * c[2] for c in gasoline_components) / total_gasoline_kg_h
        
        # Diesel Pool: CDU Diesel + HCU ULSD + FCC LCO + Coker LCGO
        diesel_components = [
            ('CDU Diesel (AGO)', cdu_yields['Diesel / AGO']['flow_kg_h'], 50.0, 0.25),
            ('HCU ULSD', hcu_out['Ultra-Low Sulfur Diesel (ULSD)']['flow_kg_h'], 62.0, 0.001), # <10 ppm
            ('FCC LCO (Hydrotreated)', fcc_out['Light Cycle Oil (LCO -> Diesel)']['flow_kg_h'], 42.0, 0.05),
            ('Coker LCGO (Hydrotreated)', coker_out['Light Coker Gas Oil (LCGO)']['flow_kg_h'], 46.0, 0.03),
        ]
        total_diesel_kg_h = sum(d[1] for d in diesel_components)
        blended_cetane = sum(d[1] * d[2] for d in diesel_components) / total_diesel_kg_h
        blended_sulfur_pct = sum(d[1] * d[3] for d in diesel_components) / total_diesel_kg_h
        
        # Jet Fuel Pool: CDU Kerosene + HCU Jet
        jet_components = [
            ('CDU Kerosene / Jet A-1', cdu_yields['Kerosene / Jet A-1']['flow_kg_h']),
            ('HCU Jet Fuel', hcu_out['Hydrocracker Jet Fuel']['flow_kg_h']),
        ]
        total_jet_kg_h = sum(j[1] for j in jet_components)
        
        # LPG & Light Ends
        total_lpg_kg_h = cdu_yields['Off-Gas & LPG']['flow_kg_h'] + fcc_out['LPG (C3/C4 Alkylation Feed)']['flow_kg_h'] + hcu_out['Light Ends (LPG / C1-C4)']['flow_kg_h'] + coker_out['Coker Off-Gas']['flow_kg_h']
        
        # Solid Petroleum Coke & Heavy Fuel Oil
        total_coke_kg_h = coker_out['Petroleum Green Coke']['flow_kg_h']
        total_fuel_oil_kg_h = fcc_out['Clarified Slurry Oil']['flow_kg_h'] + coker_out['Heavy Coker Gas Oil (HCGO)']['flow_kg_h']
        
        results = {
            'crude_input_kg_h': self.cdu_vdu.crude_kg_h,
            'gasoline_pool': {'flow_kg_h': total_gasoline_kg_h, 'bpd': total_gasoline_kg_h / (745.0 * 0.1589873 / 24.0), 'ron': blended_ron},
            'diesel_pool': {'flow_kg_h': total_diesel_kg_h, 'bpd': total_diesel_kg_h / (840.0 * 0.1589873 / 24.0), 'cetane': blended_cetane, 'sulfur_wt_pct': blended_sulfur_pct},
            'jet_fuel_pool': {'flow_kg_h': total_jet_kg_h, 'bpd': total_jet_kg_h / (805.0 * 0.1589873 / 24.0)},
            'lpg_pool': {'flow_kg_h': total_lpg_kg_h, 'bpd': total_lpg_kg_h / (550.0 * 0.1589873 / 24.0)},
            'fuel_oil_pool': {'flow_kg_h': total_fuel_oil_kg_h, 'bpd': total_fuel_oil_kg_h / (960.0 * 0.1589873 / 24.0)},
            'petroleum_coke_kg_h': total_coke_kg_h,
            'coke_tons_day': total_coke_kg_h * 24.0 / 1000.0,
        }
        return results

def main():
    print("=" * 80)
    print("VIRTUAL REFINERY: MATERIAL BALANCE & FINISHED PRODUCT SLATE")
    print("=" * 80)
    net = RefineryStreamNetwork(100000.0)
    bal = net.solve_refinery_balance()
    
    print(f"Crude Feed: 100,000 BPD ({bal['crude_input_kg_h']:,.0f} kg/h)\n")
    print(f"{'FINISHED PRODUCT POOL':<28} | {'VOL RATE (BPD)':<16} | {'MASS FLOW (kg/h)':<18} | {'SPECIFICATIONS'}")
    print("-" * 85)
    print(f"{'Premium Gasoline Pool':<28} | {bal['gasoline_pool']['bpd']:>12,.0f} BPD | {bal['gasoline_pool']['flow_kg_h']:>14,.0f} kg/h | RON: {bal['gasoline_pool']['ron']:.1f}")
    print(f"{'Ultra-Low Sulfur Diesel':<28} | {bal['diesel_pool']['bpd']:>12,.0f} BPD | {bal['diesel_pool']['flow_kg_h']:>14,.0f} kg/h | Cetane: {bal['diesel_pool']['cetane']:.1f}, S: {bal['diesel_pool']['sulfur_wt_pct']*10000:.0f} ppm")
    print(f"{'Aviation Jet A-1 Fuel':<28} | {bal['jet_fuel_pool']['bpd']:>12,.0f} BPD | {bal['jet_fuel_pool']['flow_kg_h']:>14,.0f} kg/h | Freeze: -47 C")
    print(f"{'LPG & Light Petrochem':<28} | {bal['lpg_pool']['bpd']:>12,.0f} BPD | {bal['lpg_pool']['flow_kg_h']:>14,.0f} kg/h | High Propane/Butane")
    print(f"{'Heavy Fuel Oil / Bunker':<28} | {bal['fuel_oil_pool']['bpd']:>12,.0f} BPD | {bal['fuel_oil_pool']['flow_kg_h']:>14,.0f} kg/h | Viscosity 380 cSt")
    print(f"{'Petroleum Solid Coke':<28} | {bal['coke_tons_day']:>11,.0f} T/day | {bal['petroleum_coke_kg_h']:>14,.0f} kg/h | High Carbon Anode")
    print("=" * 80)

if __name__ == '__main__':
    main()
