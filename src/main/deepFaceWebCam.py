from xxsubtype import bench

import cv2
from deepface import DeepFace
import random
import webbrowser

cap = cv2.VideoCapture(0)
print("Press SPACE to capture image")

while True:
    ret, frame = cap.read()
    cv2.imshow('Space to see frame: ', frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite("captured.jpg", frame)
        break

cap.release()
cv2.destroyAllWindows()

#facial analysis