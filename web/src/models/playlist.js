export default class Playlist {
    constructor(id, name, description, tracks) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.tracks = tracks || [];
    }

}