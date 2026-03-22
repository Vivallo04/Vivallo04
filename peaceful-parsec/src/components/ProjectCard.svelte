<script lang="ts">
  interface Props {
    title: string;
    description: string;
    tags?: string[];
    href?: string;
    imageSrc?: string;
    imageScale?: number;
  }

  let { title, description, tags = [], href, imageSrc, imageScale = 1 }: Props = $props();

  const tagColors = {
    'TypeScript': '#3178c6',
    'Astro': '#ff5a03',
    'Rust': '#dea584',
    'Go': '#00add8',
    'React': '#61dafb',
    'Node.js': '#339933',
    'PostgreSQL': '#336791',
    'Svelte': '#ff3e00',
    'Python': '#3572A5',
    'Next.js': '#ffffff',
    'Tailwind': '#38bdf8'
  };
</script>

<svelte:element this={href ? 'a' : 'div'} href={href || undefined} target={href ? '_blank' : undefined} rel={href ? 'noopener noreferrer' : undefined} class="flex flex-col sm:flex-row gap-4 sm:gap-5 mb-10 sm:mb-8 group cursor-pointer">
  <!-- Image Thumbnail -->
  <div class="w-full sm:w-72 flex-shrink-0 bg-secondary border border-border rounded-lg overflow-hidden group-hover:border-muted-foreground/30 transition-colors" style="aspect-ratio: 40/21;">
    {#if imageSrc}
      <img src={imageSrc} alt={title} loading="lazy" decoding="async" class="w-full h-full object-cover" style="transform: scale({imageScale}); transform-origin: center;" />
    {:else}
      <div class="w-full h-full bg-gradient-to-br from-secondary to-background p-2 flex items-center justify-center text-xs text-muted-foreground text-center">
        {title} Image
      </div>
    {/if}
  </div>

  <!-- Content -->
  <div class="flex flex-col justify-center w-full">
    <h4 class="text-foreground text-lg font-medium mb-1 group-hover:text-primary transition-colors">{title}</h4>
    <p class="text-muted-foreground text-sm mb-3 leading-relaxed max-w-xl">{description}</p>

    <!-- Tags -->
    <div class="flex flex-wrap gap-2">
      {#each tags as tag}
        <span class="px-3 py-1 text-xs border rounded-full font-medium"
              style="color: {tagColors[tag] || '#d4d4d8'}; background-color: {tagColors[tag] ? tagColors[tag] + '1A' : 'rgba(255,255,255,0.05)'}; border-color: {tagColors[tag] ? tagColors[tag] + '33' : 'rgba(255,255,255,0.1)'};">
          {tag}
        </span>
      {/each}
    </div>
  </div>
</svelte:element>