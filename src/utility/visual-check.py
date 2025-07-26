
# -- written by cwa -- # 22/11/2023

import cv2
import os
import matplotlib.pyplot as plt
import random

# this script generates an overlay for manual visual inspection

dataset = 'ytbb_cat'     # specify which dataset
subset = 'train'         # specify which subset

# functioned used to create a bounding box overlay
def draw_label(image_path, label_path, image_size=640):

    image = cv2.imread(image_path)
    if image is None:
        print(f"       image not found: {image_path}")
        return
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_height, image_width, _ = image.shape

    with open(label_path, 'r') as file:
        labels = file.readlines()

    for label in labels:
        class_id, x_center, y_center, width, height = [float(x) for x in label.split()]

        x_center, y_center, width, height = x_center * image_width, y_center * image_height, width * image_width, height * image_height

        x_min = int(x_center - width / 2)
        y_min = int(y_center - height / 2)
        x_max = int(x_center + width / 2)
        y_max = int(y_center + height / 2)

        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    plt.imshow(image)
    plt.show()

print('\n\n -- VISUAL INSPECTION : STARTING..')

print('\n -- choosing random image..')
images_files = os.listdir('../../data/processed/' + dataset + '/data/images/' +  subset + '/')
video_ids = [filename.rsplit('.', 1)[0] for filename in images_files if filename.endswith('.jpg')]
video_id = random.choice(video_ids)

print('\n -- generating a bounding box overlay for manual visual inspection..')
image_path = '../../data/processed/' + dataset + '/data/images/' +  subset + '/' + video_id + '.jpg'
label_path = '../../data/processed/' + dataset + '/data/labels/' +  subset + '/' + video_id + '.txt'
draw_label(image_path, label_path)

print('\n -- VISUAL INSPECTION : DONE ! :)')
