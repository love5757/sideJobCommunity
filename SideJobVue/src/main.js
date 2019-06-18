// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import vueAnalytics from 'vue-analytics'

export const eventBus = new Vue()

Vue.config.productionTip = false
Vue.prototype.$axios = axios
/* eslint-disable no-new */

Vue.use(vueAnalytics, {
  id : 'UA-142334436-1',
  router,
  autoTracking: {
    pageviewOnLoad : false
  }
})

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
}).$mount('#app')
