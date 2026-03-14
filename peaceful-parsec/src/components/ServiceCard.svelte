<script>
  let { title, description, price, imageSrc } = $props();
</script>

<div class="flex flex-col border border-gray-800 rounded-xl overflow-hidden bg-[#050505] group hover:border-gray-600 transition-all duration-300">
  
  <!-- Vercel Style Top Image Area -->
  <div class="h-48 border-b border-gray-800 relative overflow-hidden bg-[#111]">
    <!-- Placeholder for your actual project/abstract image -->
    <img src={imageSrc} alt={title} class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-500" />
  </div>

  <!-- Content Area -->
  <div class="p-6 flex flex-col flex-grow relative">

    <h3 class="text-gray-100 text-lg font-semibold mb-2">{title}</h3>
    <p class="text-gray-400 text-sm leading-relaxed mb-6 flex-grow">{description}</p>
    
    <!-- Footer: Price & Action -->
    <div class="flex justify-between items-center mt-auto pt-4 border-t border-gray-800/50">
      <span class="text-white font-medium text-sm">{price}</span>
      <button class="w-8 h-8 flex items-center justify-center border border-gray-700 rounded text-gray-400 hover:text-white hover:bg-gray-800 transition-colors" aria-label="Contact">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
      </button>
    </div>
  </div>
</div>