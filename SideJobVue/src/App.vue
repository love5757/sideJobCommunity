<template>
  <div id="app">
    <div id="header">
      <header/>
    </div>
    <router-view/>
  </div>
</template>

<script>
import header from '../components/Header.vue'

export default {
  name: 'App'
}
</script>

<style>
@import '../assets/css/chicken_main.css'
</style>
