import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(17,IO.OUT)	#gpio 2 -> red led as output
IO.setup(27,IO.OUT)	#gpio 3 -> blue led as output
IO.setup(22,IO.OUT)	#gpio 14 -> IR sensor as output
while 1:
	if(IO.input(22)==True):	#object is far away
		IO.output(17,True)	#Red led on
		IO.output(27,False)	#Blue led off

	if(IO.input(22)==False): #object is near
		IO.output(27,True) #Blue led on
		IO.output(17,False) # red led off
