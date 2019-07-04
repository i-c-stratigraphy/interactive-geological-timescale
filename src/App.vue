<template>
  <div id="app">
    <heading></heading>
    <toggle-switch v-bind:values="['None', 'Logarithmic', 'Linear']" v-bind:defaultSelected="'None'" v-bind:label="'Time Scale Type'" v-model="currentGraphicScale"></toggle-switch>
    <graphic></graphic>
    <transition name='fade'>
      <data-sheet v-if="dataSheetOn" v-bind:id="dataSheetId"></data-sheet>
    </transition>
    <custom-footer></custom-footer>
  </div>
</template>

<script>
import Heading from './components/Heading.vue' 
import Graphic from './components/Graphic.vue'
import CustomFooter from './components/Footer.vue'
import DataSheet from './components/DataSheet.vue'
import ToggleSwitch from './components/ToggleSwitch.vue'
import EventBus from './assets/event-bus.js'


export default {
  name: 'app',
  components: {
    Heading,
    Graphic,
    CustomFooter,
    DataSheet,
    ToggleSwitch
  },
  data () {
    return {
      dataSheetOn: false,
      dataSheetId: null,
      currentGraphicScale: 'None'
    }
  },
  mounted () {
    EventBus.$on('create-data-sheet', id => {
      this.dataSheetOn = true
      this.dataSheetId = id
    })
    EventBus.$on('destroy-data-sheet', payload =>{
      this.dataSheetOn = false
      this.dataSheetId = null
    })
  }
}
</script>

<style>
html, body {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
