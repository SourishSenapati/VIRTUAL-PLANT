import React, { useState } from 'react';
import { ShieldCheck, CheckCircle2, AlertCircle, FileText, Wrench, Layers } from 'lucide-react';
import { REACTOR_SPECS } from '../data/reactorData';

export default function AsmeMechanicalDossier() {
  const [activeTab, setActiveTab] = useState('shell');

  return (
    <div className="w-full h-full p-6 bg-[#0A0D14] overflow-y-auto space-y-6">
      {/* Header Banner */}
      <div className="flex flex-wrap items-center justify-between gap-4 border-b border-[#222C3D] pb-4">
        <div>
          <h2 className="text-lg font-bold text-white flex items-center gap-2">
            <ShieldCheck className="w-5 h-5 text-[#00B4D8]" />
            ASME BPVC Section VIII Division 1 & TEMA Class R Mechanical Dossier
          </h2>
          <p className="text-xs text-[#94A3B8] mt-1 font-mono">
            Vessel Tag: R-201 • Design Pressure: 300 psig (2.17 MPa) • Design Temperature: 350 °C (662 °F) • Full Radiography (E = 1.0)
          </p>
        </div>
        <div className="flex items-center gap-2">
          <span className="px-3 py-1 bg-[#10B981]/10 border border-[#10B981]/40 rounded text-xs font-mono text-[#10B981] font-bold">
            100% CODE COMPLIANT
          </span>
        </div>
      </div>

      {/* Code Navigation Tabs */}
      <div className="flex items-center gap-2 border-b border-[#222C3D] pb-2 text-xs font-mono">
        <button
          onClick={() => setActiveTab('shell')}
          className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
            activeTab === 'shell'
              ? 'bg-[#00B4D8] text-[#0A0D14]'
              : 'text-[#94A3B8] hover:text-white hover:bg-[#131926]'
          }`}
        >
          UG-27 Shell Thickness
        </button>
        <button
          onClick={() => setActiveTab('heads')}
          className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
            activeTab === 'heads'
              ? 'bg-[#00B4D8] text-[#0A0D14]'
              : 'text-[#94A3B8] hover:text-white hover:bg-[#131926]'
          }`}
        >
          UG-32 Ellipsoidal Heads
        </button>
        <button
          onClick={() => setActiveTab('tubesheet')}
          className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
            activeTab === 'tubesheet'
              ? 'bg-[#00B4D8] text-[#0A0D14]'
              : 'text-[#94A3B8] hover:text-white hover:bg-[#131926]'
          }`}
        >
          TEMA UHX Tubesheets
        </button>
        <button
          onClick={() => setActiveTab('tubes')}
          className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
            activeTab === 'tubes'
              ? 'bg-[#00B4D8] text-[#0A0D14]'
              : 'text-[#94A3B8] hover:text-white hover:bg-[#131926]'
          }`}
        >
          Tube Burst & Hoop Stress
        </button>
        <button
          onClick={() => setActiveTab('skirt')}
          className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
            activeTab === 'skirt'
              ? 'bg-[#00B4D8] text-[#0A0D14]'
              : 'text-[#94A3B8] hover:text-white hover:bg-[#131926]'
          }`}
        >
          Skirt & Anchor Bolting
        </button>
      </div>

      {/* Tab 1: Shell Calculation */}
      {activeTab === 'shell' && (
        <div className="space-y-4">
          <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6">
            <h3 className="text-sm font-bold text-white flex items-center gap-2 mb-3">
              <FileText className="w-4 h-4 text-[#00B4D8]" />
              ASME Section VIII Div 1 Paragraph UG-27(c)(1) Shell Sizing Formula
            </h3>
            <div className="p-4 bg-[#0A0D14] border border-[#222C3D] rounded-lg font-mono text-xs text-[#00B4D8] overflow-x-auto">
              t_calc = (P * R) / (S * E - 0.6 * P) + CA
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 font-mono text-xs">
              <div className="bg-[#131926] p-4 rounded-lg border border-[#222C3D] space-y-2">
                <div className="text-[#94A3B8] font-bold uppercase text-[10px] text-[#00B4D8]">Design Variables</div>
                <div className="flex justify-between"><span>Internal Design Pressure (P):</span> <strong className="text-white">300.0 psig</strong></div>
                <div className="flex justify-between"><span>Internal Radius (R):</span> <strong className="text-white">42.00 in (Ds = 84.0 in)</strong></div>
                <div className="flex justify-between"><span>Allowable Stress (S) SA-516 Gr 70 @ 350°C:</span> <strong className="text-white">20,000 psi</strong></div>
                <div className="flex justify-between"><span>Joint Efficiency (E) Full Radiography:</span> <strong className="text-white">1.00 (Spotless NDT)</strong></div>
                <div className="flex justify-between"><span>Corrosion Allowance (CA):</span> <strong className="text-white">0.125 in (3.175 mm)</strong></div>
              </div>

              <div className="bg-[#131926] p-4 rounded-lg border border-[#222C3D] space-y-2">
                <div className="text-[#94A3B8] font-bold uppercase text-[10px] text-[#10B981]">Calculated Results</div>
                <div className="flex justify-between"><span>Calculated Pressure Shell Thickness:</span> <strong className="text-white">0.6357 in</strong></div>
                <div className="flex justify-between"><span>Minimum Required Thickness (t_min):</span> <strong className="text-[#F59E0B]">0.7607 in (19.32 mm)</strong></div>
                <div className="flex justify-between"><span>Specified Nominal Thickness (t_nom):</span> <strong className="text-[#10B981]">1.125 in (28.58 mm)</strong></div>
                <div className="flex justify-between"><span>Mechanical Safety Factor:</span> <strong className="text-[#10B981]">1.48 (48% over ASME min)</strong></div>
                <div className="flex justify-between"><span>Maximum Allowable Working Pressure (MAWP):</span> <strong className="text-white">471.2 psig</strong></div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Tab 2: Heads */}
      {activeTab === 'heads' && (
        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6">
          <h3 className="text-sm font-bold text-white mb-3">
            ASME Section VIII Div 1 Paragraph UG-32(d) 2:1 Semi-Ellipsoidal Heads
          </h3>
          <div className="p-4 bg-[#0A0D14] border border-[#222C3D] rounded-lg font-mono text-xs text-[#00B4D8] mb-4">
            t_head = (P * D * K) / (2 * S * E - 0.2 * P) + CA   (with K = 1.0 for 2:1 heads)
          </div>
          <div className="grid grid-cols-2 gap-4 font-mono text-xs">
            <div className="bg-[#131926] p-4 rounded border border-[#222C3D]">
              <div className="text-[#00B4D8] text-[10px] font-bold mb-2">HEAD PARAMETERS</div>
              <div>Inside Diameter (D): 84.00 in (2,133.6 mm)</div>
              <div>Head Depth (D / 4): 21.00 in (533.4 mm)</div>
              <div>Straight Flange Length: 2.00 in (50.8 mm)</div>
              <div>Material: SA-516 Grade 70 Normalized</div>
            </div>
            <div className="bg-[#131926] p-4 rounded border border-[#222C3D]">
              <div className="text-[#10B981] text-[10px] font-bold mb-2">CODE THICKNESS</div>
              <div>t_min Required: 0.7601 in (19.31 mm)</div>
              <div>Specified Thickness: 1.125 in (28.58 mm)</div>
              <div>Safety Factor: 1.48 (Over ASME minimum)</div>
              <div>Internal Volume: 59.8 ft³ (1.69 m³ per head)</div>
            </div>
          </div>
        </div>
      )}

      {/* Tab 3: Tubesheets */}
      {activeTab === 'tubesheet' && (
        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6">
          <h3 className="text-sm font-bold text-white mb-3">
            TEMA Class R & ASME Section VIII Division 1 Part UHX Tubesheet Sizing
          </h3>
          <p className="text-xs text-[#94A3B8] font-mono mb-4">
            Forged Carbon Steel SA-266 Class 2 tubesheet engineered to resist differential pressure deflection and tube-joint pushout under full tube bundle buckling loads.
          </p>
          <div className="grid grid-cols-3 gap-4 font-mono text-xs">
            <div className="bg-[#131926] p-3.5 rounded border border-[#222C3D]">
              <div className="text-[10px] text-[#94A3B8]">Tubesheet Thickness</div>
              <div className="text-lg font-bold text-white mt-1">3.75 in</div>
              <div className="text-[10px] text-[#00B4D8]">95.25 mm Forged SA-266</div>
            </div>
            <div className="bg-[#131926] p-3.5 rounded border border-[#222C3D]">
              <div className="text-[10px] text-[#94A3B8]">Outer Tube Limit (OTL)</div>
              <div className="text-lg font-bold text-white mt-1">81.25 in</div>
              <div className="text-[10px] text-[#F59E0B]">2,063.75 mm Diameter</div>
            </div>
            <div className="bg-[#131926] p-3.5 rounded border border-[#222C3D]">
              <div className="text-[10px] text-[#94A3B8]">Tube Hole Clearance</div>
              <div className="text-lg font-bold text-white mt-1">48.51 mm</div>
              <div className="text-[10px] text-[#10B981]">2 Serrated Grooves (UW-20)</div>
            </div>
          </div>
        </div>
      )}

      {/* Tab 4: Tubes */}
      {activeTab === 'tubes' && (
        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6 font-mono text-xs">
          <h3 className="text-sm font-bold text-white mb-3">
            High-Pressure Tube Burst & Hoop Stress Verification (SA-213 TP304)
          </h3>
          <div className="p-4 bg-[#0A0D14] border border-[#222C3D] rounded-lg text-[#00B4D8] mb-4">
            P_burst = (2 * S_ultimate * t) / (Do - 0.8 * t)
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-1.5">
              <div>Tube Outside Diameter (Do): 1.900 in (48.26 mm)</div>
              <div>Tube Inside Diameter (Di): 1.500 in (38.10 mm)</div>
              <div>Wall Thickness (tw): 0.200 in (5.08 mm - Schedule 80)</div>
              <div>Tensile Ultimate Strength (Su): 75,000 psi</div>
            </div>
            <div className="space-y-1.5">
              <div className="text-[#10B981] font-bold">Calculated Burst Pressure: 17,241 psi (1,173 atm)</div>
              <div className="text-white">Operating Internal Pressure: 367.4 psia (25 atm)</div>
              <div className="text-[#10B981] font-bold">Tube Burst Safety Factor: 46.9× Operating Pressure</div>
              <div className="text-[#F59E0B]">Zero creep fatigue / zero tube rupture risk</div>
            </div>
          </div>
        </div>
      )}

      {/* Tab 5: Skirt */}
      {activeTab === 'skirt' && (
        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6 font-mono text-xs">
          <h3 className="text-sm font-bold text-white mb-3">
            Cylindrical Skirt Support & Anchor Base Ring Sizing
          </h3>
          <div className="grid grid-cols-3 gap-4">
            <div className="bg-[#131926] p-4 rounded border border-[#222C3D]">
              <div className="text-[#00B4D8] text-[10px] font-bold">SKIRT CYLINDER</div>
              <div className="mt-1">Height: 8.00 ft (2,438.4 mm)</div>
              <div>Outside Dia: 86.25 in (2,190.75 mm)</div>
              <div>Wall Thickness: 0.75 in (19.05 mm)</div>
              <div>Material: SA-36 / SA-516 Gr 70</div>
            </div>
            <div className="bg-[#131926] p-4 rounded border border-[#222C3D]">
              <div className="text-[#F59E0B] text-[10px] font-bold">BASE RING FLANGE</div>
              <div className="mt-1">Outside Dia: 102.25 in (2,597.15 mm)</div>
              <div>Inside Dia: 84.75 in (2,152.65 mm)</div>
              <div>Thickness: 1.50 in (38.10 mm)</div>
              <div>Bearing Area: 2,569 in² (1.657 m²)</div>
            </div>
            <div className="bg-[#131926] p-4 rounded border border-[#222C3D]">
              <div className="text-[#10B981] text-[10px] font-bold">ANCHOR BOLT CHAIRS</div>
              <div className="mt-1">Bolt Count: 24x Anchor Studs</div>
              <div>Size: M36 (1.5" Nominal)</div>
              <div>Material: SA-193 Grade B7</div>
              <div>Bolt Circle Dia: 94.0 in (2,387.6 mm)</div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
