#from xxsubtype import bench
from tkinter import messagebox

from MusicLibrary import MusicLibrary

library = MusicLibrary()

from deepface import DeepFace
import random
import webbrowser
global dominant_emotion

def deepFaceAnalysis(image_path):
    img = image_path
    result = DeepFace.analyze(img_path = img , actions = ["emotion"])
    dominant_emotion = result[0]["dominant_emotion"]
    print("Detected emotion:", dominant_emotion)
    return dominant_emotion

#facial analysis
def get_song(emotion):
    if(not(library.contains_mood(emotion))):
        print("No emotion detected")
        #tell user to add a recommendation or just find one randomly?

    else:
        songList = library.get(emotion)
        if(len(songList) > 0):
            song = random.choice(songList)
            if messagebox.askyesno("Play Song", "Do you want to play a song?"):
                webbrowser.open_new_tab(song)


