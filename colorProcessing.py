import cv2
import numpy as np
from datetime import datetime
import time

def colorRecognition(frame):
    anoMesDia = datetime.now().strftime('%Y-%m-%d')
    horaMinuto = datetime.now().strftime('%H:%M')
    frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerRed = np.array([0, 164, 164])
    upper = np.array([255, 255, 255])
    mascaraRed = cv2.inRange(frameHsv, lowerRed, upper)
    resultadoRed = cv2.bitwise_and(frame, frame, mask=mascaraRed)
    frameGrayRed = cv2.cvtColor(resultadoRed, cv2.COLOR_BGR2GRAY)

    lowerGreen = np.array([36, 241, 0])
    mascaraGreen = cv2.inRange(frameHsv, lowerGreen, upper)
    resultadoGreen = cv2.bitwise_and(frame, frame, mask=mascaraGreen)
    frameGrayGreen = cv2.cvtColor(resultadoGreen, cv2.COLOR_BGR2GRAY)

    _, threshRed = cv2.threshold(frameGrayRed, 3, 255, cv2.THRESH_BINARY)
    red, _ = cv2.findContours(threshRed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    _, threshGreen = cv2.threshold(frameGrayGreen, 3, 255, cv2.THRESH_BINARY)
    green, _ = cv2.findContours(threshGreen, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for objetoRed in red:
        contadorRed = 0
        (xv, yv, wv, hv) = cv2.boundingRect(objetoRed)
        areaRed = cv2.contourArea(objetoRed)
        if areaRed > 1000:
            time.sleep(2)
            contadorRed = contadorRed + 1
            vermelho = cv2.rectangle(frame, (xv, yv), (xv+wv, yv+hv), (0, 0, 255), 1)
            cv2.imwrite("ColorRecognition/VermelhoDetectado.png ",vermelho)
            ContadorVermelho = open('ContadorDeAvaliacao','a')
            ContadorVermelho.write("Objeto Vermelho Captado ")
            ContadorVermelho.write(str(contadorRed))
            ContadorVermelho.write(" ------------ ")
            ContadorVermelho.write(horaMinuto)
            ContadorVermelho.write("\n")    
            ContadorVermelho.close()
            time.sleep(2)

    for objetoGreen in green:
        contadorGreen = 0
        (xv, yv, wv, hv) = cv2.boundingRect(objetoGreen)
        areaGreen = cv2.contourArea(objetoGreen)
        if areaGreen > 1000:
            time.sleep(2)
            contadorGreen = contadorGreen + 1
            verde = cv2.rectangle(frame, (xv, yv), (xv+wv, yv+hv), (0,252,124), 1)
            cv2.imwrite("ColorRecognition/VerdeDetectado.png ",verde)
            ContadorVerde = open('ContadorDeAvaliacao','a')
            ContadorVerde.write("Objeto Verde Captado ")
            ContadorVerde.write(str(contadorGreen))
            ContadorVerde.write(" ------------ ")
            ContadorVerde.write(horaMinuto)
            ContadorVerde.write("\n")    
            ContadorVerde.close()
            time.sleep(2)
    