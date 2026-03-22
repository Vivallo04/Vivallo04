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
  image: {
    remotePatterns: [
      { protocol: 'https', hostname: 'opengraph.githubassets.com' },
      { protocol: 'https', hostname: 'images.unsplash.com' },
    ]
  },
  integrations: [svelte()],
  adapter: vercel({
    imageService: true,
    webAnalytics: {
      enabled: true
    },
  })
});