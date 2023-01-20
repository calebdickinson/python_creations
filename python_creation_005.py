"""
Generates chromatic scale.
If num=SAMPLE_RATE * x where x is equal to 5, scale begins on E.
If x = 4, scale begins on G#/Ab
If x = 3, scale begins on C#/Db
If x = 2, scale begins on G#/Ab 415 Hz
If x = 1, scale begins on G#/Ab 831 Hz
"""

import numpy as np
from scipy.io import wavfile

q = []
Z = SAMPLE_RATE = 44100
t = np.linspace(
    start=0,
    stop=20,
    num=SAMPLE_RATE * 1
)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for x in list1:
    if x == 1:
        y = np.sin(262 * t)
    if x == 2:
        y = np.sin(277 * t)
    if x == 3:
        y = np.sin(294 * t)
    if x == 4:
        y = np.sin(311 * t)
    if x == 5:
        y = np.sin(330 * t)
    if x == 6:
        y = np.sin(349 * t)
    if x == 7:
        y = np.sin(370 * t)
    if x == 8:
        y = np.sin(392 * t)
    if x == 9:
        y = np.sin(415 * t)
    if x == 10:
        y = np.sin(440 * t)
    if x == 11:
        y = np.sin(466 * t)
    if x == 12:
        y = np.sin(493 * t)
    q = np.concatenate((q, y))

wavfile.write('python_creation_005.wav', SAMPLE_RATE, q)
