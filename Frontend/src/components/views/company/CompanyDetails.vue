<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
    <div class="bg-white rounded-lg shadow-xl max-w-3xl w-full max-h-[90vh] overflow-y-auto">
      <div class="p-6 border-b sticky top-0 bg-white z-10 flex items-center justify-between">
        <h2 class="text-xl font-bold text-gray-900">{{ company.company_name }}</h2>
        <button @click="$emit('close')" class="text-gray-500 hover:text-gray-700">
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
            class="h-5 w-5"
          >
            <path d="M18 6 6 18"></path>
            <path d="m6 6 12 12"></path>
          </svg>
        </button>
      </div>
      <div class="p-6 space-y-6">
        <div>
          <h3 class="text-sm font-medium text-gray-500 mb-1">Company Description</h3>
          <p class="text-gray-900">{{ company.what_you_do }}</p>
        </div>
        <div>
          <h3 class="text-sm font-medium text-gray-500 mb-1">Products & Services</h3>
          <p class="text-gray-900">{{ company.products_services }}</p>
        </div>
        <div>
          <h3 class="text-sm font-medium text-gray-500 mb-1">Problems Solved</h3>
          <p class="text-gray-900">{{ company.problems_solved }}</p>
        </div>
        <div>
          <h3 class="text-sm font-medium text-gray-500 mb-1">Unique Selling Points</h3>
          <p class="text-gray-900">{{ company.what_makes_special }}</p>
        </div>
        <div>
          <h3 class="text-sm font-medium text-gray-500 mb-1">Success Stories</h3>
          <p class="text-gray-900">{{ company.success_stories }}</p>
        </div>
        <div>
          <h3 class="text-sm font-medium text-gray-500 mb-1">Work Process</h3>
          <p class="text-gray-900">{{ company.client_process }}</p>
        </div>
        <div>
          <h3 class="text-sm font-medium text-gray-500 mb-1">Expected Results</h3>
          <p class="text-gray-900">{{ company.expected_results }}</p>
        </div>
      </div>
      <div class="p-6 border-t bg-gray-50 flex justify-end">
        <button
          @click="$emit('close')"
          class="inline-flex items-center justify-center rounded-md px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 hover:bg-gray-50"
        >
          Close
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Company } from '@/stores/companyStore'
import type { PropType } from 'vue'

defineProps({
  company: {
    type: Object as PropType<Company>,
    required: true,
  },
})

defineEmits(['close'])
</script>
