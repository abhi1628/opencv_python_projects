import cv2
 
img = cv2.imread('C:\\Users\\Global\\Documents\\ocv\\Images\\lenna.jpg')
edges = cv2.Canny(img,100,100)
 
cv2.imshow("Edge Detected Image", edges)
 
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()
