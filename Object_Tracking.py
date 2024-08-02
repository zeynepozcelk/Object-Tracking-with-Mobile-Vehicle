import maestro
import time
import pygame
import RPi.GPIO as GPIO
import cv2
import numpy as np

Surucu = maestro.Controller() // Maestro denetleyici için bir nesne yaratır.
Surucu.setAccel(5,3) // Kanal 5 üzerindeki servo motorun ivmelenme değerini ayarlar. 3 değeri, motorun ivmelenme hızını belirtir.
Surucu.setTarget(5,6000)
pozisyon = 6000

Daire_x = 0
Daire_y = 0
Daire_r = 0
Sabit_cap = 90
cap=cv2.VideoCapture(0)
Sag_Motor_Ileri = 27
Sag_Motor_Geri = 22
Sol_Motor_Ileri = 23
Sol_Motor_Geri = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Sag_Motor_Ileri, GPIO.OUT)
GPIO.setup(Sag_Motor_Geri, GPIO.OUT)
GPIO.setup(Sol_Motor_Ileri, GPIO.OUT)
GPIO.setup(Sol_Motor_Geri, GPIO.OUT)
def kontrol(sag,sol):
	GPIO.output(Sag_Motor_Ileri,sag)
	GPIO.output(Sag_Motor_Geri,not sag)
	GPIO.output(Sol_Motor_Ileri,sol)
	GPIO.output(Sol_Motor_Geri,not sol)
def dur():
	GPIO.output(Sag_Motor_Ileri,0)
	GPIO.output(Sag_Motor_Geri,0)
	GPIO.output(Sol_Motor_Ileri,0)
	GPIO.output(Sol_Motor_Geri,0)
def daire_tespiti(goruntu):
	global Daire_x,Daire_y,Daire_r,Sabit_cap
	gri = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
	gri = cv2.medianBlur(gri,5)
	daireler = cv2.HoughCircles(gri, cv2.HOUGH_GRADIENT, dp=1, minDist=40, param1=100, param2=50, minRadius=30, maxRadius=100)
	if daireler is not None:
		daireler = np.uint16(np.around(daireler))
		for daire in daireler[0, :]:
			merkez = (daire[0], daire[1])
			Daire_r = daire[2]
			Daire_x = daire[0]
			Daire_y = daire[1]
			cv2.circle(goruntu, merkez, Daire_r, (0, 255, 0), 2)
			cv2.circle(goruntu, merkez, 2, (0, 0, 255), 3)
	else:
		Daire_x = 320
		Daire_y = 240
		Daire_r = Sabit_cap
	return goruntu,Daire_x,Daire_y,Daire_r
def Yatay_Arama(yatay,x):	
	if (x < ((yatay/2) + (yatay*0.05))) and (x > ((yatay/2) - (yatay*0.05))):
		dur()
		print("DUR")
	elif x <= ((yatay/2)-(yatay*0.05)):
		kontrol(1,0)
		print("SOL")
	elif x >= ((yatay/2) + (yatay*0.05)):
		kontrol(0,1)
		print("SAĞ")
	else:
		dur()
		print("DUR")
	time.sleep(0.01)
	dur()
	time.sleep(0.19)
def Dikey_Arama(poz):	
	Surucu.setTarget(5,poz)
def Mesafe(r):
	if r >= (Sabit_cap+10):
		kontrol(1,1)
		print("GERİ")
	elif r <= (Sabit_cap-10):
		kontrol(0,0)
		print("İLERİ")
	else:
		dur()
	time.sleep(0.05)
	dur()
	time.sleep(0.15)
while True:
	ret,frame = cap.read()
	tespit_edilmis_goruntu,x,y,r = daire_tespiti(frame)
	cv2.imshow('Daire Tespiti', tespit_edilmis_goruntu)
	cv2.waitKey(1)
	dikey,yatay,kanal = tespit_edilmis_goruntu.shape
	if (x > ((yatay/2) + (yatay*0.05))) or (x < ((yatay/2) - (yatay*0.05))):
		Yatay_Arama(yatay,x)
	else:
		if y <= ((dikey/2)-(dikey*0.05)):
			pozisyon -= 5
			print("YUKARI")
		elif y >= ((dikey/2)+(dikey*0.05)):
			pozisyon += 5
			print("AŞAĞI")
		else:
			pozisyon = pozisyon
			print("ORTA")
			Mesafe(r)
		Dikey_Arama(pozisyon)

cap.release()
cv2.destroyAllWindows()
