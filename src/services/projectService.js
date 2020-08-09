import api from '@/services/api'

export default {
  
  all() {
    return api.get('projects/').then(response => response.data)
  }
  
}