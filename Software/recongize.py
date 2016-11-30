#!/usr/bin/env python3

from pydub import AudioSegment
from pylab import *

class recog_voice(object)
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype

    def recognize(self):
        down_Thres = 100
        up_Thres = 3000
        sound = AudioSegment.from_file(self.filename, self.filetype)
        Sample_Freq = sound.frame_rate
        duration = int(sound.duration_seconds * 10)
        freqlist = []
        for i in range(0, duration):
            item = sound[i * 100 : (i + 1) * 100]
            if item.max > 1.0:
                length = len(item.raw_data)
                freq_range = up_Thres * length / Sample_Freq
                freq_list = list(arange(down_Thres * length / Sample_Freq, freq_range) * Sample_Freq / length )
                itemfft = list(abs(fft(list(item.raw_data))))[40: (len(freq_list) + 40)]
                max_freq = freq_list[itemfft.index(max(itemfft))]
                freq_list.append(max_freq)
