"""
Generates sound & prints notes for serial 12-tone row from tones G#5/Ab5 to B6
"""
# Edit: For some reason actual notes played are a M10 above Hz number
# Because of this all note names were renamed to show actual note being played
# These are the notes played only when there is a "1" in num=SAMPLE_RATE * "1"
# Changing this number changes the pitch of all the notes

from random import sample
import numpy as np
from scipy.io import wavfile

q = []
Z = SAMPLE_RATE = 44100
t = np.linspace(
    start=0,
    stop=20,
    num=SAMPLE_RATE * 1
)
list1 = [
    "G#5/Ab5",
    "A5",
    "A#5/Bb5",
    "B5",
    "C6",
    "C#6/Db6",
    "D6",
    "D#6/Eb6",
    "E6",
    "F6",
    "F#6/Gb6",
    "G6"
]
twelve_tone_list = sample(list1, 12)
print(twelve_tone_list)
for x in twelve_tone_list:
    if x == "G#5/Ab5":
        y = np.sin(262 * t)  # 262 Hz is Middle C
    if x == "A5":
        y = np.sin(277 * t)
    if x == "A#5/Bb5":
        y = np.sin(294 * t)
    if x == "B5":
        y = np.sin(311 * t)
    if x == "C6":
        y = np.sin(330 * t)
    if x == "C#6/Db6":
        y = np.sin(349 * t)
    if x == "D6":
        y = np.sin(370 * t)
    if x == "D#6/Eb6":
        y = np.sin(392 * t)
    if x == "E6":
        y = np.sin(415 * t)
    if x == "F6":
        y = np.sin(440 * t)
    if x == "F#6/Gb6":
        y = np.sin(466 * t)
    if x == "G6":
        y = np.sin(493 * t)
    q = np.concatenate((q, y))

wavfile.write('python_creation_004A.wav', SAMPLE_RATE, q)
