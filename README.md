# YOLOv5-DeepLearning-Notebook

tinkering with the YOLOv5 object detection model and the YouTube Bounding Boxes dataset..

PROJECT PLAN:
to create an easy-to-use deep learning notebook that will allow others to train a YOLOv5 object detection model using a subset of the YouTube Bounding Boxes dataset by abstracting and automating much of the process including environment set-up, data filtering, data acquisition, frame extraction, label generation, dataset splitting, YOLOv5 training preparation, etc. 

COMPLETED FEATURES SO FAR:
- YouTube-BB class selection
- downloading videos (now ~3x faster with multithreading)
- extracting frames (now much faster by only calling ffmpeg once per video)
- generating labels
- splitting the dataset
- YOLOv5-ready file structure

instructions:
- clone repo
- run set-up script (in progress..)
- 
