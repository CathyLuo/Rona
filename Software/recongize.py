#!/usr/bin/env python3

import os
from pydub import AudioSegment
from pylab import *

class Recongize(object)
    def __init__(self, down_Thres = 10, up_Thres = 1000):
        self.down_Thres = down_Thres
        self.up_Thres = up_Thres

    def recognize(self, filename, filetype):
        filedir = os.path.abspath(__file__) + '/' + filename
        sound = AudioSegment.from_file(filename, filetype)
        Sample_Freq = sound.frame_rate
        duration = int(sound.duration_seconds * 10)
        freq_list = []
        for i in range(0, duration):
            item = sound[i * 100 : (i + 1) * 100]
            if item.max> 1.0:
                length = len(item.raw_data)
                solution = Sample_Freq / length
                itemfft = list(abs(fft(list(item.raw_data))))[down_Thres, up_Thres]
                max_db = max(itemfft)
                freq_near = solution * (itemfft.index(max_db) + down_Thres)
                freq_list.append(freq_near)
        return freq_list

    def classify(self, freq_list):
        pass
        #############

if __name__ == '__main__':
    pass
