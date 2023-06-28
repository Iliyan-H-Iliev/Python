from project.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = []
        self.published = False

        self.songs.extend(list(args))

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        try:
            current_song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(current_song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return "Album {name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"

        return result

