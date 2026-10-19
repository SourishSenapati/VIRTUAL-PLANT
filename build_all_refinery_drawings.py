"""
MASTER BUILD SCRIPT: COMPILE ALL REFINERY CAD DRAWINGS (01 - 06)
VIRTUAL PETROLEUM REFINERY DIGITAL TWIN (VIRTUAL-PLANT)
AUTHOR: SOURISH SENAPATI (ROLL: 002310301035) | JADAVPUR UNIVERSITY
"""

import sys
import os
import subprocess
import time

DRAWING_SCRIPTS = [
    ('DWG-01', 'generate_refinery_dwg01.py', 'Refinery Block Flow Diagram & Plant-Wide Mass Balance'),
    ('DWG-02', 'generate_refinery_dwg02.py', 'CDU & VDU Fractionation & Cut-Point Profiles'),
    ('DWG-03', 'generate_refinery_dwg03.py', 'FCCU, Hydrocracker & Delayed Coker Conversion Flowsheet'),
    ('DWG-04', 'generate_refinery_dwg04.py', 'Refinery Plant Plot Plan & Gazebo 3D Layout'),
    ('DWG-05', 'generate_refinery_dwg05.py', 'ROS 2 Digital Twin & Industrial Automation Architecture'),
    ('DWG-06', 'generate_refinery_dwg06.py', 'Process Dynamics, Protection Layers & Flare Safety System'),
]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_dir = os.path.join(base_dir, 'scripts')
    out_dir = os.path.join(base_dir, 'CAD_Drawings')
    os.makedirs(out_dir, exist_ok=True)
    
    print("=" * 78)
    print("  VIRTUAL-PLANT CAD DRAWINGS MASTER BUILD PIPELINE")
    print("  Author: Sourish Senapati (Roll: 002310301035)")
    print("  Jadavpur University | Department of Chemical Engineering")
    print("=" * 78)
    
    t0 = time.time()
    success_count = 0
    
    for tag, script_name, description in DRAWING_SCRIPTS:
        script_path = os.path.join(scripts_dir, script_name)
        print(f"\n[BUILDING {tag}] -> {description} ({script_name})...")
        res = subprocess.run([sys.executable, script_path], cwd=base_dir, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  --> SUCCESS: {tag} compiled cleanly.")
            success_count += 1
        else:
            print(f"  --> FAILED: {tag} with exit code {res.returncode}")
            print(res.stderr)
            
    elapsed = time.time() - t0
    print("\n" + "=" * 78)
    print(f"  BUILD COMPLETE: {success_count}/{len(DRAWING_SCRIPTS)} drawings successfully compiled in {elapsed:.2f}s")
    print(f"  Output directory: {out_dir}")
    print("=" * 78)
    
    return 0 if success_count == len(DRAWING_SCRIPTS) else 1

if __name__ == '__main__':
    sys.exit(main())
