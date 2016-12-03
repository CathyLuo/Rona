#! /usr/bin/env python3

import threading
import control
import record
import recognize
from protocol import *
from record import que

port = '/dev/ttyUSB0'
baud_rate = 9600

ser = serial.Serial(port, baud_rate)

teacher = teach.Teach()
recongizer = recongize.Recongize(down_Thres = 10, up_Thres = 1000)

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
            signal.set()
            record_t = threading.Thread(target = record.record_audio, argc = (signal))
        else:
            signal.clear()
            if not que.empty():
                filename = que.get()
                if not filename == None:
                    freq_list = recongizer.recongize(filename, 'wav')
                    ######classify

    if function == 'teach':
        pass
