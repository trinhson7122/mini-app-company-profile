<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black/30 z-50">
    <div class="bg-white rounded-lg p-6 shadow-lg w-full max-w-sm">
      <h3 class="text-lg font-bold mb-2">{{ title }}</h3>
      <p class="mb-4">{{ message }}</p>
      <div class="flex justify-end gap-2">
        <button @click="$emit('cancel')" class="px-4 py-2 rounded border">Cancel</button>
        <button @click="$emit('confirm')" class="px-4 py-2 rounded bg-blue-600 text-white">
          Submit
        </button>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
defineProps<{ visible: boolean; title: string; message: string }>()
defineEmits(['confirm', 'cancel'])
</script>
