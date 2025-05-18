import api from './api'
import type { Company } from '@/stores/companyStore'

export const listCompanies = () => {
  return api.get('/companies')
}

export const getCompany = (id: string) => {
  return api.get(`/companies/${id}`)
}

export const createCompany = (data: Company) => {
  return api.post('/companies', data)
}

export const aiSimulate = async (url: string) => {
  return api.post<Company>('/ai-simulate', { url })
}
