import Vue from 'vue'
import App from '@/App.vue'

// import store from '@/store' 
// import router from '@/router'

import Buefy from 'buefy'

import 'buefy/dist/buefy.css' 
import '@mdi/font/css/materialdesignicons.css'

Vue.config.productionTip = false

Vue.use(Buefy)

const vue = new Vue({
  // router,
  // store,
  render: h => h(App)
})

vue.$mount('#app')
