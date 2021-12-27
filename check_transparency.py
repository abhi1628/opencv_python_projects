import cv2

img = cv2.imread('C:\\Users\\Global\\Documents\\ocv\\Images\\peacock.png', cv2.IMREAD_UNCHANGED)
print(img[850][600])
print(img.shape)
