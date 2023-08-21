import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/components/LandingPage.vue';
import PlaylistList from '@/components/PlaylistList.vue';
import TrackList from '@/components/TrackList.vue';

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage,
  },
  {
    path: '/playlists',
    name: 'PlaylistList',
    component: PlaylistList,
  },
  {
    path: '/playlist/:id',
    name: 'TrackList',
    component: TrackList,
    props: true,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
