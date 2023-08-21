# Music Player Demo

# Project Directory Structure

This Django project follows a specific directory structure for organizing its components. Below, you'll find an overview of the main directories and their purposes.

## /api

The `/api` directory is where you'll find the Django REST API.

## /web

The `/web` directory contains the frontend of the music player, built using Vue.js. It's a separate client-side application that communicates with the Django API.

## /cdn

The `/cdn` directory serves MP3 files directly to the player via an Nginx server.

## /processing

The `/processing` directory contains Python scripts related to message processing using RabbitMQ.

This is an active work-in-progress and is not yet feature-complete. I believe it's better to release early and often to gather feedback and iterate rather than to wait until it's perfect.