"""
Loops wav file for x number of seconds where x is equal to time.sleep(x)
In this example, a 60 second file is played and then repeated for 10 seconds.

In mixer.Sound.play(loops=y), y is equal to the number of loops.
If y = -1, loops repeat indefinitely.

Note: wav files with a few seconds of silence at the end or beginning
can be edited in Audacity simply by deleting empty front and back of waveform
in order to have a cleaner music loop.
"""
import time
from pygame import mixer
mixer.init()
path_music1 = mixer.Sound(
    "C:/Users/CALEB DICKINSON/Documents/Scores/"
    "Choose your own adventure music 1.wav"
)
mixer.Sound.play(path_music1, loops=-1)
time.sleep(70)
