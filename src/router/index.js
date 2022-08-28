import { createRouter, createWebHistory } from 'vue-router';
import HomePageView from "@/views/HomePageView";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePageView
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router
