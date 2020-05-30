#######
# Author: James Poole
# Date: 23 April 2016
# jgaple@gmail.com
#
# motors.py
#######

# https://gpiozero.readthedocs.io/en/stable/api_boards.html?highlight=CamJamKitRobot#gpiozero.Robot
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library
from time import sleep

robot = CamJamKitRobot()

# Set speeds between 0.0 and 1.0
# https://gpiozero.readthedocs.io/en/stable/api_boards.html?highlight=CamJamKitRobot#gpiozero.Robot
forwardspeed = 1.0
backwardspeed = 1.0
leftspeed = 0.4
rightspeed = leftspeed

def forward():
    robot.forward(forwardspeed)

def backward():
    robot.backward(backwardspeed)

def turnRight():
    robot.right(rightspeed)

def turnLeft():
    robot.left(leftspeed)

def stop():
    robot.stop()
