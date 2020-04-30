import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

import VueSimpleSVG from 'vue-simple-svg'
import router from './router'
Vue.use(VueSimpleSVG)

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
