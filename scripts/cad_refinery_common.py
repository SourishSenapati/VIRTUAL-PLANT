"""
CAD COMMON UTILITIES OPTIMIZED FOR ISO A4 LANDSCAPE (297 x 210 mm)
VIRTUAL PETROLEUM REFINERY DIGITAL TWIN (VIRTUAL-PLANT)
Author: Sourish Senapati (Department of Chemical Engineering, Jadavpur University)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, Circle, Polygon, Arc
import numpy as np

# Canvas Setup: ISO A4 Landscape (29.7 x 21.0 cm)
W, H = 29.7, 21.0
FONT_CAD = 'DejaVu Sans'
BK = '#000000'
GREY = '#555555'

def create_a4_canvas():
    fig = plt.figure(figsize=(W / 2.54, H / 2.54), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('white')
    return fig, ax

def cad_line(ax, x1, y1, x2, y2, lw=0.75, ls='-', color=BK, zorder=3):
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw, ls=ls, zorder=zorder, solid_capstyle='butt')

def cad_rect(ax, x, y, w, h, lw=0.75, ls='-', fill=False, fc='white', ec=BK, zorder=2):
    fill_color = fc if fill else 'none'
    ax.add_patch(Rectangle((x, y), w, h, fc=fill_color, ec=ec, lw=lw, linestyle=ls, zorder=zorder))

def cad_circle(ax, cx, cy, r, lw=0.75, ls='-', fill=False, fc='white', ec=BK, zorder=2):
    fill_color = fc if fill else 'none'
    ax.add_patch(Circle((cx, cy), r, fc=fill_color, ec=ec, lw=lw, linestyle=ls, zorder=zorder))

def cad_arc(ax, cx, cy, width, height, angle=0.0, theta1=0.0, theta2=360.0, lw=0.75, ls='-', color=BK, zorder=3):
    arc = Arc((cx, cy), width, height, angle=angle, theta1=theta1, theta2=theta2, color=color, lw=lw, linestyle=ls, zorder=zorder)
    ax.add_patch(arc)

def cad_text(ax, x, y, text, sz=5.5, ha='center', va='center', bold=False, zorder=8, bg=None, color=BK, rotation=0):
    weight = 'bold' if bold else 'normal'
    bbox_dict = dict(boxstyle='square,pad=0.10', fc='white', ec='none', alpha=0.95) if bg else None
    clean_txt = str(text).replace('³', '3').replace('²', '2').replace('⁻', '-').replace('°', ' DEG ').replace('µ', 'u').replace('ε', 'eps').replace('Δ', 'D_').replace('Ø', 'DIA ')
    ax.text(x, y, clean_txt, fontsize=sz, ha=ha, va=va, color=color,
            fontweight=weight, fontfamily=FONT_CAD, zorder=zorder, bbox=bbox_dict, rotation=rotation)

def cad_arrow(ax, x1, y1, x2, y2, lw=0.85, ls='-', color=BK, zorder=5, head_scale=7):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                linestyle=ls, shrinkA=0, shrinkB=0,
                                mutation_scale=head_scale),
                zorder=zorder)

def cad_dim_h(ax, x1, x2, y, label, ext=0.18, sz=4.8, bold=True, bg='white'):
    cad_line(ax, x1, y - ext, x1, y + ext, lw=0.40)
    cad_line(ax, x2, y - ext, x2, y + ext, lw=0.40)
    cad_line(ax, x1, y, x2, y, lw=0.50)
    t = 0.07
    cad_line(ax, x1 - t, y - t, x1 + t, y + t, lw=0.75)
    cad_line(ax, x2 - t, y - t, x2 + t, y + t, lw=0.75)
    cad_text(ax, (x1 + x2)/2, y, label, sz=sz, bold=bold, bg=bg)

def cad_dim_v(ax, x, y1, y2, label, ext=0.18, sz=4.8, bold=True, bg='white', text_offset=0.0, rotation=90):
    cad_line(ax, x - ext, y1, x + ext, y1, lw=0.40)
    cad_line(ax, x - ext, y2, x + ext, y2, lw=0.40)
    cad_line(ax, x, y1, x, y2, lw=0.50)
    t = 0.07
    cad_line(ax, x - t, y1 - t, x + t, y1 + t, lw=0.75)
    cad_line(ax, x - t, y2 - t, x + t, y2 + t, lw=0.75)
    cad_text(ax, x + text_offset, (y1 + y2)/2, label, sz=sz, bold=bold, bg=bg, rotation=rotation)

def cad_balloon(ax, cx, cy, mark, radius=0.28, sz=5.0):
    ax.add_patch(Circle((cx, cy), radius, fc='white', ec=BK, lw=0.70, zorder=6))
    cad_text(ax, cx, cy, mark, sz=sz, bold=True)

def cad_flange(ax, x, y, orientation='V', length=0.40, thickness=0.08, lw=0.80):
    d = length / 2
    if orientation == 'V':
        cad_rect(ax, x - d, y, length, thickness, lw=lw, fill=True, zorder=4)
        cad_line(ax, x - d - 0.04, y + thickness/2, x + d + 0.04, y + thickness/2, lw=0.30, ls='-.')
    else:
        cad_rect(ax, x, y - d, thickness, length, lw=lw, fill=True, zorder=4)
        cad_line(ax, x + thickness/2, y - d - 0.04, x + thickness/2, y + d + 0.04, lw=0.30, ls='-.')

def cad_valve(ax, cx, cy, orientation='H', size=0.35, valve_type='GATE', zorder=5):
    s = size / 2
    if orientation == 'H':
        p1 = [(cx - s, cy + s/1.5), (cx, cy), (cx - s, cy - s/1.5)]
        p2 = [(cx + s, cy + s/1.5), (cx, cy), (cx + s, cy - s/1.5)]
        ax.add_patch(Polygon(p1, closed=True, fc='white', ec=BK, lw=0.75, zorder=zorder))
        ax.add_patch(Polygon(p2, closed=True, fc='white', ec=BK, lw=0.75, zorder=zorder))
        if valve_type == 'CONTROL':
            cad_line(ax, cx, cy, cx, cy + s*1.2, lw=0.65, zorder=zorder)
            ax.add_patch(Arc((cx, cy + s*1.6), s*1.3, s*0.8, theta1=0, theta2=180, ec=BK, lw=0.75, zorder=zorder))
            cad_line(ax, cx - s*0.65, cy + s*1.6, cx + s*0.65, cy + s*1.6, lw=0.75, zorder=zorder)
    else:
        p1 = [(cx - s/1.5, cy - s), (cx, cy), (cx + s/1.5, cy - s)]
        p2 = [(cx - s/1.5, cy + s), (cx, cy), (cx + s/1.5, cy + s)]
        ax.add_patch(Polygon(p1, closed=True, fc='white', ec=BK, lw=0.75, zorder=zorder))
        ax.add_patch(Polygon(p2, closed=True, fc='white', ec=BK, lw=0.75, zorder=zorder))

def cad_hatch_rect(ax, x, y, w, h, pitch=0.20, lw=0.30, angle=45, color=BK):
    if angle == 45:
        x_coords = np.arange(x - h, x + w + h, pitch)
        for xc in x_coords:
            x_start = max(x, xc)
            y_start = y + max(0, x - xc)
            x_end = min(x + w, xc + h)
            y_end = y + min(h, x + w - xc)
            if x_start < x_end and y_start < y_end:
                cad_line(ax, x_start, y_start, x_end, y_end, lw=lw, color=color, zorder=2)
    elif angle == -45:
        x_coords = np.arange(x, x + w + 2*h, pitch)
        for xc in x_coords:
            x_start = max(x, xc - h)
            y_start = y + min(h, xc - x)
            x_end = min(x + w, xc)
            y_end = y + max(0, xc - (x + w))
            if x_start < x_end and y_start > y_end:
                cad_line(ax, x_start, y_start, x_end, y_end, lw=lw, color=color, zorder=2)

def draw_a4_border(ax):
    cad_rect(ax, 0.5, 0.5, W - 1.0, H - 1.0, lw=1.3)
    cad_rect(ax, 0.8, 0.8, W - 1.6, H - 1.6, lw=0.8)

def draw_refinery_title_block(ax, dwg_title, dwg_no, scale='DIAGRAMMATIC', date='19 / 10 / 2026',
                              sub_info='VIRTUAL PETROLEUM REFINERY  |  100,000 BPD CRUDE DIET  |  GAZEBO & ROS 2 DIGITAL TWIN  |  API / ASME BPVC'):
    TB_X = 0.8
    TB_Y = 0.8
    TB_W = W - 1.6
    TB_H = 2.30
    
    cad_rect(ax, TB_X, TB_Y, TB_W, TB_H, lw=1.1, fill=True)
    Y_R1 = TB_Y + 1.75
    Y_R2 = TB_Y + 1.15
    Y_R3 = TB_Y + 0.55
    
    cad_line(ax, TB_X, Y_R1, TB_X + TB_W, Y_R1, lw=0.8)
    cad_line(ax, TB_X, Y_R2, TB_X + TB_W, Y_R2, lw=0.6)
    cad_line(ax, TB_X, Y_R3, TB_X + TB_W, Y_R3, lw=0.6)
    
    # Row 1: Header / University
    cad_text(ax, TB_X + TB_W / 2, TB_Y + 2.02,
             'JADAVPUR UNIVERSITY  |  CHEMICAL ENGINEERING DEPARTMENT  |  PROCESS PLANT DIGITAL TWIN SIMULATION',
             sz=6.5, bold=True)
    
    col_splits = [0.42, 0.65, 0.84]
    for cs in col_splits:
        cad_line(ax, TB_X + TB_W * cs, TB_Y + 0.55, TB_X + TB_W * cs, Y_R1, lw=0.6)
    
    # Row 2
    cad_text(ax, TB_X + TB_W * 0.21, TB_Y + 1.57, 'DRAWING TITLE', sz=4.2, bold=True)
    cad_text(ax, TB_X + TB_W * 0.21, TB_Y + 1.33, dwg_title, sz=5.5, bold=True)
    cad_text(ax, TB_X + TB_W * 0.535, TB_Y + 1.57, 'LAB / SUBJECT', sz=4.2, bold=True)
    cad_text(ax, TB_X + TB_W * 0.535, TB_Y + 1.33, 'PROCESS PLANT DIGITAL TWIN & CAD', sz=5.0, bold=True)
    cad_text(ax, TB_X + TB_W * 0.745, TB_Y + 1.57, 'COURSE / BRANCH', sz=4.2, bold=True)
    cad_text(ax, TB_X + TB_W * 0.745, TB_Y + 1.33, 'B.E. CHEMICAL ENGINEERING', sz=5.0, bold=True)
    cad_text(ax, TB_X + TB_W * 0.92, TB_Y + 1.57, 'SCALE', sz=4.2, bold=True)
    cad_text(ax, TB_X + TB_W * 0.92, TB_Y + 1.33, scale, sz=5.2, bold=True)
    
    # Row 3
    cad_text(ax, TB_X + TB_W * 0.21, TB_Y + 0.97, 'STUDENT NAME', sz=4.2, bold=True)
    cad_text(ax, TB_X + TB_W * 0.21, TB_Y + 0.73, 'SOURISH SENAPATI', sz=6.0, bold=True)
    cad_text(ax, TB_X + TB_W * 0.535, TB_Y + 0.97, 'ROLL NO.', sz=4.2, bold=True)
    cad_text(ax, TB_X + TB_W * 0.535, TB_Y + 0.73, '002310301035', sz=6.0, bold=True)
    cad_text(ax, TB_X + TB_W * 0.745, TB_Y + 0.97, 'DRAWING NO.', sz=4.2, bold=True)
    cad_text(ax, TB_X + TB_W * 0.745, TB_Y + 0.73, dwg_no, sz=5.5, bold=True)
    cad_text(ax, TB_X + TB_W * 0.92, TB_Y + 0.97, 'DATE', sz=4.2, bold=True)
    cad_text(ax, TB_X + TB_W * 0.92, TB_Y + 0.73, date, sz=5.5, bold=True)
    
    # Row 4: Standards and Baseline Information
    cad_text(ax, TB_X + TB_W * 0.50, TB_Y + 0.28, sub_info, sz=4.8, bold=True)

def cad_draw_table_a4(ax, x, y, headers, rows, col_widths, row_h=0.38, title=None, title_sz=5.0, sz=4.2):
    tbl_w = sum(col_widths)
    num_rows = len(rows)
    
    if title:
        title_h = row_h * 1.05
        title_y = y + (num_rows + 1) * row_h
        cad_rect(ax, x, title_y, tbl_w, title_h, lw=0.85, fill=True)
        cad_text(ax, x + tbl_w/2, title_y + title_h/2, title, sz=title_sz, bold=True)
    
    cur_x = x
    for h_txt, cw in zip(headers, col_widths):
        cad_rect(ax, cur_x, y + num_rows * row_h, cw, row_h, lw=0.80, fill=True)
        cad_text(ax, cur_x + cw/2, y + num_rows * row_h + row_h/2, h_txt, sz=sz + 0.3, bold=True)
        cur_x += cw
        
    for r_idx, row in enumerate(rows):
        cur_x = x
        row_y = y + (num_rows - 1 - r_idx) * row_h
        for val, cw in zip(row, col_widths):
            cad_rect(ax, cur_x, row_y, cw, row_h, lw=0.55, fill=True)
            bold_val = any(k in str(val) for k in ['CDU', 'VDU', 'FCC', 'HCU', 'DCU', 'TOTAL', 'PASS', '100,000', 'CRITICAL'])
            cad_text(ax, cur_x + cw/2, row_y + row_h/2, str(val), sz=sz, bold=bold_val)
            cur_x += cw
