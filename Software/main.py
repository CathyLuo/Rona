#! /usr/bin/env python3

import threading
import control
import record
import recognize
from protocol import *

port = '/dev/ttyUSB0'
baud_rate = 9600

ser = serial.Serial(port, baud_rate)

teacher = teach.Teach()
recongizer = recongize.Recongize()

while(True):
    pac = ser.read(5)
    if len(pac) == 0:
        continue

    scale = dic_scale(pac[1])
    music_type = dic_music_type(pac[2])
    function = dic_fuctions(pac[3])
    action = pac[4]

    if function == 'simple':
        simple_t = threading.Thread(target = play.play_audio, argc = (music_type, music_region, scale))
        simple_t.start()
    if function == 'record':
        signal = threading.Event()
        if action == 1:
            record_t = threading.Thread(target = record.record_audio, argc = (signal))
            signal.set()
        else:
            signal.clear()
            ###recongize

    if function == 'teach':
        pass
