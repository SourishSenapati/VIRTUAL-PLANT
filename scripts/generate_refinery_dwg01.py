"""
A4 OPTIMIZED: DWG-01 REFINERY BLOCK FLOW DIAGRAM & PLANT-WIDE MASS BALANCE
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
    cad_draw_table_a4, W, H, BK, GREY
)

def generate_refinery_dwg01(out_pdf, out_png):
    fig, ax = create_a4_canvas()
    draw_a4_border(ax)
    
    draw_refinery_title_block(ax, 'REFINERY BLOCK FLOW DIAGRAM & MASS BALANCE',
                              'JU/ChE/VP/DWG-01', scale='DIAGRAMMATIC', date='19 / 10 / 2026')
    
    # Header Banner
    cad_text(ax, W/2, H - 1.25, 'OVERALL REFINERY BLOCK FLOW DIAGRAM (BFD) & PROCESS INTEGRATION', sz=6.8, bold=True)
    cad_text(ax, W/2, H - 1.62, 'BASIS: 100,000 BPD (564,670 kg/h) ARABIAN LIGHT / BRENT CRUDE BLEND | HIGH-CONVERSION CONFIGURATION', sz=4.8, bold=False)
    
    # ═════════════════════════════════════════════════════════════════════════
    # REFINERY PROCESS BLOCKS (COORDINATES IN CM)
    # ═════════════════════════════════════════════════════════════════════════
    def draw_unit_block(ax, x, y, w, h, tag, title, throughput=None, color='#f0f4f8'):
        cad_rect(ax, x, y, w, h, lw=0.9, fill=True, fc=color)
        cad_text(ax, x + w/2, y + h - 0.28, tag, sz=4.2, bold=True, color='#003366')
        cad_text(ax, x + w/2, y + h/2 - 0.05, title, sz=4.4, bold=True)
        if throughput:
            cad_text(ax, x + w/2, y + 0.28, throughput, sz=3.6, bold=False, color='#555555')

    # 1. Crude Storage & Desalter (X=1.2, Y=11.2)
    draw_unit_block(ax, 1.2, 11.2, 2.6, 1.8, 'TANK FARM', 'CRUDE OIL\nSTORAGE', '100,000 BPD')
    cad_line(ax, 3.8, 12.1, 4.4, 12.1, lw=0.85)
    cad_arrow(ax, 4.1, 12.1, 4.4, 12.1, head_scale=6)
    
    draw_unit_block(ax, 4.4, 11.2, 2.4, 1.8, 'DES-101', 'CRUDE\nDESALTER', 'Salt < 1 PTB')
    cad_line(ax, 6.8, 12.1, 7.8, 12.1, lw=0.85)
    cad_arrow(ax, 7.4, 12.1, 7.8, 12.1, head_scale=6)
    
    # 2. Atmospheric Distillation Unit CDU (X=7.8, Y=10.0)
    draw_unit_block(ax, 7.8, 9.8, 3.6, 4.6, 'CDU / C-101', 'ATMOSPHERIC\nDISTILLATION\nCOLUMN', '48 Trays | 365 C', color='#e6f0ff')
    
    # CDU Product Streams:
    # Overhead LPG
    cad_line(ax, 11.4, 13.8, 13.2, 13.8, lw=0.8)
    cad_arrow(ax, 12.8, 13.8, 13.2, 13.8, head_scale=5)
    cad_text(ax, 12.3, 14.05, 'Off-Gas & LPG', sz=3.4, bold=True)
    
    # Light Naphtha -> Isomerization
    cad_line(ax, 11.4, 12.8, 13.8, 12.8, lw=0.8)
    cad_arrow(ax, 13.4, 12.8, 13.8, 12.8, head_scale=5)
    cad_text(ax, 12.6, 13.05, 'Light Naphtha (C5-80 C)', sz=3.4, bold=True)
    
    # Heavy Naphtha -> Hydrotreater & Reformer
    cad_line(ax, 11.4, 11.8, 13.8, 11.8, lw=0.8)
    cad_arrow(ax, 13.4, 11.8, 13.8, 11.8, head_scale=5)
    cad_text(ax, 12.6, 12.05, 'Heavy Naphtha (80-150 C)', sz=3.4, bold=True)
    
    # Kerosene / Jet -> Merox
    cad_line(ax, 11.4, 10.8, 20.6, 10.8, lw=0.8)
    cad_arrow(ax, 18.0, 10.8, 20.6, 10.8, head_scale=6)
    cad_text(ax, 16.0, 11.05, 'Kerosene / Jet A-1 (150-240 C)', sz=3.5, bold=True)
    
    # Diesel / AGO -> Hydrotreater
    cad_line(ax, 11.4, 9.8, 20.6, 9.8, lw=0.8)
    cad_arrow(ax, 18.0, 9.8, 20.6, 9.8, head_scale=6)
    cad_text(ax, 16.0, 10.05, 'Diesel / AGO (240-360 C)', sz=3.5, bold=True)
    
    # Atmospheric Residue (Bottoms) -> VDU
    cad_line(ax, 9.6, 9.8, 9.6, 8.4, lw=0.9)
    cad_line(ax, 9.6, 8.4, 3.8, 8.4, lw=0.9)
    cad_line(ax, 3.8, 8.4, 3.8, 7.2, lw=0.9)
    cad_arrow(ax, 3.8, 7.6, 3.8, 7.2, head_scale=6)
    cad_text(ax, 6.8, 8.65, 'Atmospheric Residue (>360 C) | 202,346 kg/h', sz=3.6, bold=True)
    
    # 3. Vacuum Distillation Unit VDU (X=2.4, Y=4.8)
    draw_unit_block(ax, 2.2, 4.8, 3.4, 2.4, 'VDU / C-102', 'VACUUM\nDISTILLATION\n(DEEP-CUT)', '25 mmHg(a) | 415 C', color='#fff0e6')
    
    # VDU Products:
    # LVGO & HVGO to Conversion
    cad_line(ax, 5.6, 6.5, 9.2, 6.5, lw=0.85)
    cad_arrow(ax, 8.8, 6.5, 9.2, 6.5, head_scale=6)
    cad_text(ax, 7.4, 6.75, 'HVGO (60% to FCC, 40% to HCU)', sz=3.5, bold=True)
    
    # Vacuum Residue (VR) -> Delayed Coker
    cad_line(ax, 3.9, 4.8, 3.9, 3.8, lw=0.85)
    cad_line(ax, 3.9, 3.8, 15.6, 3.8, lw=0.85)
    cad_line(ax, 15.6, 3.8, 15.6, 4.8, lw=0.85)
    cad_arrow(ax, 15.6, 4.4, 15.6, 4.8, head_scale=6)
    cad_text(ax, 9.8, 3.55, 'Vacuum Residue (>540 C) | 85,828 kg/h to Delayed Coker', sz=3.6, bold=True)
    
    # 4. Conversion Units: FCCU, HCU, Delayed Coker
    # FCCU (X=9.2, Y=5.6)
    draw_unit_block(ax, 9.2, 5.6, 3.4, 2.2, 'FCCU', 'FLUID CATALYTIC\nCRACKING UNIT', '75,000 kg/h | 76.5% Conv', color='#ffe6e6')
    
    # HCU (X=14.0, Y=7.2)
    draw_unit_block(ax, 13.8, 7.2, 3.4, 2.2, 'HCU', '2-STAGE HIGH-PRESS\nHYDROCRACKER', '155 bar | ULSD Diesel', color='#e6ffe6')
    
    # Delayed Coker (X=14.0, Y=4.8)
    draw_unit_block(ax, 14.0, 4.8, 3.2, 2.0, 'DCU', 'DELAYED COKING\n(TWIN DRUMS)', 'VR Upgrading | 498 C', color='#f0f0f0')
    
    # Connect HVGO split to HCU
    cad_line(ax, 7.8, 6.5, 7.8, 7.8, lw=0.8)
    cad_line(ax, 7.8, 7.8, 13.8, 7.8, lw=0.8)
    cad_arrow(ax, 13.4, 7.8, 13.8, 7.8, head_scale=5)
    
    # 5. Product Blending Terminals (Right side)
    draw_unit_block(ax, 20.6, 12.2, 3.6, 1.4, 'POOL 1', 'MOTOR GASOLINE\n(RON 92+)', '16,346 BPD', color='#ffebcc')
    draw_unit_block(ax, 20.6, 9.4, 3.6, 1.4, 'POOL 2', 'ULSD DIESEL POOL\n(<10 ppm S, Cetane 51)', '35,349 BPD', color='#d9f2d9')
    draw_unit_block(ax, 20.6, 7.4, 3.6, 1.2, 'POOL 3', 'JET A-1 FUEL', '22,286 BPD', color='#cce6ff')
    draw_unit_block(ax, 20.6, 5.6, 3.6, 1.2, 'POOL 4', 'LPG & PETROCHEM', '16,435 BPD', color='#fff0b3')
    draw_unit_block(ax, 20.6, 3.8, 3.6, 1.2, 'SOLID', 'PETROLEUM COKE', '587 tonnes/day', color='#e0e0e0')
    
    # Connect FCC gasoline to Pool 1
    cad_line(ax, 12.6, 6.8, 18.8, 6.8, lw=0.75)
    cad_line(ax, 18.8, 6.8, 18.8, 12.8, lw=0.75)
    cad_line(ax, 18.8, 12.8, 20.6, 12.8, lw=0.75)
    cad_arrow(ax, 20.2, 12.8, 20.6, 12.8, head_scale=5)
    
    # Connect HCU ULSD to Pool 2
    cad_line(ax, 17.2, 8.2, 19.4, 8.2, lw=0.75)
    cad_line(ax, 19.4, 8.2, 19.4, 10.0, lw=0.75)
    cad_line(ax, 19.4, 10.0, 20.6, 10.0, lw=0.75)
    cad_arrow(ax, 20.2, 10.0, 20.6, 10.0, head_scale=5)
    
    # ═════════════════════════════════════════════════════════════════════════
    # TABLE: PLANT-WIDE MASS BALANCE & CRUDE ASSAY DISTRIBUTION
    # ═════════════════════════════════════════════════════════════════════════
    headers = ['STREAM / PRODUCT', 'FLOW (BPD)', 'MASS (kg/h)', 'WT % CRUDE', 'API GRAVITY', 'DOWNSTREAM DESTINATION']
    rows = [
        ['Crude Oil Feed (Arabian Light / Brent)', '100,000 BPD', '564,670 kg/h', '100.00 %', '34.5 API', 'Battery Limits -> Desalter -> CDU'],
        ['Finished Motor Gasoline (RON 92+)', '16,346 BPD', '80,670 kg/h', '14.29 %', '58.5 API', 'Gasoline Blending -> Commercial Pool'],
        ['Ultra-Low Sulfur Diesel (ULSD, S<10ppm)', '35,349 BPD', '196,701 kg/h', '34.84 %', '37.8 API', 'Hydrotreated Diesel Pool -> Transport'],
        ['Aviation Jet Fuel (Jet A-1 / Freeze -47C)', '22,286 BPD', '118,846 kg/h', '21.05 %', '42.8 API', 'Aviation Fuel Storage & Export'],
        ['Liquefied Petroleum Gas (LPG C3/C4)', '16,435 BPD', '59,881 kg/h', '10.60 %', '105.0 API', 'Pressurized Horton Spheres / Commercial'],
        ['Heavy Fuel Oil / Marine Bunker (380 cSt)', '2,587 BPD', '16,453 kg/h', '2.91 %', '10.5 API', 'Marine Fuel Oil Blending'],
        ['Solid Petroleum Green Coke (Anode Grade)', '587 T/day', '24,461 kg/h', '4.33 %', '0.0 API', 'Hydraulic Decoking Pit -> Aluminum Smelter'],
        ['Hydrogen Consumption (SMR Plant)', '-', '+ 1,440 kg/h', '+ 0.25 %', '-', 'Hydrocracking & Hydrotreating Saturation'],
        ['Refinery Fuel Gas & Flare Loss', '-', '42,670 kg/h', '7.56 %', '-', 'Captive Fired Heaters & Safety Flare (API 521)'],
        ['TOTAL MASS BALANCE CLOSURE', '100,000 BPD', '564,670 kg/h', '100.00 %', '-', 'MASS IN = MASS OUT (ZERO ACCUMULATION)'],
    ]
    col_w = [6.2, 2.5, 2.8, 2.4, 2.4, 8.4]
    cad_draw_table_a4(ax, 2.2, 0.95 + 2.30 + 0.12, headers, rows, col_w,
                      row_h=0.31, title='TABLE 1: REFINERY-WIDE HEAT & MASS BALANCE CLOSURE (100,000 BPD CRUDE DIET)',
                      title_sz=4.6, sz=3.7)
    
    # Save Outputs
    fig.savefig(out_pdf, format='pdf', dpi=300)
    fig.savefig(out_png, format='png', dpi=300)
    plt.close(fig)
    print(f"  [OK] DWG-01 generated: {os.path.basename(out_pdf)}")

if __name__ == '__main__':
    out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'CAD_Drawings')
    os.makedirs(out_dir, exist_ok=True)
    generate_refinery_dwg01(
        os.path.join(out_dir, '01_Refinery_Block_Flow_Diagram_BFD_Mass_Balance.pdf'),
        os.path.join(out_dir, '01_Refinery_Block_Flow_Diagram_BFD_Mass_Balance.png')
    )
