<template>
    <div class="app-container">
        <header>
            <h1>Welcome to My Music App</h1>
        </header>

        <main>
            <div class="two-panel-layout">
                <section class="playlist-section">
                    <PlaylistList :playlists="playlists" @selectPlaylist="selectPlaylist" />
                </section>

                <section class="song-list-section" v-if="selectedPlaylist">
                    <h2>{{ selectedPlaylist.name }} Songs</h2>
                    <ul>
                        <li v-for="song in selectedPlaylist.songs" :key="song.id">
                            {{ song.title }} by {{ song.artist }}
                        </li>
                    </ul>
                </section>
            </div>
        </main>
    </div>

    <footer>
        <p>&copy; 2023 My Music App</p>
    </footer>
</template>
  
<script>
import PlaylistList from "@/views/PlaylistList.vue";
import Playlist from "@/models/playlist";
import Song from "@/models/song";

export default {
    name: "LandingPage",
    props: {
        msg: String,
    },
    components: {
        PlaylistList,
    },
    data() {
        return {
            playlists: [],
            selectedPlaylist: null,
        };
    },
    created() {
        this.fetchPlaylists();
    },
    methods: {
        async fetchPlaylists() {
            try {
                const response = await fetch("http://localhost:8000/playlists/");
                if (!response.ok) {
                    throw new Error("Error with response.");
                }
                const playlistsData = await response.json();

                this.playlists = playlistsData.map((playlist) => {
                    const songs = playlist.songs.map(
                        (songData) =>
                            new Song(songData.id, songData.title, songData.artist)
                    );

                    return new Playlist(
                        playlist.id,
                        playlist.name,
                        playlist.description,
                        songs
                    );
                });

                this.selectedPlaylist = this.playlists[0];
            } catch (error) {
                console.error("Error fetching playlists:", error);
            }
        },

        selectPlaylist(playlist) {
            this.selectedPlaylist = playlist;
        },
    },
};
</script>
  