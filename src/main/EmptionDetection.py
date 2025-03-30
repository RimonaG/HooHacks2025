#from xxsubtype import bench
#from tkinter import messagebox

from MusicLibrary import MusicLibrary

library = MusicLibrary()

from deepface import DeepFace
import random
import webbrowser


def deepFaceAnalysis(image):

    result = DeepFace.analyze(img_path = image , actions = ["emotion"])
    dominant_emotion = result[0]["dominant_emotion"]
    print("Detected emotion:", dominant_emotion)
    return dominant_emotion

#facial analysis: no longer in use because code was refactored to MusicLibrary due to dependency conflicts




