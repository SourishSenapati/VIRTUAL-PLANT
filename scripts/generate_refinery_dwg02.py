"""
A4 OPTIMIZED: DWG-02 CDU & VDU FRACTIONATION & CUT-POINT PROFILES
VIRTUAL PETROLEUM REFINERY DIGITAL TWIN (VIRTUAL-PLANT)
STUDENT: SOURISH SENAPATI | ROLL: 002310301035 | DATE: 19/10/2026
SUBJECT: PROCESS PLANT DIGITAL TWIN & CAD | JADAVPUR UNIVERSITY
"""

import sys
import os
import math
sys.path.append(os.path.dirname(__file__))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, Arc
from cad_refinery_common import (
    create_a4_canvas, draw_a4_border, draw_refinery_title_block,
    cad_line, cad_rect, cad_circle, cad_arc, cad_text, cad_arrow,
    cad_dim_h, cad_dim_v, cad_balloon, cad_valve, cad_draw_table_a4, W, H, BK, GREY
)

def generate_refinery_dwg02(out_pdf, out_png):
    fig, ax = create_a4_canvas()
    draw_a4_border(ax)
    
    draw_refinery_title_block(ax, 'CDU & VDU FRACTIONATION & CUT-POINT PROFILES',
                              'JU/ChE/VP/DWG-02', scale='DIAGRAMMATIC / GRAPHICAL', date='19 / 10 / 2026')
    
    # Header Banner
    cad_text(ax, W/2, H - 1.25, 'CRUDE FRACTIONATION & CUT-POINT TEMPERATURE PROFILES (CDU C-101 / VDU C-102)', sz=6.6, bold=True)
    cad_text(ax, W/2, H - 1.62, 'TRUE BOILING POINT (TBP) CUT ARCHITECTURE | CRUDE HEATER F-101 & VACUUM EJECTOR CONDENSER SYSTEM', sz=4.8, bold=False)
    
    # ═════════════════════════════════════════════════════════════════════════
    # LEFT HALF: PROCESS FLOW ELEVATIONS (CDU & VDU COLUMNS)
    # ═════════════════════════════════════════════════════════════════════════
    # 1. CDU Column C-101 (X=4.6, Y=11.2)
    CX1, CY1 = 4.6, 11.2
    cad_text(ax, CX1, 16.8, 'ATMOSPHERIC COLUMN C-101', sz=5.0, bold=True)
    cad_text(ax, CX1, 16.45, '48 TRAYS | 5.2 m ID x 54 m H', sz=3.8, bold=True)
    
    # Column Shell
    cad_rect(ax, CX1 - 0.7, 9.8, 1.4, 6.2, lw=0.95, fill=True)
    cad_arc(ax, CX1, 16.0, 1.4, 0.45, theta1=0, theta2=180, lw=0.95)
    cad_arc(ax, CX1, 9.8, 1.4, 0.45, theta1=180, theta2=360, lw=0.95)
    
    # Crude Fired Heater F-101
    cad_rect(ax, 1.4, 10.6, 1.2, 1.4, lw=0.85, fill=True)
    cad_text(ax, 2.0, 11.3, 'F-101\nCRUDE\nHEATER\n365 C', sz=3.4, bold=True)
    cad_line(ax, 2.6, 11.3, CX1 - 0.7, 11.3, lw=0.85)
    cad_arrow(ax, CX1 - 1.0, 11.3, CX1 - 0.7, 11.3, head_scale=5)
    cad_text(ax, 3.4, 11.55, 'FLASH ZONE (365 C)', sz=3.2, bold=True)
    
    # CDU Side Draws:
    # Overhead Naphtha
    cad_line(ax, CX1, 16.22, CX1 + 1.8, 16.22, lw=0.75)
    cad_arrow(ax, CX1 + 1.5, 16.22, CX1 + 1.8, 16.22, head_scale=5)
    cad_text(ax, CX1 + 2.0, 16.22, 'OVERHEAD NAPHTHA (108 C)', sz=3.2, bold=True, ha='left')
    
    # Kerosene Side Stripper
    cad_line(ax, CX1 + 0.7, 14.2, CX1 + 1.8, 14.2, lw=0.75)
    cad_rect(ax, CX1 + 1.8, 13.8, 0.5, 0.8, lw=0.65, fill=True)
    cad_text(ax, CX1 + 2.05, 14.2, 'SS-1', sz=3.0, bold=True)
    cad_line(ax, CX1 + 2.3, 14.2, CX1 + 3.4, 14.2, lw=0.75)
    cad_arrow(ax, CX1 + 3.1, 14.2, CX1 + 3.4, 14.2, head_scale=5)
    cad_text(ax, CX1 + 3.5, 14.2, 'KEROSENE / JET (185 C)', sz=3.2, bold=True, ha='left')
    
    # Diesel Side Stripper
    cad_line(ax, CX1 + 0.7, 12.6, CX1 + 1.8, 12.6, lw=0.75)
    cad_rect(ax, CX1 + 1.8, 12.2, 0.5, 0.8, lw=0.65, fill=True)
    cad_text(ax, CX1 + 2.05, 12.6, 'SS-2', sz=3.0, bold=True)
    cad_line(ax, CX1 + 2.3, 12.6, CX1 + 3.4, 12.6, lw=0.75)
    cad_arrow(ax, CX1 + 3.1, 12.6, CX1 + 3.4, 12.6, head_scale=5)
    cad_text(ax, CX1 + 3.5, 12.6, 'DIESEL / AGO (280 C)', sz=3.2, bold=True, ha='left')
    
    # Atmospheric Residue to VDU
    cad_line(ax, CX1, 9.58, CX1, 8.8, lw=0.85)
    cad_line(ax, CX1, 8.8, 2.0, 8.8, lw=0.85)
    cad_line(ax, 2.0, 8.8, 2.0, 6.2, lw=0.85)
    cad_arrow(ax, 2.0, 6.6, 2.0, 6.2, head_scale=5)
    cad_text(ax, 3.4, 8.95, 'ATMOSPHERIC RESIDUE (>360 C)', sz=3.4, bold=True)
    
    # 2. VDU Vacuum Column C-102 (X=4.6, Y=5.0)
    CX2, CY2 = 4.6, 5.0
    cad_text(ax, CX2, 8.5, 'VACUUM COLUMN C-102', sz=5.0, bold=True)
    cad_text(ax, CX2, 8.15, 'DEEP-CUT BULB | 8.5 m ID | 25 mmHg(a)', sz=3.8, bold=True)
    
    # Vacuum Heater F-102
    cad_rect(ax, 1.4, 5.0, 1.2, 1.2, lw=0.85, fill=True)
    cad_text(ax, 2.0, 5.6, 'F-102\nVACUUM\nFURNACE\n415 C', sz=3.2, bold=True)
    cad_line(ax, 2.6, 5.6, CX2 - 1.0, 5.6, lw=0.85)
    cad_arrow(ax, CX2 - 1.3, 5.6, CX2 - 1.0, 5.6, head_scale=5)
    
    # VDU Bulb Column Shell
    cad_rect(ax, CX2 - 1.0, 4.4, 2.0, 1.8, lw=0.95, fill=True)  # Lower 8.5m bulb
    cad_rect(ax, CX2 - 0.7, 6.2, 1.4, 1.5, lw=0.95, fill=True)  # Upper 6.0m section
    cad_arc(ax, CX2, 7.7, 1.4, 0.45, theta1=0, theta2=180, lw=0.95)
    cad_arc(ax, CX2, 4.4, 2.0, 0.50, theta1=180, theta2=360, lw=0.95)
    
    # VDU Product Draws:
    # 3-Stage Steam Ejectors
    cad_line(ax, CX2, 7.92, CX2 + 1.6, 7.92, lw=0.75)
    cad_text(ax, CX2 + 1.8, 7.92, 'STEAM EJECTORS (25 mmHg)', sz=3.2, bold=True, ha='left')
    
    # LVGO Draw
    cad_line(ax, CX2 + 0.7, 6.8, CX2 + 2.4, 6.8, lw=0.75)
    cad_arrow(ax, CX2 + 2.1, 6.8, CX2 + 2.4, 6.8, head_scale=5)
    cad_text(ax, CX2 + 2.5, 6.8, 'LVGO (360-440 C)', sz=3.2, bold=True, ha='left')
    
    # HVGO Draw
    cad_line(ax, CX2 + 1.0, 5.2, CX2 + 2.4, 5.2, lw=0.75)
    cad_arrow(ax, CX2 + 2.1, 5.2, CX2 + 2.4, 5.2, head_scale=5)
    cad_text(ax, CX2 + 2.5, 5.2, 'HVGO (440-540 C) -> FCC/HCU', sz=3.2, bold=True, ha='left')
    
    # Vacuum Residue Bottoms
    cad_line(ax, CX2, 4.15, CX2, 3.4, lw=0.85)
    cad_arrow(ax, CX2, 3.7, CX2, 3.4, head_scale=5)
    cad_text(ax, CX2 + 0.2, 3.55, 'VACUUM RESIDUE (>540 C) -> DELAYED COKER', sz=3.4, bold=True, ha='left')
    
    # ═════════════════════════════════════════════════════════════════════════
    # RIGHT TOP: RIAZI-DAUBERT TBP DISTILLATION CURVE GRAPH
    # ═════════════════════════════════════════════════════════════════════════
    GX0, GY0 = 14.8, 10.4
    GW, GH = 13.6, 6.0
    
    cad_rect(ax, GX0, GY0, GW, GH, lw=0.85, fill=True)
    cad_text(ax, GX0 + GW/2, GY0 + GH + 0.35, 'TRUE BOILING POINT (TBP) DISTILLATION CURVE & FRACTIONATION CUT-POINTS', sz=4.8, bold=True)
    
    # TBP Curve Coordinates: Temp from 0 to 700 C, Yield from 0 to 100%
    temp_to_gx = lambda t: GX0 + (t / 700.0) * GW
    pct_to_gy = lambda p: GY0 + (p / 100.0) * GH
    
    # Distillation Cut Bands with Color Fill
    cuts_data = [
        ('LPG', 0, 35, 7.1, '#fff2cc'),
        ('Light Naphtha', 35, 80, 5.6, '#ffe6cc'),
        ('Heavy Naphtha', 80, 150, 11.8, '#ffcc99'),
        ('Kerosene / Jet', 150, 240, 17.9, '#cce6ff'),
        ('Diesel / AGO', 240, 360, 21.8, '#d9f2d9'),
        ('LVGO', 360, 440, 11.0, '#e6ccff'),
        ('HVGO', 440, 540, 9.7, '#d9b3ff'),
        ('Vacuum Residue', 540, 700, 15.1, '#e0e0e0'),
    ]
    
    for name, t1, t2, wt, col in cuts_data:
        gx1 = temp_to_gx(t1)
        gx2 = temp_to_gx(t2)
        cad_rect(ax, gx1, GY0, gx2 - gx1, GH, lw=0.25, fill=True, fc=col)
        cad_line(ax, gx2, GY0, gx2, GY0 + GH, lw=0.45, ls=':')
        cad_text(ax, (gx1 + gx2)/2, GY0 + 0.5, f"{name}\n({wt:.1f}%)", sz=3.2, bold=True, rotation=90)
        
    # Plot Continuous Sigmoidal TBP Curve
    t_vals = np.linspace(20, 700, 150)
    for i in range(len(t_vals) - 1):
        t1, t2 = t_vals[i], t_vals[i+1]
        p1 = 100.0 * math.exp(-3.65 * math.exp(-0.0055 * (t1 + 273.15 - 250.0)))
        p2 = 100.0 * math.exp(-3.65 * math.exp(-0.0055 * (t2 + 273.15 - 250.0)))
        cad_line(ax, temp_to_gx(t1), pct_to_gy(p1), temp_to_gx(t2), pct_to_gy(p2), lw=1.2, color='#cc0000')
        
    cad_text(ax, temp_to_gx(300), pct_to_gy(75), 'CUMULATIVE TBP CURVE (wt%)', sz=4.2, bold=True, color='#cc0000')
    cad_text(ax, GX0 + GW/2, GY0 - 0.40, 'TRUE BOILING POINT TEMPERATURE (deg C)', sz=4.4, bold=True)
    cad_text(ax, GX0 - 0.45, GY0 + GH/2, 'CUMULATIVE YIELD (wt %)', sz=4.4, bold=True, rotation=90)
    
    # ═════════════════════════════════════════════════════════════════════════
    # RIGHT BOTTOM: DETAILED FRACTIONATION SPECIFICATIONS TABLES
    # ═════════════════════════════════════════════════════════════════════════
    t1_headers = ['FRACTION STREAM', 'CUT T (C)', 'YIELD (wt%)', 'MASS (kg/h)', 'API', 'DOWNSTREAM UNIT']
    t1_rows = [
        ['Off-Gas & LPG', '< 35 C', '7.06 %', '39,858', '95.0', 'Amine Treating -> LPG Spheres'],
        ['Light Naphtha', '35 - 80 C', '5.56 %', '31,417', '72.0', 'Isomerization Unit (RON 88)'],
        ['Heavy Naphtha', '80 - 150 C', '11.83 %', '66,816', '54.5', 'NHT -> Platformer (RON 102)'],
        ['Kerosene / Jet A-1', '150 - 240 C', '17.93 %', '101,220', '42.0', 'Merox Sweetening -> Jet Pool'],
        ['Diesel / AGO', '240 - 360 C', '21.78 %', '123,012', '34.0', 'Diesel HDS -> ULSD Blend'],
        ['Light Vacuum Gas Oil', '360 - 440 C', '10.98 %', '61,993', '26.0', 'Hydrocracker / Diesel Blend'],
        ['Heavy Vacuum Gas Oil', '440 - 540 C', '9.66 %', '54,526', '20.5', 'FCCU (60%) & HCU (40%) Feed'],
        ['Vacuum Residue (VR)', '> 540 C', '15.20 %', '85,828', '5.5', 'Delayed Coking Unit (DCU)'],
    ]
    t1_col_w = [3.8, 2.0, 1.8, 2.0, 1.2, 2.8]
    cad_draw_table_a4(ax, 14.8, 4.40, t1_headers, t1_rows, t1_col_w,
                      row_h=0.32, title='TABLE 1: PRIMARY FRACTIONATION CUT-POINTS & STREAM YIELDS',
                      title_sz=4.6, sz=3.7)
    
    # Save Outputs
    fig.savefig(out_pdf, format='pdf', dpi=300)
    fig.savefig(out_png, format='png', dpi=300)
    plt.close(fig)
    print(f"  [OK] DWG-02 generated: {os.path.basename(out_pdf)}")

if __name__ == '__main__':
    out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'CAD_Drawings')
    os.makedirs(out_dir, exist_ok=True)
    generate_refinery_dwg02(
        os.path.join(out_dir, '02_CDU_VDU_Fractionation_CutPoints_Process_CAD.pdf'),
        os.path.join(out_dir, '02_CDU_VDU_Fractionation_CutPoints_Process_CAD.png')
    )
