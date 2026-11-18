import React from 'react';
import { Box, Activity, ShieldCheck, GitBranch, Download, Layers } from 'lucide-react';
import { REACTOR_SPECS } from '../data/reactorData';

export default function Header({ activeTab, setActiveTab }) {
  const tabs = [
    { id: '3d_cad', label: '3D CAD Digital Twin', icon: Box, badge: 'SolidWorks 2025' },
    { id: 'kinetics', label: 'Kinetics & Ergun Hydraulics', icon: Activity, badge: 'Problem R2' },
    { id: 'asme_code', label: 'ASME Sec VIII Mechanical', icon: ShieldCheck, badge: 'Code Dossier' },
    { id: 'piping_pid', label: 'ISA-5.1 P&ID & Line Lists', icon: GitBranch, badge: 'Zero Disconnects' },
    { id: 'assets', label: 'CAD & Blueprint Assets', icon: Download, badge: 'STEP / DXF / PDF' }
  ];

  return (
    <header className="h-16 bg-[#101520] border-b border-[#222C3D] px-6 flex items-center justify-between shrink-0 select-none z-20">
      {/* Brand & Project Identity */}
      <div className="flex items-center gap-3">
        <div className="w-9 h-9 rounded-lg bg-gradient-to-br from-[#00B4D8] to-[#0284C7] flex items-center justify-center text-[#0A0D14] font-black font-mono shadow-md shadow-[#00B4D8]/20">
          R-201
        </div>
        <div>
          <div className="flex items-center gap-2">
            <span className="font-bold text-sm text-white tracking-wide">
              ETHYLENE OXIDE TUBULAR REACTOR (R-201)
            </span>
            <span className="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold bg-[#00B4D8]/10 text-[#00B4D8] border border-[#00B4D8]/30">
              ASME SEC VIII DIV 1
            </span>
            <span className="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold bg-[#F59E0B]/10 text-[#F59E0B] border border-[#F59E0B]/30">
              TEMA CLASS R
            </span>
          </div>
          <div className="text-[11px] text-[#94A3B8] font-mono">
            Lead Process & Mechanical Engineer: <strong className="text-[#E2E8F0]">Sourish Senapati</strong> (Roll: 002310301035) • Jadavpur University
          </div>
        </div>
      </div>

      {/* Navigation Tab Bar */}
      <nav className="flex items-center gap-1.5 bg-[#0A0D14] p-1 border border-[#222C3D] rounded-xl">
        {tabs.map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all ${
                isActive
                  ? 'bg-[#00B4D8] text-[#0A0D14] shadow-md shadow-[#00B4D8]/20'
                  : 'text-[#94A3B8] hover:text-white hover:bg-[#131926]'
              }`}
            >
              <Icon className="w-3.5 h-3.5" />
              <span>{tab.label}</span>
              <span className={`text-[9px] font-mono px-1 py-0.2 rounded ${
                isActive ? 'bg-[#0A0D14]/20 text-[#0A0D14]' : 'bg-[#171E2D] text-[#94A3B8]'
              }`}>
                {tab.badge}
              </span>
            </button>
          );
        })}
      </nav>
    </header>
  );
}
