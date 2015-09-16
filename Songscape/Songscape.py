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

fs, data = sc.io.wavfile.read('/home/zechthurman/Songscape/03. Kali 47 (Original Mix).wav')
t = data.size

def do_tplot():
    pylab.figure()
    pylab.plot(t,data)
    pylab.title("Membrane Potential over Time")
    pylab.xlabel("Time")
    pylab.ylabel("Membrane Potential")
    pylab.xlim(0,100)
    pylab.ylim(-1.9,2.2)
    pylab.show()
    return

print do_tplot()

