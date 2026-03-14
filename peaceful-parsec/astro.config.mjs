// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

import svelte from '@astrojs/svelte';

import vercel from '@astrojs/vercel';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
    ssr: {
      noExternal: ['phosphor-svelte']
    }
  },
  integrations: [svelte()],
  adapter: vercel({
    imageService: true,
    webAnalytics: {
      enabled: true
    },
  })
});