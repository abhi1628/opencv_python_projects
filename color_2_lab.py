import cv2 as cv

org_img = cv.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\groot_resized.jpg')
lab_img = cv.cvtColor(org_img, cv.COLOR_BGR2LAB)

cv.imshow('Original Image', org_img)
cv.imshow('LAB Image', lab_img)

cv.waitKey(0)