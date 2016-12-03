#!/usr/bin/env python3
import pyaudio
import wave
import time

que = Queue.Queue()

def record_audio(signal):
    signal.wait()
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    MAX_RECORD_SECONDS = 15

    WAVE_OUTPUT_FILENAME = time.strftime("%D_%H-%M-%S", time.localtime()) + '.wav'

    try:
        p = pyaudio.PyAudio()
    except Exception:
        print(Exception)
        que.put(None)
        return None

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frame_per_buffer = CHUNK)
    frames = []

    while(signal.is_set()):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframesraw(frames)
    wf.close()

    que.put(WAVE_OUTPUT_FILENAME)


if __name__ == '__main__':
