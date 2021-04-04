import os
import cv2

def get_files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def read_img(filename):
    print("Reading file: " + filename)
    return cv2.imread(filename)

def save_img(image, filename):
    print("Saving file: " + filename)
    cv2.imwrite(filename, image)

def convert_image_to_greyscale(path):
    for file in get_files(path):
        print("Reading file: " + file)
        img = read_img(file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        save_img(gray, file)

def grab_label_plates(label_img_path):
    for file in get_files(label_img_path):
        yield read_img(file), file

def save_label_plates(img, file, save_path):
    save_img(img, save_path + file)

def grab_image_plates(label_img_path):
    for (image, file) in grab_label_plates(label_img_path):
        print("Grabbed file: " + file)
