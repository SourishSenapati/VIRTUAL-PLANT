# SolidWorks 3D Modeling Specification: Delayed Coking, Flare System & Tank Farm

**Author:** Sourish Senapati  
**Department:** Department of Chemical Engineering, Jadavpur University  
**Project:** Virtual Petroleum Refinery Digital Twin (`VIRTUAL-PLANT`)  
**Design Standards:** API 521 (Pressure Relieving & Depressuring), API 650 (Welded Steel Tanks), ASME BPVC Sec VIII Div 1

---

## 1. Delayed Coking Unit (DCU / V-401A & V-401B)

### 1.1 Twin Coke Drum Mechanical Design
- **Configuration:** 2-Drum batch-continuous switching cycle (24-hour cycle: Fill / Coking $\rightarrow$ Switch $\rightarrow$ Steam out $\rightarrow$ Water quench $\rightarrow$ Hydraulic cutting $\rightarrow$ Warmup).
- **Vessel Dimensions:**
  - Inside Diameter ($D_i$): $8,500\ \text{mm}$ ($8.5\ \text{m}$)
  - Tangent-to-Tangent Height ($H_{TT}$): $34,000\ \text{mm}$ ($34.0\ \text{m}$)
  - Bottom Cone: $90^\circ$ included angle cone with automated bottom unheading slide valve ($1,800\ \text{mm}$ throat).
  - Top Head: Hemispherical head with automated top unheading device ($1,200\ \text{mm}$ throat).
- **Metallurgy & Thermal Fatigue:**
  - Material: SA-387 Gr 11 Class 2 ($1.25\ \text{Cr} - 0.5\ \text{Mo}$) base plate ($32\ \text{mm}$ thickness) with $3.0\ \text{mm}$ TP 410S cladding.
  - Skirt-to-cone junction: Forged integral transition ring with parabolic transition fillet to resist severe low-cycle thermal shock during water quenching.
- **Hydraulic Decoking Derrick Structure:**
  - $48.0\ \text{m}$ structural steel lattice derrick mounted on drum top platforms.
  - Drill stem hoist, rotary swivel, high-pressure water cutting nozzle ($280\ \text{bar}$ jet pressure) for pilot hole boring and final radial cutting.

---

## 2. Elevated Emergency Flare System (FL-501)

### 2.1 Flare Stack & Radiation Envelope
- **Stack Architecture:**
  - Height: $90,000\ \text{mm}$ ($90.0\ \text{m}$) self-supported lattice derrick structure.
  - Flare Riser Tip: $1,200\ \text{mm}$ diameter with steam-assist smokeless injection nozzles and 4 continuous gas pilots with electronic spark ignition.
  - Seal Drums: Water seal drum ($4,200\ \text{mm}$ ID) and molecular velocity seal to prevent atmospheric air flashback into the relief header.
- **Relief Capacity:** Sized for full electrical power failure / total cooling water loss relief load: $485,000\ \text{kg/h}$ hydrocarbon vapor relieving.
- **Sterile Safety Radius:** $150\ \text{m}$ ground radiation exclusion zone (Maximum radiant heat intensity $< 4.73\ \text{kW/m}^2$ at fence line per API 521).

---

## 3. Refinery Tank Farm Storage (TK-601 to TK-612)

### 3.1 Crude Oil Storage Tanks (TK-601 & TK-602)
- **Type:** API 650 Pontoon-Type External Floating Roof Tank with primary mechanical shoe seal and secondary wiper seal.
- **Capacity:** $65,000\ \text{m}^3$ each ($52,000\ \text{metric tonnes}$).
- **Dimensions:** $68,000\ \text{mm}$ diameter $\times 18,500\ \text{mm}$ shell height.

### 3.2 Pressurized LPG Horton Spheres (TK-605 & TK-606)
- **Type:** Spherical pressure storage vessels designed to ASME Section VIII Division 1.
- **Capacity:** $2,500\ \text{m}^3$ each @ $18.0\ \text{bar(g)}$ design pressure for propane/butane storage.
- **Support:** 10 tubular column legs with fireproofing insulation (concrete encased).
