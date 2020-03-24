import glob
import cv2
import os

def load_images(image_folder):
    imgs = dict()
    for filename in glob.glob(os.path.join("data/input/", image_folder, "*.JPG")):
        file = os.path.basename(filename)
        imgs[file] = cv2.imread(filename)
    return imgs
