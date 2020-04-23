import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

import VueSimpleSVG from 'vue-simple-svg'
Vue.use(VueSimpleSVG)

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
