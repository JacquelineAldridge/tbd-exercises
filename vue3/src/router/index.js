import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DirectivesView from '../views/DirectivesView.vue'
import EventsView from '@/views/EventsView.vue'
import Users from '@/views/Users.vue'
import ProductsView from '@/views/ProductsView.vue'
import LoginView from '@/views/LoginView.vue'
import { useAuthStore } from '@/stores/auth.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/directives',
      name: 'directives',
      component: DirectivesView,
    },
      {
      path: '/events',
      name: 'events',
      component: EventsView,
    },
    {
      path: '/users',
      name: 'users',
      component: Users,
    },
    {
      path: '/products',
      name: 'products',
      component: ProductsView,
      meta: {requiresAuth: true}
    },
     {
      path: '/login',
      name: 'login',
      component: LoginView,
    }
  ],
})
router.beforeEach((to)=>{
  const auth= useAuthStore()
  if(to.meta.requiresAuth && !auth.estaLogueado){
    return {name: "login"}
  }
})
export default router
