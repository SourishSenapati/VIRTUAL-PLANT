import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  root: './',
  publicDir: 'public',
  plugins: [
    react(),
    tailwindcss()
  ],
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    chunkSizeWarningLimit: 1200,
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('three')) {
            return 'vendor-three';
          }
          if (id.includes('framer-motion') || id.includes('lucide-react')) {
            return 'vendor-ui';
          }
        }
      }
    }
  },
  server: {
    port: 5174,
    open: false
  }
});
