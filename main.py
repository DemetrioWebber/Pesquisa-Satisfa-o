import cv2
import numpy as np
from colorProcessing import colorRecognition, mediaSatisfacao

camera = cv2.VideoCapture(0)
view_cascade = cv2.CascadeClassifier("treinamento/cascade.xml")

while True:
    _,img = camera.read()
    height, width, c = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rosto = view_cascade.detectMultiScale(gray, 1.50, 5)
    for (x,y,w,h) in rosto:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    colorRecognition(img)
        
    cv2.imshow("Camera", img)
    k = cv2.waitKey(60)
    if k == 27:
        break
cv2.destroyAllWindows()
camera.release()

mediaSatisfacao()

