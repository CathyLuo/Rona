#!/usr/bin/env python3

import serial
import protocol
import play
import record
import threading

class control(object):
    def analyze(pac, sys_status):


















class control(object):
    def __init__(self, port = '/dev/ttyUSB0', baud_rate = 9600, time_out = 1):
        self.ser = serial.Serial(port, baud_rate, timeout = time_out)

    def analyze_pac(self):
        pac_fromA = ser.read(5)
        if len(pac_fromA) == 0:
            return None

        head = pac_fromA[0]
        scale = dic_scale(pac_fromA[1])
        music_type = dic_music_type(pac_fromA[2])
        function = dic_fuctions(pac_fromA[3])
        action = pac_fromA[4]

        if function == 'teach':
            #############
        if function == 'record':
        t = threading.Thread(target = play.play_audio, argc = (music_type, music_region, scale))
        t.setDaemon(True)
        t.start()
