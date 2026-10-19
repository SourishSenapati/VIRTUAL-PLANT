# Virtual Petroleum Refinery Digital Twin: SolidWorks CAD, Gazebo ODE Simulation & ROS 2 Process Automation

[![Educational License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)
[![Author: Sourish Senapati](https://img.shields.io/badge/Author-Sourish%20Senapati-blue.svg)](https://github.com/SourishSenapati)
[![Institution: Jadavpur University](https://img.shields.io/badge/Institution-Jadavpur%20University-crimson.svg)](http://www.jaduniv.edu.in/)
[![Department: Chemical Engineering](https://img.shields.io/badge/Department-Chemical%20Engineering-darkgreen.svg)](http://www.jaduniv.edu.in/)
[![Roll: 002310301035](https://img.shields.io/badge/Roll-002310301035-orange.svg)](https://github.com/SourishSenapati)
[![Physics Engine: Gazebo ODE](https://img.shields.io/badge/Gazebo-ODE%20Physics-blueviolet.svg)](https://gazebosim.org/)
[![Middleware: ROS 2 Humble/Iron](https://img.shields.io/badge/ROS%202-Humble%20%2F%20Iron-brightgreen.svg)](https://docs.ros.org/)
[![Design Standards: ASME BPVC & API](https://img.shields.io/badge/Standards-ASME%20BPVC%20%7C%20API%20521-yellow.svg)](https://www.asme.org/)

---

## 📌 Project Overview & Engineering Scope

The **Virtual Petroleum Refinery Digital Twin** (`VIRTUAL-PLANT`) is an industrial-scale, physics-accurate simulation environment of a **100,000 BPD (564,670 kg/h)** high-conversion petroleum refinery. Developed by **Sourish Senapati** at the **Department of Chemical Engineering, Jadavpur University**, the platform bridges mechanical CAD engineering, chemical reaction thermodynamics, robotics middleware, and industrial automation.

The environment integrates:
1. **Mechanical Design & SolidWorks CAD Specifications**: ASME Boiler & Pressure Vessel Code (BPVC) Section VIII Div 1 & 2 mechanical sizing, tray hydraulics, shell wall thicknesses, and API 650 / API 521 compliant offsites.
2. **Rigorous Thermodynamics & Physics Kinetics**: Continuous True Boiling Point (TBP) Riazi-Daubert probability density distribution, 4-lump Weekman catalytic cracking kinetics, high-pressure 155 bar hydrocracking reactions, delayed coking pyrolysis cycles, and API 521 point-source thermal radiation profiles.
3. **Gazebo 3D Simulation World**: Open Dynamics Engine (ODE) multi-body physical environment with collisions, inertial properties, mass distributions, and visual state rendering across a 600 m × 400 m battery limit plot plan.
4. **ROS 2 Robotics & Process Control Middleware**: Real-time distributed node network (ROS 2 Humble/Iron) managing mass balance closure, dynamic cut-point optimization, IEC 61511 Safety Instrumented Systems (SIS), and ISA-95 Level 0–4 plant-wide automation.

---

## 🏛️ Refinery Flowsheet & Unit Operations

The refinery configuration represents a modern **High-Conversion Deep-Upgrading Refinery Diet** processing Arabian Light / Brent crude blend (32.8° API, 1.78 wt% Sulfur, 4.2 wt% Conradson Carbon Residue):

```
                                  ARABIAN LIGHT CRUDE (100,000 BPD)
                                                │
                                    ┌───────────▼───────────┐
                                    │  CRUDE DESALTER (DES) │
                                    │    Salt < 1.0 PTB     │
                                    └───────────┬───────────┘
                                                │ Preheated to 365 °C
                                    ┌───────────▼───────────┐
                          ┌─────────┤   ATMOSPHERIC (CDU)   ├─────────┬────────────────────────┐
                          │         │    48 Sieve Trays     │         │                        │
                          ▼         └───────────┬───────────┘         ▼                        ▼
                   Off-Gas & LPG                │              Kerosene/Jet A-1          Diesel / AGO
                 (To Gas Plant)                 │               (150 - 240 °C)          (240 - 360 °C)
                                                ▼                      │                        │
                                      Atmospheric Residue              ▼                        ▼
                                          (> 360 °C)              Merox Sweeten             Diesel HDS
                                                │                      │                        │
                                    ┌───────────▼───────────┐          │                        │
                                    │     VACUUM (VDU)      │          │                        │
                                    │   40 mmHg abs (Deep)  │          │                        │
                                    └─────┬───────────┬─────┘          │                        │
                                          │           │                │                        │
                         Light VGO (LVGO) │           │ Heavy VGO      │                        │
                          (360 - 440 °C)  │           │ (440 - 540 °C) │                        │
                                 │        │           │                │                        │
                                 ▼        │           ▼                │                        │
                      ┌───────────────────┘    ┌──────────────┐        │                        │
                      │                        │              │        │                        │
                      ▼                        ▼              │        │                        │
          ┌───────────────────────┐ ┌───────────────────────┐ │        │                        │
          │   FCCU RISER (U-300)  │ │   HYDROCRACKER (U-400)│ │        │                        │
          │ Zeolite USY | 535 °C  │ │ 155 bar | NiMo/Zeolite│ │        │                        │
          └───────────┬───────────┘ └───────────┬───────────┘ │        │                        │
                      │                         │             │        │                        │
            ┌─────────┴─────────┐     ┌─────────┴─────────┐   │        │                        │
            ▼                   ▼     ▼                   ▼   │        │                        │
       FCC Gasoline         Cycle Oil Heavy Naphtha     ULSD  │        │                        │
         (RON 93)            (LCO)    (To Reformer) (Cetane58)│        │                        │
                                │           │             │   │        │                        │
                                └─────┬─────┘             │   │        │                        │
                                      ▼                   │   │        │                        │
                                Vacuum Residue (VR)       │   │        │                        │
                                     (> 540 °C)           │   │        │                        │
                                          │               │   │        │                        │
                              ┌───────────▼───────────┐   │   │        │                        │
                              │  DELAYED COKER (DCU)  │   │   │        │                        │
                              │ Twin Drums A/B | 24h  │   │   │        │                        │
                              └─────┬───────────┬─────┘   │   │        │                        │
                                    │           │         │   │        │                        │
                                    ▼           ▼         │   │        │                        │
                               Solid Coke   Coker Gas Oil │   │        │                        │
                              (Anode Grd)      (HCGO)     │   │        │                        │
                                                │         │   │        │                        │
                                                └─────────┼───┼────────┼────────► ULSD POOL
                                                          │   │        │          (S < 10 ppm)
                                                          ▼   ▼        ▼
                                                       HIGH-OCTANE  COMMERCIAL
                                                        GASOLINE    JET FUEL A-1
```

---

## ⚙️ Rigorous Thermodynamics & Physics-Accurate Kinetics

### 1. Riazi-Daubert Continuous True Boiling Point (TBP) Distillation Model
The crude assay is evaluated through continuous cumulative probability distribution based on the Riazi-Daubert framework:
$$\text{Yield}(T) = 1.0 - \exp\left[-\left(\frac{T - T_0}{\theta}\right)^\beta\right]$$
Where $T_0 = 288.15\ \text{K}$, $\theta = 485.2\ \text{K}$, and shape factor $\beta = 1.62$.

| Fraction Name | TBP Boiling Range (°C) | Cut wt% Yield | Mass Rate (kg/h) | Vol Rate (BPD) | Specific Gravity | Downstream Upgrading Route |
|---|---|---|---|---|---|---|
| **Off-Gas & LPG** | Initial – 35 °C | 2.85 % | 16,093 | 3,850 | 0.582 | Amine Treating & Gas Plant |
| **Light Naphtha** | 35 – 80 °C | 6.42 % | 36,252 | 7,420 | 0.665 | Isomerization (RON 88) |
| **Heavy Naphtha** | 80 – 150 °C | 15.16 % | 85,604 | 16,100 | 0.748 | Catalytic Reformer (RON 100) |
| **Kerosene / Jet** | 150 – 240 °C | 17.93 % | 101,220 | 17,950 | 0.812 | Merox Treating (Jet A-1 Pool) |
| **Diesel / AGO** | 240 – 360 °C | 21.78 % | 123,012 | 20,800 | 0.852 | Hydrotreater (ULSD Pool) |
| **Light Vacuum Gas Oil** | 360 – 440 °C | 10.98 % | 61,993 | 10,200 | 0.898 | Hydrocracker / Diesel Pool |
| **Heavy Vacuum Gas Oil** | 440 – 540 °C | 9.66 % | 54,526 | 8,780 | 0.925 | FCCU (60%) & HCU (40%) |
| **Vacuum Residue (VR)** | > 540 °C | 15.20 % | 85,828 | 13,100 | 1.022 | Delayed Coking Unit (DCU) |
| **REFINERY TOTAL DIET** | Whole Crude Range | **100.00 %** | **564,670 kg/h** | **100,000 BPD** | **0.861** | **Strict Mass Balance Closure** |

### 2. Fluid Catalytic Cracking (FCCU) 4-Lump Kinetics
The riser reactor operates at $535\ ^\circ\text{C}$ and $2.5\ \text{bar(g)}$ with ultra-stable Y-zeolite (USY) catalyst. The kinetic network follows the second-order Weekman-Nace model:
$$\frac{d y_{\text{VGO}}}{d t_c} = -k_0 \exp\left(-\frac{E_a}{R T}\right) \cdot \phi(t_c) \cdot y_{\text{VGO}}^2$$
$$\phi(t_c) = \exp(-\alpha \cdot t_c) \quad (\text{Catalyst Deactivation})$$

- **Feed Conversion**: $72.4\ \text{wt}\%$
- **Gasoline Yield**: $51.2\ \text{wt}\%$ (Research Octane Number $\text{RON} = 93.2$)
- **Light Olefinic Gas ($\text{C}_3/\text{C}_4$)**: $18.6\ \text{wt}\%$ (Rich in Propylene for alkylation)
- **Light Cycle Oil (LCO)**: $18.2\ \text{wt}\%$ (Routed to HCU/Diesel blending)
- **Coke on Catalyst**: $4.8\ \text{wt}\%$ (Combusted in 2-stage regenerator at $710\ ^\circ\text{C}$ for heat balance)

### 3. Two-Stage Hydrocracker (HCU) Kinetics & Thermodynamics
- **Operating Pressure**: $155\ \text{bar(g)}$ ($2,250\ \text{psig}$)
- **Stage 1 (R-401)**: $\text{NiMo}/\text{Al}_2\text{O}_3$ catalyst for Hydrodenitrogenation (HDN, $N < 10\ \text{ppm}$) and Hydrodesulfurization (HDS, $S < 15\ \text{ppm}$).
- **Stage 2 (R-402)**: Noble metal / USY Zeolite for multi-bed cracked hydrocarbon conversion with cold hydrogen quench zones.
- **Hydrogen Consumption**: $2.42\ \text{wt}\%$ of feed.
- **Yield Structure**: Ultra-Low Sulfur Diesel ($48.4\ \text{wt}\%$, Cetane Index $58.5$, $S < 8\ \text{ppm}$), Jet/Kerosene ($24.2\ \text{wt}\%$), Naphtha ($18.1\ \text{wt}\%$), Unconverted Oil ($9.3\ \text{wt}\%$ recycle).

### 4. Delayed Coker Unit (DCU) Cyclic Dynamics
- **Thermal Pyrolysis**: Furnace coil outlet at $495\ ^\circ\text{C}$ with anti-fouling velocity steam injection.
- **Twin Drum Cycle (24 h)**: Drum A in filling/coking mode ($460\ ^\circ\text{C}$, $2.2\ \text{bar}$); Drum B in decoking/steam-out/quench/cutting sequence.
- **Hydraulic Decoking**: Water jet cutting tool operating at $250\ \text{bar}$ ($3,600\ \text{psi}$) dislodging solid anode-grade pet-coke into coke pit.
- **Yields**: Anode/Sponge Coke ($32.4\ \text{wt}\%$), Heavy Coker Gas Oil ($48.1\ \text{wt}\%$ routed to HCU), Naphtha ($12.2\ \text{wt}\%$), Gas ($7.3\ \text{wt}\%$).

### 5. API 521 Flare Thermal Radiation Dispersion Physics
Point-source thermal radiation flux $K\ (\text{kW/m}^2)$ at radial distance $R$ from a $90\ \text{m}$ elevated flare stack:
$$K(R) = \frac{\tau \cdot F \cdot Q}{4 \pi (R^2 + H_{\text{stack}}^2)}$$
Where atmospheric transmissivity $\tau = 0.85$, emissivity fraction $F = 0.25$, and emergency depressuring heat release $Q = 450\ \text{MW}$.
- **$K = 9.46\ \text{kW/m}^2$**: Maximum permissible on equipment structures (escape time $< 30\ \text{s}$).
- **$K = 4.73\ \text{kW/m}^2$**: API 521 limit at plant sterile radius ($R = 150\ \text{m}$ perimeter exclusion zone).
- **$K = 1.58\ \text{kW/m}^2$**: Unrestricted public access / control room boundary.

---

## 📐 SolidWorks Mechanical Detailing & ASME BPVC Compliance

The mechanical architecture adheres strictly to ASME BPVC Section VIII Division 1 & 2 and API standards:

```
                          ASME BPVC SECTION VIII SHELL THICKNESS:
                                    P · R_i
                          t = ─────────────────── + C_A
                                S · E - 0.6 · P
```

- **Atmospheric Column (C-101)**:
  - Height: $54.0\ \text{m}$ | Inner Diameter: $5.20\ \text{m}$
  - Trays: 48 316L SS valve trays (weir height $50\ \text{mm}$, downcomer clearance $38\ \text{mm}$).
  - Shell Material: ASTM A516 Gr 70 Carbon Steel with $3.0\ \text{mm}$ 316L SS cladding in sour zones.
  - Calculated Shell Thickness: $24\ \text{mm}$ base, tapering to $16\ \text{mm}$ top.
- **Vacuum Column (C-201)**:
  - Height: $44.0\ \text{m}$ | Lower ID: $4.50\ \text{m}$ | Upper Flash Zone Bulb ID: $7.20\ \text{m}$.
  - Deep-cut structured packing (Mellapak 250X) with external vacuum stiffening rings per ASME BPVC Sec VIII Div 1 UG-29.
- **Hydrocracker Reactor (R-401/402)**:
  - Wall Thickness: $240\ \text{mm}$ ($9.45\ \text{in}$) forged 2.25Cr-1Mo-0.25V steel with $5\ \text{mm}$ 347 SS overlay to eliminate high-temperature hydrogen attack (Nelson Curves).
- **Crude Storage Tankage (T-101 to T-104)**:
  - API 650 Welded Steel Tanks for Oil Storage: $50,000\ \text{m}^3$ each, external floating roof with mechanical shoe seal and $110\%$ containment bunds.

---

## 🤖 Gazebo 3D Simulation & ODE Engine Integration

The virtual plant is packaged in `gazebo_simulation/worlds/refinery_complex.world` and rendered in 3D:

- **Physics Engine**: Open Dynamics Engine (ODE) configured for high-fidelity rigid-body dynamics:
  - Max step size: `0.001 s` ($1\ \text{kHz}$)
  - ERP (Error Reduction Parameter): `0.2`
  - CFM (Constraint Force Mixing): `1e-5`
- **Spatial Plot Plan**: $600\ \text{m} \times 400\ \text{m}$ refinery battery limits:
  - `cdu_column`: `[-120.0, 45.0, 0.0]`
  - `vdu_column`: `[-60.0, 45.0, 0.0]`
  - `fccu_riser_regenerator`: `[10.0, 50.0, 0.0]`
  - `hydrocracker_reactors`: `[85.0, 50.0, 0.0]`
  - `coker_twin_drums`: `[85.0, -45.0, 0.0]`
  - `crude_tank_farm`: `[-100.0, -50.0, 0.0]`
  - `central_control_room`: `[10.0, -30.0, 0.0]`
  - `elevated_flare_stack`: `[160.0, 60.0, 0.0]`
- **Virtual Sensors**:
  - 16-beam 3D LiDAR for structural deflection and pipe rack sagging inspection.
  - FLIR Thermal IR camera for furnace refractory hot-spot monitoring ($8-14\ \mu\text{m}$).
  - Electrochemical and catalytic gas sensors for hazardous $\text{H}_2\text{S}$ and LEL hydrocarbon leak tracking.

---

## 🌐 ROS 2 Distributed Architecture & Topic Topology

The ROS 2 package `virtual_refinery` implements the ISA-95 control hierarchy through deterministic message passing:

```
               ┌────────────────────────┐
               │  refinery_orchestrator │ ◄── Service: /refinery/step_simulation
               └───────────┬────────────┘
                           │ Synchronous Step Clock (100 Hz)
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
     ┌─────────────┐┌─────────────┐┌─────────────┐
     │   cdu_vdu   ││ conversion  ││   stream    │
     │  simulator  ││    units    ││   router    │
     └──────┬──────┘└──────┬──────┘└──────┬──────┘
            │              │              │
            ▼              ▼              ▼
   /refinery/streams/  /refinery/streams/ /refinery/blends/
        cdu_vdu          conversion          final
            │              │              │
            └──────────────┼──────────────┘
                           │ Process Telemetry
            ┌──────────────┴──────────────┐
            ▼                             ▼
   ┌───────────────────┐        ┌───────────────────┐
   │process_safety_sis │        │   gazebo_bridge   │
   └────────┬──────────┘        └─────────┬─────────┘
            │                             │
            ▼                             ▼
   /refinery/emergency_trip     /gazebo/model_states
```

### ROS 2 Message Definitions
- **`ProcessStream.msg`**: Mass flow rate ($\text{kg/h}$), temperature ($^\circ\text{C}$), pressure ($\text{bar}$), phase, enthalpy ($\text{kJ/kg}$), and 12-component hydrocarbon mass fractions.
- **`UnitTelemetry.msg`**: Unit ID, operating pressure, tray temperature vector, differential pressure, level %, and interlock state.
- **`ValveCommand.msg`**: Valve tag, demand position ($0-100\%$), slew rate, and override trip commands.
- **`EmergencyTrip.msg`**: Trip ID, cause string, high-priority timestamp, and tripped valve isolation list.
- **`SetCutPoints.srv`**: Runtime service enabling dynamic adjustment of CDU/VDU cut temperatures to observe yield redistribution.

---

## 🛡️ Process Safety, Protection Layers & SIS Cause-and-Effect

The digital twin models a 7-layer **Layer of Protection Analysis (LOPA)** architecture per IEC 61508 / IEC 61511:

| Trip Loop | Initiating Condition | Sensor Voting | Target SIL | Executive Automated Action |
|---|---|---|---|---|
| **ESD-101** | CDU Overpressure ($PT > 3.5\ \text{bar(g)}$) | 2oo3 Transmitters | SIL 2 | Cut fuel gas XV-101 to heater H-101 in $<2.0\ \text{s}$; trip crude charge pumps P-101A/B; open flare depressuring valve XV-102. |
| **ESD-201** | VDU Furnace Loss of Flow ($FT < 60\%$) | 1oo2 Transmitters | SIL 3 | Trip vacuum heater burners; inject emergency steam into coil passes to prevent tube coking/rupture. |
| **ESD-301** | FCC Riser Thermal Runaway ($TT > 560\ ^\circ\text{C}$) | 2oo3 Transmitters | SIL 3 | Slam shut regenerated catalyst slide valve in $<1.0\ \text{s}$; activate lift-steam quench. |
| **ESD-401** | Hydrocracker Loop Overpressure ($PT > 170\ \text{bar}$) | 2oo3 Transmitters | SIL 3 | Trip recycle $\text{H}_2$ compressor C-401; open twin fail-open depressuring valves to flare ($155\ \text{bar} \to 10\ \text{bar}$ in $15\ \text{min}$ per API 521). |

---

## 📊 Complete Engineering Drawing Catalog (ISO A4)

All engineering drawings have been prepared, audited, and rendered in high-resolution vector PDF and PNG formats within `CAD_Drawings/`:

| Drawing No. | Drawing Title | Scale | File Links |
|---|---|---|---|
| **JU/ChE/VP/DWG-01** | Refinery Block Flow Diagram & Plant-Wide Mass Balance | Diagrammatic | [PDF](CAD_Drawings/01_Refinery_Block_Flow_Diagram_BFD_Mass_Balance.pdf) \| [PNG](CAD_Drawings/01_Refinery_Block_Flow_Diagram_BFD_Mass_Balance.png) |
| **JU/ChE/VP/DWG-02** | CDU & VDU Fractionation & Cut-Point Profiles | Graphical | [PDF](CAD_Drawings/02_CDU_VDU_Fractionation_CutPoints_Process_CAD.pdf) \| [PNG](CAD_Drawings/02_CDU_VDU_Fractionation_CutPoints_Process_CAD.png) |
| **JU/ChE/VP/DWG-03** | FCCU, Hydrocracker & Delayed Coker Conversion Flowsheet | Diagrammatic | [PDF](CAD_Drawings/03_FCCU_Hydrocracker_Delayed_Coker_Conversion_CAD.pdf) \| [PNG](CAD_Drawings/03_FCCU_Hydrocracker_Delayed_Coker_Conversion_CAD.png) |
| **JU/ChE/VP/DWG-04** | Refinery Plant Plot Plan & Gazebo 3D Layout | 1 : 2500 | [PDF](CAD_Drawings/04_Refinery_Plant_Plot_Plan_Gazebo_General_Arrangement_CAD.pdf) \| [PNG](CAD_Drawings/04_Refinery_Plant_Plot_Plan_Gazebo_General_Arrangement_CAD.png) |
| **JU/ChE/VP/DWG-05** | ROS 2 Digital Twin & Industrial Automation Architecture | Architectural | [PDF](CAD_Drawings/05_ROS2_Digital_Twin_Industrial_Automation_Architecture_CAD.pdf) \| [PNG](CAD_Drawings/05_ROS2_Digital_Twin_Industrial_Automation_Architecture_CAD.png) |
| **JU/ChE/VP/DWG-06** | Process Dynamics, Protection Layers & Flare Safety System | Analytic | [PDF](CAD_Drawings/06_Process_Dynamics_Protection_Layers_Flare_Safety_CAD.pdf) \| [PNG](CAD_Drawings/06_Process_Dynamics_Protection_Layers_Flare_Safety_CAD.png) |

---

## 🚀 Build, Simulation & Execution Guide

### 1. Rebuild All CAD Engineering Drawings
```bash
# Verify Python 3 dependencies (matplotlib, numpy)
py build_all_refinery_drawings.py

# Run QA/QC drawing audit
py scripts/audit_refinery_drawings.py
```

### 2. Launching Gazebo 3D Simulation
```bash
# Ensure Gazebo 11 or Gazebo Fortress is installed
gazebo gazebo_simulation/worlds/refinery_complex.world
```

### 3. Compiling & Running ROS 2 Digital Twin
```bash
# Source ROS 2 Humble/Iron
source /opt/ros/humble/setup.bash

# Build the ROS 2 workspace
cd ros2_ws
colcon build --symlink-install
source install/setup.bash

# Launch complete virtual refinery twin
ros2 launch virtual_refinery refinery_simulation.launch.py
```

### 4. Dynamic Cut-Point Optimization via ROS 2 CLI
```bash
# Shift CDU cut-points to maximize kerosene/jet production:
ros2 service call /refinery/set_cut_points virtual_refinery/srv/SetCutPoints "{cdu_naphtha_cut_c: 140.0, cdu_kerosene_cut_c: 260.0, cdu_diesel_cut_c: 360.0}"
```

---

## 📜 Intellectual Property, Copyright & Educational License

```
========================================================================================
VIRTUAL PETROLEUM REFINERY DIGITAL TWIN (VIRTUAL-PLANT)
Copyright (c) 2026 Sourish Senapati. All Rights Reserved.
Department of Chemical Engineering, Jadavpur University, Kolkata, India.
========================================================================================
```

This repository is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)** and the **Educational Non-Commercial Source License**.

### Terms of Use:
- **Educational and Academic Use**: Permitted free of charge for non-commercial educational instruction, student research, and academic evaluation, **provided that full and prominent credit and citation is given to Sourish Senapati**.
- **Commercial Use Strictly Prohibited**: No part of this repository, including CAD specifications, kinetics codes, ROS 2 nodes, simulation worlds, or engineering drawings, may be used, distributed, sublicensed, or integrated into commercial software without prior written authorization from Sourish Senapati.
- **Mandatory Attribution**:
  ```
  Senapati, Sourish. (2026). Virtual Petroleum Refinery Digital Twin: SolidWorks CAD,
  Gazebo ODE Simulation, and ROS 2 Industrial Automation.
  Department of Chemical Engineering, Jadavpur University.
  GitHub: https://github.com/SourishSenapati/VIRTUAL-PLANT
  ```
