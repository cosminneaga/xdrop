import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '../views/Login.vue'
import Licences from '../views/Licences.vue'
import LicenceGenerator from '../views/LicenceGenerator.vue'
import Messages from '../views/Messages.vue'

import { state } from '../store'

Vue.use(VueRouter)

const guardRoute = (to, from, next) => {
  if (sessionStorage.getItem('sessionKey')) {
    state.isAuthenticated = true
  } else {
    state.isAuthenticated = false
  }

  if (state.isAuthenticated) {
    next()
  } else {
    next('/')
  }
}

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/licences',
    name: ' Licences',
    component: Licences,
    beforeEnter: guardRoute
  },
  {
    path: '/generator',
    name: 'Generator',
    component: LicenceGenerator,
    beforeEnter: guardRoute
  }, {
    path: '/default-messages',
    name: 'Messages',
    component: Messages,
    beforeEnter: guardRoute
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {

//   if (to.path !== '/' && !state.isAuthenticated) next({ path: '/' })
//   else next()

// })

export default router
