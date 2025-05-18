import { ref } from 'vue'

export interface Toast {
  title: string
  message: string
  type: 'default' | 'error' | 'success'
}

export function useToast() {
  const toasts = ref<Toast[]>([])

  const showToast = (
    title: string,
    message: string,
    type: 'default' | 'error' | 'success' = 'default',
  ) => {
    const toast: Toast = {
      title,
      message,
      type,
    }

    toasts.value.push(toast)

    // Auto remove after 3 seconds
    setTimeout(() => {
      toasts.value.shift()
    }, 3000)
  }

  return {
    toasts,
    showToast,
  }
}
