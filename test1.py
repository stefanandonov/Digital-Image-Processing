import cv2

img = cv2.imread('messi.jpg',0)
cv2.imshow('MESSI',img)
cv2.waitKey(0)
cv2.imwrite('messigray.png',img)
cv2.destroyAllWindows()
