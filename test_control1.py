# Program Object following
# By : Adhyatmo Suryo Akintoro
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import thread
import time
import RPi.GPIO as GPIO
import os       
os.system ("sudo pigpiod")
time.sleep(1) 
import pigpio
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
ESC_1 = 17      #motor A
ESC_2 = 27      #motor B
ESC_3 = 22      #motor C
ESC_4 = 23      #motor D
ESC_5 = 24      #motor E
ESC_6 = 25      #motor F
Count_ESC = [ESC_1, ESC_2, ESC_3, ESC_4, ESC_5, ESC_6]
pi = pigpio.pi()
max_value = 1800
min_value = 790 
speed = min_value

print("please disconnect battery.. then type kal")

#Program Navigasi
def navigasi(arah):
	global Count_ESC,pi,speed,min_value,max_value
	if(arah=="kanan"):
		speed = 870
		pi.set_servo_pulsewidth(ESC_1, speed)
		print "speed motor A = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_2, speed)
		print "speed motor B = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_3, speed)
		print "speed motor C = %d" % speed
		speed = 870
		pi.set_servo_pulsewidth(ESC_4, speed)
		print "speed motor D = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_5, speed)
		print "speed motor E = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_6, speed)
		print "speed motor F = %d" % speed

	elif(arah=="kiri"):
		speed = 0
		pi.set_servo_pulsewidth(ESC_1, speed)
		print "speed motor A = %d" % speed
		speed = 870
		pi.set_servo_pulsewidth(ESC_2, speed)
		print "speed motor B = %d" % speed
		speed = 870
		pi.set_servo_pulsewidth(ESC_3, speed)
		print "speed motor C = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_4, speed)
		print "speed motor D = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_5, speed)
		print "speed motor E = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_6, speed)
		print "speed motor F = %d" % speed
		
	elif(arah=="lurus"):
		speed = 900
		pi.set_servo_pulsewidth(ESC_1, speed)
		print "speed motor A = %d" % speed
		speed = 900
		pi.set_servo_pulsewidth(ESC_2, speed)
		print "speed motor B = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_3, speed)
		print "speed motor C = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_4, speed)
		print "speed motor D = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_5, speed)
		print "speed motor E = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_6, speed)
		print "speed motor F = %d" % speed
	
	elif(arah=="berhenti"):
		speed = 0
		pi.set_servo_pulsewidth(ESC_1, speed)
		print "speed motor A = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_2, speed)
		print "speed motor B = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_3, speed)
		print "speed motor C = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_4, speed)
		print "speed motor D = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_5, speed)
		print "speed motor E = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_6, speed)
		print "speed motor F = %d" % speed

	elif(arah=="mundur"):
		speed = 0
		pi.set_servo_pulsewidth(ESC_1, speed)
		print "speed motor A = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_2, speed)
		print "speed motor B = %d" % speed
		speed = 870
		pi.set_servo_pulsewidth(ESC_3, speed)
		print "speed motor C = %d" % speed
		speed = 870
		pi.set_servo_pulsewidth(ESC_4, speed)
		print "speed motor D = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_5, speed)
		print "speed motor E = %d" % speed
		speed = 0
		pi.set_servo_pulsewidth(ESC_6, speed)
		print "speed motor F = %d" % speed
		

def tracking():
	camera = PiCamera()
	image_width = 640
	image_height = 480
	camera.resolution = (image_width, image_height)
	camera.framerate = 32
	rawCapture = PiRGBArray(camera, size=(image_width, image_height))
	center_image_x = image_width / 2
	center_image_y = image_height / 2
	minimum_area = 250
	maximum_area = 10000
 
	while True:
		HUE_VAL = 75
 
		lower_color = np.array([HUE_VAL-10,100,100])
		upper_color = np.array([HUE_VAL+10, 255, 255])
 
		for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
			image = frame.array
			img = cv2.rectangle(image, (155, 1000), (490, -10), (0, 0, 255), 3)
        
			hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
     
			color_mask = cv2.inRange(hsv, lower_color, upper_color)
			result = cv2.bitwise_and(image, image, mask= color_mask)
 
			cv2.imshow("Camera Output", img)
      
			image2, countours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        
			object_area = 0
			object_x = 0
			object_y = 0
     
			for contour in countours:
				x, y, width, height = cv2.boundingRect(contour)
				found_area = width * height
				center_x = x + (width / 2)
				center_y = y + (height / 2)
				if object_area < found_area:
					object_area = found_area
					object_x = center_x
					object_y = center_y
			if object_area > 0:
				ball_location = [object_area, object_x, object_y]
			else:
				ball_location = None
     
			if ball_location:
				if (ball_location[0] > minimum_area) and (ball_location[0] < maximum_area):
					if ball_location[1] > (center_image_x + (image_width/3)):
						navigasi('kanan')
						print("Turning right")
                
					elif ball_location[1] < (center_image_x - (image_width/3)):
						navigasi('kiri')
						print("Turning left")
                    
					else:
						navigasi("lurus")
						print("Forward")
 
				elif (ball_location[0] < minimum_area):
					navigasi('berhenti')
					print("Target isn't large enough, searching")
				else:
					navigasi('mundur')
					print("Target large enough, stopping")
                
			else:
				print("Target not found, searching")
     
     
			rawCapture.truncate(0)
			k = cv2.waitKey(5) #& 0xFF
			if "q" == chr(k & 255):
				break

def calibrate():
	#Count_ESC = [ESC, ESC_2, ESC_3, ESC_4]
	#pi = pigpio.pi()
	global Count_ESC,pi,speed,min_value,max_value
	for E in Count_ESC:
		pi.set_servo_pulsewidth(E, 0) 
	#max_value = 1800
	#min_value = 790 
	for E in Count_ESC: 
		pi.set_servo_pulsewidth(E, 0)
		time.sleep(1)
		pi.set_servo_pulsewidth(E, max_value)
	print("Connect battery.. then press Enter")
	inp = raw_input()
	if inp == '': 
		for E in Count_ESC:
			pi.set_servo_pulsewidth(E, min_value)   
		time.sleep(7)
		time.sleep (8)        
		for E in Count_ESC:
			pi.set_servo_pulsewidth(E, 0)           
        time.sleep(6) 
        print "Arming.."
        for E in Count_ESC:
            pi.set_servo_pulsewidth(E, min_value)
        time.sleep(4)
        tracking()


inp = raw_input()
if inp == "kal":
    calibrate()

