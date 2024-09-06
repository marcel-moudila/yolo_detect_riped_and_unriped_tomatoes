# -*- coding: utf-8 -*-
"""
Spyder Editor


Marcel MOUDILA
"""

from ultralytics import YOLO



# training gives best.pt, which detect ripsed and unripsed tomatoes
model = YOLO("best.pt")

# Define source 
source = "video_tomate.mp4"

# Run inference on the source
results = model(source, stream=True)  # generator of Results objects


# Run predict on the source
model.predict("video_tomate.mp4", save=True, imgsz=960, conf=0.25)