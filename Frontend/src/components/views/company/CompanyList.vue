<template>
  <div class="max-w-5xl mx-auto">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-2xl font-bold text-gray-900">Saved Companies</h2>
      <button
        @click="$emit('add-new')"
        class="inline-flex items-center justify-center rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700"
      >
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
          class="h-4 w-4 mr-2"
        >
          <path d="M5 12h14"></path>
          <path d="M12 5v14"></path>
        </svg>
        Add New Company
      </button>
    </div>

    <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      <div
        v-for="(company, index) in companies"
        :key="index"
        class="bg-white rounded-lg border shadow-sm hover:shadow-md transition-shadow cursor-pointer"
        @click="$emit('view-company', company)"
      >
        <div class="p-5">
          <h3 class="font-semibold text-lg text-gray-900 mb-1">{{ company.company_name }}</h3>
          <p class="text-sm text-gray-600 line-clamp-2">{{ company.what_you_do }}</p>
        </div>
      </div>
    </div>

    <!-- Empty state -->
    <div v-if="companies.length === 0" class="text-center py-12">
      <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gray-100 mb-4">
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
          class="h-8 w-8 text-gray-400"
        >
          <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
          <circle cx="9" cy="7" r="4"></circle>
          <path d="M22 21v-2a4 4 0 0 0-3-3.87"></path>
          <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
        </svg>
      </div>
      <h3 class="text-lg font-medium text-gray-900 mb-1">No companies yet</h3>
      <p class="text-gray-600 mb-4">Start by creating your first company profile</p>
      <button
        @click="$emit('add-new')"
        class="inline-flex items-center justify-center rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700"
      >
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
          class="h-4 w-4 mr-2"
        >
          <path d="M5 12h14"></path>
          <path d="M12 5v14"></path>
        </svg>
        Create Company Profile
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Company } from '@/stores/companyStore'

defineProps({
  companies: {
    type: Array<Company>,
    required: true,
  },
})

defineEmits(['view-company', 'add-new'])
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
