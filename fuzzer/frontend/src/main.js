import Vue from 'vue'
import vuetify from './plugins/vuetify'
import App from './App.vue'
import store from './store'
import router from './router'
import 'leaflet/dist/leaflet.css'
// import Axios from 'axios'

Vue.config.productionTip = false

new Vue({
  vuetify,
  store,
  router,
  render: h => h(App)
}).$mount('#app')
