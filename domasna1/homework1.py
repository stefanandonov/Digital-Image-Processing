#Прва домашна задача по Обработка на слики 2018 година
#Стефан Андонов, 151020

import numpy as np
import cv2

def lin_equ(p1,p2):
	"""Funkcija koja prima vrednost dve tocki vo format (x,y), a vrakja rezultat par na tocki
	a,b sto gi oznacuvaat koeficientite vo ravenkata na prava y=ax+b"""
	a = (p2[1]-p1[1])/(p2[0]-p1[0])
	b = p1[1]-a*p1[0]
	return a, b
	
def getValue(x,function):
	"""Funkcija koja ja presmetuva novata vrednost za grayscale pixel (prviot argument) spored funkcijata za stretching
	(definirana na delovi) koja se predava kako vtor argument vo vid na recnik."""
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
	
	#Za sekoj pixel od slikata img se primenuva funkcijata za stretching so povik na funkcijata getValue(x,function)
	x,y = img.shape	
	for i in range(0,x):
		for j in range (0,y):
			img.itemset(i,j,getValue(img.item(i,j),coeff))
	
	#Novodobienata slika se prikazuva na ekran i se zacuvuva vo tekovniot direktorium.
	cv2.imshow("Stretched image",img)
	cv2.imwrite("stretched.png",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def main():
	contrastStretching('strech.png',[[0,0],[50,30],[70,100],[150,200],[200,220],[240,20],[255,255]])

if __name__ == "__main__":
	main()	

