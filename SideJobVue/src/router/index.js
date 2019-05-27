import Vue from 'vue'
import Router from 'vue-router'
import listView1 from '@/components/listView1'
import chickenMain from '@/components/Chicken_main'

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

Vue.use(Vuetify)
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'chicken-main',
      component: chickenMain
    },
    {
      path: '/main',
      name: 'listView1',
      component: listView1

    }
  ]
})
