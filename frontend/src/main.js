import Vue from 'vue'
import App from './App.vue'
import router from "./router/index.js";
import store from "./store/index.js";
import VueExcelEditor from "vue-excel-editor";
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueExcelEditor);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

