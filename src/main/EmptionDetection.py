#from xxsubtype import bench

from MusicLibrary import MusicLibrary

library = MusicLibrary()

from deepface import DeepFace
import random
import webbrowser
global dominant_emotion

def deepFace(image_path):
    img = "~/Desktop/folder/Angry.jpg"
    result = DeepFace.analyze(img_path = img , actions = ["emotion"])
    dominant_emotion = result[0]["dominant_emotion"]
    print("Detected emotion:", dominant_emotion)
    return dominant_emotion

#facial analysis
def get_song():
    name = #function from gui
    if(not(library.contains_mood(deepFace(name)))):
        print("No emotion detected")
        #tell user to add a recommendation or just find one randomly?

    else:
        songList = library.get(deepFace(name))
        if(len(songList) > 0):
            song = random.choice(songList)
            if(input("Do you want song to play? :") == "yes"):
                webbrowser.open_new_tab(song.url)


