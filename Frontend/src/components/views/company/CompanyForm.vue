<template>
  <div>
    <div class="mb-6 flex items-center justify-between">
      <div class="flex items-center">
        <button
          type="button"
          @click="$emit('cancel')"
          class="mr-2 inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors hover:bg-gray-100 p-2"
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
            <path d="m12 19-7-7 7-7"></path>
            <path d="M19 12H5"></path>
          </svg>
          Back
        </button>
        <h2 class="text-2xl font-bold tracking-tight text-gray-900">Company Profile</h2>
      </div>

      <div v-if="url" class="flex items-center text-sm text-gray-500">
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
          <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
          <polyline points="15 3 21 3 21 9"></polyline>
          <line x1="10" x2="21" y1="14" y2="3"></line>
        </svg>
        <span>Generated from: {{ url }}</span>
      </div>
    </div>

    <div class="bg-white rounded-lg border shadow-sm">
      <form @submit.prevent="$emit('submit')" class="p-6 space-y-8">
        <div class="space-y-6">
          <div>
            <label for="companyName" class="block text-sm font-medium text-gray-700 mb-1"
              >Company Name</label
            >
            <input
              id="companyName"
              v-model="localFormData.company_name"
              placeholder="Enter your company name"
              class="flex h-10 w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-gray-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              :class="{ 'border-red-500': fieldErrors['company_name'] }"
            />
            <span v-if="fieldErrors['company_name']" class="text-red-500 text-sm"
              >{{ fieldErrors['company_name'] }}
            </span>
          </div>

          <div>
            <label for="companyDescription" class="block text-sm font-medium text-gray-700 mb-1"
              >What does your company do?</label
            >
            <textarea
              id="companyDescription"
              v-model="localFormData.what_you_do"
              placeholder="Describe your company's main activities"
              rows="3"
              class="flex min-h-[80px] w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm ring-offset-background placeholder:text-gray-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              :class="{ 'border-red-500': fieldErrors['what_you_do'] }"
            ></textarea>
            <span v-if="fieldErrors['what_you_do']" class="text-red-500 text-sm"
              >{{ fieldErrors['what_you_do'] }}
            </span>
          </div>

          <div>
            <label for="products" class="block text-sm font-medium text-gray-700 mb-1"
              >What are your main products or services?</label
            >
            <input
              id="products"
              v-model="localFormData.products_services"
              placeholder="Enter your main products or services"
              class="flex h-10 w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-gray-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              :class="{ 'border-red-500': fieldErrors['products_services'] }"
            />
            <span v-if="fieldErrors['products_services']" class="text-red-500 text-sm"
              >{{ fieldErrors['products_services'] }}
            </span>
          </div>

          <div>
            <label for="problems" class="block text-sm font-medium text-gray-700 mb-1"
              >What problems do you solve for your clients?</label
            >
            <textarea
              id="problems"
              v-model="localFormData.problems_solved"
              placeholder="Describe the problems you solve"
              rows="3"
              class="flex min-h-[80px] w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm ring-offset-background placeholder:text-gray-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              :class="{ 'border-red-500': fieldErrors['problems_solved'] }"
            ></textarea>
            <span v-if="fieldErrors['problems_solved']" class="text-red-500 text-sm"
              >{{ fieldErrors['problems_solved'] }}
            </span>
          </div>

          <div>
            <label for="uniqueSellingPoints" class="block text-sm font-medium text-gray-700 mb-1"
              >What makes your company special?</label
            >
            <textarea
              id="uniqueSellingPoints"
              v-model="localFormData.what_makes_special"
              placeholder="Describe what makes your company unique"
              rows="3"
              class="flex min-h-[80px] w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm ring-offset-background placeholder:text-gray-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              :class="{ 'border-red-500': fieldErrors['what_makes_special'] }"
            ></textarea>
            <span v-if="fieldErrors['what_makes_special']" class="text-red-500 text-sm"
              >{{ fieldErrors['what_makes_special'] }}
            </span>
          </div>

          <div>
            <label for="successStories" class="block text-sm font-medium text-gray-700 mb-1"
              >Share some success stories. What results have you achieved for clients?</label
            >
            <textarea
              id="successStories"
              v-model="localFormData.success_stories"
              placeholder="Describe your success stories"
              rows="3"
              class="flex min-h-[80px] w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm ring-offset-background placeholder:text-gray-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              :class="{ 'border-red-500': fieldErrors['success_stories'] }"
            ></textarea>
            <span v-if="fieldErrors['success_stories']" class="text-red-500 text-sm"
              >{{ fieldErrors['success_stories'] }}
            </span>
          </div>

          <div>
            <label for="workProcess" class="block text-sm font-medium text-gray-700 mb-1"
              >How do you typically work with new clients? Describe your process.</label
            >
            <textarea
              id="workProcess"
              v-model="localFormData.client_process"
              placeholder="Describe your work process"
              rows="3"
              class="flex min-h-[80px] w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm ring-offset-background placeholder:text-gray-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              :class="{ 'border-red-500': fieldErrors['client_process'] }"
            ></textarea>
            <span v-if="fieldErrors['client_process']" class="text-red-500 text-sm"
              >{{ fieldErrors['client_process'] }}
            </span>
          </div>

          <div>
            <label for="expectedResults" class="block text-sm font-medium text-gray-700 mb-1"
              >What results can clients typically expect?</label
            >
            <textarea
              id="expectedResults"
              v-model="localFormData.expected_results"
              placeholder="Describe the expected results"
              rows="3"
              class="flex min-h-[80px] w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm ring-offset-background placeholder:text-gray-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              :class="{ 'border-red-500': fieldErrors['expected_results'] }"
            ></textarea>
            <span v-if="fieldErrors['expected_results']" class="text-red-500 text-sm"
              >{{ fieldErrors['expected_results'] }}
            </span>
          </div>
        </div>

        <div class="flex justify-end gap-3 pt-4 border-t">
          <button
            type="button"
            @click="$emit('cancel')"
            class="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-gray-300 bg-white hover:bg-gray-50 h-10 px-4 py-2"
          >
            Cancel
          </button>
          <button
            type="submit"
            :disabled="isSubmitting"
            class="inline-flex items-center justify-center rounded-md bg-blue-600 text-white hover:bg-blue-700 h-10 px-4 py-2 text-sm font-medium disabled:opacity-50"
          >
            <span v-if="isSubmitting" class="mr-2">
              <svg
                class="animate-spin h-5 w-5 text-white"
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
            <svg
              v-if="!isSubmitting"
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
              <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path>
              <polyline points="17 21 17 13 7 13 7 21"></polyline>
              <polyline points="7 3 7 8 15 8"></polyline>
            </svg>
            {{ isSubmitting ? 'Saving...' : 'Save Profile' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, watch } from 'vue'
import type { Company } from '@/stores/companyStore'

const props = defineProps<{
  formData: Company
  url: string
  isSubmitting: boolean
  fieldErrors: Record<string, string>
}>()

const emit = defineEmits(['update:form-data', 'submit', 'cancel'])

// Create a local copy of the form data
const localFormData = reactive({ ...props.formData })

// Watch for changes in the local form data and emit updates
watch(
  localFormData,
  (newValue) => {
    emit('update:form-data', newValue)
  },
  { deep: true },
)

// Watch for changes in the props and update local data
watch(
  () => props.formData,
  (newValue) => {
    Object.assign(localFormData, newValue)
  },
  { deep: true },
)
</script>
