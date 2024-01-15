import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
// axios.defaults.baseURL = 'https://api.xdroppro.com/'
axios.defaults.baseURL = 'http://192.168.0.15:5000'
axios.defaults.headers.common['Authorization'] = 'Bearer ' + sessionStorage.getItem('sessionKey')

new Vue({
  axios,
  router,
  vuetify,
  render: h => h(App),
  mounted() {
    // console.log(this);
  }
}).$mount('#app')
