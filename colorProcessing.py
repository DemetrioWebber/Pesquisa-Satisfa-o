import cv2
import numpy as np
from datetime import datetime
import time
import os

def colorRecognition(frame):
    anoMesDia = datetime.now().strftime('%Y-%m-%d')
    horaMinuto = datetime.now().strftime('%H:%M')
    frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerRed = np.array([6, 255, 252])
    upper = np.array([255, 255, 255])
    mascaraRed = cv2.inRange(frameHsv, lowerRed, upper)
    resultadoRed = cv2.bitwise_and(frame, frame, mask=mascaraRed)
    frameGrayRed = cv2.cvtColor(resultadoRed, cv2.COLOR_BGR2GRAY)

    lowerGreen = np.array([79, 232, 201])
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
            vermelho = cv2.rectangle(frame, (xv, yv), (xv+wv, yv+hv), (0, 0, 255), 1)
            cv2.imwrite("ColorRecognition/VermelhoDetectado.png ",vermelho)
            ContadorVermelho = open('ContadorVermelho.txt','a')
            ContadorVermelho.write("Objeto Vermelho Captado ")
            with open('ContadorVermelho.txt') as f:
                ContadorVermelho.write(str(sum(1 for _ in f)+ 1))
            ContadorVermelho.write(" ------------ ")
            ContadorVermelho.write(horaMinuto)
            ContadorVermelho.write("\n")    
            ContadorVermelho.close()
            cv2.rectangle(frame, (xv, yv), (xv+wv, yv+hv), (0, 0, 255), 1)
            time.sleep(3)

    for objetoGreen in green:
        (xv, yv, wv, hv) = cv2.boundingRect(objetoGreen)
        areaGreen = cv2.contourArea(objetoGreen)
        if areaGreen > 1000:
            verde = cv2.rectangle(frame, (xv, yv), (xv+wv, yv+hv), (0,252,124), 1)
            cv2.imwrite("ColorRecognition/VerdeDetectado.png ",verde)
            ContadorVerde = open('ContadorVerde.txt','a')
            ContadorVerde.write("Objeto Verde Captado ")
            with open('ContadorVerde.txt') as f:
                ContadorVerde.write(str(sum(1 for _ in f)+ 1))
            ContadorVerde.write(" ------------ ")
            ContadorVerde.write(horaMinuto)
            ContadorVerde.write("\n")
            ContadorVerde.close()
            time.sleep(3)

def mediaSatisfacao():
    somaVerde = 0
    somaVermelho = 0
    with open('ContadorVerde.txt') as G:
        somaVerde = sum(1 for _ in G)+ 1
    with open('ContadorVermelho.txt') as R:
        somaVermelho = sum(1 for _ in R) + 1
    somaTotal = somaVermelho + somaVerde
    os.system("cls")
    print("A contagem de avaliações teve:", somaVerde, "positivas, e", somaVermelho, "negativas.")
    print("A média de satisfação dos clientes foi de:", int((somaVerde*100)/ somaTotal), "%")



