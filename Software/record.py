#!/usr/bin/env python3
import pyaudio
import wave
import time

def record_audio(signal):
    signal.wait()
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
    frames = []

    signal.wait(1)
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_str
