import random
import webbrowser
#from tkinter import messagebox

class MusicLibrary:
    music_library = {"happy": ["https://www.youtube.com/watch?v=zoq0tAKpLBI&ab_channel=TheLivingTombstone-Topic", "https://youtu.be/ZbZSe6N_BXs?si=Vv8UsoWLnXugD10C", "https://youtu.be/5NV6Rdv1a3I?si=z6yo9eb0AaaC5Ceh"],
                     "sad": ["https://www.youtube.com/watch?v=4fWyzwo1xg0&ab_channel=SimonGarfunkelVEVO", "https://youtu.be/pB-5XG-DbAA?si=6KbkkYTIasxiu7gB", "https://youtu.be/k4V3Mo61fJM?si=iqPJN6SGt6DYawiT"],
                "angry": ["https://youtu.be/CdhqVtpR2ts?si=ppEAZVi8xB2MDvia", "https://youtu.be/OBqw818mQ1E?si=jkF3crJLPb6ZjiDO"],
                     "surprise": ["https://youtu.be/u5CVsCnxyXg?si=8jV3G07Dw8Og7HcN"]} #+more

    # Constructor method - needs 'self' as parameter
    def __init__(self):
        pass

    # Fixed method definition
    def get(self, mood):
        return MusicLibrary.music_library.get(mood)

    def add_song(self, mood, song):
        self.add_mood(mood, song)
        if song not in MusicLibrary.music_library[mood]:
            MusicLibrary.music_library[mood].append(song)

    def remove_song(self, mood):
        if mood in MusicLibrary.music_library:
            del MusicLibrary.music_library[mood]

    def remove_songs(self, mood, song):
        if mood in MusicLibrary.music_library:
            if song in MusicLibrary.music_library[mood]:
                return MusicLibrary.music_library[mood].remove(song)

    def add_mood(self, mood, song):
        if mood not in MusicLibrary.music_library:
            MusicLibrary.music_library[mood] = [song]

    def contains_mood(self, mood):
        if mood in MusicLibrary.music_library:
            return True
        return False

    def get_song(self, mood):
        if mood not in self.music_library:
            return "No emotion detected :("
        else:
            songList = self.music_library[mood]
            if (len(songList) > 0):
                song = random.choice(songList)
                print("here is the Link to your song!: " + song)

                #if(input("Wanna go listen?: ")=="yes"):
                    #webbrowser.open_new_tab(song)
                return song
                #if messagebox.askyesno("Play Song", "Do you want to play a song?"):
                    #webbrowser.open_new_tab(song)

