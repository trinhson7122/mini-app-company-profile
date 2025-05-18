<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <app-header :active-view="activeView" @change-view="activeView = $event" />

    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8">
      <!-- Company List View -->
      <company-list
        v-if="activeView === 'list'"
        :companies="companies"
        @view-company="selectedCompany = $event"
        @add-new="((activeView = 'generator'), (showForm = false))"
      />

      <!-- Generator View -->
      <div v-if="activeView === 'generator'" class="max-w-5xl mx-auto">
        <!-- Main Generator Options -->
        <generator-options
          v-if="!showForm"
          @manual-input="((showForm = true), initEmptyForm())"
          @generate="handleGenerate"
        />

        <!-- Company Form -->
        <company-form
          v-else
          :form-data="formData"
          :url="url"
          :is-submitting="isSubmitting"
          :field-errors="fieldErrors"
          @update:form-data="updateFormData"
          @submit="handleSubmit"
          @cancel="showForm = false"
        />
      </div>
    </main>

    <!-- Company Details Modal -->
    <company-details
      v-if="selectedCompany"
      :company="selectedCompany"
      @close="selectedCompany = null"
    />

    <!-- Toast Container -->
    <toast-container :toasts="toasts" />

    <!-- Confirm Dialog -->
    <ConfirmDialog
      :visible="showConfirm"
      title="Confirm Save"
      message="Are you sure you want to save this company profile?"
      @confirm="doSubmit"
      @cancel="showConfirm = false"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import AppHeader from './components/layout/AppHeader.vue'
import CompanyList from './components/views/company/CompanyList.vue'
import GeneratorOptions from './components/views/company/GeneratorOptions.vue'
import CompanyForm from './components/views/company/CompanyForm.vue'
import CompanyDetails from './components/views/company/CompanyDetails.vue'
import ToastContainer from './components/ui/ToastContainer.vue'
import { useCompanyStore, type Company } from './stores/companyStore'
import { useToast } from './composables/useToast'
import { createCompany, aiSimulate } from './services/company'
import ConfirmDialog from './components/ui/ConfirmDialog.vue'
import { watch } from 'vue'
// Composables
const { toasts, showToast } = useToast()
const { companies, fetchCompanies, addCompany } = useCompanyStore()

fetchCompanies()

// State
const activeView = ref('generator') // 'generator' or 'list'
const showForm = ref(false)
const formData = reactive<Company>({
  client_process: '',
  company_name: '',
  expected_results: '',
  problems_solved: '',
  products_services: '',
  success_stories: '',
  what_makes_special: '',
  what_you_do: '',
  id: '',
})
const url = ref('')
const isLoading = ref(false)
const isSubmitting = ref(false)
const selectedCompany = ref(null)
const showConfirm = ref(false)
const pendingSubmit = ref(false)
const fieldErrors = ref<Record<string, string>>({})

// Methods
const initEmptyForm = () => {
  // Reset form data to empty values
  formData.client_process = ''
  formData.company_name = ''
  formData.expected_results = ''
  formData.problems_solved = ''
  formData.products_services = ''
  formData.success_stories = ''
  formData.what_makes_special = ''
  formData.what_you_do = ''
}

watch(showForm, () => {
  //reset field errors
  fieldErrors.value = {}
})

const updateFormData = (newData: Company) => {
  Object.assign(formData, newData)
}

const handleGenerate = async (websiteUrl: string) => {
  if (!websiteUrl) {
    showToast('URL Required', 'Please enter a website URL to generate the profile.', 'error')
    return
  }

  url.value = websiteUrl
  isLoading.value = true

  try {
    // Simulate API call to extract data from website
    const response = await aiSimulate(websiteUrl)
    const company = response as Company

    // Mock response data
    formData.company_name = company.company_name
    formData.products_services = company.products_services
    formData.problems_solved = company.problems_solved
    formData.what_makes_special = company.what_makes_special
    formData.success_stories = company.success_stories
    formData.client_process = company.client_process
    formData.expected_results = company.expected_results
    formData.what_you_do = company.what_you_do

    showForm.value = true
    showToast(
      'Profile Generated',
      'Company profile has been successfully generated from the website.',
      'success',
    )
  } catch {
    showToast(
      'Generation Failed',
      'There was a problem generating the profile. Please try again.',
      'error',
    )
  } finally {
    isLoading.value = false
  }
}

const handleSubmit = () => {
  showConfirm.value = true
  pendingSubmit.value = true
}

const doSubmit = async () => {
  fieldErrors.value = {}
  showConfirm.value = false
  isSubmitting.value = true

  try {
    const company = await createCompany(formData)

    showToast('Success', 'Profile saved successfully.', 'success')

    addCompany(company)

    showForm.value = false
  } catch (err: any) {
    console.log(err)

    if (err.response?.status === 422 && Array.isArray(err.response.data.detail)) {
      err.response.data.detail.forEach((e: any) => {
        const field = e.loc?.[1]
        if (field) fieldErrors.value[field] = e.msg
      })
    } else {
      showToast('Error', 'Có lỗi xảy ra khi lưu profile.', 'error')
    }
  } finally {
    isSubmitting.value = false
    pendingSubmit.value = false
  }
}
</script>
