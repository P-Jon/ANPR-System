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

def convert_image_to_greyscale(path, file):
    img = read_img(path + file)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def grab_plates(label_img_path):
    for file in get_files(label_img_path):
        yield read_img(label_img_path + file), file

def save_label_plates(img_path, save_path):
    for (img, file) in grab_plates(img_path):
        save_img(img, save_path + file)

def grab_image_plates(label_img_path, img_path, save_path):
    fileList = []
    for (image, file) in grab_plates(label_img_path):
        file = file.replace("mask_", '')
        fileList.append(file)

    for file in get_files(img_path):
        if file in str(fileList):
            gray = convert_image_to_greyscale(img_path,file)
            save_img(gray, save_path + file)