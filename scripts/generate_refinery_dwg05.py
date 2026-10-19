"""
A4 OPTIMIZED: DWG-05 ROS 2 DIGITAL TWIN & INDUSTRIAL AUTOMATION ARCHITECTURE
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
    cad_draw_table_a4, cad_balloon, W, H, BK, GREY
)

def generate_refinery_dwg05(out_pdf, out_png):
    fig, ax = create_a4_canvas()
    draw_a4_border(ax)
    
    draw_refinery_title_block(ax, 'ROS 2 DIGITAL TWIN & INDUSTRIAL AUTOMATION ARCHITECTURE',
                              'JU/ChE/VP/DWG-05', scale='LOGICAL / ARCHITECTURAL', date='19 / 10 / 2026')
    
    # Header Banner
    cad_text(ax, W/2, H - 1.25, 'ROS 2 DIGITAL TWIN ARCHITECTURE, COMPUTATIONAL GRAPH & DCS INTEGRATION', sz=6.8, bold=True)
    cad_text(ax, W/2, H - 1.62, 'ISA-95 CONTROL PYRAMID | ROS 2 HUMBLE/IRON PUB-SUB GRAPH | DDS MIDDLEWARE | OPC-UA GATEWAY', sz=4.8, bold=False)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 1: ISA-95 CONTROL PYRAMID & LEVEL MAPPING (LEFT: X=1.2 to 8.2)
    # ═════════════════════════════════════════════════════════════════════════
    pyr_x, pyr_y, pyr_w, pyr_h = 1.2, 8.6, 7.2, 10.2
    cad_rect(ax, pyr_x, pyr_y, pyr_w, pyr_h, lw=0.8, fill=True, fc='#fafbfc')
    cad_text(ax, pyr_x + pyr_w/2, pyr_y + pyr_h - 0.28, 'ISA-95 REFINERY AUTOMATION PYRAMID', sz=4.4, bold=True, color='#003366')
    
    # Pyramid Levels (Trapezoids / Rectangles stacked)
    levels = [
        ('LEVEL 4: BUSINESS PLANNING & LOGISTICS', 'Refinery ERP / Crude Assay Scheduling / Linear Prog. (LP)', '#f5f0eb', 1.4),
        ('LEVEL 3: MANUFACTURING OPERATIONS (MOM)', 'Advanced Process Control (APC) / Real-Time Optim. (RTO)', '#eef4fa', 1.4),
        ('LEVEL 2: SUPERVISORY CONTROL (SCADA/ROS 2)', 'ROS 2 Digital Twin Nodes / Gazebo Bridge / CCR HMI Displays', '#e6f0fa', 1.6),
        ('LEVEL 1: BASIC PROCESS CONTROL & SIS', 'DCS Field Controllers / SIS Triconex Triplicated Safety PLCs', '#e0ecf8', 1.6),
        ('LEVEL 0: FIELD SENSORS & ACTUATORS', 'Smart Transmitters (HART/FF) / Fisher Control Valves / ESDVs', '#d6e5f5', 1.8)
    ]
    cur_py = pyr_y + 0.6
    for idx, (lvl_title, lvl_desc, lvl_col, lh) in enumerate(reversed(levels)):
        cad_rect(ax, pyr_x + 0.4, cur_py, pyr_w - 0.8, lh, lw=0.7, fill=True, fc=lvl_col)
        cad_text(ax, pyr_x + pyr_w/2, cur_py + lh - 0.32, lvl_title, sz=3.4, bold=True)
        cad_text(ax, pyr_x + pyr_w/2, cur_py + 0.35, lvl_desc, sz=2.8, color='#444444')
        cur_py += lh + 0.25
        
    # Vertical Bidirectional Data Flow Arrow
    cad_line(ax, pyr_x + 0.2, pyr_y + 0.8, pyr_x + 0.2, pyr_y + pyr_h - 0.8, lw=0.75)
    cad_arrow(ax, pyr_x + 0.2, pyr_y + 1.2, pyr_x + 0.2, pyr_y + 0.8, head_scale=5)
    cad_arrow(ax, pyr_x + 0.2, pyr_y + pyr_h - 1.2, pyr_x + 0.2, pyr_y + pyr_h - 0.8, head_scale=5)
    cad_text(ax, pyr_x + 0.2, pyr_y + pyr_h/2, 'OPC-UA / MQTT / DDS REAL-TIME BUS', sz=3.0, bold=True, rotation=90, bg='white')
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 2: ROS 2 COMPUTATIONAL GRAPH (MIDDLE: X=8.8 to 20.6)
    # ═════════════════════════════════════════════════════════════════════════
    cg_x, cg_y, cg_w, cg_h = 8.8, 8.6, 11.6, 10.2
    cad_rect(ax, cg_x, cg_y, cg_w, cg_h, lw=0.9, fill=True, fc='#fcfdfe')
    cad_text(ax, cg_x + cg_w/2, cg_y + cg_h - 0.28, 'ROS 2 REFINERY COMPUTATIONAL GRAPH & TOPIC MESSAGING', sz=4.8, bold=True, color='#003366')
    
    # Helper to draw ROS 2 Node (Ellipse or Rounded Box)
    def draw_ros_node(ax, cx, cy, name, pkg='virtual_refinery'):
        nw, nh = 2.8, 1.2
        cad_rect(ax, cx - nw/2, cy - nh/2, nw, nh, lw=0.85, fill=True, fc='#ffffcc')
        cad_circle(ax, cx - nw/2 + 0.22, cy, 0.12, lw=0.5, fill=True, fc='#ff9900')
        cad_text(ax, cx + 0.1, cy + 0.22, name, sz=3.6, bold=True)
        cad_text(ax, cx + 0.1, cy - 0.25, f'[{pkg}]', sz=2.8, color='#666666')
        
    # Helper to draw ROS 2 Topic (Rectangular pill)
    def draw_ros_topic(ax, cx, cy, topic, msg_type):
        tw, th = 2.6, 0.7
        cad_rect(ax, cx - tw/2, cy - th/2, tw, th, lw=0.6, ls='--', fill=True, fc='#eaf2f8')
        cad_text(ax, cx, cy + 0.14, topic, sz=3.0, bold=True, color='#003366')
        cad_text(ax, cx, cy - 0.18, msg_type, sz=2.5, color='#777777')
        
    # 1. Orchestrator Node (Top Center)
    draw_ros_node(ax, cg_x + 5.8, cg_y + 8.8, 'refinery_orchestrator')
    
    # Clock / Step Topic
    draw_ros_topic(ax, cg_x + 5.8, cg_y + 7.4, '/clock & /refinery/step', 'rosgraph_msgs/Clock')
    cad_arrow(ax, cg_x + 5.8, cg_y + 8.2, cg_x + 5.8, cg_y + 7.75, head_scale=5)
    
    # 2. CDU/VDU Simulator Node (Left)
    draw_ros_node(ax, cg_x + 2.0, cg_y + 5.8, 'cdu_vdu_simulator')
    cad_arrow(ax, cg_x + 4.5, cg_y + 7.4, cg_x + 2.0, cg_y + 6.4, head_scale=5)
    
    # Stream from CDU/VDU Topic
    draw_ros_topic(ax, cg_x + 2.0, cg_y + 4.2, '/refinery/streams/cdu_vdu', 'ProcessStream.msg')
    cad_arrow(ax, cg_x + 2.0, cg_y + 5.2, cg_x + 2.0, cg_y + 4.55, head_scale=5)
    
    # 3. Conversion Units Node (Center)
    draw_ros_node(ax, cg_x + 5.8, cg_y + 5.8, 'conversion_units')
    cad_arrow(ax, cg_x + 5.8, cg_y + 7.05, cg_x + 5.8, cg_y + 6.4, head_scale=5)
    
    # Feed from CDU/VDU into Conversion Units
    cad_arrow(ax, cg_x + 3.3, cg_y + 4.2, cg_x + 4.5, cg_y + 5.4, head_scale=5)
    
    # Stream from Conversion Units
    draw_ros_topic(ax, cg_x + 5.8, cg_y + 4.2, '/refinery/streams/conversion', 'ProcessStream.msg')
    cad_arrow(ax, cg_x + 5.8, cg_y + 5.2, cg_x + 5.8, cg_y + 4.55, head_scale=5)
    
    # 4. Stream Router Node (Right)
    draw_ros_node(ax, cg_x + 9.6, cg_y + 5.8, 'stream_router')
    cad_arrow(ax, cg_x + 7.1, cg_y + 7.4, cg_x + 9.6, cg_y + 6.4, head_scale=5)
    cad_arrow(ax, cg_x + 7.1, cg_y + 4.2, cg_x + 8.3, cg_y + 5.4, head_scale=5)
    
    # Final Blends Topic
    draw_ros_topic(ax, cg_x + 9.6, cg_y + 4.2, '/refinery/blends/final', 'ProcessStream.msg')
    cad_arrow(ax, cg_x + 9.6, cg_y + 5.2, cg_x + 9.6, cg_y + 4.55, head_scale=5)
    
    # 5. Process Safety SIS Node (Bottom Left)
    draw_ros_node(ax, cg_x + 2.5, cg_y + 2.0, 'process_safety_sis')
    draw_ros_topic(ax, cg_x + 2.5, cg_y + 0.7, '/refinery/emergency_trip', 'EmergencyTrip.msg')
    cad_arrow(ax, cg_x + 2.5, cg_y + 1.4, cg_x + 2.5, cg_y + 1.05, head_scale=5)
    
    # Telemetry subscription into SIS
    cad_line(ax, cg_x + 2.0, cg_y + 3.85, cg_x + 2.0, cg_y + 2.8, lw=0.6, ls=':')
    cad_arrow(ax, cg_x + 2.0, cg_y + 3.0, cg_x + 2.0, cg_y + 2.6, head_scale=4)
    
    # 6. Gazebo Bridge Node (Bottom Right)
    draw_ros_node(ax, cg_x + 8.8, cg_y + 2.0, 'gazebo_bridge')
    draw_ros_topic(ax, cg_x + 8.8, cg_y + 0.7, '/gazebo/model_states', 'gazebo_msgs/ModelStates')
    cad_arrow(ax, cg_x + 8.8, cg_y + 1.4, cg_x + 8.8, cg_y + 1.05, head_scale=5)
    
    # Interconnection between Bridge and Safety
    cad_line(ax, cg_x + 3.9, cg_y + 2.0, cg_x + 7.4, cg_y + 2.0, lw=0.75, ls='--')
    cad_text(ax, cg_x + 5.65, cg_y + 2.25, 'Visual Flare / Trip State Sync', sz=2.8, bold=True)
    
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 3: CUSTOM MESSAGE SPECIFICATIONS (RIGHT: X=20.8 to 28.5)
    # ═════════════════════════════════════════════════════════════════════════
    msg_x, msg_y, msg_w, msg_h = 20.8, 8.6, 7.7, 10.2
    cad_rect(ax, msg_x, msg_y, msg_w, msg_h, lw=0.8, fill=True, fc='#fafbfc')
    cad_text(ax, msg_x + msg_w/2, msg_y + msg_h - 0.28, 'ROS 2 CUSTOM INTERFACES (.msg / .srv)', sz=4.4, bold=True, color='#003366')
    
    # ProcessStream.msg Box
    cad_rect(ax, msg_x + 0.4, msg_y + 6.2, msg_w - 0.8, 3.2, lw=0.65, fill=True, fc='#ffffff')
    cad_text(ax, msg_x + 0.6, msg_y + 9.15, 'ProcessStream.msg:', sz=3.3, bold=True, color='#990000', ha='left')
    ps_fields = [
        'std_msgs/Header header',
        'string stream_name',
        'float64 mass_flow_kg_h',
        'float64 temperature_c',
        'float64 pressure_bar',
        'float64 enthalpy_kj_kg',
        'string phase  # VAPOR / LIQUID',
        'float64[12] component_fractions'
    ]
    for idx, fld in enumerate(ps_fields):
        cad_text(ax, msg_x + 0.7, msg_y + 8.75 - idx*0.34, fld, sz=2.8, ha='left')
        
    # UnitTelemetry.msg Box
    cad_rect(ax, msg_x + 0.4, msg_y + 3.2, msg_w - 0.8, 2.7, lw=0.65, fill=True, fc='#ffffff')
    cad_text(ax, msg_x + 0.6, msg_y + 5.65, 'UnitTelemetry.msg:', sz=3.3, bold=True, color='#006600', ha='left')
    ut_fields = [
        'string unit_id  # CDU / VDU / FCC',
        'float64 operating_pressure_bar',
        'float64[] tray_temperatures_c',
        'float64 liquid_level_pct',
        'float64 differential_press_mbar',
        'bool trip_interlock_active'
    ]
    for idx, fld in enumerate(ut_fields):
        cad_text(ax, msg_x + 0.7, msg_y + 5.25 - idx*0.34, fld, sz=2.8, ha='left')
        
    # ValveCommand.msg & SetCutPoints.srv
    cad_rect(ax, msg_x + 0.4, msg_y + 0.5, msg_w - 0.8, 2.4, lw=0.65, fill=True, fc='#ffffff')
    cad_text(ax, msg_x + 0.6, msg_y + 2.65, 'SetCutPoints.srv:', sz=3.3, bold=True, color='#0000aa', ha='left')
    srv_fields = [
        'float64 cdu_naphtha_cut_c',
        'float64 cdu_kerosene_cut_c',
        'float64 cdu_diesel_cut_c',
        '---',
        'bool success',
        'string message'
    ]
    for idx, fld in enumerate(srv_fields):
        cad_text(ax, msg_x + 0.7, msg_y + 2.30 - idx*0.34, fld, sz=2.8, ha='left')
        
    # ═════════════════════════════════════════════════════════════════════════
    # SECTION 4: INDUSTRIAL AUTOMATION & BUS SPECIFICATIONS TABLE
    # ═════════════════════════════════════════════════════════════════════════
    headers = [
        'AUTOMATION BUS / INTERFACE', 'PHYSICAL / NETWORK LAYER', 'CYCLE TIME / FREQ', 'SECURITY / PROTOCOL', 'PRIMARY FUNCTION IN REFINERY TWIN'
    ]
    col_w = [5.6, 5.2, 4.2, 4.5, 8.2]
    table_rows = [
        ['ROS 2 FastDDS / CycloneDDS', 'Gigabit Ethernet (TCP/UDP)', '1000 Hz / 1 ms', 'DDS-Security (TLS/PKI)', 'Inter-node process telemetry & unit coordination'],
        ['OPC-UA Server (IEC 62541)', 'TCP/IP over Ethernet 802.3', '10 Hz / 100 ms', 'X.509 Certificate Encrypt', 'SCADA / DCS HMI real-time data exchange'],
        ['Modbus TCP / Fieldbus', 'RS-485 / Industrial Ethernet', '20 Hz / 50 ms', 'Role-Based Access (RBAC)', 'Smart actuator commands & valve position feedback'],
        ['HART 7.0 Digital Protocol', 'FSK superimposed 4-20 mA', '2 - 4 Hz / 500 ms', 'Point-to-Point / Wireless', 'Transmitter calibration, diagnostics & PV polling'],
        ['Safety Instrumented Net (SIS)', 'Dual Redundant Fiber Optic', '< 10 ms Deterministic', 'TÜV Rheinland IEC 61508', 'Emergency shutdown interlocks (ESD-101 to ESD-401)'],
        ['Gazebo Transport Engine', 'ZeroMQ / Protobuf Socket', '1000 Hz Physics Step', 'Local IPC / Socket Domain', 'Synchronous rigid-body physics & visual mesh updates'],
        ['Alarm & Event Logger (A&E)', 'PostgreSQL / InfluxDB TSDB', 'Event Driven (<5 ms)', 'AES-256 at Rest', 'Trip sequence of events (SOE) timestamp logging']
    ]
    cad_draw_table_a4(ax, 1.0, 3.45, headers, table_rows, col_w, row_h=0.45,
                      title='INDUSTRIAL AUTOMATION ARCHITECTURE, PROTOCOL STANDARDS & ROS 2 MIDDLEWARE INTEGRATION',
                      title_sz=4.8, sz=3.8)
    
    # Save Figure
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
    fig.savefig(out_pdf, format='pdf', dpi=300)
    fig.savefig(out_png, format='png', dpi=300)
    plt.close(fig)
    print(f"Generated DWG-05:\n  PDF -> {out_pdf}\n  PNG -> {out_png}")

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    pdf_path = os.path.join(base_dir, 'CAD_Drawings', '05_ROS2_Digital_Twin_Industrial_Automation_Architecture_CAD.pdf')
    png_path = os.path.join(base_dir, 'CAD_Drawings', '05_ROS2_Digital_Twin_Industrial_Automation_Architecture_CAD.png')
    generate_refinery_dwg05(pdf_path, png_path)
