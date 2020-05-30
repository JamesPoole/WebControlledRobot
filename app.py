#!/usr/bin/env python3
#######
# Author: James Poole
# Date: 23 April 2016
# jgaple@gmail.com
#
# app.py
#######

# https://flask.palletsprojects.com/en/1.1.x/
from flask import Flask, render_template, request, redirect, url_for, make_response
import motors
import streamer
import signal # https://docs.python.org/3/library/signal.html
import sys

streamer.start()

def signal_handler(sig, frame):
    print('WebControlledRobot exiting')
    streamer.stop()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

app = Flask(__name__) #set up flask server

#when the root IP is selected, return index.html page
@app.route('/')
def index():

	return render_template('index.html')

#receive which pin to change from the button press on index.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin) #cast changepin to an int

    if changePin == 1:
        motors.turnLeft()
    elif changePin == 2:
        motors.forward()
    elif changePin == 3:
        motors.turnRight()
    elif changePin == 4:
        motors.backward()
    else:
        motors.stop()

    response = make_response(redirect(url_for('index')))
    return(response)

app.run(debug=True, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000
