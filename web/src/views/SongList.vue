<template>
    <div class="song-list-section">
        <h2>{{ playlistName }} Songs</h2>
        <ul>
            <li v-for="song in songs" :key="song.id" @click="playSong(song)">
                {{ song.title }} by {{ song.artist }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    props: {
        songs: Array,
        playlistName: String
    },
    methods: {
        playSong(song) {
            this.$emit("playSong", song);
        }
    }
};
</script>