import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login'
import Home from '../components/Home'

Vue.use(VueRouter)

  export default new VueRouter({
    routes: [
      {
        path: '/',
        name: 'login',
        component: Login
      },
      {
        path: '/Home',
        name: 'home',
        component: Home
      }
    ]
  })
