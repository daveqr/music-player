<template>
    <div>
        <h2>Playlists</h2>
        <ul class="playlist-list">
            <li class="playlist-item" v-for="playlist in playlists" :key="playlist.id" @click="selectPlaylist(playlist)">
                {{ playlist.name }}
            </li>
        </ul>
    </div>
</template>
  
<script>
export default {
    props: {
        playlists: Array,
    },
    
    methods: {
        selectPlaylist(playlist) {
            this.$emit("selectPlaylist", playlist);
        }
    }
};
</script>
  