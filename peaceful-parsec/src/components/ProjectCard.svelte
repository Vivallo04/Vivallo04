<script>
  let { title, description, tags = [] } = $props();

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

<div class="flex flex-col sm:flex-row gap-4 sm:gap-5 mb-10 sm:mb-8 group cursor-pointer">
  <!-- Image Thumbnail -->
  <div class="w-full sm:w-32 h-44 sm:h-24 flex-shrink-0 bg-[#111] border border-gray-800 rounded-lg overflow-hidden group-hover:border-gray-600 transition-colors">
    <!-- Replace with actual images -->
    <div class="w-full h-full bg-gradient-to-br from-gray-800 to-black p-2 flex items-center justify-center text-xs text-gray-500 text-center">
      {title} Image
    </div>
  </div>

  <!-- Content -->
  <div class="flex flex-col justify-center w-full">
    <h4 class="text-white text-lg font-medium mb-1 group-hover:text-purple-300 transition-colors">{title}</h4>
    <p class="text-gray-400 text-sm mb-3 leading-relaxed max-w-xl">{description}</p>
    
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
</div>