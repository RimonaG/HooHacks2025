#from xxsubtype import bench

from MusicLibrary import MusicLibrary

library = MusicLibrary()

from deepface import DeepFace
import random
import webbrowser

img = "~/Desktop/folder/Angry.jpg"

result = DeepFace.analyze(img_path = img , actions = ["emotion"])
dominant_emotion = result[0]["dominant_emotion"]
print("Detected emotion:", dominant_emotion)

#facial analysis
library.