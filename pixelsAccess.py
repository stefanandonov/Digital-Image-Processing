import numpy
import cv2

img = cv2.imread('messi.jpg',1)

x,y,z = img.shape

b,g,r = cv2.split(img)

img2 = cv2.imread('messi.jpg',0)


cv2.imshow('grayscale',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()