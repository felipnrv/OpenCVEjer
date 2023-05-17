import cv2
import numpy as np
import imutils
import os

umbral=127
valor_maximo=255

captura = cv2.VideoCapture(0) # para que detecte la camara es 0


while True:
    # devuelve 2 argumentos, 1 es bool y el otro es la imagen
    ret, imagen = captura.read()
    _, th = cv2.threshold(imagen, umbral, valor_maximo, cv2.THRESH_BINARY_INV)
    gris=cv2.cvtColor(th,cv2.COLOR_BGR2GRAY)
    contornos, _ = cv2.findContours(gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #print('Contornos: ',len(contornos))
    #texto = "Contornos: "+ str(len(contornos))



    # el -1 es para que se dibujen todos los contornos
    # el 2 es el grosor de la linea y el color es el 255,0,0
    cv2.drawContours(imagen,contornos,-1,(255,0,0),20)
    #pone el texto de los contornos
    #cv2.putText(imagen,texto ,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),1)

    cv2.imshow('video',imagen)
    cv2.imshow('video',th)
        # saca 1 frame x seg, si es 5000 seria 1 frame cada 5 segundos,
        # si es 0 la ventana se despliega infinita como imagen hasta que presiones una tecla

        #0xFF es para que detecte el valor en una maquina x64
        # ord recibe un caracter y regresa el unicode

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


captura.release()
cv2.destroyAllWindows()


