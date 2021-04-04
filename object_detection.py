import os
import numpy as np
import torch
from PIL import image

class NumberPlateDataset(object):
    def __init__(self, root, transforms):
        self.root = root
        self.transforms = transforms
        self.imgs = list(sorted(os.listdir(os.path.join(root, ""))))
        self.imgs = list(sorted(os.listdir(os.path.join(root, ""))))
