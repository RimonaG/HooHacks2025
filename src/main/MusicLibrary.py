
class MusicLibrary:
    musicLibrary = {"Happy": ["song1", "song2"], "Sad": ["song3", "song4"],
                "Angry" : ["song5", "song6"]} #+more


    def get(str):
        return MusicLibrary.musicLibrary.get(str)