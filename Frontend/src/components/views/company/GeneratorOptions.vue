<template>
  <div>
    <div class="mb-8 text-center">
      <h2 class="text-3xl font-bold tracking-tight text-gray-900">Company Profile Generator</h2>
      <p class="mt-2 text-lg text-gray-600">
        Create your company profile manually or generate it automatically from your website
      </p>
    </div>

    <div class="grid gap-8 md:grid-cols-2">
      <div class="bg-white rounded-lg border shadow-sm p-6 hover:shadow-md transition-shadow">
        <div class="flex items-center mb-4">
          <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center mr-3">
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
              class="h-5 w-5 text-blue-600"
            >
              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
              <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-900">Manual Input</h3>
        </div>
        <p class="text-gray-600 mb-6">
          Enter all your company information manually through our comprehensive form.
        </p>
        <button
          @click="$emit('manual-input')"
          class="w-full inline-flex items-center justify-center rounded-md bg-blue-600 px-4 py-2.5 text-sm font-medium text-white hover:bg-blue-700 transition-colors"
        >
          Start Manual Input
        </button>
      </div>

      <div class="bg-white rounded-lg border shadow-sm p-6 hover:shadow-md transition-shadow">
        <div class="flex items-center mb-4">
          <div class="w-10 h-10 rounded-full bg-purple-100 flex items-center justify-center mr-3">
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
              class="h-5 w-5 text-purple-600"
            >
              <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
              <path d="M2 17l10 5 10-5"></path>
              <path d="M2 12l10 5 10-5"></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-900">Website URL</h3>
        </div>
        <p class="text-gray-600 mb-4">
          Let us extract information from your website to pre-fill the company profile.
        </p>

        <div class="flex items-start gap-4">
          <div class="relative flex h-12 w-12 shrink-0 overflow-hidden rounded-full bg-purple-100">
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
              class="h-6 w-6 text-purple-600 m-auto"
            >
              <circle cx="12" cy="12" r="10"></circle>
              <polygon points="10 8 16 12 10 16 10 8"></polygon>
            </svg>
          </div>
          <div class="flex-1">
            <p class="text-sm text-gray-700 mb-3">
              I'll pull your company information straight from your website. Think of it as training
              me about your company, so I can deliver the perfect profile every time.
            </p>

            <div class="flex items-center gap-2">
              <div class="flex flex-1 items-center rounded-md border bg-white">
                <span class="pl-3 text-sm text-gray-500">https://</span>
                <input
                  v-model="websiteUrl"
                  class="flex h-10 w-full rounded-md border-0 bg-transparent px-3 py-2 text-sm focus-visible:outline-none focus-visible:ring-0"
                  placeholder="www.example.com"
                />
              </div>
              <button
                @click="generateFromUrl"
                :disabled="isLoading"
                class="inline-flex items-center justify-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700 disabled:opacity-50 transition-colors"
              >
                <span v-if="isLoading" class="mr-2">
                  <svg
                    class="animate-spin h-4 w-4 text-white"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      class="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      stroke-width="4"
                    ></circle>
                    <path
                      class="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    ></path>
                  </svg>
                </span>
                {{ isLoading ? 'Generating...' : 'Generate' }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const websiteUrl = ref('')
const isLoading = ref(false)

const emit = defineEmits(['manual-input', 'generate'])

const generateFromUrl = () => {
  isLoading.value = true
  emit('generate', websiteUrl.value)
  // The parent component will handle the actual generation
  // and will need to reset isLoading when done
  setTimeout(() => {
    isLoading.value = false
  }, 2000)
}
</script>
