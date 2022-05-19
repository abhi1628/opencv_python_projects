
import cv2 as cv

org_img = cv.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\groot_resized.jpg')
hsv_img = cv.cvtColor(org_img, cv.COLOR_BGR2HSV)

cv.imshow('Original Image', org_img)
cv.imshow('HSV Image', hsv_img)

cv.waitKey(0)