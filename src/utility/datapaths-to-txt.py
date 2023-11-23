
# -- written by cwa -- 21/11/2023

import os

# this script is for creating txt files with all image paths (used for training)

dataset = 'ytbb_cat'    #specify which dataset

# function used for creating .txt file which contains all the image paths
def create_image_paths_file(data, filename):
    with open(filename, 'w') as file:
        for image in os.listdir(data):
            if image.endswith('.jpg'):
                file.write(os.path.join(os.path.abspath(data), image) + '\n')

print('\n\n -- FRAME PATHS TO .TXT : STARTING..')

print('\n -- writing paths to file..')
create_image_paths_file('../../data/processed/' + dataset + '/data/train/', 'train.txt')
create_image_paths_file('../../data/processed/' + dataset + '/data/val/', 'val.txt')
create_image_paths_file('../../data/processed/' + dataset + '/data/test/', 'test.txt')

print('\n -- FRAME PATHS TO .TXT : DONE ! :)')
