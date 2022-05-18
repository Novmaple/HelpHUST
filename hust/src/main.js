import Vue from 'vue'
import App from './App.vue'
import router from './router/index.js'
import axios from 'axios'
// 引入组件
import './plugins/element.js'
import './plugins/echarts.js'
Vue.config.productionTip = false
axios.defaults.baseURL = 'http://218.197.209.26:8081'
// 挂载axios
// 在别的组件中用 this.$http
Vue.prototype.$http = axios
Vue.config.productionTip = false

// 挂载全局 echarts 
Vue.prototype.$echarts = window.echarts
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')



