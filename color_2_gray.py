import cv2 as cv

org_img = cv.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\groot_resized.jpg')
print(org_img.shape)
gray_img = cv.cvtColor(org_img, cv.COLOR_BGR2GRAY) # Method 1
print(gray_img.shape)

gray_img_2 = cv.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\groot_resized.jpg',0) # Method 2

cv.imshow('Original Image', org_img)
cv.imshow('Grayscale Image', gray_img_2)

cv.waitKey(0)