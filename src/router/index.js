import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: require('../components/Main.vue').default
    },
    {
      path: '/blog',
      name: 'blog',
      component: require('../components/Blog.vue').default
    },
    {
      path: '/resume',
      name: 'resume',
      component: require('../components/Resume.vue').default
    }
  ]
})
