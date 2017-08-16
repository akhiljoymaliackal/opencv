import cv2
import numpy as np
from random import randint

path=raw_input("enter the image path:\t")
img = cv2.imread(path)
opr=input("choose the option\n1)encription\n2)decription")
def encrypt():
	string=raw_input("enter the character to encode :")
	cha_list=[ord(c) for c in string]
	print len(cha_list)
	img_hlf=len(img)/2
	img_key=len(img)/3
	
	print "img_key :",img_key
	
	i=0
	p=0
	j=0

	test=len(cha_list)
	while i<len(cha_list):
		img[img_hlf][p][j]=cha_list[i]
		
		j=j+1
		if j==3:
			j=0
			p=p+1
		i=i+1
	img[img_hlf][p][j]=0 #encription completed
	key_set=randint(111,255)
	img[img_key][1][1]=key_set #encripted with key
	cv2.imwrite('encrypted.png',img)
	print "the image is encripted with key :\t",key_set
	print "encrypted image name is : encrypted.png  is saved in your current working directory"
	
	cv2.imshow("encrypted",img)
	cv2.waitKey(0)
def decrypt():
	ask_key=input("enter the key\t")
	img_key=len(img)/3
	char_list=[]
	if ask_key==img[img_key][1][1]:
		print "key accepted"
		img_hlf=len(img)/2
		i=0
		j=0
		p=0
		while img[img_hlf][p][j]!=0:
			char_list.append(img[img_hlf][p][j])
			
			j=j+1
			if j==3:
				j=0
				p=p+1
			i=i+1
		 #decrypted
		cha_finlist=[chr(c) for c in char_list]
		for i in cha_finlist:
			print i,
	else :
		print "invalid key"
if opr==1:
	encrypt()
elif opr==2:
	decrypt()
