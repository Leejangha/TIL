import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DepositView from '@/views/DepositView.vue'
import DepositDetail from '@/views/DepositDetail.vue'
import SavingView from '@/views/SavingView.vue'
import SavingDetail from '@/views/SavingDetail.vue'
import ExchangeView from '@/views/ExchangeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: DepositView
    },
    {
      path: '/deposit/:id',
      name: 'depositdetail',
      component: DepositDetail
    },
    {
      path: '/saving',
      name: 'saving',
      component: SavingView
    },
    {
      path: '/saving/:id',
      name: 'savingdetail',
      component: SavingDetail
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
  ]
})

export default router