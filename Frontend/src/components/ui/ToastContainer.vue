<template>
  <div class="fixed top-0 right-0 p-4 z-50">
    <div
      v-for="(toast, index) in toasts"
      :key="index"
      class="mb-2 p-4 rounded-md shadow-md min-w-[300px] transition-all duration-300 transform translate-x-0"
      :class="{
        'bg-white border text-gray-900': toast.type === 'default',
        'bg-red-600 text-white': toast.type === 'error',
        'bg-green-600 text-white': toast.type === 'success',
      }"
    >
      <div class="font-semibold">{{ toast.title }}</div>
      <div class="text-sm">{{ toast.message }}</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Toast } from '@/composables/useToast'

defineProps({
  toasts: {
    type: Array<Toast>,
    required: true,
  },
})
</script>
