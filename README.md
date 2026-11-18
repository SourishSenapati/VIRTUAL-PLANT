# Virtual Petroleum Refinery & Petrochemical Plant Digital Twin (`VIRTUAL-PLANT`)

[![Educational License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)
[![Author: Sourish Senapati](https://img.shields.io/badge/Author-Sourish%20Senapati-blue.svg)](https://github.com/SourishSenapati)
[![Institution: Jadavpur University](https://img.shields.io/badge/Institution-Jadavpur%20University-crimson.svg)](http://www.jaduniv.edu.in/)
[![Department: Chemical Engineering](https://img.shields.io/badge/Department-Chemical%20Engineering-darkgreen.svg)](http://www.jaduniv.edu.in/)
[![Roll: 002310301035](https://img.shields.io/badge/Roll-002310301035-orange.svg)](https://github.com/SourishSenapati)
[![Simulator Engine: Three.js WebGL & React 19](https://img.shields.io/badge/Simulator-Three.js%20%7C%20WebGL-blueviolet.svg)](https://threejs.org/)
[![Physics Engine: Gazebo ODE](https://img.shields.io/badge/Gazebo-ODE%20Physics-blueviolet.svg)](https://gazebosim.org/)
[![Middleware: ROS 2 Humble/Iron](https://img.shields.io/badge/ROS%202-Humble%20%2F%20Iron-brightgreen.svg)](https://docs.ros.org/)
[![Design Standards: ASME BPVC & API](https://img.shields.io/badge/Standards-ASME%20BPVC%20%7C%20API%20521-yellow.svg)](https://www.asme.org/)

---

## 📌 Project Architecture

The **Virtual Plant Digital Twin** (`VIRTUAL-PLANT`) is an industrial-scale simulation platform combining interactive 3D WebGL game engine visualization, robotic middleware, and rigorous process thermodynamics. Developed by **Sourish Senapati** at the **Department of Chemical Engineering, Jadavpur University**, this repository hosts the interactive plant simulator and real-time physical simulation runtime.

The repository provides three simulation tiers:
1. **Interactive 3D WebGL Plant Simulator (`plant_simulator/`)**:
   - Modern React 19 + Three.js 3D industrial graphics engine.
   - Interactive orbit, elevation, and first-person walkthrough camera modes.
   - Live Aspen HYSYS kinetic-hydraulic telemetry and stream table solvers.
   - Dynamic P&ID console with automated valve/pump instrumentation.
   - ASME Section VIII Div 1 mechanical stress and shell calculation inspector.
   - Procedural Web Audio API sound synthesis simulating industrial acoustic environments.
2. **Gazebo ODE Physics World (`gazebo_simulation/`)**:
   - Open Dynamics Engine (ODE) multi-body physical environment with collisions, inertial properties, mass distributions, and visual state rendering across a 600 m × 400 m battery limit plot plan.
3. **ROS 2 Automation Middleware (`ros2_ws/`)**:
   - Distributed node network (ROS 2 Humble/Iron) managing mass balance closure, dynamic cut-point optimization, IEC 61511 Safety Instrumented Systems (SIS), and ISA-95 Level 0–4 plant-wide automation.

---

## 🚀 Quick Start: Running the 3D Plant Simulator

The 3D interactive simulator is located in the `plant_simulator/` directory:

```bash
# Navigate to the plant simulator directory
cd plant_simulator

# Install dependencies (React 19, Three.js, Lucide Icons, Tailwind CSS)
npm install

# Start local interactive simulation server
npm run dev

# Or view production-compiled workstation build
npm run preview
```

Open `http://localhost:5173` in any modern web browser to access:
- **3D Reactor & Plant Viewport**: Rotate, pan, zoom, inspect internal cutaway catalyst tubes and baffles.
- **Process Telemetry**: Live conversion curves, axial temperature profiles ($T_{max} = 265.4^\circ\text{C}$), pressure drops ($\Delta P = 0.528\text{ bar}$), and Damköhler numbers.
- **P&ID Operations Console**: Control loops (TIC-201, PIC-201, FIC-201, LIC-201), valve positions, and safety interlocks.
- **ASME Mechanical Dossier**: Pressure vessel thickness, ligament efficiencies, nozzle compensation, and skirt wind/seismic moments.

---

## 🏭 Simulated Industrial Units

```
                                  CRUDE & PETROCHEMICAL FEEDS
                                                │
                                    ┌───────────▼───────────┐
                                    │  CRUDE DESALTER (DES) │
                                    └───────────┬───────────┘
                                                │
                        ┌───────────────────────┴───────────────────────┐
                        ▼                                               ▼
             ┌─────────────────────┐                         ┌─────────────────────┐
             │ ATMOSPHERIC (CDU)   │                         │  ETHYLENE OXIDE     │
             │ 100,000 BPD Column  │                         │  REACTOR (R-201)    │
             └──────────┬──────────┘                         │  7,654 Catalyst Tube│
                        │                                    └──────────┬──────────┘
           ┌────────────┼────────────┐                                  │
           ▼            ▼            ▼                                  ▼
      ┌─────────┐  ┌─────────┐  ┌─────────┐                  ┌─────────────────────┐
      │   VDU   │  │  FCCU   │  │ HYDRO-  │                  │ EO / GLYCOL         │
      │ Vacuum  │  │ Catalytic│ │ CRACKER │                  │ PURIFICATION TRAIN  │
      └─────────┘  └─────────┘  └─────────┘                  └─────────────────────┘
```

### 1. Ethylene Oxide Multi-Tubular Reactor (R-201)
- **Catalyst Bed**: 7,654 Schedule 80 silver-on-alumina tubes ($21.2\text{ mm ID} \times 6,700\text{ mm}$ length).
- **Cooling Medium**: Boiling DOWTHERM A eutectic liquid ($230^\circ\text{C}$, $18.8\text{ bar}$) generating $40\text{ bar}$ saturated steam.
- **Kinetics**: Parallel-consecutive catalytic epoxidation of ethylene ($C_2H_4 + \frac{1}{2}O_2 \rightarrow C_2H_4O$) with complete combustion mitigation ($C_2H_4 + 3O_2 \rightarrow 2CO_2 + 2H_2O$).

### 2. High-Conversion Petroleum Refinery
- **CDU / VDU Fractionation**: True Boiling Point distillation producing LPG, Light Naphtha, Heavy Naphtha, Kerosene/Jet-A1, Diesel, Atmospheric Gas Oil, and Vacuum Residue.
- **FCCU Weekman 4-Lump Kinetics**: Catalytic conversion of heavy gas oils into gasoline and olefins.
- **Hydrocracker & Delayed Coker**: High-pressure $155\text{ bar}$ catalytic cracking and thermal pyrolysis delayed coking.

---

## 📊 Gazebo & ROS 2 Physical Simulation

### Launching Gazebo ODE World
```bash
# Source ROS 2 environment
source /opt/ros/humble/setup.bash

# Launch the full battery-limit refinery world
ros2 launch virtual_refinery refinery_world.launch.py
```

### Running Process Automation Nodes
```bash
# Stream router & mass balance supervisor
ros2 run virtual_refinery stream_router

# Safety Instrumented System (SIS) watchdog
ros2 run virtual_refinery safety_watchdog
```

---

## 👨‍💻 Engineering Attribution
- **Author & Lead Designer**: Sourish Senapati
- **Academic Roll**: 002310301035
- **Department**: Department of Chemical Engineering, Jadavpur University
- **Repository Link**: [SourishSenapati/VIRTUAL-PLANT](https://github.com/SourishSenapati/VIRTUAL-PLANT)
