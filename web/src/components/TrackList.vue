<script setup>
import { defineProps } from 'vue';

const props = defineProps(['tracks', 'playlistName']);
</script>

<template>
    <div class="track-list-section">
        <h2>{{ props.playlistName }} Tracks</h2>
        <ul>
            <li v-for="track in props.tracks" :key="track.id" @click="$emit('playTrack', track)">
                {{ track.title }} by {{ track.artist }}
            </li>
        </ul>
    </div>
</template>
