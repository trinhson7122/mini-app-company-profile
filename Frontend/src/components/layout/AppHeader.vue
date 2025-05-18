<template>
  <header class="bg-white border-b sticky top-0 z-10">
    <div class="container mx-auto px-4 py-4 flex items-center justify-between">
      <h1
        @click="$emit('change-view', 'generator')"
        class="text-xl font-bold text-gray-900 cursor-pointer"
      >
        Company Profile Manager
      </h1>
      <div class="flex items-center gap-4">
        <button
          @click="$emit('change-view', 'list')"
          class="text-sm font-medium text-gray-600 hover:text-gray-900"
          :class="{ 'text-blue-600 hover:text-blue-700': activeView === 'list' }"
        >
          <span class="flex items-center">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="h-4 w-4 mr-1"
            >
              <rect width="7" height="7" x="3" y="3" rx="1"></rect>
              <rect width="7" height="7" x="14" y="3" rx="1"></rect>
              <rect width="7" height="7" x="14" y="14" rx="1"></rect>
              <rect width="7" height="7" x="3" y="14" rx="1"></rect>
            </svg>
            Companies
          </span>
        </button>
        <button
          @click="$emit('change-view', 'generator')"
          class="text-sm font-medium text-gray-600 hover:text-gray-900"
          :class="{ 'text-blue-600 hover:text-blue-700': activeView === 'generator' }"
        >
          <span class="flex items-center">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="h-4 w-4 mr-1"
            >
              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
              <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
            </svg>
            Generator
          </span>
        </button>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
defineProps({
  activeView: {
    type: String,
    required: true,
  },
})

defineEmits(['change-view'])
</script>
