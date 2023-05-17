import cv2
import numpy as np
import imutils
import os

umbral=100
valor_maximo=255

captura = cv2.VideoCapture(0) # para que detecte la camara es 0


while True:
    ret,imagen = captura.read() # devuelve 2 argumentos, 1 es bool y el otro es la imagen
    _, th = cv2.threshold(imagen, umbral, valor_maximo, cv2.THRESH_BINARY_INV)

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


