# Multi ESC Calibration
import os    
import time   
os.system ("sudo pigpiod")
time.sleep(1) 
import pigpio
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

ESC_1 = 17      #motor A
ESC_2 = 27      #motor B
ESC_3 = 22      #motor C
ESC_4 = 23      #motor D
ESC_5 = 24      #motor E
ESC_6 = 25      #motor F
Count_ESC = [ESC_1, ESC_2, ESC_3, ESC_4, ESC_5, ESC_6]

pi = pigpio.pi()

for E in Count_ESC:
    pi.set_servo_pulsewidth(E, 0) 

max_value = 1800
min_value = 790  

print("please disconnect battery.. then type kal")
                
def calibrate():   
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
        control()
                   
             
def control(): 

    time.sleep(1)
    speed = min_value
    print "w : maju, a : kiri, d : kanan, s : mundur, e : berhenti, z : turun "
    while True:
        inp = raw_input()
        
        if inp == "w":
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
            print "maju"
            #time.sleep(1)
        if inp == "d":
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
            print "kanan"
            #time.sleep(1)
        if inp == "a":
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
            print "kiri"
            #time.sleep(1)
        if inp == "s":
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
            print "mundur"
            #time.sleep(1)
        if inp == "z":
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
            speed = 870
            pi.set_servo_pulsewidth(ESC_5, speed)
            print "speed motor E = %d" % speed
            speed = 870
            pi.set_servo_pulsewidth(ESC_6, speed)
            print "speed motor F = %d" % speed
            print "turun"
            #time.sleep(1)
        if inp == "e":
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
            print "berhenti"
            #time.sleep(1)
        if inp =="b":
            break
        else:
            print "Press a,w,s or d"
        '''
        for E in Count_ESC:
            pi.set_servo_pulsewidth(E, speed)
        inp = raw_input()
        
        if inp == "q":
            speed -= 100    
            print "speed = %d" % speed
        elif inp == "e":    
            speed += 100 
            print "speed = %d" % speed
            
        elif inp == "d":
            speed += 10     
            print "speed = %d" % speed
        elif inp == "a":
            speed -= 10     
            print "speed = %d" % speed
        elif inp == "stop":
            stop() 
                    
            break
        else:
            print "Press a,q,d or e"
            '''
      
def stop(): 
    for E in Count_ESC:
        pi.set_servo_pulsewidth(E, 0)
    pi.stop()

  
inp = raw_input()

if inp == "kal":
    calibrate()

elif inp == "stop":
    stop()
