import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import genre from '@/components/genre.vue'
import quiz from '@/components/quiz.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/genre',
      component: genre
    },
    {
      path: '/genre/quiz',
      component: quiz
    }
  ]
})
