# YOLOv5-deeplearning-notebook

**automated pipeline for training custom YOLOv5 object detection models using the YouTube Bounding Box dataset**
- simple notebook interface
- supports 23 different object classes (person, cat, dog, vehicles, etc.)
- processes YouTube videos into training-ready datasets
- supports cloud or local GPU resources for training models

## usage

1. set parameters in `yolobook.ipynb`
2. run cells sequentially
3. get trained model + performance metrics

![linkedin-version(1)](https://github.com/c-w-a/YOLOv5-DeepLearning-Notebook/assets/108597555/0874883d-046b-489e-9ede-a67f55448546)

## automated pipeline features

**data processing** (`src/utility/process-data.py`):
- downloads YouTube videos (added multithreading, ~3x faster now)
- extracts frames efficiently (a single ffmpeg call per video)
- generates YOLO-format bounding box labels
- remaps class IDs to zero-indexed format
- splits data into train/validation/test sets
- handles cleanup and error cases

**YOLOv5 integration**:
- pre-configured for accepted dataset formats
- automated YAML config generation
- ready-to-run training pipeline

**utilities**:
- `visual-check.py` - randomized dataset inspection with bounding box overlays
- `datapaths-to-txt.py` - generates image path files for training
