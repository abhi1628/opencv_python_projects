import cv2

# read image as grey scale
img = cv2.imread('C:\\Users\\Global\\Documents\\ocv\\Youtube Videos\\groot.jpg', cv2.IMREAD_UNCHANGED)

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)

# save image
status = cv2.imwrite('C:\\Users\\Global\\Documents\\ocv\\Images\\groot_resized.jpg',resized)

print("Image written to file-system : ",status)
