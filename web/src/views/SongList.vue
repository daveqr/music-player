<template>
    <div>
        <h2>Songs</h2>
        <ul class="song-list">
            <li class="song-item" v-for="song in songs" :key="song.id">
                {{ song.title }} - {{ song.artist }}
            </li>
        </ul>
    </div>
</template>
  
<script>
export default {
    props: ['songs']
};
</script>