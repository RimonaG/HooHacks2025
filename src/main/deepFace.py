from xxsubtype import bench

from deepface import DeepFace
import random
import webbrowser

img = "happy.jpg"

result = DeepFace.analyze(img = img , actions = ["emotion"])
dominant_emotion = result[0]["dominant_emotion"]
print("Detected emotion:", dominant_emotion)

#facial analysis