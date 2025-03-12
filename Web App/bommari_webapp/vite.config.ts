import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",
    allowedHosts: ["bommari.vraminhos.com"]
  },
  build:{
    outDir: "../../Database/dist",
    emptyOutDir: true,
  }
})
