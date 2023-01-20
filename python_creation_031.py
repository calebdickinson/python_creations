"""
Opens a window with two buttons: "play" and "stop"
Music starts when "play" is pressed and plays in an infinite loop.
Music stops when "stop" is pressed or window is closed.
"""
import tkinter as tk
from pygame import mixer
mixer.init()

root = tk.Tk()
root.geometry("150x100")


def play():
    """
    play
    """
    mixer.music.load("Choose your own adventure music 1.wav")
    mixer.music.play(loops=-1)


def stop():
    """
    stop
    """
    mixer.music.stop()


frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Music")
label.pack()

button1 = tk.Button(frame, text="Play", command=play, width=15)
button1.pack(pady=5)
button2 = tk.Button(frame, text="Stop", command=stop, width=15)
button2.pack(pady=5)

root.mainloop()
