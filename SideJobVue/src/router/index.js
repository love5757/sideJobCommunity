import Vue from 'vue'
import Router from 'vue-router'
import listView1 from '@/components/listView1'
import chickenMain from '@/components/Chicken_main'
import chickenStation from '@/components/Chicken_station'

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

Vue.use(Vuetify)
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'recruite',
      component: chickenMain
    },
    {
      path: '/station',
      name: 'station',
      component: chickenStation
    },
    {
      path: '/main',
      name: 'listView1',
      component: listView1

    }
  ]
})
