import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: () =>
      import( "../views/AboutView.vue"),
  },
  {
    path: "/flows",
    name: "flow-list",
    component: () =>
        import( "../views/apps/flows/FlowList"),
  },
  {
    path: "/flow/:uuid",
    name: "ussd-flow",
    component: () =>
        import( "../views/USSD"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
