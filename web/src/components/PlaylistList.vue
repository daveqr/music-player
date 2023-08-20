<script setup>
import { defineProps } from 'vue';

const props = defineProps(['playlists']);
</script>
  
<template>
    <div>
        <h2>Playlists</h2>
        <ul class="playlist-list">
            <li class="playlist-item" v-for="playlist in props.playlists" :key="playlist.id"
                @click="$emit('selectPlaylist', playlist)">
                {{ playlist.name }}
            </li>
        </ul>
    </div>
</template>