import Vue from 'vue'
import VueRouter from 'vue-router'
import MapView from '../views/MapView.vue'
import PlotView from '../views/PlotView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/mapview',
    name: 'MapView',
    component: MapView
  },
  {
    path: '/plotview',
    name: 'PlotView',
    component: PlotView,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
  }
]

const router = new VueRouter({
  routes
})

export default router
