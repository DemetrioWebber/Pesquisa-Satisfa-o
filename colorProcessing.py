import cv2
import numpy as np
from datetime import datetime
import time

def colorRecognition(frame):
    anoMesDia = datetime.now().strftime('%Y-%m-%d')
    horaMinuto = datetime.now().strftime('%H:%M')
    frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerRed = np.array([167, 146, 0])
    upper = np.array([255, 255, 255])
    mascaraRed = cv2.inRange(frameHsv, lowerRed, upper)
    resultadoRed = cv2.bitwise_and(frame, frame, mask=mascaraRed)
    frameGrayRed = cv2.cvtColor(resultadoRed, cv2.COLOR_BGR2GRAY)

    lowerGreen = np.array([84, 144, 97])
    mascaraGreen = cv2.inRange(frameHsv, lowerGreen, upper)
    resultadoGreen = cv2.bitwise_and(frame, frame, mask=mascaraGreen)
    frameGrayGreen = cv2.cvtColor(resultadoGreen, cv2.COLOR_BGR2GRAY)

    _, threshRed = cv2.threshold(frameGrayRed, 3, 255, cv2.THRESH_BINARY)
    red, _ = cv2.findContours(threshRed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    _, threshGreen = cv2.threshold(frameGrayGreen, 3, 255, cv2.THRESH_BINARY)
    green, _ = cv2.findContours(threshGreen, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for objetoRed in red:
        (xv, yv, wv, hv) = cv2.boundingRect(objetoRed)
        areaRed = cv2.contourArea(objetoRed)
        if areaRed > 1000:
            cv2.rectangle(frame, (xv, yv), (xv+wv, yv+hv), (0, 0, 255), 1)

    for objetoGreen in green:
        (xv, yv, wv, hv) = cv2.boundingRect(objetoGreen)
        areaGreen = cv2.contourArea(objetoGreen)
        if areaGreen > 1000:
            verde = cv2.rectangle(frame, (xv, yv), (xv+wv, yv+hv), (0,252,124), 1)
            cv2.imwrite("GreenRecognition/VerdeDetectado.png ",verde)
            ContadorVerde = open('ContadorVerde','a')
            ContadorVerde.write("Objeto Verde Captado ----- ")
            ContadorVerde.write(horaMinuto)
            ContadorVerde.write("\n")    
            ContadorVerde.close()
            time.sleep(1)