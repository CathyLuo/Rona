#!/usr/bin/env python3

import os

def play_audio(music_type, music_region, scale):
    filename = os.path.pardir + '/Resouse/' + music_type + '/' + scale + '.wav'
    os.system('play ' + file_path)
