<template>
  <div id="app">
    <div id="header">
      <main-header/>
    </div>
    <router-view/>
  </div>
</template>

<script>
import header from '@/components/Header.vue'

export default {
  name: 'App',
  components: {
    'main-header' : header
  },
}
</script>

<style>
@import 'assets/css/chicken_main.css'
</style>
