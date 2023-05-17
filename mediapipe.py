import cv2
import numpy as np
import imutils
import os

captura = cv2.VideoCapture(cv2.CAP_ANY)

while(captura.isOpened()):
    ret,imagen = captura.read() # devuelve 2 argumentos, 1 es bool y el otro es la imagen
    if ret == True:
        cv2.imshow('video',imagen)
        cv2.waitkey(0)


captura.release()
#cv2.waitkey(0)
cv2.destroyAllWindows()


