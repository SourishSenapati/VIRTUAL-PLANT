/**
 * Authoritative Process, Kinetic, Mechanical & Piping Master Dataset
 * Ethylene Oxide Packed-Bed Tubular Reactor (R-201)
 * Lead Process & Mechanical Engineer: Sourish Senapati (Roll: 002310301035)
 * Jadavpur University
 */

export const REACTOR_SPECS = {
  tag: "R-201",
  name: "Ethylene Oxide Packed-Bed Tubular Reactor",
  code: "ASME Section VIII Division 1 / TEMA Class R",
  flangeStandard: "ASME B16.5 Class 300 WNRF",
  instrumentStandard: "ISA-5.1 Documentation Standard",
  author: "Sourish Senapati (Roll: 002310301035)",
  institution: "Department of Chemical Engineering, Jadavpur University",
  reaction: "C2H4 + 0.5 O2 -> C2H4O (ΔHR = -105.7 kJ/mol)",
  catalyst: "Ag / α-Al2O3 Spheres (Dp = 0.50 in = 12.7 mm)",
  bulkDensity: "70.0 lb/ft³ (1,121.29 kg/m³)",
  voidFraction: 0.50,
  
  // Solved Problem R2 Results
  feedEthylene: "3,240 lbmol/h (0.90 lbmol/s = 25.25 kg/s)",
  targetConversion: "40.0% (XA = 0.40)",
  inletPressure: "25.00 atm (367.4 psia / 2.533 MPa)",
  exitPressure: "20.998 atm (308.59 psia / 2.128 MPa)",
  pressureDrop: "4.002 atm (58.81 psi / 0.405 MPa)",
  catalystWeight: "26,469.02 lb (12,006.16 kg)",
  idealCatalystWeight: "24,390.55 lb (11,063.38 kg)",
  catalystPenalty: "+8.52% (Due to Ergun friction momentum loss)",
  netExpansion: "+12.02% (v/v0 = 1.1202)",
  reactionDuty: "17.26 MW (58.89 MMBtu/h)",
  
  // Dimensions
  shellID: '84.00 in (2,133.6 mm)',
  shellOD: '86.25 in (2,190.75 mm)',
  shellThickness: '1.125 in (28.58 mm SA-516 Gr 70)',
  shellMinRequired: '0.761 in (Safety Factor = 1.48)',
  shellLength: '30.00 ft (9,144.0 mm)',
  tubesheetThickness: '3.75 in (95.25 mm Forged SA-266 Cl 2)',
  tubeCount: '1,021 Seamless Tubes',
  tubeSpec: '1.5-in Schedule 80 SA-213 TP304 Stainless',
  tubeOD: '1.900 in (48.26 mm)',
  tubeID: '1.500 in (38.10 mm)',
  tubeWall: '0.200 in (5.08 mm)',
  tubePitch: '2.375 in (60.325 mm) Equilateral Triangular (30°)',
  otl: '81.25 in (2,063.75 mm)',
  baffleCount: '9 Transverse Segmental Baffles (20% Cut)',
  baffleSpacing: '36.00 in (914.4 mm)',
  skirtHeight: '8.00 ft (2,438.4 mm)',
  skirtThickness: '0.75 in (19.05 mm SA-36)',
  baseRingOD: '102.25 in (2,597.15 mm)',
  baseRingThickness: '1.50 in (38.10 mm)',
  anchorBolts: '24x M36 (SA-193 B7) on 94.0 in Bolt Circle',
  
  // Coolant
  coolantFluid: 'Dowtherm A Synthetic Thermal Oil',
  coolantFlow: '420 gpm (4,723,650 lb/h)',
  coolantInletTemp: '255 °C (491 °F)',
  coolantOutletTemp: '270 °C (518 °F)',
  coolantPressure: '140 psig (9.65 bar)'
};

export const NOZZLE_SCHEDULE = [
  { tag: "N1", size: '16" NPS', rating: "300# WNRF", service: "Feed Gas Inlet", elevation: "+9.677 m", orient: "Top Head Apex", material: "SA-106 Gr B / SA-105" },
  { tag: "N2", size: '16" NPS', rating: "300# WNRF", service: "Product Gas Outlet", elevation: "-0.533 m", orient: "Bottom Head Apex", material: "SA-106 Gr B / SA-105" },
  { tag: "N3", size: '10" NPS', rating: "300# WNRF", service: "Dowtherm A Coolant In", elevation: "+0.850 m", orient: "0° (Side Shell)", material: "SA-106 Gr B / SA-105" },
  { tag: "N4", size: '10" NPS', rating: "300# WNRF", service: "Dowtherm A Coolant Out", elevation: "+8.300 m", orient: "180° (Side Shell)", material: "SA-106 Gr B / SA-105" },
  { tag: "N5", size: '4" NPS', rating: "300# WNRF", service: "PSV Safety Relief Valve", elevation: "+9.350 m", orient: "270° (Top Channel)", material: "SA-106 Gr B / SA-105" },
  { tag: "N6", size: '3" NPS', rating: "300# WNRF", service: "Catalyst Dump & Drain", elevation: "-0.533 m", orient: "Bottom Head Tangent", material: "SA-106 Gr B / SA-105" },
  { tag: "TI-1..10", size: '2" NPS', rating: "300# WNRF", service: "10-Zone Thermowell Flange", elevation: "+9.400 m", orient: "Top Head 45°", material: "SA-182 F304" }
];

export const LINE_LIST = [
  { line: 'L-201-16"-HC-01', from: "KO-201 Knockout Drum", to: "R-201 Nozzle N1", size: '16"', sched: "Sch 40", rating: "300#", fluid: "Ethylene / Air Feed", p: "367.4 psia", t: "260 °C" },
  { line: 'L-202-16"-HC-02', from: "R-201 Nozzle N2", to: "Downstream Quench Absorber", size: '16"', sched: "Sch 40", rating: "300#", fluid: "Ethylene Oxide Product Gas", p: "308.6 psia", t: "260 °C" },
  { line: 'L-203-10"-DT-03', from: "P-201A/B Coolant Pumps", to: "R-201 Nozzle N3", size: '10"', sched: "Sch 40", rating: "300#", fluid: "Dowtherm A Coolant Supply", p: "140 psig", t: "255 °C" },
  { line: 'L-204-10"-DT-04', from: "R-201 Nozzle N4", to: "E-201 Steam Generator / Cooler", size: '10"', sched: "Sch 40", rating: "300#", fluid: "Dowtherm A Return", p: "125 psig", t: "270 °C" },
  { line: 'L-205-4"-PSV-05', from: "R-201 Nozzle N5", to: "Flare Relief Header", size: '4"', sched: "Sch 80", rating: "300#", fluid: "Overpressure Relief Gas", p: "300 psig Set", t: "350 °C" },
  { line: 'L-206-4"-PSE-06', from: "R-201 Nozzle N6", to: "Atmospheric Vent Stack", size: '4"', sched: "Sch 80", rating: "300#", fluid: "Rupture Disc Relief", p: "315 psig Burst", t: "350 °C" },
  { line: 'L-207-3"-DR-07', from: "R-201 Shell Bottom Drain", to: "Dowtherm Storage Sump", size: '3"', sched: "Sch 80", rating: "300#", fluid: "Dowtherm A Drain", p: "Hydrostatic", t: "Amb" },
  { line: 'L-208-3"-VT-08', from: "R-201 Shell Top Vent", to: "Thermal Vent Condenser", size: '3"', sched: "Sch 80", rating: "300#", fluid: "Nitrogen Purge & Deaeration", p: "15 psig", t: "Amb" }
];

export const VALVE_SCHEDULE = [
  { tag: "FCV-201", line: 'L-201', size: '16"', type: "Globe Control Valve", rating: "Class 300#", fail: "Fail Closed (FC)", actuator: "Pneumatic Diaphragm", func: "Feed Flow Rate Control (3,240 lbmol/h)" },
  { tag: "TCV-201", line: 'L-203', size: '10"', type: "3-Way Diverter Valve", rating: "Class 300#", fail: "Fail Safe (Max Cooling)", actuator: "Electro-Hydraulic", func: "Reactor Coolant Temperature Bypass" },
  { tag: "PSV-201A", line: 'L-205', size: '4" x 6"', type: "Pilot-Operated Relief Valve", rating: "300# x 150#", fail: "Spring Open", actuator: "Pilot Operated", func: "Reactor Top Channel Overpressure (300 psig)" },
  { tag: "PSV-201B", line: 'L-205', size: '4" x 6"', type: "Pilot-Operated Relief Valve", rating: "300# x 150#", fail: "Spring Open", actuator: "Pilot Operated", func: "100% Installed Spare Relief Valve" },
  { tag: "PSE-201", line: 'L-206', size: '4"', type: "Buckling Pin Rupture Disc", rating: "Class 300#", fail: "Burst Open", actuator: "Passive Rupture", func: "Secondary Runaway Reaction Protection (315 psig)" },
  { tag: "XV-201", line: 'L-201', size: '16"', type: "Full-Bore Ball Valve (ESD)", rating: "Class 300#", fail: "Fail Closed (FC)", actuator: "Pneumatic Spring-Return", func: "Emergency Shutdown Feed Isolation" },
  { tag: "XV-202", line: 'L-202', size: '16"', type: "Full-Bore Ball Valve (ESD)", rating: "Class 300#", fail: "Fail Closed (FC)", actuator: "Pneumatic Spring-Return", func: "Emergency Shutdown Effluent Isolation" },
  { tag: "HV-201", line: 'L-207', size: '3"', type: "Gate Valve (Double Block)", rating: "Class 300#", fail: "Manual", actuator: "Handwheel", func: "Shell Dowtherm A Drain Isolation" },
  { tag: "HV-202", line: 'L-208', size: '3"', type: "Globe Valve (Needle Trim)", rating: "Class 300#", fail: "Manual", actuator: "Handwheel", func: "Shell High-Point Vent Isolation" }
];

export const INSTRUMENT_INDEX = [
  { tag: "FIT-201", loop: "F-201", var: "Flow Rate", range: "0 - 4,000 lbmol/h", type: "Venturi Differential Pressure (4-20mA HART)", loc: "L-201 Inlet Feed Header" },
  { tag: "PIT-201", loop: "P-201", var: "Inlet Pressure", range: "0 - 35 atm", type: "Smart Piezo-Resistive Transmitter", loc: "R-201 Top Channel" },
  { tag: "PIT-202", loop: "P-202", var: "Discharge Pressure", range: "0 - 35 atm", type: "Smart Piezo-Resistive Transmitter", loc: "R-201 Bottom Channel" },
  { tag: "PDIT-201", loop: "P-201", var: "Reactor Bed DP", range: "0 - 8 atm", type: "Differential Pressure Transmitter (Ergun Monitoring)", loc: "Across Upper/Lower Tubesheets" },
  { tag: "TIT-201A..J", loop: "T-201", var: "Axial Bed Temp", range: "0 - 400 °C", type: "10-Zone Multipoint Thermocouple Array (Pt100/Type K)", loc: "Reactor Centerline Tube Guide" },
  { tag: "TIT-202", loop: "T-202", var: "Coolant In Temp", range: "0 - 350 °C", type: "Duplex RTD Class A", loc: "Line L-203 (Shell Coolant In)" },
  { tag: "TIT-203", loop: "T-203", var: "Coolant Out Temp", range: "0 - 350 °C", type: "Duplex RTD Class A", loc: "Line L-204 (Shell Coolant Out)" },
  { tag: "FIT-202", loop: "F-202", var: "Coolant Flow Rate", range: "0 - 600 gpm", type: "Coriolis Mass Flow Meter", loc: "Line L-203 Discharge" },
  { tag: "LIT-201", loop: "L-201", var: "Coolant Level", range: "0 - 10 m", type: "Guided Wave Radar Level Transmitter", loc: "R-201 Shell Expansion Dome" },
  { tag: "AIT-201", loop: "A-201", var: "Effluent C2H4O", range: "0 - 100 mol%", type: "On-Line Process Gas Chromatograph", loc: "Line L-202 Effluent Sample Line" }
];
