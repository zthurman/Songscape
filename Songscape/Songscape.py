
#!/usr/bin/env python
#  Songscape.py
## This is a program that will take an audio file input and generate a real-time 3D spectrogram of the audio file.

from __future__ import division
from scipy.io import wavfile
import scipy as sc
from numpy import *
import numpy as np
import pylab
import matplotlib as mp
from matplotlib import pyplot as plt
import sys


def spectrogram():
    fs, data = sc.io.wavfile.read('/home/zechthurman/Songscape/03. Kali 47 (Original Mix).wav')
    t = data.size/500
    NFFT = 1024
    Fs = int(1.0/dt)  # the sampling frequency

    plt.specgram(data[:,1], NFFT=NFFT, Fs=Fs, noverlap=900,
                                cmap=cm.gist_heat)

