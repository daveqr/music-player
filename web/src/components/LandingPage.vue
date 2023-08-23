<script setup>
import PlaylistList from "@/components/PlaylistList.vue";
import TrackList from "@/components/TrackList.vue";
import Playlist from "@/models/Playlist";
import FileUpload from "@/components/FileUpload";
import RegistrationForm from "@/components/RegistrationForm";
import Track from "@/models/Track";
import { Howl } from 'howler';
import { ref, onMounted, } from 'vue';

const playlists = ref([]);
const selectedPlaylist = ref(null);
const selectedTrack = ref(null);
const audioPlayer = ref(null);

const fetchPlaylists = async () => {
    try {
        const response = await fetch("http://localhost:8000/playlists/");
        if (!response.ok) {
            throw new Error("Error with response.");
        }
        const playlistsData = await response.json();

        playlists.value = playlistsData.map((playlist) => {
            const tracks = playlist.tracks.map((trackData) =>
                new Track(trackData.id, trackData.title, trackData.artist, trackData.url)
            );

            return new Playlist(playlist.id, playlist.name, playlist.description, tracks);
        });

        selectedPlaylist.value = playlists.value[0];
    } catch (error) {
        console.error("Error fetching playlists:", error);
    }
};

const selectPlaylist = (playlist) => {
    selectedPlaylist.value = playlist;
};

const playTrack = (track) => {
    if (audioPlayer.value) {
        audioPlayer.value.stop();
    }

    audioPlayer.value = new Howl({
        src: [track.url],
        html5: true,
    });

    audioPlayer.value.play();
    selectedTrack.value = track;
};

const stopTrack = () => {
    if (audioPlayer.value) {
        audioPlayer.value.stop();
    }
    selectedTrack.value = null;
};

// Fetch playlists when the component is mounted
onMounted(fetchPlaylists);

</script>

<template>
    <div class="app-container">
        <header>
            <h1>Welcome to My Music App</h1>
        </header>

        <main>
            <RegistrationForm />
            <br/><Br/>
            <FileUpload />
            <br/><Br/>
            <div class="two-panel-layout">
                <!-- playlist -->
                <div class="playlist-section">
                    <PlaylistList :playlists="playlists" @selectPlaylist="selectPlaylist" />
                </div>

                <!-- track list -->
                <track-list v-if="selectedPlaylist" :tracks="selectedPlaylist.tracks" :playlistName="selectedPlaylist.name"
                    @playTrack="playTrack"></track-list>

                <!-- audio player -->
                <div class="audio-player" v-if="selectedTrack">
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
                    <h3>Now Playing: {{ selectedTrack.title }} - {{ selectedTrack.artist }}</h3>
                    <button @click="stopTrack">Stop</button>
                </div>
            </div>
        </main>
    </div>

    <footer>
        <p>&copy; 2023 My Music App</p>
    </footer>
</template>