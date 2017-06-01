import Vue from 'vue'
import Router from 'vue-router'
import List from '@/components/List'
import Info from '@/components/Info'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'List',
      component: List
    },
    {
      path: '/card',
      name: 'List',
      component: List
    },
    {
      path: '/card/:id',
      name: 'Info',
      component: Info
    },
  ]
})
