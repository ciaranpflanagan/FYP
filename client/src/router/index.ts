import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import Model from '../views/Model.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Model
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
