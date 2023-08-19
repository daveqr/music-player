<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
/* Reset some default styles for consistency */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Apply a dark background to the entire page */
body {
    background-color: #121212;
    /* Dark background color */
    color: #fff;
    /* Text color */
    font-family: Arial, sans-serif;
    /* Font family for text */
}

/* Style the app container */
.app-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Style the header */
header {
    text-align: center;
    padding: 20px;
}

header h1 {
    font-size: 36px;
}

/* Style the playlist section */
.playlist-section {
    margin-bottom: 40px;
}

.playlist-list {
    list-style: none;
    padding: 0;
}

.playlist-item {
    margin-bottom: 10px;
}

.playlist-item a {
    text-decoration: none;
    color: #fff;
    font-size: 18px;
    display: block;
}

/* Style the music control bar */
.music-control-bar {
    text-align: center;
}

.music-control-bar button {
    background-color: #ff5722;
    /* Play button color */
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    margin: 10px;
}

/* Style the footer */
footer {
    text-align: center;
    padding: 20px 0;
    background-color: #333;
    /* Footer background color */
}

footer p {
    color: #fff;
}
</style>
