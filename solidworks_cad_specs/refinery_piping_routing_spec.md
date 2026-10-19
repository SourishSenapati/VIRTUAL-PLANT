# SolidWorks 3D Modeling Specification: Interconnecting Piping & Stream Routing

**Author:** Sourish Senapati  
**Department:** Department of Chemical Engineering, Jadavpur University  
**Project:** Virtual Petroleum Refinery Digital Twin (`VIRTUAL-PLANT`)  
**Design Standards:** ASME B31.3 (Process Piping), ASME B16.5, PFI Standards

---

## 1. Multi-Tier Pipe Rack Spine Design

### 1.1 Structural Pipe Rack Architecture
- **Spine Dimensions:** $12.0\ \text{m}$ width $\times 320.0\ \text{m}$ overall length with $6.0\ \text{m}$ transverse bent spacing.
- **Elevation Tiers:**
  - Lower Tier (EL +4.5 m): Liquid hydrocarbon process lines (Crude feed, Atmospheric bottoms, Heavy Vacuum Gas Oil, Coker Gas Oil).
  - Intermediate Tier (EL +7.5 m): Light ends, vapor lines, LPG, and finished products (Gasoline, Kerosene, ULSD).
  - Upper Tier (EL +10.5 m): Utilities (High-pressure steam $40\ \text{bar}$, MP steam $15\ \text{bar}$, cooling water supply/return, fuel gas header, instrument air).
  - Cantilevered Top Bracket (EL +13.0 m): Flare collection header ($36''\ \text{DN900}$ sloping $1:500$ toward knockout drum).

---

## 2. Key Hydrocarbon Stream Routing Matrices

| Stream Description | From Unit | To Unit | Line Size | ASME Class | Metallurgy / Insulation |
|:---|:---|:---|:---|:---|:---|
| **Atmospheric Residue** | CDU Bottoms (C-101) | Vacuum Furnace (F-102) | DN350 (14") | CL 300 RF | Carbon Steel + 75 mm Hot Insulation |
| **Heavy Vacuum Gas Oil (HVGO)** | VDU Side-Draw (C-102) | FCCU (R-201) / HCU (R-301)| DN300 (12") | CL 300 RF | Carbon Steel + Heat Tracing |
| **Vacuum Residue (VR)** | VDU Bottoms (C-102) | Delayed Coker (F-401) | DN300 (12") | CL 600 RF | 5Cr-0.5Mo Alloy + High Temp Insulation |
| **FCC Heavy Cycle Oil** | FCC Fractionator | Slurry Exchanger / Bunker | DN200 (8") | CL 300 RF | Erosion-resistant hardened steel |
| **Hydrocracker ULSD** | HCU Fractionator | Diesel Storage (TK-603) | DN250 (10") | CL 150 RF | 304L SS (Low sulfur product purity) |
| **High Pressure Hydrogen** | SMR Plant / Compressor | HCU Reactor (R-301) | DN150 (6") | CL 1500 RTJ | High-strength forged alloy (Nelson curve safe) |
