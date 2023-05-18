import os

from ultralytics import YOLO
import cv2
import numpy as np

Video = os.path.join('.','media')

video_path = os.path.join(Video,'video.mp4')
video_path_out= '{}_out.mp4'.format(video_path)
ret, frame = cap.read()
H,W , _ =frame.shape
out= cv2.VideoWriter(video_path_out,cv2.VideoWriter_fourcc(*'mp4v'), 30, (W,H))

model_path =os.path.join('.','model','yolov8n.pt')

model =YOLO(model_path)

threshold = 0.5

