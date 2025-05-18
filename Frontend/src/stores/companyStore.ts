import { listCompanies } from '@/services/company'
import { ref } from 'vue'

export interface Company {
  id?: string
  company_name: string
  what_you_do: string
  products_services: string
  problems_solved: string
  what_makes_special: string
  success_stories: string
  client_process: string
  expected_results: string
}

// This is a simple store implementation
// In a real app, you might use Pinia or Vuex
export function useCompanyStore() {
  const companies = ref<Company[]>([])

  const addCompany = (company: Company) => {
    // Add date to the company
    const newCompany = { ...company }

    // Add to the beginning of the array
    companies.value.unshift(newCompany)
  }

  // fetch companies
  const fetchCompanies = async () => {
    const response = await listCompanies()
    companies.value = response
  }

  return {
    companies,
    addCompany,
    fetchCompanies,
  }
}
