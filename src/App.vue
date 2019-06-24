<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <heading></heading>
    <graphic></graphic>
  </div>
</template>

<script>
import Heading from './components/Heading.vue' 
import Graphic from './components/Graphic.vue'
export default {
  name: 'app',
  components: {
    Heading,
    Graphic
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
