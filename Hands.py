import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)

mpHands=mp.solutions.hands
hands = mpHands.Hands()

while True:
    success,img =cap.read()