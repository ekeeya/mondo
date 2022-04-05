
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Vuesax from "vuesax";

import "vuesax/dist/vuesax.css"; //Vuesax styles
import 'boxicons/css/boxicons.css';
import 'material-icons/iconfont/material-icons.css';
import './index.css' // load tailwind css
import 'flowbite';

import colors from "../themeConfig";
Vue.config.productionTip = false;

Vue.use(Vuesax, {
  theme: { colors:colors}

});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
