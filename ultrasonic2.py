#System Function Test

# Import libraries
import RPi.GPIO as GPIO
import time
from array import *

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)
'''
# Set pin 12 as an output, and set servo1 as pin 12 as PWM
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(12,50) # Note 12 is pin, 50 = 50Hz pulse

# Set pin 14 as an output, and set servo2 as pin 14 as PWM
GPIO.setup(14,GPIO.OUT)
servo2 = GPIO.PWM(14,50) # Note 12 is pin, 50 = 50Hz pulse
'''
# Set Ultrsonic GPIO numbering mode
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 15
GPIO_ECHO = 14

#set Ultrasonic GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#Define Range Measurement Lines
def distance():
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()

	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()

	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed * 34300) / 2

	return distance
