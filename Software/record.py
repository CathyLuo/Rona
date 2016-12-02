#!/usr/bin/env python3

import pyaudio
import wave
import time

def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    MAX_RECORD_SECONDS = 15

    WAVE_OUTPUT_FILENAME = time.strftime("%D_%H-%M-%S", time.localtime()) + '.wav'
    ####may be wrong
    try:
        p = pyaudio.PyAudio()
    except Exception:
        print(Exception)
        #### handler
        pass

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frame_per_buffer = CHUNK)

    ######## record handler
