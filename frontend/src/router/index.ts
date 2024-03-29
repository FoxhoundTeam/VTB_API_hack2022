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
      path: "/upload",
      name: "UploadAPI",
      component: () => import("../views/UploadSchema.vue"),
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/profile",
      name: "Profile",
      component: () => import("../views/Profile.vue"),
      meta: {
        requiresAuth: true,
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
    {
      path: "/fuzzing",
      name: "Fuzzing",
      component: () => import("../views/Fuzzing.vue"),
      meta: {
        requiresAuth: true,
      },
    },
  ],
  linkExactActiveClass: "active",
};
const router = new VueRouter(opts);

export default router;
