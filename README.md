# yolo_detect_riped_and_unriped_tomatoes

I'm sharing my work on a computer vision project using the well-known YOLO (version 8) tool. 
My project took place in several stages: 
- downloading the dataset from kaggle
- modifying the database and annotations (see the datasets folder)
- creating the YAML file (see the tomatoes.yaml file)
- installing the Ultralytics package 
- learning and validating the model (see the train_val.py file)
- obtaining my pre-trained model (see the best.pt file)
- prediction of detections on a video (see the video_tomate.mp4 file)
- finally obtain the result of the prediction (see the track_tomate.mp4 file)

Files and folders generated during the learning and validation phase are not deposited. (To obtain them, simply run the train_val.py file).

To go straight to detection using my pre-trained model, you need to run the track.py file, taking care to change the source if necessary.
