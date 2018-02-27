import cv2

cap = cv2.VideoCapture(0)

i = 1
while(1):
	ret, frame = cap.read()
	
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	cv2.imshow('prenos', gray) 	
	
	if cv2.waitKey(1) & 0xFF == ord('s'):
		pictureName = 'capture' + str(i) + '.jpg'
		print(pictureName)
		cv2.imwrite(pictureName,gray)
		i=i+1
		
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()