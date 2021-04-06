import os
import numpy as np
import torch
from PIL import Image

# Guidance being taken from
# https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html

class NumberPlateDataset(object):
    def __init__(self, root, transforms):
        self.root = root
        self.transforms = transforms
        self.imgs = list(sorted(os.listdir(os.path.join(root, "./Data/Image/"))))
        self.masks = list(sorted(os.listdir(os.path.join(root, "./Data/Label"))))

    def __getitem__(self, idx):
        img_path = os.path.join(self.root, "./Data/Image/", self.imgs[idx])
        mask_path = os.path.join(self.root, "./Data/Label/", self.masks[idx])
        
        mask = Image.open(mask_path)
        mask = np.array(mask)

        obj_id = np.unique(mask)

