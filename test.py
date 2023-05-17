import torch
import numpy as np
import cv2
from time import timefrom ultralytics import YOLO

from supervision.draw.color import ColorPalette
from supervision.tools.detection import Detections,BoxAnnotator

# Load model

class objectdetection:

    def __init__(self,capture_index):

        self.capture_index=capture_index

        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using device:", self.device)

        self.model = self.load_model()

        self.CLASS_NAMES_DICT = self.model.model.names

        self.box_annotator = BoxAnnotator(color=ColorPalette(),thickness=3,text_thickness=3,text_scale=1.5)

def load_model(self):

    model = YOLO("yolov8m.pt")
    model.fuse()

    return model 

def predict(self,frame):

    results=self.model(frame)

    return results

def plot_bboxes(self,results,frame):
    
    xyxys = []
    confidences = []
    class_ids = []

    for result in results[0]:
        class_id = result.boxes.cls.numpy().astype(int)
