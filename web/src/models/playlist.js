
export default class Playlist {
    constructor(id, name, description, songs) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.songs = songs || [];
    }

}
