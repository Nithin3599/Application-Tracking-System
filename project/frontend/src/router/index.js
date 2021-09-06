import Vue from 'vue'
import VueRouter from 'vue-router'
import candidate from "@/components/appc.vue"
import recruiter from "@/components/appr.vue"

Vue.use(VueRouter)

const routes = [
 
  {
    path: '/candidatepath',
    name: ' candidatepage',
    component: candidate
  },
  {
    path: '/jobpath',
    name: 'recruiterpage',
    component: recruiter
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
