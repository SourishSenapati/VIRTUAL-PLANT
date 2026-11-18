import React, { useEffect, useRef, useState, useCallback } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { 
  Layers, Eye, RotateCw, ZoomIn, Maximize2, Camera, 
  Sliders, ShieldCheck, Cpu, Compass, Activity, Crosshair
} from 'lucide-react';
import { REACTOR_SPECS, NOZZLE_SCHEDULE } from '../data/reactorData';

export default function SolidWorks3DViewport({ onSelectComponent }) {
  const mountRef = useRef(null);
  const sceneRef = useRef(null);
  const cameraRef = useRef(null);
  const rendererRef = useRef(null);
  const controlsRef = useRef(null);
  const modelGroupRef = useRef(new THREE.Group());
  const clipPlaneRef = useRef(new THREE.Plane(new THREE.Vector3(0, 0, -1), 100.0));

  const [activeModel, setActiveModel] = useState('cutaway'); // 'exterior' | 'cutaway'
  const [wireframe, setWireframe] = useState(false);
  const [xray, setXray] = useState(false);
  const [autoRotate, setAutoRotate] = useState(false);
  const [clipZ, setClipZ] = useState(11.0);
  const [loading, setLoading] = useState(true);
  const [loadPct, setLoadPct] = useState(0);
  const [activePin, setActivePin] = useState(null);

  // Initialize Three.js Scene
  useEffect(() => {
    const container = mountRef.current;
    if (!container) return;

    const width = container.clientWidth;
    const height = container.clientHeight;

    // 1. Scene
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0a0d14);
    sceneRef.current = scene;

    // 2. Camera
    const camera = new THREE.PerspectiveCamera(38, width / height, 0.1, 100);
    camera.position.set(13, 11, 7.5);
    cameraRef.current = camera;

    // 3. Renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: 'high-performance' });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.35;
    renderer.localClippingEnabled = true;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    container.appendChild(renderer.domElement);
    rendererRef.current = renderer;

    // 4. Controls
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.target.set(0, 0, 3.8);
    controls.maxPolarAngle = Math.PI * 0.88;
    controls.minDistance = 2.0;
    controls.maxDistance = 40.0;
    controlsRef.current = controls;

    // 5. Lighting
    const ambient = new THREE.AmbientLight(0xffffff, 0.85);
    scene.add(ambient);

    const keyLight = new THREE.DirectionalLight(0xfff8ee, 2.4);
    keyLight.position.set(12, 16, 22);
    keyLight.castShadow = true;
    scene.add(keyLight);

    const fillLight = new THREE.DirectionalLight(0x7ea8d6, 1.5);
    fillLight.position.set(-16, -12, 10);
    scene.add(fillLight);

    const rimLight = new THREE.DirectionalLight(0x00b4d8, 1.2);
    rimLight.position.set(0, 22, -18);
    scene.add(rimLight);

    // Grid Floor
    const grid = new THREE.GridHelper(26, 26, 0x00b4d8, 0x1f2c3f);
    grid.rotation.x = Math.PI / 2;
    grid.position.z = -2.44;
    scene.add(grid);

    scene.add(modelGroupRef.current);

    // Animation Loop
    let animationFrameId;
    const animate = () => {
      animationFrameId = requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      if (!container) return;
      const w = container.clientWidth;
      const h = container.clientHeight;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    };
    window.addEventListener('resize', handleResize);

    return () => {
      cancelAnimationFrame(animationFrameId);
      window.removeEventListener('resize', handleResize);
      renderer.dispose();
      if (container.contains(renderer.domElement)) {
        container.removeChild(renderer.domElement);
      }
    };
  }, []);

  // Load Model based on active selection
  const loadActiveModel = useCallback((modelType) => {
    setLoading(true);
    setLoadPct(0);

    const modelPath = modelType === 'cutaway' 
      ? '/models/R201_Reactor_Cutaway_Internal_PBR.glb'
      : '/models/R201_Ethylene_Oxide_Reactor_PBR.glb';

    const loader = new GLTFLoader();
    loader.load(
      modelPath,
      (gltf) => {
        const group = modelGroupRef.current;
        while (group.children.length > 0) {
          group.remove(group.children[0]);
        }

        const model = gltf.scene;
        model.traverse((child) => {
          if (child.isMesh) {
            child.castShadow = true;
            child.receiveShadow = true;
            if (child.material) {
              child.material.clippingPlanes = [clipPlaneRef.current];
              child.material.clipShadows = true;
              child.material.wireframe = wireframe;
              child.material.transparent = xray;
              child.material.opacity = xray ? 0.45 : 1.0;
              child.material.needsUpdate = true;
            }
          }
        });

        group.add(model);
        setLoading(false);
      },
      (xhr) => {
        if (xhr.total > 0) {
          setLoadPct(Math.round((xhr.loaded / xhr.total) * 100));
        }
      },
      (err) => {
        console.error('Error loading GLTF:', err);
        setLoading(false);
      }
    );
  }, [wireframe, xray]);

  useEffect(() => {
    loadActiveModel(activeModel);
  }, [activeModel, loadActiveModel]);

  // Update wireframe / xray
  useEffect(() => {
    const group = modelGroupRef.current;
    group.traverse((child) => {
      if (child.isMesh && child.material) {
        child.material.wireframe = wireframe;
        child.material.transparent = xray;
        child.material.opacity = xray ? 0.45 : 1.0;
        child.material.needsUpdate = true;
      }
    });
  }, [wireframe, xray]);

  // Update auto rotate
  useEffect(() => {
    if (controlsRef.current) {
      controlsRef.current.autoRotate = autoRotate;
      controlsRef.current.autoRotateSpeed = 2.0;
    }
  }, [autoRotate]);

  // Update Z Clipping
  const handleClipChange = (e) => {
    const val = parseFloat(e.target.value);
    setClipZ(val);
    if (val >= 10.5) {
      clipPlaneRef.current.constant = 100.0;
    } else {
      clipPlaneRef.current.constant = val;
    }
  };

  // Camera preset navigation
  const setCameraView = (cx, cy, cz, tx, ty, tz, pinTag = null) => {
    const camera = cameraRef.current;
    const controls = controlsRef.current;
    if (!camera || !controls) return;

    camera.position.set(cx, cy, cz);
    controls.target.set(tx, ty, tz);
    controls.update();
    setActivePin(pinTag);
  };

  return (
    <div className="relative w-full h-full bg-[#0A0D14] overflow-hidden select-none flex flex-col">
      {/* 3D Canvas Mount Point */}
      <div ref={mountRef} className="absolute inset-0 w-full h-full cursor-grab active:cursor-grabbing z-0" />

      {/* Top CAD Control Bar */}
      <div className="absolute top-4 left-4 right-4 z-10 flex flex-wrap justify-between items-center gap-3 pointer-events-none">
        {/* Left: Model switcher and status badges */}
        <div className="pointer-events-auto flex items-center gap-2 bg-[#101520]/95 border border-[#222C3D] rounded-lg p-1.5 shadow-xl">
          <button
            onClick={() => setActiveModel('cutaway')}
            className={`px-3 py-1.5 rounded-md text-xs font-semibold flex items-center gap-1.5 transition-all ${
              activeModel === 'cutaway'
                ? 'bg-[#00B4D8] text-[#0A0D14] shadow-md shadow-[#00B4D8]/20'
                : 'text-[#94A3B8] hover:text-white hover:bg-[#171E2D]'
            }`}
          >
            <Layers className="w-3.5 h-3.5" />
            Cutaway Interior (1,021 Tubes)
          </button>
          <button
            onClick={() => setActiveModel('exterior')}
            className={`px-3 py-1.5 rounded-md text-xs font-semibold flex items-center gap-1.5 transition-all ${
              activeModel === 'exterior'
                ? 'bg-[#00B4D8] text-[#0A0D14] shadow-md shadow-[#00B4D8]/20'
                : 'text-[#94A3B8] hover:text-white hover:bg-[#171E2D]'
            }`}
          >
            <ShieldCheck className="w-3.5 h-3.5" />
            Full Pressure Shell Assembly
          </button>
        </div>

        {/* Right: Render modes & Presets */}
        <div className="pointer-events-auto flex items-center gap-2 bg-[#101520]/95 border border-[#222C3D] rounded-lg p-1.5 shadow-xl">
          <button
            onClick={() => setWireframe(!wireframe)}
            className={`px-2.5 py-1.5 rounded-md text-xs font-medium flex items-center gap-1 transition-all ${
              wireframe ? 'bg-[#F59E0B] text-[#0A0D14]' : 'text-[#94A3B8] hover:text-white hover:bg-[#171E2D]'
            }`}
            title="Toggle CAD B-Rep Mesh Wireframe"
          >
            <Cpu className="w-3.5 h-3.5" />
            Wireframe
          </button>
          <button
            onClick={() => setXray(!xray)}
            className={`px-2.5 py-1.5 rounded-md text-xs font-medium flex items-center gap-1 transition-all ${
              xray ? 'bg-[#10B981] text-[#0A0D14]' : 'text-[#94A3B8] hover:text-white hover:bg-[#171E2D]'
            }`}
            title="Toggle Ghosted Semi-Transparent X-Ray"
          >
            <Eye className="w-3.5 h-3.5" />
            X-Ray
          </button>
          <button
            onClick={() => setAutoRotate(!autoRotate)}
            className={`px-2.5 py-1.5 rounded-md text-xs font-medium flex items-center gap-1 transition-all ${
              autoRotate ? 'bg-[#00B4D8] text-[#0A0D14]' : 'text-[#94A3B8] hover:text-white hover:bg-[#171E2D]'
            }`}
            title="Toggle Continuous Turntable Rotation"
          >
            <RotateCw className="w-3.5 h-3.5" />
            Auto-Spin
          </button>
        </div>
      </div>

      {/* Floating Dynamic Elevation Slicing Slider (Bottom Left) */}
      <div className="absolute bottom-6 left-6 z-10 w-72 bg-[#101520]/95 border border-[#222C3D] rounded-xl p-3.5 shadow-2xl">
        <div className="flex items-center justify-between text-xs font-bold text-[#E2E8F0] mb-2">
          <span className="flex items-center gap-1.5 text-[#00B4D8]">
            <Sliders className="w-3.5 h-3.5" />
            Dynamic Z-Elevation Slicing
          </span>
          <span className="tabular-nums font-mono text-[#F59E0B]">
            {clipZ >= 10.5 ? 'UNCLIPPED' : `${clipZ.toFixed(1)} m`}
          </span>
        </div>
        <input
          type="range"
          min="-2.5"
          max="11.0"
          step="0.1"
          value={clipZ}
          onChange={handleClipChange}
          className="w-full h-1.5 bg-[#1E293B] rounded-lg appearance-none cursor-pointer accent-[#00B4D8]"
        />
        <div className="flex justify-between text-[10px] text-[#94A3B8] font-mono mt-1.5">
          <span>Skirt (-2.5m)</span>
          <span>Center (4.5m)</span>
          <span>Apex (9.7m)</span>
        </div>
      </div>

      {/* Camera Presets Toolbar (Bottom Center) */}
      <div className="absolute bottom-6 left-1/2 -translate-x-1/2 z-10 flex items-center gap-1.5 bg-[#101520]/95 border border-[#222C3D] rounded-full px-3 py-2 shadow-2xl">
        <button
          onClick={() => setCameraView(13, 11, 7.5, 0, 0, 3.8)}
          className="px-3 py-1 rounded-full text-xs font-semibold text-[#E2E8F0] hover:bg-[#171E2D] hover:text-[#00B4D8] transition-all"
        >
          Isometric
        </button>
        <button
          onClick={() => setCameraView(0, 18, 4.5, 0, 0, 4.5)}
          className="px-3 py-1 rounded-full text-xs font-semibold text-[#E2E8F0] hover:bg-[#171E2D] hover:text-[#00B4D8] transition-all"
        >
          GA Elevation
        </button>
        <button
          onClick={() => setCameraView(0, 0.1, 20, 0, 0, 4.5)}
          className="px-3 py-1 rounded-full text-xs font-semibold text-[#E2E8F0] hover:bg-[#171E2D] hover:text-[#00B4D8] transition-all"
        >
          Tubesheet Plan
        </button>
        <button
          onClick={() => setCameraView(4, 5, 9.0, 0, 0, 9.0, 'N1')}
          className="px-3 py-1 rounded-full text-xs font-semibold text-[#E2E8F0] hover:bg-[#171E2D] hover:text-[#00B4D8] transition-all"
        >
          Nozzles N1/N5
        </button>
        <button
          onClick={() => setCameraView(4, 5, 0.0, 0, 0, -1.0, 'SK1')}
          className="px-3 py-1 rounded-full text-xs font-semibold text-[#E2E8F0] hover:bg-[#171E2D] hover:text-[#00B4D8] transition-all"
        >
          Base Skirt
        </button>
      </div>

      {/* Right Engineering Telemetry Sidebar */}
      <div className="absolute top-20 right-6 z-10 w-80 bg-[#101520]/95 border border-[#222C3D] rounded-xl p-4 shadow-2xl max-h-[calc(100vh-140px)] overflow-y-auto space-y-4">
        <div>
          <div className="text-[10px] font-mono uppercase tracking-wider text-[#00B4D8] font-bold border-b border-[#222C3D] pb-1 flex items-center justify-between">
            <span>Core B-Rep Geometry</span>
            <span className="text-[#F59E0B]">FinFET Nanometer-Standard</span>
          </div>
          <div className="grid grid-cols-2 gap-2 mt-2.5">
            <div className="bg-[#131926] p-2 rounded border border-[#222C3D]">
              <div className="text-[10px] text-[#94A3B8]">Shell ID / OD</div>
              <div className="text-xs font-bold font-mono text-white mt-0.5">84.0" / 86.25"</div>
              <div className="text-[9px] text-[#F59E0B]">SA-516 Gr 70 (1.125")</div>
            </div>
            <div className="bg-[#131926] p-2 rounded border border-[#222C3D]">
              <div className="text-[10px] text-[#94A3B8]">Active Tubes (Nt)</div>
              <div className="text-xs font-bold font-mono text-white mt-0.5">1,021 Seamless</div>
              <div className="text-[9px] text-[#10B981]">1.5" Sch 80 TP304</div>
            </div>
            <div className="bg-[#131926] p-2 rounded border border-[#222C3D]">
              <div className="text-[10px] text-[#94A3B8]">Tube Pitch Pattern</div>
              <div className="text-xs font-bold font-mono text-white mt-0.5">2.375" Δ Pitch</div>
              <div className="text-[9px] text-[#94A3B8]">OTL = 81.25 in</div>
            </div>
            <div className="bg-[#131926] p-2 rounded border border-[#222C3D]">
              <div className="text-[10px] text-[#94A3B8]">Tubesheet Pair</div>
              <div className="text-xs font-bold font-mono text-white mt-0.5">3.75" Thick</div>
              <div className="text-[9px] text-[#00B4D8]">Forged SA-266 Cl 2</div>
            </div>
            <div className="bg-[#131926] p-2 rounded border border-[#222C3D] col-span-2">
              <div className="text-[10px] text-[#94A3B8]">Catalyst & Reaction Duty</div>
              <div className="text-xs font-bold font-mono text-white mt-0.5">26,469 lb Cat • 17.26 MW Duty</div>
              <div className="text-[9px] text-[#F59E0B]">Ag/α-Al2O3 Spheres • ΔP = 4.002 atm (Ergun Solved)</div>
            </div>
          </div>
        </div>

        {/* Process Nozzle Callouts */}
        <div>
          <div className="text-[10px] font-mono uppercase tracking-wider text-[#00B4D8] font-bold border-b border-[#222C3D] pb-1">
            ASME B16.5 300# Nozzle Schedule
          </div>
          <div className="space-y-1.5 mt-2">
            {NOZZLE_SCHEDULE.map((noz) => (
              <div
                key={noz.tag}
                onClick={() => {
                  if (noz.tag === 'N1') setCameraView(3, 4, 9.6, 0, 0, 9.6, 'N1');
                  else if (noz.tag === 'N2') setCameraView(3, 4, -0.6, 0, 0, -0.6, 'N2');
                  else if (noz.tag === 'N3') setCameraView(4, 3, 0.85, 1.2, 0, 0.85, 'N3');
                  else if (noz.tag === 'N4') setCameraView(-4, 3, 8.3, -1.2, 0, 8.3, 'N4');
                  else if (noz.tag === 'N5') setCameraView(2, -4, 9.4, 0, -1.2, 9.4, 'N5');
                }}
                className={`p-2 rounded border transition-all cursor-pointer flex items-center justify-between text-xs ${
                  activePin === noz.tag
                    ? 'bg-[#00B4D8]/20 border-[#00B4D8] text-white shadow-md'
                    : 'bg-[#131926] border-[#222C3D] text-[#E2E8F0] hover:border-[#00B4D8]/50'
                }`}
              >
                <div>
                  <span className="font-bold font-mono text-[#00B4D8] mr-2">{noz.tag}:</span>
                  <span>{noz.service}</span>
                </div>
                <span className="text-[10px] font-mono text-[#94A3B8]">{noz.size}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Loading Overlay */}
      {loading && (
        <div className="absolute inset-0 bg-[#0A0D14]/90 z-50 flex flex-col items-center justify-center gap-3">
          <div className="w-12 h-12 border-3 border-[#00B4D8]/20 border-t-[#00B4D8] rounded-full animate-spin" />
          <div className="text-xs font-mono tracking-widest text-[#00B4D8]">
            LOADING FINFET-ACCURATE B-REP MESH ({loadPct}%)
          </div>
        </div>
      )}
    </div>
  );
}
