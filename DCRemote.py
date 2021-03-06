#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)
direction = ""

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
myMotorL = mh.getMotor(3)
myMotorR = mh.getMotor(1)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotorL.setSpeed(150)
myMotorL.run(Adafruit_MotorHAT.FORWARD);
myMotorR.setSpeed(150)
myMotorR.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
myMotorL.run(Adafruit_MotorHAT.RELEASE);
myMotorR.run(Adafruit_MotorHAT.RELEASE);

while (direction != 'q'):
        direction = raw_input("Enter direction (w = Forward; s = Backward; a = Left; d = Right): ")
        
        # Move Forward
        if (direction == "w"):
                print("Ok, going forward")
                myMotorL.run(Adafruit_MotorHAT.FORWARD)
                myMotorR.run(Adafruit_MotorHAT.FORWARD)
                print "\tSpeed up..."
		for i in range(255):
			myMotorL.setSpeed(i)
			myMotorR.setSpeed(i)
			time.sleep(0.01)
	
		print "\tSlow down..."
		for i in reversed(range(255)):
			myMotorL.setSpeed(i)
			myMotorR.setSpeed(i)
			time.sleep(0.01)
	
	# Move Backward		
        elif (direction == "s"):
                print("Ok, going backward")
		myMotorL.run(Adafruit_MotorHAT.BACKWARD)
		myMotorR.run(Adafruit_MotorHAT.BACKWARD)
		print "\tSpeed up..."
		for i in range(255):
			myMotorL.setSpeed(i)
			myMotorR.setSpeed(i)
			time.sleep(0.01)
	
		print "\tSlow down..."
		for i in reversed(range(255)):
			myMotorL.setSpeed(i)
			myMotorR.setSpeed(i)
			time.sleep(0.01)
		
	# Move Left
        elif (direction == "a"):
                print("Ok, going left")
                myMotorL.run(Adafruit_MotorHAT.BACKWARD)
		myMotorR.run(Adafruit_MotorHAT.FORWARD)
		print "\tSpeed up..."
		for i in range(255):
			myMotorL.setSpeed(i)
			myMotorR.setSpeed(i)
			time.sleep(0.01)
	
		print "\tSlow down..."
		for i in reversed(range(255)):
			myMotorL.setSpeed(i)
			myMotorR.setSpeed(i)
			time.sleep(0.01)
                
        # Move Right
        elif (direction == "d"):
                print("Ok, going right")
                myMotorL.run(Adafruit_MotorHAT.FORWARD)
		myMotorR.run(Adafruit_MotorHAT.BACKWARD)
                print "\tSpeed up..."
		for i in range(255):
			myMotorL.setSpeed(i)
			myMotorR.setSpeed(i)
			time.sleep(0.01)
	
		print "\tSlow down..."
		for i in reversed(range(255)):
			myMotorL.setSpeed(i)
			myMotorR.setSpeed(i)
			time.sleep(0.01)
                
        # Catch typos
        else:
                print("Direction not recognised.")
        
        # Turn off motors
        print "Release"
	myMotorL.run(Adafruit_MotorHAT.RELEASE)
	myMotorR.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)