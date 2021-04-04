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
    print(image)
    cv2.imwrite(filename, image)

def convert_image_to_greyscale(path):
    for file in get_files(path):
        print("Reading file: " + file)
        img = read_img(path + file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        save_img(gray, file)

def grab_plates(label_img_path):
    for file in get_files(label_img_path):
        yield read_img(label_img_path + file), file

def save_label_plates(img_path, save_path):
    for (img, file) in grab_plates(img_path):
        print("Saving img file: " + file + " to: " + save_path)
        print("Savepath: " + save_path)
        save_img(img, save_path + file)

def grab_image_plates(label_img_path):
    for (image, file) in grab_plates(label_img_path):
        print("Grabbed file: " + file)
