# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:39:35 2024

@author: MOUDILA Marcel
"""

from ultralytics import YOLO



# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# train the model
model.train(data="tomatoes.yaml", epochs=100, imgsz=640)  # train the model
metrics = model.val()  # evaluate model performance on the validation set