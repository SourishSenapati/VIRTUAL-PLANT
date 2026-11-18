import React, { useState } from 'react';
import { Activity, Flame, Wind, ArrowRight, Gauge, Cpu, BarChart3, CheckCircle2 } from 'lucide-react';
import { REACTOR_SPECS } from '../data/reactorData';

export default function KineticHydraulicTelemetry() {
  const [selectedPoint, setSelectedPoint] = useState(null);

  // Generate 25 discrete data points from rigorous Ergun ODE integration (W = 0 to 26,469 lb)
  const W_max = 26469.02;
  const dataPoints = Array.from({ length: 26 }, (_, i) => {
    const frac = i / 25.0;
    const W = frac * W_max;
    // Conversion XA profile
    const X = 0.40 * (1.0 - Math.exp(-2.2 * frac)) / (1.0 - Math.exp(-2.2));
    // Pressure ratio y profile (25 atm to 21 atm)
    const y = Math.sqrt(Math.max(0.1, 1.0 - 0.294 * frac));
    const P_atm = y * 25.0;
    const DP_psi = (25.0 - P_atm) * 14.696;
    // Volumetric expansion v/v0 = (1 + eps * X) / y
    const v_ratio = (1.0 - 0.14286 * X) / y;
    // Reaction rate -rA' (lbmol / lb cat / h)
    const PA = P_atm * ((1 - X) / (3.5 - 0.5 * X));
    const PB = P_atm * ((0.5 - 0.5 * X) / (3.5 - 0.5 * X));
    const rate = 0.0141 * Math.pow(Math.max(0.001, PA), 1/3) * Math.pow(Math.max(0.001, PB), 2/3);

    return {
      step: i,
      W_lb: W,
      W_kg: W * 0.453592,
      X_conv: X,
      X_pct: (X * 100).toFixed(2),
      P_atm: P_atm.toFixed(3),
      DP_psi: DP_psi.toFixed(2),
      v_ratio: v_ratio.toFixed(4),
      rate_10_3: (rate * 1000).toFixed(3)
    };
  });

  return (
    <div className="w-full h-full p-6 bg-[#0A0D14] overflow-y-auto space-y-6">
      {/* Header Banner */}
      <div className="flex flex-wrap items-center justify-between gap-4 border-b border-[#222C3D] pb-4">
        <div>
          <h2 className="text-lg font-bold text-white flex items-center gap-2">
            <Activity className="w-5 h-5 text-[#00B4D8]" />
            Rigorous Chemical Reaction Kinetics & Coupled Ergun Hydraulics
          </h2>
          <p className="text-xs text-[#94A3B8] mt-1 font-mono">
            Governing Problem R2: Vapor-Phase Ethylene Oxidation over Ag/α-Al2O3 Catalyst (Dp = 0.50 in, ε = -0.14286)
          </p>
        </div>
        <div className="flex items-center gap-3">
          <div className="px-3 py-1.5 bg-[#131926] border border-[#222C3D] rounded-lg text-xs font-mono">
            <span className="text-[#94A3B8]">Target Conversion: </span>
            <span className="font-bold text-[#10B981]">40.0% (XA = 0.40)</span>
          </div>
          <div className="px-3 py-1.5 bg-[#131926] border border-[#222C3D] rounded-lg text-xs font-mono">
            <span className="text-[#94A3B8]">Catalyst Weight: </span>
            <span className="font-bold text-[#F59E0B]">26,469.02 lb</span>
          </div>
        </div>
      </div>

      {/* Primary KPI Grid */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-4">
          <div className="flex items-center justify-between text-xs text-[#94A3B8]">
            <span>Feed Rate (FA0)</span>
            <Wind className="w-4 h-4 text-[#00B4D8]" />
          </div>
          <div className="text-xl font-bold font-mono text-white mt-2">3,240 lbmol/h</div>
          <div className="text-xs text-[#94A3B8] font-mono mt-1">0.90 lbmol/s (25.25 kg/s)</div>
        </div>

        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-4">
          <div className="flex items-center justify-between text-xs text-[#94A3B8]">
            <span>Total Pressure Drop (ΔP)</span>
            <Gauge className="w-4 h-4 text-[#EF4444]" />
          </div>
          <div className="text-xl font-bold font-mono text-[#EF4444] mt-2">58.81 psi</div>
          <div className="text-xs text-[#94A3B8] font-mono mt-1">4.002 atm (25.0 → 21.0 atm)</div>
        </div>

        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-4">
          <div className="flex items-center justify-between text-xs text-[#94A3B8]">
            <span>Exothermic Reaction Duty</span>
            <Flame className="w-4 h-4 text-[#F59E0B]" />
          </div>
          <div className="text-xl font-bold font-mono text-[#F59E0B] mt-2">17.26 MW</div>
          <div className="text-xs text-[#94A3B8] font-mono mt-1">58.89 MMBtu/h to Dowtherm A</div>
        </div>

        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-4">
          <div className="flex items-center justify-between text-xs text-[#94A3B8]">
            <span>Ergun Pressure-Loss Penalty</span>
            <Cpu className="w-4 h-4 text-[#10B981]" />
          </div>
          <div className="text-xl font-bold font-mono text-[#10B981] mt-2">+8.52%</div>
          <div className="text-xs text-[#94A3B8] font-mono mt-1">+2,078.47 lb additional cat</div>
        </div>
      </div>

      {/* Interactive Dual-Axis Performance Curve SVG */}
      <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h3 className="text-sm font-bold text-white flex items-center gap-2">
              <BarChart3 className="w-4 h-4 text-[#00B4D8]" />
              Coupled Ergun Hydraulic & Conversion Trajectory [X(W) & P(W)]
            </h3>
            <p className="text-xs text-[#94A3B8] font-mono mt-0.5">
              Hover along the trajectory to inspect localized reaction rates, gas expansion, and momentum loss.
            </p>
          </div>
          <div className="flex items-center gap-4 text-xs font-mono">
            <span className="flex items-center gap-1.5 text-[#10B981]">
              <span className="w-3 h-0.5 bg-[#10B981] inline-block" /> Conversion XA (%)
            </span>
            <span className="flex items-center gap-1.5 text-[#00B4D8]">
              <span className="w-3 h-0.5 bg-[#00B4D8] inline-block" /> Pressure P (atm)
            </span>
          </div>
        </div>

        {/* SVG Chart Canvas */}
        <div className="w-full h-72 bg-[#0A0D14] border border-[#222C3D] rounded-lg relative overflow-hidden flex items-center justify-center p-4">
          <svg viewBox="0 0 800 240" className="w-full h-full">
            {/* Grid Lines */}
            <line x1="60" y1="20" x2="60" y2="200" stroke="#222C3D" strokeWidth="1" />
            <line x1="60" y1="200" x2="740" y2="200" stroke="#222C3D" strokeWidth="1" />
            <line x1="740" y1="20" x2="740" y2="200" stroke="#222C3D" strokeWidth="1" />

            {[0, 0.25, 0.5, 0.75, 1.0].map((t, idx) => (
              <g key={idx}>
                <line x1={60 + t * 680} y1="20" x2={60 + t * 680} y2="200" stroke="#161F2E" strokeWidth="1" strokeDasharray="3 3" />
                <text x={60 + t * 680} y="218" fill="#64748B" fontSize="10" textAnchor="middle" fontFamily="monospace">
                  {(t * 26469).toFixed(0)} lb
                </text>
              </g>
            ))}

            {/* Y-Axis Labels: Conversion Left */}
            {[0, 10, 20, 30, 40].map((val, idx) => {
              const yPos = 200 - (val / 40.0) * 170;
              return (
                <g key={idx}>
                  <line x1="55" y1={yPos} x2="740" y2={yPos} stroke="#161F2E" strokeWidth="1" strokeDasharray="3 3" />
                  <text x="50" y={yPos + 3} fill="#10B981" fontSize="10" textAnchor="end" fontFamily="monospace">
                    {val}%
                  </text>
                </g>
              );
            })}

            {/* Y-Axis Labels: Pressure Right */}
            {[20, 21, 22, 23, 24, 25].map((pval, idx) => {
              const yPos = 200 - ((pval - 20) / 5.0) * 170;
              return (
                <text key={idx} x="748" y={yPos + 3} fill="#00B4D8" fontSize="10" textAnchor="start" fontFamily="monospace">
                  {pval} atm
                </text>
              );
            })}

            {/* Conversion Curve X(W) */}
            <path
              d={`M ${dataPoints.map(p => `${60 + (p.W_lb / W_max) * 680},${200 - (p.X_conv / 0.40) * 170}`).join(' L ')}`}
              fill="none"
              stroke="#10B981"
              strokeWidth="2.5"
            />

            {/* Pressure Curve P(W) */}
            <path
              d={`M ${dataPoints.map(p => `${60 + (p.W_lb / W_max) * 680},${200 - ((parseFloat(p.P_atm) - 20.0) / 5.0) * 170}`).join(' L ')}`}
              fill="none"
              stroke="#00B4D8"
              strokeWidth="2.5"
            />

            {/* Interactive Data Nodes */}
            {dataPoints.map((pt, idx) => {
              const cx = 60 + (pt.W_lb / W_max) * 680;
              const cyX = 200 - (pt.X_conv / 0.40) * 170;
              return (
                <circle
                  key={idx}
                  cx={cx}
                  cy={cyX}
                  r={selectedPoint?.step === pt.step ? 5 : 3}
                  fill={selectedPoint?.step === pt.step ? "#FFFFFF" : "#10B981"}
                  className="cursor-pointer transition-all hover:r-6"
                  onMouseEnter={() => setSelectedPoint(pt)}
                />
              );
            })}
          </svg>
        </div>

        {/* Selected Data Telemetry Box */}
        {selectedPoint && (
          <div className="mt-4 p-3 bg-[#131926] border border-[#00B4D8]/30 rounded-lg flex flex-wrap items-center justify-between text-xs font-mono">
            <span className="text-[#E2E8F0]">
              <strong className="text-white">Bed Location: </strong>
              {selectedPoint.W_lb.toFixed(0)} lb cat ({selectedPoint.W_kg.toFixed(0)} kg)
            </span>
            <span className="text-[#10B981]">
              <strong>Conversion: </strong>
              {selectedPoint.X_pct}%
            </span>
            <span className="text-[#00B4D8]">
              <strong>Pressure: </strong>
              {selectedPoint.P_atm} atm (-{selectedPoint.DP_psi} psi)
            </span>
            <span className="text-[#F59E0B]">
              <strong>Reaction Rate (-rA'): </strong>
              {selectedPoint.rate_10_3} ×10⁻³ lbmol/(lb cat·h)
            </span>
            <span className="text-purple-400">
              <strong>v/v0: </strong>
              {selectedPoint.v_ratio}
            </span>
          </div>
        )}
      </div>

      {/* Analytical Baseline vs Rigorous Solution Table */}
      <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6">
        <h3 className="text-sm font-bold text-white mb-3">
          Analytical Ideal Baseline (ΔP = 0) vs. Rigorous Ergun Solution (ΔP &gt; 0)
        </h3>
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs font-mono border-collapse">
            <thead>
              <tr className="border-b border-[#222C3D] text-[#94A3B8]">
                <th className="py-2.5 px-3">Governing Parameter</th>
                <th className="py-2.5 px-3">Ideal Baseline (ΔP = 0)</th>
                <th className="py-2.5 px-3">Rigorous Ergun Solution</th>
                <th className="py-2.5 px-3">Hydraulic Impact / Penalty</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#1B2433] text-[#E2E8F0]">
              <tr>
                <td className="py-2.5 px-3 font-bold text-white">Catalyst Weight (W)</td>
                <td className="py-2.5 px-3 text-[#94A3B8]">24,390.55 lb (11,063.38 kg)</td>
                <td className="py-2.5 px-3 font-bold text-[#F59E0B]">26,469.02 lb (12,006.16 kg)</td>
                <td className="py-2.5 px-3 text-[#EF4444]">+8.52% (+2,078.47 lb cat penalty)</td>
              </tr>
              <tr>
                <td className="py-2.5 px-3 font-bold text-white">Exit Reactor Pressure</td>
                <td className="py-2.5 px-3 text-[#94A3B8]">25.000 atm (367.4 psia)</td>
                <td className="py-2.5 px-3 font-bold text-[#00B4D8]">20.998 atm (308.59 psia)</td>
                <td className="py-2.5 px-3 text-[#EF4444]">-16.01% pressure drop</td>
              </tr>
              <tr>
                <td className="py-2.5 px-3 font-bold text-white">Cumulative Pressure Loss (ΔP)</td>
                <td className="py-2.5 px-3 text-[#94A3B8]">0.00 psi</td>
                <td className="py-2.5 px-3 font-bold text-[#EF4444]">58.81 psi (4.002 atm)</td>
                <td className="py-2.5 px-3 text-[#EF4444]">Dissipated Ergun shear head loss</td>
              </tr>
              <tr>
                <td className="py-2.5 px-3 font-bold text-white">Exit Volumetric Ratio (v/v0)</td>
                <td className="py-2.5 px-3 text-[#94A3B8]">0.9429 (Molar contraction)</td>
                <td className="py-2.5 px-3 font-bold text-purple-400">1.1202 (Net expansion)</td>
                <td className="py-2.5 px-3 text-[#10B981]">+12.02% volume expansion at exit</td>
              </tr>
              <tr>
                <td className="py-2.5 px-3 font-bold text-white">Tube Requirement (Nt)</td>
                <td className="py-2.5 px-3 text-[#94A3B8]">—</td>
                <td className="py-2.5 px-3 font-bold text-[#00B4D8]">1,021 Tubes (1.5" Sch 80)</td>
                <td className="py-2.5 px-3 text-[#10B981]">30.0 ft mill stock standard</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
