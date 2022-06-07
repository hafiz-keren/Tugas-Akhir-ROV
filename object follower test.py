# Code source (Matt-Timmons Brown): https://github.com/the-raspberry-pi-guy/raspirobots
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import thread
import time
import RPi.GPIO as GPIO
motorA=11
motorB=13
motorC=15
motorD=16
motorE=18
motorF=22

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motorA, GPIO.OUT)
GPIO.setup(motorB, GPIO.OUT)
GPIO.setup(motorC, GPIO.OUT)
GPIO.setup(motorD, GPIO.OUT)
GPIO.setup(motorE, GPIO.OUT)
GPIO.setup(motorF, GPIO.OUT)

def navigasi(arah,kecepatan):
    if(arah=="kanan"):
        GPIO.output(motorA,False)
        GPIO.output(motorB,False)
        GPIO.output(motorC,True)
        GPIO.output(motorD,True)
        GPIO.output(motorE,False)
        GPIO.output(motorF,False)
        
        
    elif(arah=="kiri"):
        GPIO.output(motorA,True)
        GPIO.output(motorB,False)
        GPIO.output(motorC,False)
        GPIO.output(motorD,False)
        GPIO.output(motorE,False)
        GPIO.output(motorF,True)
        
        
    elif(arah=="lurus"):
        GPIO.output(motorA,False)
        GPIO.output(motorB,False)
        GPIO.output(motorC,True)
        GPIO.output(motorD,False)
        GPIO.output(motorE,False)
        GPIO.output(motorF,True)
        
    elif(arah=="naik"):
        GPIO.output(motorA,False)
        GPIO.output(motorB,True)
        GPIO.output(motorC,False)
        GPIO.output(motorD,False)
        GPIO.output(motorE,True)
        GPIO.output(motorF,False)
            
    elif(arah=="turun"):
        GPIO.output(motorA,False)
        GPIO.output(motorB,True)
        GPIO.output(motorC,False)
        GPIO.output(motorD,False)
        GPIO.output(motorE,True)
        GPIO.output(motorF,False)
    
    

    elif(arah=="berhenti"):
        GPIO.output(motorA,False)
        GPIO.output(motorB,False)
        GPIO.output(motorC,False)
        GPIO.output(motorD,False)
        GPIO.output(motorE,False)
        GPIO.output(motorF,False)
        
'''
    else:
        print("belum terdefinisi")
'''
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
        cv2.imshow("Camera Output", img)
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
     
        color_mask = cv2.inRange(hsv, lower_color, upper_color)
        result = cv2.bitwise_and(image, image, mask= color_mask)
 
        
        '''
        cv2.imshow("HSV", hsv)
        cv2.imshow("Color Mask", color_mask)
        cv2.imshow("Final Result", result)
        '''
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
                    navigasi('kanan',100)
                    print("Turning right")
                
                elif ball_location[1] < (center_image_x - (image_width/3)):
                    navigasi('kiri',100)
                    print("Turning left")
                    
                else:
                    navigasi("lurus",100)
                    print("Forward")
                
                if ball_location[1] > (center_image_y + (image_height/3)):
                    navigasi('naik',100)
                    print("up")
                
                elif ball_location[1] < (center_image_y - (image_height/3)):
                    navigasi('turun',100)
                    print("down")
                    
                else:
                    navigasi("hovering",100)
                    print("hovering")
                    
            elif (ball_location[0] < minimum_area):
                print("Target isn't large enough, searching")
            else:
                navigasi('berhenti',100)
                print("Target large enough, stopping")
                
        else:
            print("Target not found, searching")
     
        
        rawCapture.truncate(0)
        k = cv2.waitKey(5) #& 0xFF
        if "q" == chr(k & 255):
            break
    
