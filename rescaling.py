import cv2

# read the image
im = cv2.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\groot.jpg')
# display the image
cv2.imshow('Displayed Window',im)
# hold the displaying window until any key is pressed

h = cv2.resize(im, (0,0), fx = 0.1, fy = 0.1,)
w = cv2.resize(im, (850, 800))

resized_image = cv2.resize(im, (780, 540), interpolation=cv2.INTER_NEAREST)
cv2. imshow('Resized Image', resized_image)
cv2.waitKey(0) # waitKey(0) will display the window infinitely
