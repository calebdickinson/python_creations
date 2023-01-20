"""
Plays an mp3 file in a tkinter window
"""
import tkinter as tk
from playsound import playsound
from PIL import ImageTk, Image
window = tk.Tk()
window.geometry("516x516")
window.title("CHOOSE YOUR OWN ADVENTURE")
PATH1 = ("C:/Users/CALEB DICKINSON/Downloads/Choose your own adventure.png")
img1 = ImageTk.PhotoImage(Image.open(PATH1))
label = tk.Label(window, image=img1)
label.place(x=0, y=0)


def play1():
    """
    Plays original music written by me
    """
    path_2 = (
        "C:/Users/CALEB DICKINSON/Downloads/"
        "Choose your own adventure music 1.mp3"
    )
    playsound(path_2, block=False)


z = tk.Button(window, text="Play Music", command=play1)
z.pack(pady=60)
window.mainloop()
