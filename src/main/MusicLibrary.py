
class MusicLibrary:
    music_Library = {"Happy": ["song1", "song2"], "Sad": ["song3", "song4"],
                "Angry" : ["song5", "song6"]} #+more

    # Constructor method - needs 'self' as parameter
    def __init__(self):
        if self not in music_Library:
            music_Library[self] = []


    def get(str):
        return MusicLibrary.musicLibrary.get(str)