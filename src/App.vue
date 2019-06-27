<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <heading></heading>
    <graphic></graphic>
    <data-sheet v-if="dataSheetOn" v-bind:id="dataSheetId"></data-sheet>
    <custom-footer></custom-footer>
  </div>
</template>

<script>
import Heading from './components/Heading.vue' 
import Graphic from './components/Graphic.vue'
import CustomFooter from './components/Footer.vue'
import DataSheet from './components/DataSheet.vue'
import EventBus from './assets/event-bus.js'


export default {
  name: 'app',
  components: {
    Heading,
    Graphic,
    CustomFooter,
    DataSheet
  },
  methods: {
    httpRequestAsync: function(url){
    var xmlHttp = new XMLHttpRequest()
    xmlHttp.onreadystatechange = function () {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
        console.log(xmlHttp.responseText)
        this.elementData = xmlHttp.responseText
        this.dataReceived = true
        Vue.nextTick()
      }
    }
    xmlHttp.open("GET", url, true)
    xmlHttp.send(null)
    }
  },
  data () {
    return {
      dataSheetOn: false,
      dataSheetId: null
    }
  },
  mounted () {
    EventBus.$on('create-data-sheet', id => {
      this.dataSheetOn = true
      this.dataSheetId = id
    })
  }
}
//console.log(EventBus)
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
