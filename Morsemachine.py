#!/bin/python3
import RPi.GPIO as GPIO #importing GPIO PINS TIME OS and SYS commands
import time
import os
import sys

B_pin = 18 #buzzer pin number
Trg = 22 #touch sensor pin number
LDG = 23 # LED PIN variables
LDR = 24 # LED PIN variables
LDY = 17 # LED PIN variables
GPIO.setmode(GPIO.BCM) #sets up pins
GPIO.setwarnings(False)
GPIO.setup(Trg,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LDG,GPIO.OUT) 
GPIO.setup(LDY,GPIO.OUT)
GPIO.setup(LDR,GPIO.OUT)
GPIO.setup(B_pin,GPIO.OUT)
count = int(0) #counter to change phase

global touchstatus
touchstatus = False
if (GPIO.input(Trg)==True): 
    count =(count+1) #this variable keeps a count to swap between loops.
time.sleep(2)

while (count == 1): # this loop will turn on the first LED and display the second Morse code message
    print(count)
    if (GPIO.input(Trg)==True): 
        count =(count+1) #this variable keeps a count to swap between loops.
    print ("LED ON") # LOW turns buzzer on High turns off, Sleep time decides Long or short beep
    #S
    GPIO.output(LDR,GPIO.HIGH)
    time.sleep(1)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)

    
    #O
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    
    #S
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(4.5)
    print ("LED OFF")
    GPIO.output(LDR,GPIO.LOW)
    time.sleep(4)
while (count == 2): # This loop will flash the second LED and display the second message until the sensor is touched again
    print(count)
    if (GPIO.input(Trg)==True): 
        count =(count+1) #this variable keeps a count to swap between loops.
    print ("LED ON") #H
    GPIO.output(LDY,GPIO.HIGH)
    time.sleep(1)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    #E
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    #LL
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    #O
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    print ("LED OFF")
    GPIO.output(LDY,GPIO.LOW)
    time.sleep(4)
while (count == 3): # This loop will flash the Third LED and display the Third message until the sensor is touched again
    print(count)
    if (GPIO.input(Trg)==True): 
        count =(count+1) #this variable keeps a count to swap between loops.
    print ("LED ON")
    #S
    GPIO.output(LDG,GPIO.HIGH)
    time.sleep(1)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)

    
    #o
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    
    #S
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output (B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(B_pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output (B_pin,GPIO.HIGH)
    print ("LED OFF")
    GPIO.output(LDG,GPIO.LOW)
    time.sleep(4)
if count >= 4: # This loop will reset the program and quit.
    count = count = 0
    GPIO.cleanup
    sys.exit()