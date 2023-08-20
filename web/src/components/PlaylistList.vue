<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps(['playlists']);
const emit = defineEmits(['selectPlaylist']);

const selectPlaylist = (playlist) => {
    emit('selectPlaylist', playlist);
};
</script>
  
<template>
    <div>
        <h2>Playlists</h2>
        <ul class="playlist-list">
            <li class="playlist-item" v-for="playlist in props.playlists" :key="playlist.id"
                @click="selectPlaylist(playlist)">
                {{ playlist.name }}
            </li>
        </ul>
    </div>
</template>