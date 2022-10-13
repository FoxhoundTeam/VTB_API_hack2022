import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const opts = {
  routes: [
    {
      path: "/",
      name: "Index",
      component: () => import("../views/Index.vue"),
      meta: {
        requiresAuth: false,
      },
    },
    {
      path: "/:apiCode/:versionCode",
      name: "IndexWithParams",
      component: () => import("../views/Index.vue"),
      meta: {
        requiresAuth: false,
      },
    },
    {
      path: "/login",
      name: "Login",
      component: () => import("../views/Login.vue"),
      meta: {
        requiresAuth: false,
      },
    },
  ],
  linkExactActiveClass: "active",
};
const router = new VueRouter(opts);

export default router;
