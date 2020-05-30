#!/usr/bin/env python3
# mjpg-streamer control

# https://docs.python.org/3/library/subprocess.html
import subprocess
from time import sleep

streamer_args = ["mjpg_streamer", "-i", "input_raspicam.so -hf -vf -fps 15", "-o", "output_http.so -w /usr/local/share/mjpg-streamer/www/"]
streamer_process = None

def start():
    # https://docs.python.org/2/library/subprocess.html#popen-constructor
    global streamer_process
    streamer_process = subprocess.Popen(streamer_args)

def stop():
    global streamer_process
    # https://docs.python.org/2/library/subprocess.html#subprocess.Popen.poll
    streamer_process.poll()
    # https://docs.python.org/2/library/subprocess.html#subprocess.Popen.returncode
    if streamer_process.returncode is None:
        # https://docs.python.org/2/library/subprocess.html#subprocess.Popen.terminate
        streamer_process.terminate()
