import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
p = GPIO.PWM(7,100)
while True :
	inp = raw_input()
	if inp == "q":
         p.start(7)
         time.sleep(2)
	if inp == "w":
         p.start(0)
         time.sleep(2)
	if inp == "s":
         p.stop()
         time.sleep(2)    
         break

p.ChangeDutyCycle(7)
time.sleep(1)

GPIO.cleanup()
