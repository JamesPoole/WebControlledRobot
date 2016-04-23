#######
# Author: James Poole
# Date: 23 April 2016
# jgaple@gmail.com
#
# motors.py
#######

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 16 #(GPIO 23 - Pin 16)
Motor1B = 18 #(GPIO 24 - Pin 18)
Motor1Enable = 22 #(GPIO 25 - Pin 22)

Motor2A = 21 #(GPIO 9 - Pin 21)
Motor2B = 19 #(GPIO 10 - Pin 19)
Motor2Enable = 23 #(GPIO 11 - Pin 23)


#Set up all as outputs
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1Enable,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2Enable,GPIO.OUT)


def forward():
	print("Going Forwards")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1Enable,GPIO.HIGH) #Enable Motor 1 High
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2Enable,GPIO.HIGH) #Enable Motor 2 High

	sleep(2)



def backward():
	print("Going Backwards")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1Enable,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2Enable,GPIO.HIGH)

	sleep(2)

def turnRight():
	print("Going Right")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1Enable,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2Enable,GPIO.LOW)

	sleep(2)

def turnLeft():
	print("Going Left")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1Enable,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2Enable,GPIO.HIGH)

	sleep(2)

def stop():
	print("Stopping")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1Enable,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2Enable,GPIO.LOW)
