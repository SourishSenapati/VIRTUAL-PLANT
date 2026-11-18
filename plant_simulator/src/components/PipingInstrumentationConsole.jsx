import React, { useState } from 'react';
import { GitBranch, Shield, Sliders, Activity, Database, CheckCircle2 } from 'lucide-react';
import { LINE_LIST, VALVE_SCHEDULE, INSTRUMENT_INDEX } from '../data/reactorData';

export default function PipingInstrumentationConsole() {
  const [subTab, setSubTab] = useState('lines'); // 'lines' | 'valves' | 'instruments'

  return (
    <div className="w-full h-full p-6 bg-[#0A0D14] overflow-y-auto space-y-6">
      {/* Header Banner */}
      <div className="flex flex-wrap items-center justify-between gap-4 border-b border-[#222C3D] pb-4">
        <div>
          <h2 className="text-lg font-bold text-white flex items-center gap-2">
            <GitBranch className="w-5 h-5 text-[#00B4D8]" />
            Process Piping & Instrumentation System (ISA-5.1 & ASME B16.5)
          </h2>
          <p className="text-xs text-[#94A3B8] mt-1 font-mono">
            Zero Disconnected Lines • 100% Endpoints Reconciled • Flange Rating: Class 300 WNRF Across All Lines
          </p>
        </div>
        <div className="flex items-center gap-2">
          <span className="px-3 py-1 bg-[#10B981]/10 border border-[#10B981]/40 rounded text-xs font-mono text-[#10B981] font-bold">
            ZERO DISCONNECTED PIPES
          </span>
        </div>
      </div>

      {/* Sub Tabs */}
      <div className="flex items-center gap-2 border-b border-[#222C3D] pb-2 text-xs font-mono">
        <button
          onClick={() => setSubTab('lines')}
          className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
            subTab === 'lines'
              ? 'bg-[#00B4D8] text-[#0A0D14]'
              : 'text-[#94A3B8] hover:text-white hover:bg-[#131926]'
          }`}
        >
          Master Line List (8 Lines)
        </button>
        <button
          onClick={() => setSubTab('valves')}
          className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
            subTab === 'valves'
              ? 'bg-[#00B4D8] text-[#0A0D14]'
              : 'text-[#94A3B8] hover:text-white hover:bg-[#131926]'
          }`}
        >
          Valve Schedule (9 Valves)
        </button>
        <button
          onClick={() => setSubTab('instruments')}
          className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
            subTab === 'instruments'
              ? 'bg-[#00B4D8] text-[#0A0D14]'
              : 'text-[#94A3B8] hover:text-white hover:bg-[#131926]'
          }`}
        >
          Instrument Index (10 Loops)
        </button>
      </div>

      {/* Lines Table */}
      {subTab === 'lines' && (
        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6">
          <h3 className="text-sm font-bold text-white mb-3">Authoritative Process & Utility Line Schedule</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs font-mono border-collapse">
              <thead>
                <tr className="border-b border-[#222C3D] text-[#94A3B8]">
                  <th className="py-2.5 px-3">Line Number</th>
                  <th className="py-2.5 px-3">From Equipment</th>
                  <th className="py-2.5 px-3">To Equipment</th>
                  <th className="py-2.5 px-3">Size & Sched</th>
                  <th className="py-2.5 px-3">Class</th>
                  <th className="py-2.5 px-3">Fluid Service</th>
                  <th className="py-2.5 px-3">Design (P / T)</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#1B2433] text-[#E2E8F0]">
                {LINE_LIST.map((l) => (
                  <tr key={l.line} className="hover:bg-[#171E2D] transition-colors">
                    <td className="py-2.5 px-3 font-bold text-[#00B4D8]">{l.line}</td>
                    <td className="py-2.5 px-3">{l.from}</td>
                    <td className="py-2.5 px-3">{l.to}</td>
                    <td className="py-2.5 px-3 font-bold text-white">{l.size} {l.sched}</td>
                    <td className="py-2.5 px-3 text-[#F59E0B]">{l.rating}</td>
                    <td className="py-2.5 px-3 text-[#94A3B8]">{l.fluid}</td>
                    <td className="py-2.5 px-3 text-[#10B981]">{l.p} / {l.t}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Valves Table */}
      {subTab === 'valves' && (
        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6">
          <h3 className="text-sm font-bold text-white mb-3">ASME B16.5 Class 300 Valve Schedule</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs font-mono border-collapse">
              <thead>
                <tr className="border-b border-[#222C3D] text-[#94A3B8]">
                  <th className="py-2.5 px-3">Valve Tag</th>
                  <th className="py-2.5 px-3">Line</th>
                  <th className="py-2.5 px-3">Type & Rating</th>
                  <th className="py-2.5 px-3">Fail Position</th>
                  <th className="py-2.5 px-3">Actuator</th>
                  <th className="py-2.5 px-3">Control Function</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#1B2433] text-[#E2E8F0]">
                {VALVE_SCHEDULE.map((v) => (
                  <tr key={v.tag} className="hover:bg-[#171E2D] transition-colors">
                    <td className="py-2.5 px-3 font-bold text-[#00B4D8]">{v.tag}</td>
                    <td className="py-2.5 px-3 text-[#94A3B8]">{v.line}</td>
                    <td className="py-2.5 px-3 text-white">{v.type} ({v.rating})</td>
                    <td className="py-2.5 px-3 text-[#EF4444] font-bold">{v.fail}</td>
                    <td className="py-2.5 px-3 text-[#94A3B8]">{v.actuator}</td>
                    <td className="py-2.5 px-3 text-[#10B981]">{v.func}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Instruments Table */}
      {subTab === 'instruments' && (
        <div className="bg-[#101520] border border-[#222C3D] rounded-xl p-6">
          <h3 className="text-sm font-bold text-white mb-3">ISA-5.1 Control Loop & Transmitter Index</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs font-mono border-collapse">
              <thead>
                <tr className="border-b border-[#222C3D] text-[#94A3B8]">
                  <th className="py-2.5 px-3">Instrument Tag</th>
                  <th className="py-2.5 px-3">Loop ID</th>
                  <th className="py-2.5 px-3">Measured Variable</th>
                  <th className="py-2.5 px-3">Range</th>
                  <th className="py-2.5 px-3">Transmitter Type</th>
                  <th className="py-2.5 px-3">Location</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#1B2433] text-[#E2E8F0]">
                {INSTRUMENT_INDEX.map((i) => (
                  <tr key={i.tag} className="hover:bg-[#171E2D] transition-colors">
                    <td className="py-2.5 px-3 font-bold text-[#00B4D8]">{i.tag}</td>
                    <td className="py-2.5 px-3 text-[#F59E0B]">{i.loop}</td>
                    <td className="py-2.5 px-3 font-bold text-white">{i.var}</td>
                    <td className="py-2.5 px-3 text-[#10B981]">{i.range}</td>
                    <td className="py-2.5 px-3 text-[#94A3B8]">{i.type}</td>
                    <td className="py-2.5 px-3 text-white">{i.loc}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
}
