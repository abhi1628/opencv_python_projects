
import cv2 as cv

org_img = cv.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\lenna.jpg')
b, g, r = cv.split(org_img)

cv.imshow('Original Image', org_img)
cv.imshow('Blue Channel', b)
cv.imshow('Green Channel', g)
cv.imshow('Red Channel', r)

# merged image

merge_img = cv.merge([b, g, r])
cv.imshow('Merged Image', merge_img)

cv.waitKey(0)