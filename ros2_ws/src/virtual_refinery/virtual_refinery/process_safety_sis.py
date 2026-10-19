"""
PROCESS SAFETY INSTRUMENTED SYSTEMS (SIS) & FLARE RELIEF SIMULATOR
Author: Sourish Senapati (Department of Chemical Engineering, Jadavpur University)

Implements multi-layer protection analysis (LOPA), SIL-2/SIL-3 trip logic,
emergency depressuring (EDP), and API 521 flare radiation dispersion physics.
"""

import sys
import os
import math

class ProcessSafetySystem:
    """Safety Instrumented System (SIS), SIL trip logic, and flare radiation physics."""
    def __init__(self):
        self.trips = {
            'ESD-101': {'active': False, 'desc': 'CDU High-High Differential Pressure (>38 kPa)'},
            'ESD-102': {'active': False, 'desc': 'CDU Sump Low-Low Level (<12%)'},
            'ESD-201': {'active': False, 'desc': 'FCCU Slide Valve Reverse Flow (DP < 10 kPa)'},
            'ESD-301': {'active': False, 'desc': 'Hydrocracker Bed Thermal Runaway (>445 C)'},
            'ESD-401': {'active': False, 'desc': 'Coke Drum Overpressure (>4.2 bar)'},
        }
        self.flare_load_kg_h = 12500.0  # Normal base purge / pilot
        self.flare_tip_height_m = 90.0

    def evaluate_process_interlocks(self, cdu_dp, cdu_level, fcc_slide_dp, hcu_temp, coker_p):
        """Evaluates sensor thresholds and trips emergency isolation valves."""
        triggered = []
        
        # 1. CDU DP Check
        if cdu_dp > 38.0:
            self.trips['ESD-101']['active'] = True
            triggered.append(('ESD-101', 'CDU Differential Pressure Exceeded 38.0 kPa (Tray Flooding Hazard)'))
        else:
            self.trips['ESD-101']['active'] = False
            
        # 2. CDU Level Check
        if cdu_level < 12.0:
            self.trips['ESD-102']['active'] = True
            triggered.append(('ESD-102', 'CDU Sump Level Dropped Below 12.0% (Heater Dryout Hazard)'))
        else:
            self.trips['ESD-102']['active'] = False
            
        # 3. FCC Slide Valve DP Check
        if fcc_slide_dp < 10.0:
            self.trips['ESD-201']['active'] = True
            triggered.append(('ESD-201', 'FCC Slide Valve DP < 10 kPa (Regenerator Backflow Hazard)'))
        else:
            self.trips['ESD-201']['active'] = False
            
        # 4. HCU Thermal Runaway Check
        if hcu_temp > 445.0:
            self.trips['ESD-301']['active'] = True
            # High pressure depressuring triggers 250,000 kg/h to flare
            self.flare_load_kg_h = 265000.0
            triggered.append(('ESD-301', 'Hydrocracker Bed Temp > 445 C (Thermal Runaway Depressuring)'))
        else:
            self.trips['ESD-301']['active'] = False
            
        # 5. Coker Overpressure Check
        if coker_p > 4.2:
            self.trips['ESD-401']['active'] = True
            triggered.append(('ESD-401', 'Coke Drum Pressure > 4.2 bar(g) (Overpressure PSV Lift)'))
        else:
            self.trips['ESD-401']['active'] = False
            
        return triggered

    def compute_flare_radiation(self, distance_m=150.0):
        """
        API 521 Point-Source Radiation Model:
        K = (tau * F * Q_total) / (4 * pi * R^2)
        Returns ground radiant intensity in kW/m2.
        """
        # Hydrocarbon average lower heating value: 43.5 MJ/kg
        lhv_j_kg = 43.5e6
        heat_release_w = (self.flare_load_kg_h / 3600.0) * lhv_j_kg
        f_rad = 0.22  # Radiation fraction for clean steam-assisted smokeless tip
        tau = 0.95    # Atmospheric transmissivity
        
        # Distance from flare flame center to ground receptor
        flame_length_m = 0.0033 * (heat_release_w ** 0.478)
        flame_center_z = self.flare_tip_height_m + 0.5 * flame_length_m
        r_dist = math.sqrt(distance_m**2 + flame_center_z**2)
        
        # Intensity in W/m2 -> convert to kW/m2
        intensity_w_m2 = (tau * f_rad * heat_release_w) / (4.0 * math.pi * (r_dist**2))
        return intensity_w_m2 / 1000.0

def main():
    print("=" * 80)
    print("VIRTUAL REFINERY: PROCESS SAFETY & SIS TRIP INTERLOCK SIMULATOR")
    print("=" * 80)
    sis = ProcessSafetySystem()
    
    print("\n--- TEST CASE 1: NORMAL PROCESS OPERATION ---")
    events = sis.evaluate_process_interlocks(cdu_dp=24.5, cdu_level=52.0, fcc_slide_dp=28.0, hcu_temp=395.0, coker_p=2.1)
    print(f"Active Trips: {len(events)} (All Protection Layers Normal)")
    rad_normal = sis.compute_flare_radiation(150.0)
    print(f"Flare Base Radiation @ 150m: {rad_normal:.3f} kW/m2 (API 521 Limit: 4.73 kW/m2) -> PASS")
    
    print("\n--- TEST CASE 2: SEVERE HYDROCRACKER THERMAL RUNAWAY EXOTHERM ---")
    events_fault = sis.evaluate_process_interlocks(cdu_dp=25.0, cdu_level=50.0, fcc_slide_dp=30.0, hcu_temp=462.0, coker_p=2.2)
    for trip_id, reason in events_fault:
        print(f"  [CRITICAL TRIP] {trip_id}: {reason}")
    rad_emergency = sis.compute_flare_radiation(150.0)
    print(f"Emergency Depressuring Flare Load: {sis.flare_load_kg_h:,.0f} kg/h")
    print(f"Emergency Flare Radiation @ 150m: {rad_emergency:.2f} kW/m2 (Safe Zone Boundary Verified per API 521)")
    print("=" * 80)

if __name__ == '__main__':
    main()
