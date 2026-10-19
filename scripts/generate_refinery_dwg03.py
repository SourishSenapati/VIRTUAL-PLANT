"""
A4 OPTIMIZED: DWG-03 FCCU, HYDROCRACKER & DELAYED COKER CONVERSION FLOWSHEET
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
    cad_draw_table_a4, cad_valve, W, H, BK, GREY
)

def generate_refinery_dwg03(out_pdf, out_png):
    fig, ax = create_a4_canvas()
    draw_a4_border(ax)
    
    draw_refinery_title_block(ax, 'FCCU, HYDROCRACKER & DELAYED COKER CONVERSION FLOWSHEET',
                              'JU/ChE/VP/DWG-03', scale='DIAGRAMMATIC', date='19 / 10 / 2026')
    
    # Header Banner
    cad_text(ax, W/2, H - 1.25, 'HEAVY-END UPGRADING & CONVERSION FLOWSHEETS: FCCU, HCU & DELAYED COKER', sz=6.8, bold=True)
    cad_text(ax, W/2, H - 1.62, 'DETAILED CATALYTIC & THERMAL CRACKING ARCHITECTURES | RISER KINETICS, HYDROGEN BALANCE & DRUM CYCLES', sz=4.8, bold=False)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 1: FLUID CATALYTIC CRACKING UNIT (FCCU - U-300) [LEFT REGION]
    # ═════════════════════════════════════════════════════════════════════════
    # Box Boundary
    cad_rect(ax, 1.2, 8.6, 8.8, 10.4, lw=0.7, fill=True, fc='#fafbfc')
    cad_text(ax, 5.6, 18.65, 'FLUID CATALYTIC CRACKING UNIT (FCCU - U-300)', sz=5.2, bold=True, color='#003366')
    cad_text(ax, 5.6, 18.30, 'Feed: 30,000 BPD HVGO/LVGO | Catalyst: USY Zeolite | Riser: 535 C, 2.5 bar', sz=3.8, bold=False, color='#555555')
    
    # Regenerator (R-302)
    reg_x, reg_y, reg_w, reg_h = 2.0, 11.6, 2.4, 4.4
    cad_rect(ax, reg_x, reg_y, reg_w, reg_h, lw=0.9, fill=True, fc='#fff5eb')
    # Regenerator heads
    ax.add_patch(Arc((reg_x + reg_w/2, reg_y + reg_h), reg_w, 0.9, theta1=0, theta2=180, ec=BK, lw=0.9))
    ax.add_patch(Arc((reg_x + reg_w/2, reg_y), reg_w, 0.9, theta1=180, theta2=360, ec=BK, lw=0.9))
    cad_text(ax, reg_x + reg_w/2, reg_y + reg_h/2 + 0.9, 'REGENERATOR', sz=4.5, bold=True)
    cad_text(ax, reg_x + reg_w/2, reg_y + reg_h/2 + 0.45, 'R-302', sz=4.0, bold=True)
    cad_text(ax, reg_x + reg_w/2, reg_y + reg_h/2, '710 C | 2.8 bar', sz=3.6)
    cad_text(ax, reg_x + reg_w/2, reg_y + reg_h/2 - 0.45, 'Air Combustion', sz=3.4, color='#774400')
    cad_text(ax, reg_x + reg_w/2, reg_y + reg_h/2 - 0.85, 'Coke Burnoff 4.8%', sz=3.4, color='#774400')
    
    # Air Blower stream into Regenerator
    cad_line(ax, 1.4, 11.2, reg_x + 0.4, 11.2, lw=0.75)
    cad_line(ax, reg_x + 0.4, 11.2, reg_x + 0.4, reg_y, lw=0.75)
    cad_arrow(ax, reg_x + 0.4, 11.4, reg_x + 0.4, reg_y, head_scale=5)
    cad_text(ax, 1.7, 10.95, 'Air Blast (Blower)', sz=3.3, bold=True)
    
    # Flue Gas to Power Recovery & CO Boiler
    cad_line(ax, reg_x + reg_w/2, reg_y + reg_h + 0.45, reg_x + reg_w/2, 17.5, lw=0.75)
    cad_line(ax, reg_x + reg_w/2, 17.5, 1.5, 17.5, lw=0.75)
    cad_arrow(ax, 1.8, 17.5, 1.4, 17.5, head_scale=5)
    cad_text(ax, 2.4, 17.75, 'Flue Gas to Expander & CO Boiler', sz=3.3, bold=True)
    
    # FCC Riser & Reactor Disengager (R-301)
    rx_x, rx_y, rx_w, rx_h = 6.0, 13.0, 2.2, 3.2
    cad_rect(ax, rx_x, rx_y, rx_w, rx_h, lw=0.9, fill=True, fc='#f0f9ff')
    ax.add_patch(Arc((rx_x + rx_w/2, rx_y + rx_h), rx_w, 0.8, theta1=0, theta2=180, ec=BK, lw=0.9))
    ax.add_patch(Arc((rx_x + rx_w/2, rx_y), rx_w, 0.8, theta1=180, theta2=360, ec=BK, lw=0.9))
    cad_text(ax, rx_x + rx_w/2, rx_y + rx_h/2 + 0.5, 'REACTOR /', sz=4.2, bold=True)
    cad_text(ax, rx_x + rx_w/2, rx_y + rx_h/2 + 0.1, 'DISENGAGER', sz=4.2, bold=True)
    cad_text(ax, rx_x + rx_w/2, rx_y + rx_h/2 - 0.35, 'R-301', sz=4.0, bold=True)
    cad_text(ax, rx_x + rx_w/2, rx_y + rx_h/2 - 0.75, 'Stripper Section', sz=3.4, color='#004488')
    
    # Riser Tube (slender vertical tube coming from bottom up to disengager)
    riser_x = 6.4
    cad_line(ax, riser_x, 9.4, riser_x, rx_y, lw=1.2, color='#003366')
    cad_line(ax, riser_x + 0.4, 9.4, riser_x + 0.4, rx_y, lw=1.2, color='#003366')
    cad_text(ax, riser_x + 0.2, 10.6, 'RISER (38m)', sz=3.5, bold=True, rotation=90, bg='white')
    
    # Feed injection into Riser (HVGO Feed)
    cad_line(ax, 5.0, 9.8, riser_x, 9.8, lw=0.85)
    cad_arrow(ax, 5.8, 9.8, riser_x, 9.8, head_scale=5)
    cad_text(ax, 4.6, 10.05, 'HVGO Feed (315 C)', sz=3.3, bold=True)
    
    # Regenerated Catalyst Slide Valve & Line (Regenerator -> Riser Bottom)
    cad_line(ax, reg_x + reg_w - 0.2, reg_y + 0.2, 5.8, 9.4, lw=0.85, ls='--')
    cad_line(ax, 5.8, 9.4, riser_x, 9.4, lw=0.85)
    cad_valve(ax, 5.3, 9.6, orientation='H', size=0.28, valve_type='CONTROL')
    cad_text(ax, 4.6, 9.2, 'Regen Cat (710 C)', sz=3.2, bold=True)
    
    # Spent Catalyst Line (Reactor Stripper -> Regenerator)
    cad_line(ax, rx_x + 0.3, rx_y - 0.4, 4.0, 11.0, lw=0.85, ls='--')
    cad_line(ax, 4.0, 11.0, reg_x + reg_w, 12.4, lw=0.85)
    cad_arrow(ax, 4.2, 11.2, reg_x + reg_w, 12.4, head_scale=5)
    cad_valve(ax, 4.6, 11.4, orientation='H', size=0.28, valve_type='CONTROL')
    cad_text(ax, 5.2, 11.8, 'Spent Cat (510 C)', sz=3.2, bold=True)
    
    # Cracked Hydrocarbon Vapors to Main Fractionator
    cad_line(ax, rx_x + rx_w/2, rx_y + rx_h + 0.4, rx_x + rx_w/2, 17.5, lw=0.85)
    cad_line(ax, rx_x + rx_w/2, 17.5, 9.5, 17.5, lw=0.85)
    cad_arrow(ax, 9.1, 17.5, 9.5, 17.5, head_scale=5)
    cad_text(ax, 8.0, 17.75, 'Cracked Vapors to Fractionator', sz=3.3, bold=True)
    
    # FCC 4-Lump Kinetics Summary Box
    cad_rect(ax, 1.4, 8.8, 8.4, 0.55, lw=0.5, fill=True, fc='#ffffff')
    cad_text(ax, 5.6, 9.07, '4-Lump Kinetic Model: VGO -> Gaso (51.2%) + Gas (18.6%) + LCO (18.2%) + Coke (4.8%)', sz=3.4, bold=True)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 2: TWO-STAGE HYDROCRACKER (HCU - U-400) [MIDDLE REGION]
    # ═════════════════════════════════════════════════════════════════════════
    cad_rect(ax, 10.4, 8.6, 9.4, 10.4, lw=0.7, fill=True, fc='#fafbfc')
    cad_text(ax, 15.1, 18.65, 'TWO-STAGE HYDROCRACKER COMPLEX (HCU - U-400)', sz=5.2, bold=True, color='#003366')
    cad_text(ax, 15.1, 18.30, 'Feed: 25,000 BPD HVGO/HCGO | Pressure: 155 bar | Temp: 390-410 C | H2 Cons: 2.4 wt%', sz=3.8, bold=False, color='#555555')
    
    # Stage 1 Reactor: Hydrotreating (R-401)
    r1_x, r1_y, r1_w, r1_h = 10.8, 12.6, 2.0, 4.4
    cad_rect(ax, r1_x, r1_y, r1_w, r1_h, lw=0.9, fill=True, fc='#eef9f2')
    ax.add_patch(Arc((r1_x + r1_w/2, r1_y + r1_h), r1_w, 0.7, theta1=0, theta2=180, ec=BK, lw=0.9))
    ax.add_patch(Arc((r1_x + r1_w/2, r1_y), r1_w, 0.7, theta1=180, theta2=360, ec=BK, lw=0.9))
    cad_text(ax, r1_x + r1_w/2, r1_y + r1_h/2 + 0.8, 'STAGE 1', sz=4.2, bold=True)
    cad_text(ax, r1_x + r1_w/2, r1_y + r1_h/2 + 0.4, 'HYDROTREATER', sz=4.0, bold=True)
    cad_text(ax, r1_x + r1_w/2, r1_y + r1_h/2, 'R-401', sz=4.0, bold=True)
    cad_text(ax, r1_x + r1_w/2, r1_y + r1_h/2 - 0.4, 'NiMo / Al2O3', sz=3.4)
    cad_text(ax, r1_x + r1_w/2, r1_y + r1_h/2 - 0.8, 'HDN & HDS', sz=3.4, color='#006622')
    cad_text(ax, r1_x + r1_w/2, r1_y + r1_h/2 - 1.2, 'N < 10 ppm', sz=3.4, color='#006622')
    
    # Feed + H2 to R-401
    cad_line(ax, 10.6, 17.5, r1_x + r1_w/2, 17.5, lw=0.85)
    cad_line(ax, r1_x + r1_w/2, 17.5, r1_x + r1_w/2, r1_y + r1_h + 0.35, lw=0.85)
    cad_arrow(ax, r1_x + r1_w/2, 17.2, r1_x + r1_w/2, r1_y + r1_h + 0.35, head_scale=5)
    cad_text(ax, 11.5, 17.75, 'VGO Feed + Treat Gas', sz=3.3, bold=True)
    
    # Interstage Stream R-401 to Stage 2 R-402
    cad_line(ax, r1_x + r1_w/2, r1_y - 0.35, r1_x + r1_w/2, 11.2, lw=0.85)
    cad_line(ax, r1_x + r1_w/2, 11.2, 14.2, 11.2, lw=0.85)
    cad_line(ax, 14.2, 11.2, 14.2, 17.5, lw=0.85)
    cad_line(ax, 14.2, 17.5, 14.8 + 1.0, 17.5, lw=0.85)
    cad_arrow(ax, 15.4, 17.5, 15.8, 17.5, head_scale=5)
    cad_text(ax, 12.8, 11.45, 'Hydrotreated Effluent', sz=3.3, bold=True)
    
    # Stage 2 Reactor: Hydrocracking (R-402)
    r2_x, r2_y, r2_w, r2_h = 14.8, 12.6, 2.0, 4.4
    cad_rect(ax, r2_x, r2_y, r2_w, r2_h, lw=0.9, fill=True, fc='#eef9f2')
    ax.add_patch(Arc((r2_x + r2_w/2, r2_y + r2_h), r2_w, 0.7, theta1=0, theta2=180, ec=BK, lw=0.9))
    ax.add_patch(Arc((r2_x + r2_w/2, r2_y), r2_w, 0.7, theta1=180, theta2=360, ec=BK, lw=0.9))
    cad_text(ax, r2_x + r2_w/2, r2_y + r2_h/2 + 0.8, 'STAGE 2', sz=4.2, bold=True)
    cad_text(ax, r2_x + r2_w/2, r2_y + r2_h/2 + 0.4, 'HYDROCRACKER', sz=4.0, bold=True)
    cad_text(ax, r2_x + r2_w/2, r2_y + r2_h/2, 'R-402', sz=4.0, bold=True)
    cad_text(ax, r2_x + r2_w/2, r2_y + r2_h/2 - 0.4, 'Noble Met / Zeolite', sz=3.4)
    cad_text(ax, r2_x + r2_w/2, r2_y + r2_h/2 - 0.8, 'Multi-Bed Quench', sz=3.4, color='#006622')
    cad_text(ax, r2_x + r2_w/2, r2_y + r2_h/2 - 1.2, '155 bar | 405 C', sz=3.4, color='#006622')
    
    # Cold H2 Quench injection lines
    cad_line(ax, 13.9, 14.5, r2_x, 14.5, lw=0.6, ls=':')
    cad_line(ax, 13.9, 13.5, r2_x, 13.5, lw=0.6, ls=':')
    cad_text(ax, 13.8, 15.0, 'H2 Quench', sz=3.0, bold=True)
    
    # High-Pressure Separator (V-401)
    sep_x, sep_y, sep_w, sep_h = 17.8, 12.0, 1.4, 3.2
    cad_rect(ax, sep_x, sep_y, sep_w, sep_h, lw=0.85, fill=True, fc='#ffffff')
    ax.add_patch(Arc((sep_x + sep_w/2, sep_y + sep_h), sep_w, 0.6, theta1=0, theta2=180, ec=BK, lw=0.85))
    ax.add_patch(Arc((sep_x + sep_w/2, sep_y), sep_w, 0.6, theta1=180, theta2=360, ec=BK, lw=0.85))
    cad_text(ax, sep_x + sep_w/2, sep_y + sep_h/2 + 0.3, 'HP-SEP', sz=3.8, bold=True)
    cad_text(ax, sep_x + sep_w/2, sep_y + sep_h/2 - 0.1, 'V-401', sz=3.6, bold=True)
    cad_text(ax, sep_x + sep_w/2, sep_y + sep_h/2 - 0.5, '150 bar', sz=3.2)
    
    # Line R-402 to Separator
    cad_line(ax, r2_x + r2_w/2, r2_y - 0.35, r2_x + r2_w/2, 11.2, lw=0.85)
    cad_line(ax, r2_x + r2_w/2, 11.2, sep_x + sep_w/2, 11.2, lw=0.85)
    cad_line(ax, sep_x + sep_w/2, 11.2, sep_x + sep_w/2, sep_y - 0.3, lw=0.85)
    cad_arrow(ax, sep_x + sep_w/2, 11.4, sep_x + sep_w/2, sep_y - 0.3, head_scale=5)
    
    # Recycle Hydrogen Compressor (C-401)
    cad_circle(ax, 18.5, 17.0, 0.55, lw=0.85, fill=True, fc='#ffffff')
    cad_text(ax, 18.5, 17.0, 'C-401\nREC H2', sz=3.2, bold=True)
    cad_line(ax, sep_x + sep_w/2, sep_y + sep_h + 0.3, sep_x + sep_w/2, 16.45, lw=0.75)
    cad_arrow(ax, sep_x + sep_w/2, 16.0, sep_x + sep_w/2, 16.45, head_scale=5)
    
    # Liquid from HP Sep to Fractionator
    cad_line(ax, sep_x + sep_w, 12.5, 19.4, 12.5, lw=0.85)
    cad_arrow(ax, 19.1, 12.5, 19.4, 12.5, head_scale=5)
    cad_text(ax, 18.7, 12.2, 'To Fractionator', sz=3.2, bold=True)
    
    # HCU Performance summary box
    cad_rect(ax, 10.6, 8.8, 9.0, 0.55, lw=0.5, fill=True, fc='#ffffff')
    cad_text(ax, 15.1, 9.07, 'Yields: ULSD (48.4%, Cetane 58) | Kero/Jet (24.2%) | Naphtha (18.1%) | UCO Recycle (9.3%)', sz=3.4, bold=True)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 3: DELAYED COKER UNIT (DCU - U-500) [RIGHT REGION]
    # ═════════════════════════════════════════════════════════════════════════
    cad_rect(ax, 20.2, 8.6, 8.3, 10.4, lw=0.7, fill=True, fc='#fafbfc')
    cad_text(ax, 24.3, 18.65, 'DELAYED COKING COMPLEX (DCU - U-500)', sz=5.2, bold=True, color='#003366')
    cad_text(ax, 24.3, 18.30, 'Feed: 18,000 BPD Vacuum Residue | Thermal Cracking: 495 C | Drum Cycle: 24h', sz=3.8, bold=False, color='#555555')
    
    # Coker Furnace (H-501)
    fur_x, fur_y, fur_w, fur_h = 20.6, 10.0, 1.8, 2.2
    cad_rect(ax, fur_x, fur_y, fur_w, fur_h, lw=0.85, fill=True, fc='#fff0e6')
    cad_line(ax, fur_x, fur_y + fur_h, fur_x + fur_w/2, fur_y + fur_h + 0.8, lw=0.85)
    cad_line(ax, fur_x + fur_w, fur_y + fur_h, fur_x + fur_w/2, fur_y + fur_h + 0.8, lw=0.85)
    cad_line(ax, fur_x + fur_w/2 - 0.2, fur_y + fur_h + 0.8, fur_x + fur_w/2 - 0.2, fur_y + fur_h + 1.4, lw=0.85)
    cad_line(ax, fur_x + fur_w/2 + 0.2, fur_y + fur_h + 0.8, fur_x + fur_w/2 + 0.2, fur_y + fur_h + 1.4, lw=0.85)
    cad_text(ax, fur_x + fur_w/2, fur_y + fur_h/2 + 0.2, 'COKER\nHEATER', sz=3.8, bold=True)
    cad_text(ax, fur_x + fur_w/2, fur_y + fur_h/2 - 0.45, 'H-501\n495 C', sz=3.4, bold=True)
    
    # Steam Injection into Coker Furnace Coils
    cad_line(ax, 20.4, 9.4, fur_x + 0.3, 9.4, lw=0.6, ls='--')
    cad_line(ax, fur_x + 0.3, 9.4, fur_x + 0.3, fur_y, lw=0.6)
    cad_text(ax, 21.0, 9.2, 'Velocity Steam (Anti-fouling)', sz=3.0, bold=True)
    
    # Twin Coke Drums (D-501A & D-501B)
    d1_x, d1_y, dw, dh = 23.4, 11.2, 1.8, 5.0
    cad_rect(ax, d1_x, d1_y, dw, dh, lw=0.9, fill=True, fc='#f4ede4')
    ax.add_patch(Arc((d1_x + dw/2, d1_y + dh), dw, 0.8, theta1=0, theta2=180, ec=BK, lw=0.9))
    ax.add_patch(Arc((d1_x + dw/2, d1_y), dw, 0.8, theta1=180, theta2=360, ec=BK, lw=0.9))
    cad_text(ax, d1_x + dw/2, d1_y + dh/2 + 1.2, 'COKE DRUM A', sz=3.8, bold=True)
    cad_text(ax, d1_x + dw/2, d1_y + dh/2 + 0.8, 'D-501A', sz=3.8, bold=True)
    cad_text(ax, d1_x + dw/2, d1_y + dh/2 + 0.3, 'FILLING (24h)', sz=3.6, bold=True, color='#aa2200')
    cad_text(ax, d1_x + dw/2, d1_y + dh/2 - 0.2, '460 C | 2.2 bar', sz=3.3)
    cad_text(ax, d1_x + dw/2, d1_y + dh/2 - 0.7, 'Thermal Cracking', sz=3.2)
    cad_text(ax, d1_x + dw/2, d1_y + dh/2 - 1.2, 'Pet-Coke Accum.', sz=3.2)
    
    d2_x, d2_y = 26.0, 11.2
    cad_rect(ax, d2_x, d2_y, dw, dh, lw=0.9, fill=True, fc='#f4ede4')
    ax.add_patch(Arc((d2_x + dw/2, d2_y + dh), dw, 0.8, theta1=0, theta2=180, ec=BK, lw=0.9))
    ax.add_patch(Arc((d2_x + dw/2, d2_y), dw, 0.8, theta1=180, theta2=360, ec=BK, lw=0.9))
    cad_text(ax, d2_x + dw/2, d2_y + dh/2 + 1.2, 'COKE DRUM B', sz=3.8, bold=True)
    cad_text(ax, d2_x + dw/2, d2_y + dh/2 + 0.8, 'D-501B', sz=3.8, bold=True)
    cad_text(ax, d2_x + dw/2, d2_y + dh/2 + 0.3, 'DECOKING / QUENCH', sz=3.6, bold=True, color='#0044aa')
    cad_text(ax, d2_x + dw/2, d2_y + dh/2 - 0.2, 'Hydraulic Drill 250 bar', sz=3.3)
    cad_text(ax, d2_x + dw/2, d2_y + dh/2 - 0.7, 'Steam Out & Water Fill', sz=3.2)
    cad_text(ax, d2_x + dw/2, d2_y + dh/2 - 1.2, 'Anode Grade Coke', sz=3.2)
    
    # 4-Way Switch Valve
    cad_circle(ax, 24.2, 10.4, 0.35, lw=0.85, fill=True, fc='#ffffff')
    cad_text(ax, 24.2, 10.4, '4-WAY\nVALVE', sz=3.0, bold=True)
    # Line from heater to 4-way valve
    cad_line(ax, fur_x + fur_w, fur_y + 0.6, 23.85, 10.4, lw=0.85)
    cad_arrow(ax, 23.4, 10.4, 23.85, 10.4, head_scale=5)
    # Line from 4-way valve into bottom of Drum A
    cad_line(ax, 24.2, 10.75, d1_x + dw/2, 10.75, lw=0.85)
    cad_line(ax, d1_x + dw/2, 10.75, d1_x + dw/2, d1_y - 0.4, lw=0.85)
    cad_arrow(ax, d1_x + dw/2, 10.6, d1_x + dw/2, d1_y - 0.4, head_scale=5)
    
    # Overhead Cracked Vapors from Drums to Coker Fractionator
    cad_line(ax, d1_x + dw/2, d1_y + dh + 0.4, d1_x + dw/2, 17.5, lw=0.85)
    cad_line(ax, d2_x + dw/2, d2_y + dh + 0.4, d2_x + dw/2, 17.5, lw=0.85)
    cad_line(ax, d1_x + dw/2, 17.5, 28.0, 17.5, lw=0.85)
    cad_arrow(ax, 27.6, 17.5, 28.0, 17.5, head_scale=5)
    cad_text(ax, 25.6, 17.75, 'Cracked Vapors to Coker Fractionator', sz=3.3, bold=True)
    
    # Delayed Coker Cycle summary box
    cad_rect(ax, 20.4, 8.8, 7.9, 0.55, lw=0.5, fill=True, fc='#ffffff')
    cad_text(ax, 24.35, 9.07, 'DCU Yield: Solid Coke (32.4%) | HCGO/LCGO (48.1%) | Naphtha (12.2%) | Gas (7.3%)', sz=3.4, bold=True)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 4: CONVERSION UNITS COMPARISON & DESIGN SPECIFICATION TABLE
    # ═════════════════════════════════════════════════════════════════════════
    headers = [
        'CONVERSION UNIT / METRIC', 'FLUID CATALYTIC CRACKING (FCCU)', 'HYDROCRACKER COMPLEX (HCU)', 'DELAYED COKING UNIT (DCU)'
    ]
    col_w = [6.2, 7.1, 7.5, 6.9]
    table_rows = [
        ['Primary Objective & Function', 'Maximum High-Octane Gasoline (RON 93)', 'Max Middle Distillates (Jet/ULSD)', 'Zero Fuel Oil / Solid Carbon Reject'],
        ['Operating Mechanism & Phase', 'Heterogeneous Fluidized Catalytic (Vap)', 'Fixed Bed Catalytic (Trickle Phase)', 'Thermal Non-Catalytic Pyrolysis (Liq/Vap)'],
        ['Operating Pressure & Temp', '2.5 bar(g)  |  535 C Riser / 710 C Regen', '155 bar(g)  |  390 - 410 C Reactor Bed', '2.2 bar(g)  |  495 C Heater / 460 C Drum'],
        ['Catalyst System & Form', 'Zeolite Y / USY Microspheres (75 um)', 'NiMo (Stg 1) + Pt/Zeolite (Stg 2)', 'None (Free Radical Thermal Polymerization)'],
        ['Feedstock Quality & Diet', 'HVGO + LVGO (Conradson Carbon < 0.5%)', 'HVGO + Heavy Coker Gas Oil (HCGO)', 'Vacuum Residue (VR, 538 C+, CCR 18-22 wt%)'],
        ['Major High-Value Products', 'Gasoline (51.2%), Propylene/LPG (18.6%)', 'ULSD (48.4%, S<10ppm), Jet Fuel (24.2%)', 'LCGO/HCGO (48.1%), Anode Coke (32.4%)'],
        ['Hydrogen Consumption / Offgas', 'Negligible H2 (+0.2% Net offgas H2)', 'High Cons: 2.4 - 2.8 wt% Feed H2', 'None (Net Offgas Rich in C1-C4 Fuel Gas)'],
        ['Decoking / Regeneration Mode', 'Continuous Air Blast in R-302 (CO2/CO)', 'Cyclic in-situ Catalyst Regeneration (2-3 yr)', '24h Batch Hydraulic Drill (Water 250 bar)'],
        ['Downstream Product Quality', 'RON 92.5 - 94.0 | Olefinic Gasoline', 'Cetane Index > 58 | Sulfur < 8 ppm', 'Coker Naphtha (Needs HDS) | Sponge Coke'],
        ['Gazebo & ROS 2 Simulation Tag', 'virtual_refinery/fccu_node (Kinetics)', 'virtual_refinery/hcu_node (155 bar)', 'virtual_refinery/coker_node (Drum A/B)']
    ]
    cad_draw_table_a4(ax, 1.0, 3.45, headers, table_rows, col_w, row_h=0.45,
                      title='REFINERY HEAVY-END UPGRADING UNITS: KINETIC, THERMODYNAMIC & OPERATIONAL MATRIX',
                      title_sz=4.8, sz=3.8)
    
    # Save Figure
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
    fig.savefig(out_pdf, format='pdf', dpi=300)
    fig.savefig(out_png, format='png', dpi=300)
    plt.close(fig)
    print(f"Generated DWG-03:\n  PDF -> {out_pdf}\n  PNG -> {out_png}")

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    pdf_path = os.path.join(base_dir, 'CAD_Drawings', '03_FCCU_Hydrocracker_Delayed_Coker_Conversion_CAD.pdf')
    png_path = os.path.join(base_dir, 'CAD_Drawings', '03_FCCU_Hydrocracker_Delayed_Coker_Conversion_CAD.png')
    generate_refinery_dwg03(pdf_path, png_path)
