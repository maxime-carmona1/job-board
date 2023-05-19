import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/annonce',
    name: 'Annonce',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "annonce" */ '../views/AnnonceView.vue')
    }
  },
  {
    path: '/contact',
    name: 'Contact',
    component: function (){
      return import(/* webpackChunkName: "contact" */ '../views/ContactView.vue')
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: function(){
      return import(/* webpackChunkName: "login" */ '../views/LoginView.vue')
    }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: function(){
      return import(/* webpackChunkName: "profile" */ '../views/ProfileView.vue')
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
