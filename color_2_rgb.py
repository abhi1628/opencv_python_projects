
import cv2 as cv

org_img = cv.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\groot_resized.jpg')
rgb_img = cv.cvtColor(org_img, cv.COLOR_BGR2RGB)

cv.imshow('Original Image', org_img)
cv.imshow('RGB Image', rgb_img)

cv.waitKey(0)