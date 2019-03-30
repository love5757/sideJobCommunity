import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import listView from '@/components/listView'
import listView1 from '@/components/listView1'
import test from '@/components/test'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

Vue.use(Vuetify)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/main',
      name: 'listView',
      component: listView
    },
    {
      path: '/list',
      name: 'listView1',
      component: listView1

    },
    {
      path: '/test',
      name: 'test',
      component: test

    }
  ]
})
