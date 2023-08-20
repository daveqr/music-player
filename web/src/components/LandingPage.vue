<template>
    <div class="app-container">
        <header>
            <h1>Welcome to My Music App</h1>
        </header>

        <main>
            <div class="two-panel-layout">
                <!-- playlist -->
                <div class="playlist-section">
                    <PlaylistList :playlists="playlists" @selectPlaylist="selectPlaylist" />
                </div>

                <!-- song list -->
                <song-list v-if="selectedPlaylist" :songs="selectedPlaylist.songs" :playlistName="selectedPlaylist.name"
                    @playSong="playSong"></song-list>

                <!-- audio player -->
                <div class="audio-player" v-if="selectedSong">
                    <div class="controlsOuter">
                        <div class="controlsInner">
                            <div id="loading"></div>
                            <div class="btn" id="playBtn"></div>
                            <div class="btn" id="pauseBtn"></div>
                            <div class="btn" id="prevBtn"></div>
                            <div class="btn" id="nextBtn"></div>
                        </div>
                        <div class="btn" id="playlistBtn"></div>
                        <div class="btn" id="volumeBtn"></div>
                    </div>
                    <h3>Now Playing: {{ selectedSong.title }} - {{ selectedSong.artist }}</h3>
                    <button @click="stopSong">Stop</button>
                </div>
            </div>
        </main>
    </div>

    <footer>
        <p>&copy; 2023 My Music App</p>
    </footer>
</template>
  
<script>
import PlaylistList from "@/views/PlaylistList.vue";
import Playlist from "@/models/Playlist";
import SongList from "@/views/SongList.vue";
import Song from "@/models/Song";
import { Howl } from 'howler';

export default {
    name: "LandingPage",
    props: {
        msg: String,
    },
    components: {
        PlaylistList,
        SongList
    },
    data() {
        return {
            playlists: [],
            selectedPlaylist: null,
            selectedSong: null,
            audioPlayer: null,
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
                            // Hardcoding the url for now
                            new Song(songData.id, songData.title, songData.artist, "http://localhost:8000/mp3/Shane.mp3")
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

        playSong(song) {
            if (this.audioPlayer) {
                this.audioPlayer.stop();
            }

            console.log(song.mp3Url)
            this.audioPlayer = new Howl({
                src: [song.mp3Url],
                html5: true,
            });

            this.audioPlayer.play();
            this.selectedSong = song;
        },

        stopSong() {
            if (this.audioPlayer) {
                this.audioPlayer.stop();
            }
            this.selectedSong = null;
        },
    },
};
</script>
  @/models/Playlist@/models/Song