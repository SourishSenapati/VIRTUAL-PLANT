# SolidWorks 3D Modeling Specification: Atmospheric & Vacuum Distillation Units (CDU / VDU)

**Author:** Sourish Senapati  
**Department:** Department of Chemical Engineering, Jadavpur University  
**Project:** Virtual Petroleum Refinery Digital Twin (`VIRTUAL-PLANT`)  
**Design Standards:** ASME BPVC Section VIII Division 1 & 2, API 560 (Fired Heaters), API 650, TEMA Class R

---

## 1. Atmospheric Crude Distillation Unit (CDU / C-101)

### 1.1 Column Geometry & Shell Construction
- **Inside Diameter ($D_i$):**
  - Rectifying / Top Section: $4,500\ \text{mm}$
  - Flash Zone & Stripping Section: $5,200\ \text{mm}$ (Enlarged diameter to minimize entrainment at high vapor volume)
- **Tangent-to-Tangent Height ($H_{TT}$):** $54,000\ \text{mm}$ ($54.0\ \text{m}$)
- **Overall Height (Foundation to Top Vent Flange):** $62,500\ \text{mm}$ ($62.5\ \text{m}$) including $7,000\ \text{mm}$ structural support skirt.
- **Top / Bottom Heads:** $2:1$ Semi-Ellipsoidal heads (ASME BPVC Section VIII Division 1, Appendix 1).
- **Shell Material & Thickness:**
  - Material: SA-516 Gr 70 Carbon Steel with $3.0\ \text{mm}$ 410S Stainless Steel cladding in high-corrosion zones (flash zone and tray 28 to 36).
  - Shell thickness: $22\ \text{mm}$ (top) to $34\ \text{mm}$ (lower shell and skirt junction) based on wind moment ($160\ \text{km/h}$ gust) and seismic design (Zone III).
  - Corrosion Allowance: $3.5\ \text{mm}$ for sour crude service ($1.4\ \text{wt}\%\ \text{S}$).

### 1.2 Internal Hardware & Tray Layout
- **Total Tray Count:** 48 crossflow fractionating trays:
  - Trays 1–12 (Top / Light Naphtha wash section): Low-pressure-drop sieve trays ($12.5\ \text{mm}$ pitch, $5.0\ \text{mm}$ holes).
  - Trays 13–24 (Heavy Naphtha & Kerosene section): High-capacity moving valve trays (Koch-Glitsch Type VG-10).
  - Trays 25–38 (Diesel / Atmospheric Gas Oil section): Valve trays with anti-fouling cages.
  - Trays 39–45 (Flash zone wash section): Heavy duty chimney tray and demister mesh ($150\ \text{mm}$ 316L SS wire mesh).
  - Trays 46–48 (Atmospheric Residue stripping section): 4 steam stripping trays with steam sparger ring.
- **Tray Spacing ($T_s$):**
  - Standard spacing: $600\ \text{mm}$
  - Pumparound withdrawal / return zones: $900\ \text{mm}$
  - Flash zone height: $2,800\ \text{mm}$
- **Side Strippers:**
  - 3 side stripping columns ($1,200\ \text{mm}$ ID $\times 8,500\ \text{mm}$ height, 6 trays each) for Kerosene, LGO, and HGO stripping.

---

## 2. Vacuum Distillation Unit (VDU / C-102)

### 2.1 Deep-Cut Vacuum Column Architecture
- **Diameter Profile (Bulb Fractionator Design):**
  - Upper / Condensing Section: $5,000\ \text{mm}$ ID
  - Heavy Vacuum Gas Oil (HVGO) Section: $7,200\ \text{mm}$ ID
  - Flash Zone & Wash Oil Bed: $8,500\ \text{mm}$ ID (Sized for low vapor velocity under $25\ \text{mmHg}$ absolute vacuum)
  - Bottom Residue Sump (Quench section): $3,600\ \text{mm}$ ID (Reduced volume to minimize residence time $< 2\ \text{min}$ preventing thermal cracking)
- **Tangent-to-Tangent Height:** $42,000\ \text{mm}$ ($42.0\ \text{m}$)
- **Shell Design:** Designed for Full External Vacuum ($1.0\ \text{bar}$ external pressure @ $420^\circ\text{C}$ shell temperature) with external circumferential stiffening rings spaced every $1,800\ \text{mm}$.
- **Metallurgy:** SA-387 Gr 11 Class 2 ($1.25\ \text{Cr} - 0.5\ \text{Mo}$) with full explosion-bonded Inconel 625 cladding in the flash zone.

### 2.2 Structured Packing & Internals
- **Packing Beds:**
  - Bed 1 (Overhead / LVGO): Sulzer Mellapak 250X structured packing ($2,500\ \text{mm}$ bed depth).
  - Bed 2 (HVGO Pumparound & Wash): Mellapak 250X ($3,200\ \text{mm}$ bed depth).
  - Bed 3 (Slop Wax Wash Bed): High-capacity anti-coking structured grid (Mellagrid 64X, $1,500\ \text{mm}$ depth with wash oil spray nozzles).
- **Vacuum Generation System:** 3-stage steam ejector battery with barometric inter-condensers maintaining $20 - 30\ \text{mmHg(a)}$ ($2.67 - 4.0\ \text{kPa}$) at top column tangent.
