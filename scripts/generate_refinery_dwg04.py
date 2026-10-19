"""
A4 OPTIMIZED: DWG-04 REFINERY PLANT PLOT PLAN & GAZEBO 3D LAYOUT
VIRTUAL PETROLEUM REFINERY DIGITAL TWIN (VIRTUAL-PLANT)
STUDENT: SOURISH SENAPATI | ROLL: 002310301035 | DATE: 19/10/2026
SUBJECT: PROCESS PLANT DIGITAL TWIN & CAD | JADAVPUR UNIVERSITY
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, Arc
from cad_refinery_common import (
    create_a4_canvas, draw_a4_border, draw_refinery_title_block,
    cad_line, cad_rect, cad_circle, cad_arc, cad_text, cad_arrow,
    cad_draw_table_a4, cad_dim_h, cad_dim_v, W, H, BK, GREY
)

def generate_refinery_dwg04(out_pdf, out_png):
    fig, ax = create_a4_canvas()
    draw_a4_border(ax)
    
    draw_refinery_title_block(ax, 'REFINERY PLANT PLOT PLAN & GAZEBO 3D LAYOUT',
                              'JU/ChE/VP/DWG-04', scale='1 : 2500 (METRIC)', date='19 / 10 / 2026')
    
    # Header Banner
    cad_text(ax, W/2, H - 1.25, 'OVERALL REFINERY PLOT PLAN, BATTERY LIMITS & GAZEBO 3D SPATIAL COORDINATES', sz=6.8, bold=True)
    cad_text(ax, W/2, H - 1.62, 'SCALE: 600 m x 400 m PLANT FOOTPRINT | API RP 500 / NFPA 30 / OISD-118 SAFETY SPACING | ODE PHYSICS INTEGRATION', sz=4.8, bold=False)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 1: 2D PLOT PLAN MAP (LEFT REGION: X=1.0 to 18.2, Y=8.6 to 18.8)
    # ═════════════════════════════════════════════════════════════════════════
    plan_x, plan_y, plan_w, plan_h = 1.2, 8.6, 17.0, 10.2
    cad_rect(ax, plan_x, plan_y, plan_w, plan_h, lw=1.1, fill=True, fc='#fbfcfd')
    cad_text(ax, plan_x + plan_w/2, plan_y + plan_h - 0.28, 'REFINERY COMPLEX BATTERY LIMITS (ISBL & OSBL GENERAL ARRANGEMENT)', sz=4.8, bold=True, color='#003366')
    
    # North Arrow Indicator (Top Right of Plan)
    na_x, na_y = plan_x + plan_w - 0.9, plan_y + plan_h - 0.9
    cad_circle(ax, na_x, na_y, 0.45, lw=0.65, fill=True, fc='white')
    ax.add_patch(Polygon([(na_x, na_y + 0.38), (na_x - 0.14, na_y - 0.25), (na_x, na_y - 0.10)], closed=True, fc=BK, ec=BK))
    ax.add_patch(Polygon([(na_x, na_y + 0.38), (na_x + 0.14, na_y - 0.25), (na_x, na_y - 0.10)], closed=True, fc='white', ec=BK, lw=0.5))
    cad_text(ax, na_x, na_y + 0.55, 'N', sz=5.5, bold=True)
    
    # Plant Perimeter Boundary & Roads
    # Perimeter Fencing
    cad_rect(ax, plan_x + 0.4, plan_y + 0.4, plan_w - 0.8, plan_h - 1.0, lw=0.6, ls='--', fill=False)
    cad_text(ax, plan_x + 1.8, plan_y + plan_h - 0.8, 'SECURITY PERIMETER FENCE', sz=3.2, bold=True)
    
    # Central Pipe Rack Spine (Running West to East across ISBL)
    rack_x, rack_y, rack_w, rack_h = plan_x + 1.2, plan_y + 4.6, 14.6, 0.65
    cad_rect(ax, rack_x, rack_y, rack_w, rack_h, lw=0.85, fill=True, fc='#e0e8f0')
    # Cross hatching on pipe rack
    for hx in np.arange(rack_x, rack_x + rack_w, 0.4):
        cad_line(ax, hx, rack_y, hx, rack_y + rack_h, lw=0.35, color='#8899aa')
    cad_text(ax, rack_x + rack_w/2, rack_y + rack_h/2, 'MAIN INTER-UNIT PIPE RACK SPINE (3-TIER: HC HEADERS, STEAM, UTILITIES) [Y=0 m]', sz=3.8, bold=True, bg='white')
    
    # ── ISBL PROCESS UNIT BLOCKS (North of Pipe Rack) ──
    # Unit 100: CDU & Desalter
    u100_x, u100_y, u100_w, u100_h = plan_x + 1.4, plan_y + 5.6, 2.6, 2.8
    cad_rect(ax, u100_x, u100_y, u100_w, u100_h, lw=0.8, fill=True, fc='#e6f0fa')
    cad_circle(ax, u100_x + 1.0, u100_y + 1.6, 0.42, lw=0.75, fill=True, fc='#ffffff')
    cad_text(ax, u100_x + 1.0, u100_y + 1.6, 'C-101', sz=3.3, bold=True)
    cad_rect(ax, u100_x + 1.7, u100_y + 0.4, 0.7, 0.9, lw=0.65, fill=True, fc='#ffe6cc')
    cad_text(ax, u100_x + 2.05, u100_y + 0.85, 'H-101', sz=3.0, bold=True)
    cad_text(ax, u100_x + u100_w/2, u100_y + 2.5, 'UNIT 100: CDU', sz=3.8, bold=True)
    cad_text(ax, u100_x + u100_w/2, u100_y + 0.22, 'Gazebo: (-120, 45, 0)', sz=3.0)
    
    # Unit 200: VDU
    u200_x, u200_y, u200_w, u200_h = plan_x + 4.4, plan_y + 5.6, 2.5, 2.8
    cad_rect(ax, u200_x, u200_y, u200_w, u200_h, lw=0.8, fill=True, fc='#e6f0fa')
    cad_circle(ax, u200_x + 1.0, u200_y + 1.6, 0.52, lw=0.75, fill=True, fc='#ffffff')
    cad_text(ax, u200_x + 1.0, u200_y + 1.6, 'C-201', sz=3.3, bold=True)
    cad_rect(ax, u200_x + 1.7, u200_y + 0.4, 0.65, 0.85, lw=0.65, fill=True, fc='#ffe6cc')
    cad_text(ax, u200_x + 2.02, u200_y + 0.82, 'H-201', sz=3.0, bold=True)
    cad_text(ax, u200_x + u200_w/2, u200_y + 2.5, 'UNIT 200: VDU', sz=3.8, bold=True)
    cad_text(ax, u200_x + u200_w/2, u200_y + 0.22, 'Gazebo: (-60, 45, 0)', sz=3.0)
    
    # Unit 300: FCCU
    u300_x, u300_y, u300_w, u300_h = plan_x + 7.3, plan_y + 5.6, 3.2, 3.2
    cad_rect(ax, u300_x, u300_y, u300_w, u300_h, lw=0.8, fill=True, fc='#fff5eb')
    cad_circle(ax, u300_x + 1.0, u300_y + 1.8, 0.55, lw=0.75, fill=True, fc='#ffffff')
    cad_text(ax, u300_x + 1.0, u300_y + 1.8, 'R-302\nRegen', sz=2.9, bold=True)
    cad_circle(ax, u300_x + 2.3, u300_y + 1.8, 0.42, lw=0.75, fill=True, fc='#ffffff')
    cad_text(ax, u300_x + 2.3, u300_y + 1.8, 'R-301\nRx', sz=2.9, bold=True)
    cad_text(ax, u300_x + u300_w/2, u300_y + 2.9, 'UNIT 300: FCCU', sz=3.8, bold=True)
    cad_text(ax, u300_x + u300_w/2, u300_y + 0.22, 'Gazebo: (10, 50, 0)', sz=3.0)
    
    # Unit 400: Hydrocracker Complex (HCU)
    u400_x, u400_y, u400_w, u400_h = plan_x + 11.0, plan_y + 5.6, 3.2, 3.2
    cad_rect(ax, u400_x, u400_y, u400_w, u400_h, lw=0.8, fill=True, fc='#eef9f2')
    cad_circle(ax, u400_x + 0.9, u400_y + 1.8, 0.40, lw=0.75, fill=True, fc='#ffffff')
    cad_text(ax, u400_x + 0.9, u400_y + 1.8, 'R-401', sz=3.0, bold=True)
    cad_circle(ax, u400_x + 2.2, u400_y + 1.8, 0.40, lw=0.75, fill=True, fc='#ffffff')
    cad_text(ax, u400_x + 2.2, u400_y + 1.8, 'R-402', sz=3.0, bold=True)
    cad_text(ax, u400_x + u400_w/2, u400_y + 2.9, 'UNIT 400: HCU (155 bar)', sz=3.8, bold=True)
    cad_text(ax, u400_x + u400_w/2, u400_y + 0.22, 'Gazebo: (85, 50, 0)', sz=3.0)
    
    # Unit 500: Delayed Coker Unit & Coke Pit (South-East)
    u500_x, u500_y, u500_w, u500_h = plan_x + 11.0, plan_y + 1.2, 3.6, 3.0
    cad_rect(ax, u500_x, u500_y, u500_w, u500_h, lw=0.8, fill=True, fc='#f5f0eb')
    cad_circle(ax, u500_x + 0.9, u500_y + 1.8, 0.42, lw=0.75, fill=True, fc='#ffffff')
    cad_text(ax, u500_x + 0.9, u500_y + 1.8, 'D-501A', sz=2.8, bold=True)
    cad_circle(ax, u500_x + 1.9, u500_y + 1.8, 0.42, lw=0.75, fill=True, fc='#ffffff')
    cad_text(ax, u500_x + 1.9, u500_y + 1.8, 'D-501B', sz=2.8, bold=True)
    cad_rect(ax, u500_x + 2.6, u500_y + 0.5, 0.8, 2.0, lw=0.6, fill=True, fc='#e0d8cf')
    cad_text(ax, u500_x + 3.0, u500_y + 1.5, 'COKE\nPIT', sz=2.8, bold=True, rotation=90)
    cad_text(ax, u500_x + 1.5, u500_y + 2.7, 'UNIT 500: DCU', sz=3.8, bold=True)
    cad_text(ax, u500_x + 1.5, u500_y + 0.22, 'Gazebo: (85, -45, 0)', sz=3.0)
    
    # ── OSBL TANK FARM & OFFSITES (South & West) ──
    # Crude Storage Tanks (T-101 to T-104) in Bunded Area
    bund_x, bund_y, bund_w, bund_h = plan_x + 1.4, plan_y + 1.2, 5.0, 3.0
    cad_rect(ax, bund_x, bund_y, bund_w, bund_h, lw=0.75, ls='--', fill=True, fc='#f0f4f0')
    cad_text(ax, bund_x + bund_w/2, bund_y + bund_h - 0.22, 'CRUDE TANK FARM (API 650 FLOATING ROOF TANKS)', sz=3.2, bold=True)
    tank_coords = [(bund_x + 1.3, bund_y + 1.9), (bund_x + 3.7, bund_y + 1.9),
                   (bund_x + 1.3, bund_y + 0.8), (bund_x + 3.7, bund_y + 0.8)]
    for i, (tx, ty) in enumerate(tank_coords):
        cad_circle(ax, tx, ty, 0.48, lw=0.7, fill=True, fc='#ffffff')
        cad_text(ax, tx, ty, f'T-10{i+1}\n50k m3', sz=2.6, bold=True)
        
    # Central Control Room (CCR) & Safety Substation
    ccr_x, ccr_y, ccr_w, ccr_h = plan_x + 7.2, plan_y + 2.0, 2.8, 1.8
    cad_rect(ax, ccr_x, ccr_y, ccr_w, ccr_h, lw=1.0, fill=True, fc='#fff9db')
    cad_text(ax, ccr_x + ccr_w/2, ccr_y + 1.4, 'CENTRAL CONTROL ROOM (CCR)', sz=3.4, bold=True, color='#aa6600')
    cad_text(ax, ccr_x + ccr_w/2, ccr_y + 1.0, 'Blast Resistant (10 psi / 69 kPa)', sz=2.8)
    cad_text(ax, ccr_x + ccr_w/2, ccr_y + 0.65, 'DCS / SIS / SCADA Host', sz=2.8)
    cad_text(ax, ccr_x + ccr_w/2, ccr_y + 0.28, 'Gazebo: (10, -30, 0)', sz=2.8, bold=True)
    
    # Elevated Flare Stack (API 521 Sterile Radius Exclusion Zone)
    flare_cx, flare_cy = plan_x + 15.5, plan_y + 7.5
    cad_circle(ax, flare_cx, flare_cy, 1.3, lw=0.75, ls=':', fill=False, ec='#cc0000')
    cad_circle(ax, flare_cx, flare_cy, 0.25, lw=1.0, fill=True, fc='#ffcccc', ec='#cc0000')
    cad_text(ax, flare_cx, flare_cy, 'FLARE\n90m', sz=2.8, bold=True, color='#990000')
    cad_text(ax, flare_cx, flare_cy - 0.7, 'API 521 Sterile Radius', sz=2.7, bold=True, color='#cc0000')
    cad_text(ax, flare_cx, flare_cy - 1.0, 'R = 150 m (4.7 kW/m2)', sz=2.7, color='#cc0000')
    cad_text(ax, flare_cx, flare_cy + 1.45, 'Gazebo: (160, 60, 0)', sz=2.8, bold=True)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 2: GAZEBO 3D DIGITAL TWIN ARCHITECTURE (RIGHT REGION)
    # ═════════════════════════════════════════════════════════════════════════
    gz_x, gz_y, gz_w, gz_h = 18.6, 8.6, 9.9, 10.2
    cad_rect(ax, gz_x, gz_y, gz_w, gz_h, lw=0.9, fill=True, fc='#fafbfc')
    cad_text(ax, gz_x + gz_w/2, gz_y + gz_h - 0.28, 'GAZEBO PHYSICS ENGINE & DIGITAL TWIN MAPPING', sz=4.8, bold=True, color='#003366')
    
    # Diagram of Gazebo World Coordinate Axis
    cad_line(ax, gz_x + 1.2, gz_y + 7.0, gz_x + 3.2, gz_y + 7.0, lw=1.1, color='#aa0000')
    cad_arrow(ax, gz_x + 2.8, gz_y + 7.0, gz_x + 3.2, gz_y + 7.0, head_scale=6, color='#aa0000')
    cad_text(ax, gz_x + 3.4, gz_y + 7.0, '+X (East, m)', sz=3.4, bold=True, color='#aa0000')
    
    cad_line(ax, gz_x + 1.2, gz_y + 7.0, gz_x + 1.2, gz_y + 8.8, lw=1.1, color='#008800')
    cad_arrow(ax, gz_x + 1.2, gz_y + 8.5, gz_x + 1.2, gz_y + 8.8, head_scale=6, color='#008800')
    cad_text(ax, gz_x + 1.2, gz_y + 9.05, '+Y (North, m)', sz=3.4, bold=True, color='#008800')
    
    cad_line(ax, gz_x + 1.2, gz_y + 7.0, gz_x + 0.3, gz_y + 6.3, lw=1.1, color='#0000aa')
    cad_arrow(ax, gz_x + 0.5, gz_y + 6.45, gz_x + 0.3, gz_y + 6.3, head_scale=6, color='#0000aa')
    cad_text(ax, gz_x + 0.3, gz_y + 6.05, '+Z (Altitude, m)', sz=3.4, bold=True, color='#0000aa')
    cad_text(ax, gz_x + 1.2, gz_y + 6.75, '(0, 0, 0) Refinery Center', sz=2.9, bold=True)
    
    # Box for ODE Physics Configuration
    cad_rect(ax, gz_x + 4.2, gz_y + 6.1, 5.2, 3.2, lw=0.6, fill=True, fc='#ffffff')
    cad_text(ax, gz_x + 6.8, gz_y + 9.0, 'ODE PHYSICS PARAMETERS', sz=3.6, bold=True, color='#003366')
    ode_params = [
        'Solver Type: Quick (SOR lcp)',
        'Max Step Size: 0.001 s (1 ms)',
        'Real Time Update Rate: 1000 Hz',
        'ERP (Error Reduct.): 0.20',
        'CFM (Constraint Force): 1e-5',
        'Gravity Vector: [0, 0, -9.81 m/s2]',
        'Collision Engine: Bullet / ODE Hybrid'
    ]
    for idx, prm in enumerate(ode_params):
        cad_text(ax, gz_x + 4.4, gz_y + 8.55 - idx*0.36, prm, sz=3.0, ha='left')
        
    # Virtual Sensor Integration in Gazebo
    cad_rect(ax, gz_x + 0.5, gz_y + 2.8, 8.9, 2.9, lw=0.6, fill=True, fc='#ffffff')
    cad_text(ax, gz_x + gz_w/2, gz_y + 5.4, 'VIRTUAL INSPECTION SENSORS & ROBOTIC PLATFORMS', sz=3.6, bold=True, color='#003366')
    sensor_items = [
        ('LiDAR (3D Scanning)', 'Velodyne VLP-16', 'Piping clearance & structural settlement (16-beam, 100m)'),
        ('Thermal Camera (IR)', 'FLIR Boson 640', 'Furnace casing hot-spots & insulation degradation (8-14 um)'),
        ('Gas Dispersion Array', 'Point Gas IR Sensor', 'LEL Hydrocarbon & H2S gas leak monitoring (PPM detection)'),
        ('Ground Inspection Bot', 'UGV Skid-Steer', 'ROS 2 Nav2 autonomous patrol of process unit battery limits')
    ]
    for s_idx, (s_name, s_model, s_func) in enumerate(sensor_items):
        cad_text(ax, gz_x + 0.8, gz_y + 4.95 - s_idx*0.55, f'{s_name} [{s_model}]:', sz=3.1, bold=True, ha='left')
        cad_text(ax, gz_x + 0.8, gz_y + 4.65 - s_idx*0.55, f'  -> {s_func}', sz=2.8, color='#555555', ha='left')
        
    # Bridge to ROS 2 Status
    cad_rect(ax, gz_x + 0.5, gz_y + 0.5, 8.9, 2.0, lw=0.6, fill=True, fc='#eef6ff')
    cad_text(ax, gz_x + gz_w/2, gz_y + 2.25, 'GAZEBO <-> ROS 2 TOPIC BRIDGE ARCHITECTURE', sz=3.6, bold=True, color='#003366')
    bridge_lines = [
        'Gazebo World Plugin: libgazebo_ros_state.so',
        'Telemetry Publisher: /refinery/unit_telemetry [UnitTelemetry.msg]',
        'Actuator Subscriber: /refinery/valve_cmd [ValveCommand.msg]',
        'Visual State Sync: Dynamic flame height, steam discharge & tank levels'
    ]
    for b_idx, bl in enumerate(bridge_lines):
        cad_text(ax, gz_x + 0.8, gz_y + 1.85 - b_idx*0.42, bl, sz=2.9, ha='left')
        
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 3: REFINERY SPACING STANDARDS & BATTERY LIMITS TABLE
    # ═════════════════════════════════════════════════════════════════════════
    headers = [
        'EQUIPMENT / UNIT BLOCK', 'GAZEBO COORD [X, Y, Z] (m)', 'DIMENSIONS (LxWxH m)', 'MIN SPACING CODE', 'SAFETY CRITERIA & HAZARD CLASSIFICATION'
    ]
    col_w = [5.5, 5.2, 4.8, 4.0, 8.2]
    table_rows = [
        ['Unit 100: Atmospheric CDU (C-101)', '[-120.0, 45.0, 0.0]', '60.0 x 50.0 x 62.0', 'API RP 500 / OISD', 'Fired heater H-101 separated 15 m from column shell'],
        ['Unit 200: Vacuum VDU (C-201)', '[-60.0, 45.0, 0.0]', '50.0 x 45.0 x 48.0', 'API RP 500 / OISD', 'Vacuum ejector barometric seal leg & sour water sump'],
        ['Unit 300: FCCU Riser / Regen', '[10.0, 50.0, 0.0]', '70.0 x 60.0 x 65.0', 'OISD-118 Cl 5.2', 'Catalyst hopper separation; CO boiler flue ducting'],
        ['Unit 400: Hydrocracker Complex', '[85.0, 50.0, 0.0]', '80.0 x 65.0 x 42.0', 'NFPA 30 Class I', 'High-pressure H2 zone (155 bar); 30 m blast buffer'],
        ['Unit 500: Delayed Coker (Drums A/B)', '[85.0, -45.0, 0.0]', '75.0 x 55.0 x 92.0', 'OISD-118 Cl 6.4', 'Coke pit deluge system; unheading blast shield separation'],
        ['Crude Tank Farm (T-101 to T-104)', '[-100.0, -50.0, 0.0]', '140.0 x 90.0 x 22.0', 'NFPA 30 / API 650', 'Bund dyke capacity > 110% largest tank volume'],
        ['Elevated Flare Stack (API 521)', '[160.0, 60.0, 0.0]', 'Dia 1.8 m x H 90.0 m', 'API 521 Sec 5.4', 'Sterile radius R=150 m (thermal radiation < 4.7 kW/m2)'],
        ['Central Control Room (CCR)', '[10.0, -30.0, 0.0]', '40.0 x 25.0 x 8.0', 'API RP 752 / 753', 'Blast-resistant design (69 kPa); positive pressurization']
    ]
    cad_draw_table_a4(ax, 1.0, 3.45, headers, table_rows, col_w, row_h=0.45,
                      title='REFINERY BATTERY LIMITS, GAZEBO SPATIAL LAYOUT & INDUSTRIAL SAFETY SPACING STANDARDS',
                      title_sz=4.8, sz=3.8)
    
    # Save Figure
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
    fig.savefig(out_pdf, format='pdf', dpi=300)
    fig.savefig(out_png, format='png', dpi=300)
    plt.close(fig)
    print(f"Generated DWG-04:\n  PDF -> {out_pdf}\n  PNG -> {out_png}")

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    pdf_path = os.path.join(base_dir, 'CAD_Drawings', '04_Refinery_Plant_Plot_Plan_Gazebo_General_Arrangement_CAD.pdf')
    png_path = os.path.join(base_dir, 'CAD_Drawings', '04_Refinery_Plant_Plot_Plan_Gazebo_General_Arrangement_CAD.png')
    generate_refinery_dwg04(pdf_path, png_path)
