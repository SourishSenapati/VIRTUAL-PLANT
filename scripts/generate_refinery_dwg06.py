"""
A4 OPTIMIZED: DWG-06 PROCESS DYNAMICS, PROTECTION LAYERS & FLARE SAFETY SYSTEM
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

def generate_refinery_dwg06(out_pdf, out_png):
    fig, ax = create_a4_canvas()
    draw_a4_border(ax)
    
    draw_refinery_title_block(ax, 'PROCESS DYNAMICS, PROTECTION LAYERS & FLARE SAFETY SYSTEM',
                              'JU/ChE/VP/DWG-06', scale='DIAGRAMMATIC / ANALYTIC', date='19 / 10 / 2026')
    
    # Header Banner
    cad_text(ax, W/2, H - 1.25, 'PROCESS SAFETY MANAGEMENT (PSM), IEC 61511 SIS LAYERS & API 521 FLARE RADIATION', sz=6.8, bold=True)
    cad_text(ax, W/2, H - 1.62, 'LOPA PROTECTION ONION | ESD CAUSE & EFFECT LOGIC | API 521 DEPRESSURING DYNAMICS & THERMAL FLUX', sz=4.8, bold=False)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 1: LOPA PROTECTION ONION MODEL (LEFT: X=1.2 to 9.2)
    # ═════════════════════════════════════════════════════════════════════════
    lopa_x, lopa_y, lopa_w, lopa_h = 1.2, 8.6, 8.2, 10.2
    cad_rect(ax, lopa_x, lopa_y, lopa_w, lopa_h, lw=0.8, fill=True, fc='#fafbfc')
    cad_text(ax, lopa_x + lopa_w/2, lopa_y + lopa_h - 0.28, 'LAYER OF PROTECTION ANALYSIS (LOPA)', sz=4.6, bold=True, color='#003366')
    
    # Concentric Onion Rings (Center: (lopa_x + lopa_w/2, lopa_y + 4.8))
    cx, cy = lopa_x + lopa_w/2, lopa_y + 5.2
    radii = [3.8, 3.2, 2.6, 2.0, 1.4, 0.8]
    colors = ['#feebe2', '#fcc5c0', '#fa9fb5', '#f768a1', '#c51b8a', '#7a0177']
    labels = [
        ('7. Community Emergency Evacuation', 3.5),
        ('6. Plant Emergency Response & Deluge', 2.9),
        ('5. Physical Relief: PSV & Rupture Disks', 2.3),
        ('4. Safety Instrumented System (SIS/ESD)', 1.7),
        ('3. Operator Intervention & Alarms', 1.1),
        ('2. BPCS Control', 0.5)
    ]
    for r, col in zip(radii, colors):
        cad_circle(ax, cx, cy, r, lw=0.65, fill=True, fc=col, ec=BK)
        
    # Core: Inherent Process Safety
    cad_circle(ax, cx, cy, 0.45, lw=0.8, fill=True, fc='#ffffd4', ec=BK)
    cad_text(ax, cx, cy + 0.10, 'CORE:', sz=2.8, bold=True)
    cad_text(ax, cx, cy - 0.15, 'INHERENT\nSAFETY', sz=2.6, bold=True)
    
    # Layer text tags around the rings
    cad_text(ax, cx, cy + 3.5, '7. Emergency Response Plan (Onsite / Offsite)', sz=2.8, bold=True)
    cad_text(ax, cx, cy + 2.9, '6. Secondary Containment & Deluge Foam', sz=2.8, bold=True)
    cad_text(ax, cx, cy + 2.3, '5. API 520/521 Mechanical PSVs to Flare', sz=2.8, bold=True)
    cad_text(ax, cx, cy + 1.7, '4. IEC 61511 Safety Instrumented System (SIL 2/3)', sz=2.8, bold=True, color='white')
    cad_text(ax, cx, cy + 1.1, '3. Critical Priority Alarms (ISA-18.2)', sz=2.7, bold=True, color='white')
    cad_text(ax, cx, cy + 0.65, '2. BPCS PID Loops', sz=2.7, bold=True, color='white')
    
    # Risk Reduction Factor Explanation Box
    cad_rect(ax, lopa_x + 0.4, lopa_y + 0.5, lopa_w - 0.8, 1.4, lw=0.6, fill=True, fc='#ffffff')
    cad_text(ax, lopa_x + lopa_w/2, lopa_y + 1.65, 'LOPA TARGET RISK MITIGATION:', sz=3.2, bold=True, color='#003366')
    cad_text(ax, lopa_x + lopa_w/2, lopa_y + 1.25, 'Unmitigated Event Frequency: 1.0E-01 / yr', sz=2.8)
    cad_text(ax, lopa_x + lopa_w/2, lopa_y + 0.95, 'Independent Protection Layers (IPL) RRF = 10^4', sz=2.8, bold=True, color='#990000')
    cad_text(ax, lopa_x + lopa_w/2, lopa_y + 0.65, 'Mitigated Consequence: < 1.0E-05 / yr (Broadly Acceptable)', sz=2.8)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 2: API 521 FLARE THERMAL RADIATION PROFILE (MIDDLE: X=9.8 to 18.8)
    # ═════════════════════════════════════════════════════════════════════════
    fl_x, fl_y, fl_w, fl_h = 9.8, 8.6, 9.2, 10.2
    cad_rect(ax, fl_x, fl_y, fl_w, fl_h, lw=0.8, fill=True, fc='#fafbfc')
    cad_text(ax, fl_x + fl_w/2, fl_y + fl_h - 0.28, 'API 521 FLARE THERMAL RADIATION PROFILE', sz=4.6, bold=True, color='#003366')
    
    # Subplot Coordinate Box for Radiation Curve
    ax_sub = fig.add_axes([ (fl_x + 1.1)/W, (fl_y + 2.8)/H, (fl_w - 1.6)/W, 5.2/H ])
    
    # Distance from flare stack base (meters)
    R = np.linspace(20, 250, 200)
    # Stack height H_stack = 90 m
    # Radial distance to flame center D = sqrt(R^2 + H^2)
    H_stack = 90.0
    D = np.sqrt(R**2 + H_stack**2)
    # Heat release Q = 450 MW (Major refinery depressuring scenario)
    # Radiation fraction F = 0.25, Atmospheric transmissivity tau ~ 0.85
    tau = 0.85
    F = 0.25
    Q_kW = 450000.0  # kW
    K = (tau * F * Q_kW) / (4.0 * np.pi * (D**2))  # kW/m2
    
    ax_sub.plot(R, K, color='#cc0000', lw=1.6, label='Point Source Flux K(R)')
    ax_sub.axhline(9.46, color='#ff6600', ls='--', lw=0.9, label='9.46 kW/m2 (Escape < 30s)')
    ax_sub.axhline(4.73, color='#008800', ls='--', lw=0.9, label='4.73 kW/m2 (Sterile Limit)')
    ax_sub.axhline(1.58, color='#0000cc', ls='--', lw=0.9, label='1.58 kW/m2 (Continuous)')
    ax_sub.axvline(150, color='#888888', ls=':', lw=1.1, label='R = 150 m Exclusion Perimeter')
    
    ax_sub.set_xlim(20, 250)
    ax_sub.set_ylim(0, 15)
    ax_sub.set_xlabel('Distance from Flare Base R (meters)', fontsize=5.5, fontfamily='DejaVu Sans')
    ax_sub.set_ylabel('Thermal Flux K (kW/m2)', fontsize=5.5, fontfamily='DejaVu Sans')
    ax_sub.grid(True, ls=':', lw=0.4, color='#bbbbbb')
    ax_sub.legend(fontsize=4.6, loc='upper right', framealpha=0.9)
    ax_sub.tick_params(labelsize=4.8)
    
    # Flare Specification Notes Box
    cad_rect(ax, fl_x + 0.4, fl_y + 0.5, fl_w - 0.8, 2.0, lw=0.6, fill=True, fc='#ffffff')
    cad_text(ax, fl_x + fl_w/2, fl_y + 2.25, 'FLARE SYSTEM DESIGN SPECIFICATIONS (API 521):', sz=3.2, bold=True, color='#003366')
    fl_notes = [
        'Stack Height: 90 m (Derrick Supported) | Tip Diameter: 1.8 m',
        'Smokeless Flaring Capacity: 25% Design Load with MP Steam Injection',
        'Knockout Drum (V-601): Sized for 300 um Droplet Disengagement (API 521)',
        'Molecular Seal: Purge Gas Consumption < 0.015 m/s to Prevent Air Ingress'
    ]
    for idx, fn in enumerate(fl_notes):
        cad_text(ax, fl_x + 0.6, fl_y + 1.85 - idx*0.38, fn, sz=2.8, ha='left')
        
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 3: EMERGENCY SHUTDOWN CAUSE & EFFECT (RIGHT: X=19.4 to 28.5)
    # ═════════════════════════════════════════════════════════════════════════
    esd_x, esd_y, esd_w, esd_h = 19.4, 8.6, 9.1, 10.2
    cad_rect(ax, esd_x, esd_y, esd_w, esd_h, lw=0.8, fill=True, fc='#fafbfc')
    cad_text(ax, esd_x + esd_w/2, esd_y + esd_h - 0.28, 'EMERGENCY SHUTDOWN (ESD) MATRIX', sz=4.6, bold=True, color='#003366')
    
    # 4 Detailed ESD Loop Boxes
    esd_loops = [
        ('ESD-101: CDU OVERPRESSURE', 'PT-101 > 3.5 bar(g) (2oo3 Voting)',
         '-> Close Fuel Gas XV-101 (Furnace trip)\n-> Trip Feed Pump P-101A/B\n-> Open Flare Blowdown XV-102', '#ffe6e6'),
        ('ESD-201: VDU COIL LOSS OF FLOW', 'FT-201 < 60% Design Flow',
         '-> Trip Vacuum Heater H-201 Burners\n-> Inject Emergency Quench Steam\n-> Isolate Residue Bottoms Discharge', '#fff0e6'),
        ('ESD-301: FCC RISER THERMAL TRIP', 'TT-301 > 560 C (Riser Runaway)',
         '-> Close Regen Catalyst Slide Valve XV-301\n-> Inject Lift Steam Dispersion Quench\n-> Divert HVGO Feed to Slop System', '#f5e6ff'),
        ('ESD-401: HCU HP LOOP DEPRESSURING', 'PT-401 > 170 bar OR TT-401 > 425 C',
         '-> Trip Recycle H2 Compressor C-401\n-> Open Rapid Depressuring XV-401 to Flare\n-> Rate: 155 bar to 10 bar in 15 min (API 521)', '#e6f2ff')
    ]
    cur_ey = esd_y + esd_h - 0.8
    for el_title, el_cause, el_actions, el_col in esd_loops:
        eh = 2.05
        cad_rect(ax, esd_x + 0.4, cur_ey - eh, esd_w - 0.8, eh, lw=0.65, fill=True, fc=el_col)
        cad_text(ax, esd_x + 0.6, cur_ey - 0.32, el_title, sz=3.2, bold=True, color='#990000', ha='left')
        cad_text(ax, esd_x + 0.6, cur_ey - 0.65, f'Trigger Cause: {el_cause}', sz=2.8, bold=True, ha='left')
        for a_idx, act_line in enumerate(el_actions.split('\n')):
            cad_text(ax, esd_x + 0.6, cur_ey - 1.05 - a_idx*0.32, act_line, sz=2.7, ha='left')
        cur_ey -= eh + 0.30
        
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 4: SAFETY INSTRUMENTED SYSTEMS (SIS) RELIABILITY SPECIFICATION
    # ═════════════════════════════════════════════════════════════════════════
    headers = [
        'SIF LOOP TAG', 'INITIATOR / SENSOR', 'VOTING ARCH.', 'TARGET SIL', 'PFD_avg (PROB. FAIL)', 'SAFE STATE ACTION & EXECUTIVE RESPONSE'
    ]
    col_w = [4.6, 5.4, 3.8, 3.4, 4.2, 8.3]
    table_rows = [
        ['SIF-101 (CDU Pressure)', 'Triple PT Transmitters (PT-101A/B/C)', '2oo3 Voting', 'SIL 2', '2.4E-03 (RRF 416)', 'Cut fuel gas to H-101 within 2.0s; vent column to flare'],
        ['SIF-102 (CDU Level High)', 'Dual Displacer Level (LT-101A/B)', '1oo2 Voting', 'SIL 2', '3.1E-03 (RRF 322)', 'Trip reflux pumps to prevent overhead condenser flooding'],
        ['SIF-201 (VDU Furnace)', 'Differential Flow FT-201A/B', '1oo2 Voting', 'SIL 3', '8.5E-04 (RRF 1176)', 'Immediate fuel gas trip & emergency coil steam injection'],
        ['SIF-301 (FCC Slide Valve)', 'Nuclear Bed Density & Riser Temp', '2oo3 Voting', 'SIL 3', '5.2E-04 (RRF 1923)', 'Slam-shut regenerated catalyst slide valve in < 1.0s'],
        ['SIF-401 (HCU Depressuring)', 'High-Pressure Loop PT-401A/B/C', '2oo3 Voting', 'SIL 3', '4.1E-04 (RRF 2439)', 'Open twin fail-open depressuring valves to flare (API 521)'],
        ['SIF-501 (Coker Switch)', 'Drum Level Gamma Ray Detectors', '2oo3 Voting', 'SIL 2', '1.8E-03 (RRF 555)', 'Inhibit 4-way switch valve movement during active filling'],
        ['SIF-601 (Flare Pilot Loss)', 'Triple Optical / Thermocouple Flame', '2oo3 Voting', 'SIL 2', '2.2E-03 (RRF 454)', 'Auto-spark igniter sequence & emergency fuel gas pilot enrich']
    ]
    cad_draw_table_a4(ax, 1.0, 3.45, headers, table_rows, col_w, row_h=0.45,
                      title='SAFETY INSTRUMENTED SYSTEMS (SIS): IEC 61508 / IEC 61511 RELIABILITY & SIL ASSIGNMENT MATRIX',
                      title_sz=4.8, sz=3.8)
    
    # Save Figure
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
    fig.savefig(out_pdf, format='pdf', dpi=300)
    fig.savefig(out_png, format='png', dpi=300)
    plt.close(fig)
    print(f"Generated DWG-06:\n  PDF -> {out_pdf}\n  PNG -> {out_png}")

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    pdf_path = os.path.join(base_dir, 'CAD_Drawings', '06_Process_Dynamics_Protection_Layers_Flare_Safety_CAD.pdf')
    png_path = os.path.join(base_dir, 'CAD_Drawings', '06_Process_Dynamics_Protection_Layers_Flare_Safety_CAD.png')
    generate_refinery_dwg06(pdf_path, png_path)
