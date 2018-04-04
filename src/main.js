// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'
import router from './router'

import VueSocketio from 'vue-socket.io';

Vue.config.productionTip = false
Vue.use(VueResource);
Vue.use(VueSocketio, 'http://localhost:8080');

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',//App.vue?
  components: { App }
})
