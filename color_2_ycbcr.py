import cv2 as cv

org_img = cv.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\groot_resized.jpg')
ycbcr_img = cv.cvtColor(org_img, cv.COLOR_BGR2YCrCb)

cv.imshow('Original Image', org_img)
cv.imshow('YCrCb Image', ycbcr_img)

cv.waitKey(0)