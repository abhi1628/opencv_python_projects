# checking python version

from platform import python_version
print(python_version())

# check opencv version

import cv2
print(cv2.__version__)

# read the image
im = cv2.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\lenna.jpg')
# display the image
cv2.imshow('Displayed Window',im)
# hold the displaying window until any key is pressed
cv2.waitKey(0) # waitKey(0) will display the window infinitely
