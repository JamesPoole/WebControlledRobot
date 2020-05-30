# Raspberry Pi CamJam EduKit 3 Web Controlled Robot With Video Stream

Raspberry Pi Robot that can be controlled via a website with a live streaming webcam using [Flask](https://flask.palletsprojects.com/en/1.1.x/)

Adapted from [James Poole's](http://jamespoole.me/2016/04/29/web-controlled-robot-with-video-stream/) and [Pablo Rogina's](https://bitbucket.org/pablojr/webcontrolledrobot/src/master/) projects with changes as follows:

* [Python 3](https://docs.python.org/3/)
* [CamJam EduKit 3](https://camjam.me/?page_id=1035) instead of LD293 IC + proto-board. Controlled by [gpiozero](https://gpiozero.readthedocs.io/en/stable/#) using [CamJamKitRobot API](https://gpiozero.readthedocs.io/en/stable/api_boards.html?highlight=CamJamKitRobot#camjamkitrobot)

* [Raspberry Pi Camera v1](https://uk.pi-supply.com/products/raspberry-pi-camera-board-v1-3-5mp-1080p)
* [MJPG-streamer](https://github.com/jacksonliam/mjpg-streamer) streaming application instead of motion. Since it's less resource intensive, video responsiveness and quality improved noticeably
* Updated index.html page from [Pablo Rogina's](https://bitbucket.org/pablojr/webcontrolledrobot/src/master/)
* Added automatic running and killing of MJPG-streamer using [subprocess.Popen](https://docs.python.org/2/library/subprocess.html#popen-constructor)
* Add catching of Ctrl-C using [python signals](https://docs.python.org/3/library/signal.html) with help from ["Stack Overflow How do I capture SIGINT in Python?"](https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python). Stops MJPG-streamer using [Popen.terminate](https://docs.python.org/2/library/subprocess.html#subprocess.Popen.terminate)

Developed using [VS Code](https://code.visualstudio.com/) with [Visual Studio Code Remote - SSH extension](https://code.visualstudio.com/docs/remote/ssh), [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Code Spell Checker extension](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker).

## Using VS Code (optional)
VS Code can remotely develop on the Pi, but it doesn't work on the Pi Zero. Setup by:
* Install VS Code on the remote PC from [Visual Studio Code](https://code.visualstudio.com/)
* Install [Visual Studio Code Remote - SSH extension](https://code.visualstudio.com/docs/remote/ssh)
* To do finish

## Installing Raspberry Pi Camera
https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md
'raspistill --help'
todo finish

## Installing MJPG-streamer
Based on [Michel Deslierres' instructions](https://www.sigmdel.ca/michel/ha/rpi/streaming_en.html#software) and [mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer):
* `sudo apt-get install cmake libjpeg8-dev`
* `sudo apt-get install gcc g++`
* `cd`
* `git clone git@github.com:jacksonliam/mjpg-streamer.git`
* `cd mjpg-streamer/mjpg-streamer-experimental/`
* `make`
* `sudo make install`

Get help with the Raspberry Pi input plug in:
`
Test with:

* `mjpg_streamer -i "input_raspicam.so -hf -vf -fps 10" -o "output_http.so -w /usr/local/share/mjpg-streamer/www/" &`
* http:\\\\\<pi address>\:8080/?action=stream
* `kill %1`

Get input & output option help:
* `mjpg_streamer -i "input_raspicam.so --help"`
* `mjpg_streamer -0 "output_http.so --help"`

Important raspicam input parameters:
* [-fps | --framerate]...: set video framerate, default 5 frame/sec

## Installing WebControlledRobot
From https://github.com/LegoChicken/WebControlledRobot:
* `cd`
* `git clone git@github.com:LegoChicken/WebControlledRobot.git`
* `cd WebControlledRobot`
* `chmod a+rx app.py` # Make executable

## Running the robot
* `./app.py`

## To do
* Give a fixed size to the web stream.
* Improve LEGO strength
* Document camera above
