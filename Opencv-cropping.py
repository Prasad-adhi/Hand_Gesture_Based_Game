import cv2
import numpy as np

img =cv2.imread("D:/Prasad/all projects & pictures/14992927909Arash.jpg")
print(img.shape)
imgResize=cv2.resize(img,(300,200))#resize the given image
imgCropped=img[275:450,250:]

cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)