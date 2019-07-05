import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

// Import vue-directive-tooltip module
import Tooltip from 'vue-directive-tooltip';
import 'vue-directive-tooltip/dist/vueDirectiveTooltip.css';
Vue.use(Tooltip);

new Vue({
  render: h => h(App),
}).$mount('#app')
