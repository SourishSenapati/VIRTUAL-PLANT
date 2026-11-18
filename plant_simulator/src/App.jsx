import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import SolidWorks3DViewport from './components/SolidWorks3DViewport';
import KineticHydraulicTelemetry from './components/KineticHydraulicTelemetry';
import AsmeMechanicalDossier from './components/AsmeMechanicalDossier';
import PipingInstrumentationConsole from './components/PipingInstrumentationConsole';
import EngineeringAssetDownloader from './components/EngineeringAssetDownloader';

export default function App() {
  const [activeTab, setActiveTab] = useState('3d_cad'); // '3d_cad' | 'kinetics' | 'asme_code' | 'piping_pid' | 'assets'

  // Global hotkeys for quick switching
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === '1') setActiveTab('3d_cad');
      else if (e.key === '2') setActiveTab('kinetics');
      else if (e.key === '3') setActiveTab('asme_code');
      else if (e.key === '4') setActiveTab('piping_pid');
      else if (e.key === '5') setActiveTab('assets');
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <div className="w-screen h-screen flex flex-col bg-[#0A0D14] text-[#E2E8F0] overflow-hidden select-none font-sans">
      {/* Precision Industrial Header */}
      <Header activeTab={activeTab} setActiveTab={setActiveTab} />

      {/* Main Workstation Screen */}
      <main className="flex-1 w-full h-[calc(100vh-4rem)] relative overflow-hidden">
        {activeTab === '3d_cad' && <SolidWorks3DViewport />}
        {activeTab === 'kinetics' && <KineticHydraulicTelemetry />}
        {activeTab === 'asme_code' && <AsmeMechanicalDossier />}
        {activeTab === 'piping_pid' && <PipingInstrumentationConsole />}
        {activeTab === 'assets' && <EngineeringAssetDownloader />}
      </main>
    </div>
  );
}
