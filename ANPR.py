import os
import cv2
import numpy as np
import imutils

# The bulk of this was taught by Nicholas Renotte (nicknochnack)
# https://github.com/nicknochnack/ANPRwithPython/blob/main/ANPR%20-%20Tutorial.ipynb
# I intend to use this as a test then go on to implement ML to robustly detect license plates to perform OCR upon.

def Filter(gray):
    return cv2.bilateralFilter(gray,5,50,50)

def CannyEdgeDetection(gray):
    bfilter = Filter(gray)
    return cv2.Canny(bfilter,40,200)

def SobelEdgeDetection(gray):
    bfilter = Filter(gray)
    gx = cv2.Sobel(bfilter, cv2.CV_64F, 1, 0)
    gy = cv2.Sobel(bfilter, cv2.CV_64F, 0, 1)
    g = np.sqrt(gx**2 + gy**2)
    return (g * 255 / g.max()).astype(np.uint8)

def GetContours(edged):
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    return sorted(contours, key=cv2.contourArea, reverse=True)[:10]

def FindPlate(contours):
    location = None
    for contour in contours: 
        approx = cv2.approxPolyDP(contour, 10, True)
        if (len(approx) == 4):
            location = approx
            return location

def GetMask(location, gray, img):
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
    (x,y) = np.where(mask==255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    return gray[x1:x2+1, y1:y2+1]  

def SaveMaskedImg(image, filename):
    print("Saving file: " + filename)
    cv2.imwrite('Data/Saved_Plates/' + filename, image)

def files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def GetLicensePlates():
    for file in files("Data/GB_Plates/"):
        print("Reading file: " + file)
        img = cv2.imread("Data/GB_Plates/" + file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #edged = CannyEdgeDetection(gray)
        edged = SobelEdgeDetection(gray)
        contours = GetContours(edged)
        location = FindPlate(contours)

        if (location is not None):
            mask = GetMask(location, gray, img)
            SaveMaskedImg(mask, file)

GetLicensePlates()