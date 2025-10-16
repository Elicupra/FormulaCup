import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Drivers from '../views/Drivers.vue'
import Teams from '../views/Teams.vue'
import Results from '../views/Results.vue'
import History from '../views/History.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/drivers', component: Drivers },
  { path: '/teams', component: Teams },
  { path: '/results', component: Results },
  { path: '/history', component: History }
]

export default createRouter({
  history: createWebHistory(),
  routes
})