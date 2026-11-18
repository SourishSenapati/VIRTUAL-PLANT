import React from 'react';
import { Download, FileBox, FileCode2, Image, Layers, CheckCircle2 } from 'lucide-react';

export default function EngineeringAssetDownloader() {
  const assets = [
    {
      category: "Native SolidWorks 2025 CAD Models",
      icon: Layers,
      items: [
        { name: "R201_Ethylene_Oxide_Reactor_Master.SLDASM", path: "/cad/sldasm/R201_Ethylene_Oxide_Reactor_Master.SLDASM", size: "25.9 KB", desc: "Master assembly with shell, 1,021 tubes, tubesheets, 9 baffles, and skirt" },
        { name: "R201_Vessel_Pressure_Shell.SLDPRT", path: "/cad/sldprt/R201_Vessel_Pressure_Shell.SLDPRT", size: "46.0 KB", desc: "Pressure shell (84\" ID x 1.125\" thk) and 2:1 ellipsoidal heads in SA-516 Gr 70" },
        { name: "R201_Tubesheets_Pair.SLDPRT", path: "/cad/sldprt/R201_Tubesheets_Pair.SLDPRT", size: "88.5 KB", desc: "Forged tubesheets (3.75\" thk, SA-266 Cl 2) with triangular tube pattern" },
        { name: "R201_Schedule80_Catalyst_Tube.SLDPRT", path: "/cad/sldprt/R201_Schedule80_Catalyst_Tube.SLDPRT", size: "36.4 KB", desc: "1.5\" Sch 80 seamless tube (Do=1.900\", SA-213 TP304, 30.0 ft length)" },
        { name: "R201_Transverse_Segmental_Baffle.SLDPRT", path: "/cad/sldprt/R201_Transverse_Segmental_Baffle.SLDPRT", size: "49.8 KB", desc: "20% cut transverse baffle plate (0.50\" thk, 6x tie-rod holes, SA-516)" },
        { name: "R201_Skirt_Support_BaseRing.SLDPRT", path: "/cad/sldprt/R201_Skirt_Support_BaseRing.SLDPRT", size: "69.9 KB", desc: "8 ft cylindrical skirt, 1.5\" base ring, and 24x M36 anchor bolt chairs" },
        { name: "R201_Nozzle_Flange_Subassembly.SLDPRT", path: "/cad/sldprt/R201_Nozzle_Flange_Subassembly.SLDPRT", size: "130.6 KB", desc: "16\", 10\", 4\" ASME B16.5 Class 300 WNRF flanged process nozzles" }
      ]
    },
    {
      category: "Standard ISO 10303-21 STEP AP214 Models",
      icon: FileBox,
      items: [
        { name: "R201_Ethylene_Oxide_Reactor_Assembly.step", path: "/step/R201_Ethylene_Oxide_Reactor_Assembly.step", size: "307.6 KB", desc: "Complete master B-Rep solid assembly (4,138 valid entities, zero mocks)" },
        { name: "R201_Nozzle_Flange_Subassembly.step", path: "/step/R201_Nozzle_Flange_Subassembly.step", size: "207.1 KB", desc: "ASME B16.5 300# flanged nozzle bodies in standard STEP format" },
        { name: "R201_Skirt_Support_BaseRing.step", path: "/step/R201_Skirt_Support_BaseRing.step", size: "23.0 KB", desc: "Support skirt & base ring with anchor holes" },
        { name: "R201_Vessel_Pressure_Shell.step", path: "/step/R201_Vessel_Pressure_Shell.step", size: "17.2 KB", desc: "Solid cylinder shell & 2:1 ellipsoidal heads" },
        { name: "R201_Schedule80_Catalyst_Tube.step", path: "/step/R201_Schedule80_Catalyst_Tube.step", size: "17.2 KB", desc: "Schedule 80 seamless tube STEP geometry" }
      ]
    },
    {
      category: "Standard 2D Vector DXF Blueprints (A1 Scale)",
      icon: FileCode2,
      items: [
        { name: "R201_Elevation_Cross_Section.dxf", path: "/dxf/R201_Elevation_Cross_Section.dxf", size: "34.6 KB", desc: "Full GA sectional elevation, shell, heads, nozzles N1-N5, skirt, and dimensions" },
        { name: "R201_Tubesheet_Drilling_Pattern.dxf", path: "/dxf/R201_Tubesheet_Drilling_Pattern.dxf", size: "183.2 KB", desc: "1,015 tube holes on 2.375\" triangular pitch inside 81.25\" OTL, 6x tie rods" },
        { name: "R201_Piping_PID_Flowsheet.dxf", path: "/dxf/R201_Piping_PID_Flowsheet.dxf", size: "28.2 KB", desc: "Full ISA-5.1 P&ID flowsheet with control loops (FCV, TCV, PIT, TIT, PSV)" }
      ]
    },
    {
      category: "Official 5-Sheet Drawing Prints (Vector PDF)",
      icon: Image,
      items: [
        { name: "01_Ethylene_Oxide_Reactor_General_Arrangement_Elevation_CAD.pdf", path: "/drawings/01_Ethylene_Oxide_Reactor_General_Arrangement_Elevation_CAD.pdf", size: "303.7 KB", desc: "Sheet 01: General Arrangement & Sectional Elevation" },
        { name: "02_Ethylene_Oxide_Reactor_Process_PID_Instrumentation_CAD.pdf", path: "/drawings/02_Ethylene_Oxide_Reactor_Process_PID_Instrumentation_CAD.pdf", size: "49.5 KB", desc: "Sheet 02: Process P&ID with ISA-5.1 Instrumentation Loops" },
        { name: "03_Ethylene_Oxide_Reactor_Mechanical_Fabrication_Details_CAD.pdf", path: "/drawings/03_Ethylene_Oxide_Reactor_Mechanical_Fabrication_Details_CAD.pdf", size: "34.8 KB", desc: "Sheet 03: Mechanical Fabrication & ASME Sec VIII Div 1 Details" },
        { name: "04_Ethylene_Oxide_Reactor_Kinetic_Hydraulic_Performance_Curves_CAD.pdf", path: "/drawings/04_Ethylene_Oxide_Reactor_Kinetic_Hydraulic_Performance_Curves_CAD.pdf", size: "65.1 KB", desc: "Sheet 04: Reaction Kinetics & Hydraulic Performance Curves" },
        { name: "05_Ethylene_Oxide_Reactor_3D_Isometric_Plant_Assembly_CAD.pdf", path: "/drawings/05_Ethylene_Oxide_Reactor_3D_Isometric_Plant_Assembly_CAD.pdf", size: "52.4 KB", desc: "Sheet 05: 3D Isometric Plant Integration & Piping Layout" }
      ]
    }
  ];

  return (
    <div className="w-full h-full p-6 bg-[#0A0D14] overflow-y-auto space-y-6">
      <div className="border-b border-[#222C3D] pb-4 flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-lg font-bold text-white flex items-center gap-2">
            <Download className="w-5 h-5 text-[#00B4D8]" />
            Authoritative Engineering CAD & Drawing Asset Center
          </h2>
          <p className="text-xs text-[#94A3B8] mt-1 font-mono">
            Direct access to genuine SolidWorks 2025 native parts, ISO STEP AP214 models, layered A1 DXF files, and vector PDFs.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {assets.map((grp) => {
          const Icon = grp.icon;
          return (
            <div key={grp.category} className="bg-[#101520] border border-[#222C3D] rounded-xl p-5 space-y-3">
              <div className="flex items-center gap-2 text-sm font-bold text-white border-b border-[#222C3D] pb-2">
                <Icon className="w-4 h-4 text-[#00B4D8]" />
                {grp.category}
              </div>

              <div className="space-y-2">
                {grp.items.map((item) => (
                  <div
                    key={item.name}
                    className="p-3 bg-[#131926] border border-[#222C3D] rounded-lg hover:border-[#00B4D8]/50 transition-all flex items-center justify-between gap-3 text-xs"
                  >
                    <div className="overflow-hidden">
                      <div className="font-bold font-mono text-[#E2E8F0] truncate">{item.name}</div>
                      <div className="text-[10px] text-[#94A3B8] mt-0.5">{item.desc}</div>
                    </div>
                    <a
                      href={item.path}
                      download
                      className="px-3 py-1.5 bg-[#00B4D8]/10 hover:bg-[#00B4D8] border border-[#00B4D8]/40 hover:border-[#00B4D8] text-[#00B4D8] hover:text-[#0A0D14] font-bold font-mono rounded transition-all flex items-center gap-1.5 shrink-0"
                    >
                      <Download className="w-3.5 h-3.5" />
                      {item.size}
                    </a>
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
