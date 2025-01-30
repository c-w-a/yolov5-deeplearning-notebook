# YOLOv5-DeepLearning-Notebook

example: (catbot3000)

![linkedin-version(1)](https://github.com/c-w-a/YOLOv5-DeepLearning-Notebook/assets/108597555/0874883d-046b-489e-9ede-a67f55448546)

experimenting with the YOLOv5 object detection algorithm and the YouTube Bounding Boxes dataset..

AUTOMATED SO FAR:
- class selection from the YouTube Bounding Boxes dataset
- downloading the videos (now about ~3x faster using multithreading)
- extracting frames (now much faster by only calling ffmpeg once per video..)
- generating labels in YOLOv5-ready format
- remapping selected classes for YOLOv5 (zero indexed)
- splitting the dataset and organizing files appropriately for YOLOv5 training
- 
