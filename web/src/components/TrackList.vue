<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps(['tracks', 'playlistName']);
const emit = defineEmits(['playTrack']);

const playTrack = (track) => {
    emit('playTrack', track);
};
</script>

<template>
    <div class="track-list-section">
        <h2>{{ props.playlistName }} Tracks</h2>
        <ul>
            <li v-for="track in props.tracks" :key="track.id" @click="playTrack(track)">
                {{ track.title }} by {{ track.artist }}
            </li>
        </ul>
    </div>
</template>
