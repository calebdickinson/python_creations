"""
Generates 15 random notes from an F Major scale if SAMPLE_RATE * "1"
"""

import random
import numpy as np
from scipy.io import wavfile

X = ""
Y = ""
Z = ""
q = []
for _ in range(15):  # number of notes
    x = random.randint(1, 12)  # number of different random possible notes
    if x == 1:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)  # 220 equals note A 220 Hz
        y = np.sin(220 * t)
        print("F5")
    if x == 2:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)
        y = np.sin(247 * t)
        print("G5")
    if x == 3:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)
        y = np.sin(277 * t)
        print("A5")
    if x == 4:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)
        y = np.sin(294 * t)
        print("Bb5")
    if x == 5:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)
        y = np.sin(330 * t)
        print("C6")
    if x == 6:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)
        y = np.sin(370 * t)
        print("D6")
    if x == 7:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)
        y = np.sin(415 * t)
        print("E6")
    if x == 8:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)
        y = np.sin(440 * t)
        print("F6")
    if x == 9:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)
        y = np.sin(494 * t)
        print("G6")
    if x == 10:
        Z = SAMPLE_RATE = 44100
        t = np.linspace(0, 20, SAMPLE_RATE * 1)
        y = np.sin(554 * t)
        print("A6")
    q = np.concatenate((q, y))

wavfile.write('python_creation_003A.wav', SAMPLE_RATE, q)
