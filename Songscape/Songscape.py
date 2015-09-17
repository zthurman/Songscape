#!/usr/bin/env python
#  Songscape

# This is a program that will take an wav audio file input and
# generate a real-time 3D spectrogram of the audio file.

# Copyright (C) 2015 Zechariah Thurman
# GNU GPLv2

from __future__ import division
from scipy.io import wavfile
import scipy as sc
from numpy import *
from matplotlib import pyplot as plt
import sys


def spectrogram():
    fs, data = sc.io.wavfile.read('/home/zechthurman/Songscape/03. Kali 47 (Original Mix).wav')
    t = data.size/500
    NFFT = 1024
    Fs = int(1.0/dt)  # the sampling frequency

    plt.specgram(data[:,1], NFFT=NFFT, Fs=Fs, noverlap=900,
                                cmap=cm.gist_heat)

