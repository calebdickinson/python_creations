"""
Attempt at code for pressing a button on _window1 that will open _window2.
_window2 has a button that will open _window3, and vice versa.
Currently Nonfunctioning
"""
import tkinter as tk
from PIL import ImageTk, Image
_window1 = tk.Tk()
_window1.geometry("600x650")
_window1.title("CHOOSE YOUR OWN ADVENTURE")
PATH1 = ("C:/Users/CALEB DICKINSON/Downloads/swamp road.png")
img1 = ImageTk.PhotoImage(Image.open(PATH1))
panel1 = tk.Label(_window1, image=img1)
panel1.pack(side="bottom", fill="both", expand="yes")
x_1 = tk.Label(_window1, text="Window 1")


def _window2():
    _window1.destroy()
    _window2 = tk.Tk()
    _window2.geometry("600x650")
    _window2.title("CHOOSE YOUR OWN ADVENTURE")
    path_2 = ("C:/Users/CALEB DICKINSON/Downloads/desert road.png")
    img2 = ImageTk.PhotoImage(Image.open(path_2))
    panel2 = tk.Label(_window2, image=img2)
    panel2.pack(side="bottom", fill="both", expand="yes")
    x_2 = tk.Label(_window2, text="Window 2")
    x_2.pack()
    y_2 = tk.Frame(_window2)
    z_2 = tk.Button(y_2, text="Window 3", command=_window3)
    z_2.grid(row=0, column=0, padx=5)
    y_2.pack(pady=5)
    _window2.mainloop()


def _window3():
    # _window2.destroy()
    _window3 = tk.Tk()
    _window3.geometry("600x650")
    _window3.title("CHOOSE YOUR OWN ADVENTURE")
    path_3 = (
        "C:/Users/CALEB DICKINSON/Downloads/Choose your own adventure.png"
    )
    img3 = ImageTk.PhotoImage(Image.open(path_3))
    panel3 = tk.Label(_window3, image=img3)
    panel3.pack(side="bottom", fill="both", expand="yes")
    x_3 = tk.Label(_window2, text="Window 2")
    x_3.pack()
    y_3 = tk.Frame(_window2)
    z_3 = tk.Button(y_3, text="Window 1")
    z_3.grid(row=0, column=0, padx=5)
    y_3.pack(pady=5)
    _window3.mainloop()


x_1.pack()
y_1 = tk.Frame(_window1)
x_1 = tk.Button(y_1, text="Window 2", command=_window2)
x_1.grid(row=0, column=0, padx=5)
y_1.pack(pady=5)
_window1.mainloop()
