import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    // Allows importing JSON from the parent repo directory as @schema/...
    alias: {
      '@schema': path.resolve(__dirname, '..'),
    },
  },
});
