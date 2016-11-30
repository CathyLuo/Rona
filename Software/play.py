#!/usr/bin/env python3

import os

class play_audio:
    def __init__(self, filepath, scale):
        self.filepath = filepath
        self.scale = scale

    def play(self):
        filename = self.scale + '.wav'
        os.system('play ' + filename)
