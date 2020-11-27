import cv2
import numpy as np
from colorProcessing import colorRecognition

camera = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    colorRecognition(frame)

    detect = cascade.detectMultiScale(frameGray, 1.2, 5)
    for (x, y, w, h) in detect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)
        
    cv2.imshow("Camera", frame)
    k = cv2.waitKey(60)
    if k == 27:
        break
cv2.destroyAllWindows()
camera.release()


