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
    # REFINERY PROCESS BLOCKS (UPPER REGION: Y = 8.4 to 18.8 cm)
    # STRICT BOUNDARY: NO EQUIPMENT OR FLOW LINES BELOW Y = 8.3 cm
    # ═════════════════════════════════════════════════════════════════════════
    def draw_unit_block(ax, x, y, w, h, tag, title, throughput=None, color='#f0f4f8'):
        cad_rect(ax, x, y, w, h, lw=0.9, fill=True, fc=color)
        cad_text(ax, x + w/2, y + h - 0.28, tag, sz=4.2, bold=True, color='#003366')
        cad_text(ax, x + w/2, y + h/2 - 0.05, title, sz=4.3, bold=True)
        if throughput:
            cad_text(ax, x + w/2, y + 0.28, throughput, sz=3.5, bold=False, color='#555555')

    # 1. Crude Storage & Desalter
    draw_unit_block(ax, 1.2, 14.6, 2.4, 2.2, 'TANK FARM', 'CRUDE OIL\nSTORAGE', '100,000 BPD')
    cad_line(ax, 3.6, 15.7, 4.4, 15.7, lw=0.85)
    cad_arrow(ax, 4.0, 15.7, 4.4, 15.7, head_scale=6)
    
    draw_unit_block(ax, 4.4, 14.6, 2.3, 2.2, 'DES-101', 'CRUDE\nDESALTER', 'Salt < 1 PTB')
    cad_line(ax, 6.7, 15.7, 7.6, 15.7, lw=0.85)
    cad_arrow(ax, 7.2, 15.7, 7.6, 15.7, head_scale=6)
    
    # 2. Atmospheric Distillation Unit CDU (X=7.6, Y=12.2)
    draw_unit_block(ax, 7.6, 12.2, 3.4, 4.8, 'CDU / C-101', 'ATMOSPHERIC\nDISTILLATION\nCOLUMN', '48 Trays | 365 C', color='#e6f0ff')
    
    # CDU Product Streams:
    # A. Overhead LPG -> Pool 4
    cad_line(ax, 11.0, 16.4, 22.0, 16.4, lw=0.8)
    cad_arrow(ax, 21.6, 16.4, 22.0, 16.4, head_scale=5)
    cad_text(ax, 16.5, 16.65, 'Off-Gas & LPG (39,858 kg/h)', sz=3.3, bold=True)
    
    # B. Light Naphtha -> Isomerization Unit
    cad_line(ax, 11.0, 15.2, 12.6, 15.2, lw=0.8)
    cad_arrow(ax, 12.2, 15.2, 12.6, 15.2, head_scale=5)
    cad_text(ax, 11.8, 15.45, 'Lt Naphtha', sz=3.2, bold=True)
    draw_unit_block(ax, 12.6, 14.5, 2.6, 1.4, 'ISOM', 'ISOMERIZATION', 'RON 88 Isomerate', color='#fff9e6')
    cad_line(ax, 15.2, 15.2, 22.0, 15.2, lw=0.8)
    cad_arrow(ax, 21.6, 15.2, 22.0, 15.2, head_scale=5)
    
    # C. Heavy Naphtha -> NHT + CCR Platformer (Catalytic Reformer)
    cad_line(ax, 11.0, 14.0, 12.6, 14.0, lw=0.8)
    cad_arrow(ax, 12.2, 14.0, 12.6, 14.0, head_scale=5)
    cad_text(ax, 11.8, 14.25, 'Hvy Naphtha', sz=3.2, bold=True)
    draw_unit_block(ax, 12.6, 12.8, 2.6, 1.4, 'CCR', 'CAT REFORMER\n(PLATFORMER)', 'RON 102 Reformate', color='#fff0f5')
    cad_line(ax, 15.2, 13.5, 22.0, 13.5, lw=0.8)
    cad_arrow(ax, 21.6, 13.5, 22.0, 13.5, head_scale=5)
    cad_text(ax, 18.6, 13.75, 'Reformate (58,798 kg/h)', sz=3.3, bold=True)
    
    # D. Kerosene / Jet -> Merox -> Jet Pool
    cad_line(ax, 11.0, 12.8, 11.6, 12.8, lw=0.8)
    cad_line(ax, 11.6, 12.8, 11.6, 11.6, lw=0.8)
    cad_line(ax, 11.6, 11.6, 22.0, 11.6, lw=0.8)
    cad_arrow(ax, 21.6, 11.6, 22.0, 11.6, head_scale=5)
    cad_text(ax, 16.8, 11.85, 'Kerosene / Jet A-1 (101,220 kg/h)', sz=3.3, bold=True)
    
    # E. Diesel / AGO -> Hydrotreater -> Diesel Pool
    cad_line(ax, 11.0, 12.2, 11.2, 12.2, lw=0.8)
    cad_line(ax, 11.2, 12.2, 11.2, 9.8, lw=0.8)
    cad_line(ax, 11.2, 9.8, 22.0, 9.8, lw=0.8)
    cad_arrow(ax, 21.6, 9.8, 22.0, 9.8, head_scale=5)
    cad_text(ax, 16.8, 10.05, 'Straight-Run Diesel / AGO (123,012 kg/h)', sz=3.3, bold=True)
    
    # F. Atmospheric Residue -> VDU
    cad_line(ax, 9.3, 12.2, 9.3, 11.0, lw=0.9)
    cad_line(ax, 9.3, 11.0, 3.4, 11.0, lw=0.9)
    cad_line(ax, 3.4, 11.0, 3.4, 9.8, lw=0.9)
    cad_arrow(ax, 3.4, 10.2, 3.4, 9.8, head_scale=6)
    cad_text(ax, 6.4, 11.25, 'Atmospheric Residue (>360 C) | 202,346 kg/h', sz=3.4, bold=True)
    
    # 3. Vacuum Distillation Unit VDU (X=2.0, Y=8.6)
    draw_unit_block(ax, 2.0, 8.5, 2.8, 2.0, 'VDU / C-102', 'VACUUM TOWER\n(DEEP-CUT)', '25 mmHg | 415 C', color='#fff0e6')
    
    # VDU Product Streams:
    # LVGO & HVGO Split to FCCU & HCU
    cad_line(ax, 4.8, 9.8, 6.0, 9.8, lw=0.85)
    cad_line(ax, 6.0, 9.8, 6.0, 10.2, lw=0.85)
    cad_line(ax, 6.0, 10.2, 16.0, 10.2, lw=0.85)
    
    # Vacuum Residue -> Delayed Coker
    cad_line(ax, 3.4, 8.5, 3.4, 8.45, lw=0.85)
    cad_line(ax, 3.4, 8.45, 16.0, 8.45, lw=0.85)
    cad_arrow(ax, 15.6, 8.45, 16.0, 8.45, head_scale=5)
    cad_text(ax, 9.5, 8.65, 'Vacuum Residue (>540 C) | 85,828 kg/h to DCU', sz=3.3, bold=True)
    
    # 4. Conversion Units: FCCU, HCU, Delayed Coker
    # FCCU
    draw_unit_block(ax, 16.0, 14.2, 3.4, 1.8, 'FCCU', 'FLUID CATALYTIC\nCRACKING', '54,414 kg/h Feed', color='#ffe6e6')
    cad_line(ax, 10.2, 10.2, 10.2, 14.8, lw=0.8)
    cad_line(ax, 10.2, 14.8, 16.0, 14.8, lw=0.8)
    cad_arrow(ax, 15.6, 14.8, 16.0, 14.8, head_scale=5)
    # FCC to Gasoline
    cad_line(ax, 19.4, 15.0, 22.0, 15.0, lw=0.75)
    cad_arrow(ax, 21.6, 15.0, 22.0, 15.0, head_scale=5)
    
    # HCU
    draw_unit_block(ax, 16.0, 10.8, 3.4, 1.8, 'HCU', '2-STAGE HIGH-PRESS\nHYDROCRACKER', '155 bar | 62,105 kg/h', color='#e6ffe6')
    cad_line(ax, 12.0, 10.2, 12.0, 11.4, lw=0.8)
    cad_line(ax, 12.0, 11.4, 16.0, 11.4, lw=0.8)
    cad_arrow(ax, 15.6, 11.4, 16.0, 11.4, head_scale=5)
    # HCU to ULSD
    cad_line(ax, 19.4, 11.4, 20.6, 11.4, lw=0.75)
    cad_line(ax, 20.6, 11.4, 20.6, 9.6, lw=0.75)
    cad_line(ax, 20.6, 9.6, 22.0, 9.6, lw=0.75)
    cad_arrow(ax, 21.6, 9.6, 22.0, 9.6, head_scale=5)
    
    # Delayed Coker (DCU)
    draw_unit_block(ax, 16.0, 8.4, 3.4, 1.6, 'DCU', 'DELAYED COKING\n(TWIN DRUMS)', 'VR Upgrading | 498 C', color='#f0f0f0')
    
    # 5. Product Blending Pools (Right side: X=22.0, Y=8.4 to 17.5)
    draw_unit_block(ax, 22.0, 14.8, 5.8, 1.4, 'POOL 1', 'MOTOR GASOLINE (RON 92+)', '28,132 BPD | 138,840 kg/h', color='#ffebcc')
    draw_unit_block(ax, 22.0, 13.0, 5.8, 1.4, 'POOL 4', 'LPG & PETROCHEM (C3/C4)', '15,614 BPD | 56,889 kg/h', color='#fff0b3')
    draw_unit_block(ax, 22.0, 11.2, 5.8, 1.4, 'POOL 3', 'JET A-1 FUEL (Freeze -47 C)', '22,426 BPD | 118,846 kg/h', color='#cce6ff')
    draw_unit_block(ax, 22.0, 9.4, 5.8, 1.4, 'POOL 2', 'ULSD DIESEL (<10 ppm S, Cetane 51)', '35,561 BPD | 196,701 kg/h', color='#d9f2d9')
    draw_unit_block(ax, 22.0, 8.2, 2.7, 0.9, 'POOL 5', 'BUNKER OIL', '16,453 kg/h', color='#e0e0e0')
    draw_unit_block(ax, 25.1, 8.2, 2.7, 0.9, 'SOLID', 'PET COKE', '587.1 T/day', color='#d0d0d0')
    
    # ═════════════════════════════════════════════════════════════════════════
    # TABLE: PLANT-WIDE MASS BALANCE (RIGOROUS 100.000% CLOSURE)
    # POSITIONED IN DEDICATED LOWER ZONE: Y = 3.3 to 7.9 cm | ZERO COLLISION
    # ═════════════════════════════════════════════════════════════════════════
    headers = ['STREAM / PRODUCT POOL', 'VOL (BPD)', 'MASS (kg/h)', 'WT % CRUDE', 'API / SPEC', 'REFINERY UNIT ORIGIN / DISPOSITION']
    rows = [
        ['Crude Oil Feed (Arabian Light / Brent)', '100,000 BPD', '564,670 kg/h', '100.000 %', '34.5 API', 'Battery Limits -> Desalter -> Atmospheric CDU (C-101)'],
        ['1. Finished Motor Gasoline (Euro-V)', '28,132 BPD', '138,840 kg/h', '24.588 %', 'RON 91.7', 'Isom + CCR Reformate + FCC Naphtha + HCU Naphtha'],
        ['2. Ultra-Low Sulfur Diesel (ULSD)', '35,561 BPD', '196,701 kg/h', '34.835 %', 'Cetane 50.9', 'CDU Diesel + HCU ULSD + FCC LCO + Coker LCGO (<10 ppm S)'],
        ['3. Aviation Jet Fuel (Jet A-1)', '22,426 BPD', '118,846 kg/h', '21.047 %', '42.8 API', 'CDU Merox Kerosene (101,220) + HCU Jet (17,489)'],
        ['4. LPG & Petrochem Feedstock (C3/C4)', '15,614 BPD', '56,889 kg/h', '10.075 %', '105.0 API', 'CDU LPG + Isom LPG + Reformer LPG + FCC/HCU Gas'],
        ['5. Heavy Fuel Oil / Bunker (380 cSt)', '2,587 BPD', '16,453 kg/h', '2.914 %', '10.5 API', 'FCC Clarified Slurry (2,721) + Coker HCGO (13,732)'],
        ['6. Solid Petroleum Green Coke', '587.1 T/d', '24,461 kg/h', '4.332 %', '0.0 API', 'Delayed Coking Unit (DCU) -> Aluminum Anode Pit'],
        ['7. Captive Process Fuel Gas (C1/C2)', '-', '9,634 kg/h', '1.706 %', '-', 'CCR Reformer Fuel Gas (2,339) + Coker Offgas (7,296)'],
        ['8. Coke Burnoff in FCC Regenerator', '-', '2,829 kg/h', '0.501 %', '-', 'USY Zeolite Catalyst Decoking -> CO2/CO Flue Gas'],
        ['9. Heteroatoms (H2S / Desalter Salt)', '-', '17 kg/h', '0.003 %', '-', 'Claus Sulfur Plant + Desalter Brine Effluent'],
        ['TOTAL MASS BALANCE CLOSURE', '104,227 BPD', '564,670 kg/h', '100.000 %', '-', 'EXACT MASS IN = MASS OUT (ZERO ACCUMULATION: 100.000%)'],
    ]
    col_w = [6.2, 2.6, 2.8, 2.4, 2.4, 10.0]  # Sum = 26.4 cm (Starts at X=1.4, ends at X=27.8 cm <= 28.1 cm)
    
    cad_draw_table_a4(ax, 1.4, 3.40, headers, rows, col_w,
                      row_h=0.34, title='TABLE 1: RIGOROUS PLANT-WIDE HEAT & MASS BALANCE CLOSURE (100,000 BPD CRUDE DIET)',
                      title_sz=4.6, sz=3.6)
    
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
