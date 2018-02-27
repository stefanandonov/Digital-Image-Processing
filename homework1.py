#Прва домашна задача по Обработка на слики 2018 година
#Стефан Андонов, 151020

import numpy as np
from decimal import Decimal
import cv2

def lin_equ(p1,p2):
	a = (p2[1]-p1[1])/(p2[0]-p1[0])
	b = p1[1]-a*p1[0]
	return a, b
	
def getValue(x,function):
	ret = 0
	for i in function.keys():
		if x<=i:
			ret = i;
			break
	
	return function[ret][0]*x+function[ret][1]

def contrastStretching (image, points):
	""" Funkcija koja sto prima dva argumenti, slikata i lista od parovi tocki (x,y).
		Funkcijata ne dava rezultat, tuku na ekran ja pecati novodobienata slika
		Se pocnuva so (0,0), a zavrshuva so (255,255).
	"""
	
	img = cv2.imread(image,0)
	
	#Vo recnikot coeff se stavaat vrednosti {x:[a,b]} kade sto za sekoe x1 <= x, se dadeni vrednostite
	#za koeficientite a i b vo ravenkata na prava y = ax + b
	coeff = {}
	for i in range(0,len(points)-1):		
		coefficients = lin_equ(points[i],points[i+1])
		coeff[points[i+1][0]]=coefficients
		
	x,y = img.shape
	
	for i in range(0,x):
		for j in range (0,y):
			img.itemset(i,j,getValue(img.item(i,j),coeff))
			
	cv2.imshow("Streched image",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
	

contrastStretching('strech.png',[[0,0],[50,30],[150,200],[255,255]])