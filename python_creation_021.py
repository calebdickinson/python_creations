"""
concatenation of python creations numbers 14, 15, 16, 17, 18, & 19
"""
import tkinter as tk
from PIL import ImageTk, Image
_window1 = tk.Tk()
_window1.geometry("600x650")
_window1.title("CHOOSE YOUR OWN ADVENTURE")
PATH1 = ("C:/Users/CALEB DICKINSON/Downloads/Choose your own adventure.png")
img1 = ImageTk.PhotoImage(Image.open(PATH1))
panel1 = tk.Label(_window1, image=img1)
panel1.pack(side="bottom", fill="both", expand="yes")
x_1 = tk.Label(
    _window1, text="You are off to seek your fortune.\n"
    "There are five roads that lead away from the town where you live.\n"
    "Which road do you choose to travel?"
)


def _window2():
    _window1.destroy()
    _window2 = tk.Tk()
    _window2.geometry("600x650")
    _window2.title("CHOOSE YOUR OWN ADVENTURE")
    path_2 = (
        "C:/Users/CALEB DICKINSON/Pictures/Saved Pictures/Chittyville Road.png"
    )
    img2 = ImageTk.PhotoImage(Image.open(path_2))
    panel2 = tk.Label(_window2, image=img2)
    panel2.pack(side="bottom", fill="both", expand="yes")
    x_2 = tk.Label(
        _window2, text="You begin your journey down Chittyville Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    x_2.pack()
    y_1 = tk.Frame(_window2)
    z1_2 = tk.Button(y_1, text="Walk")
    z2_2 = tk.Button(y_1, text="Bike")
    z3_2 = tk.Button(y_1, text="Drive")
    z1_2.grid(row=0, column=0, padx=20)
    z2_2.grid(row=0, column=1, padx=20)
    z3_2.grid(row=0, column=2, padx=20)
    y_1.pack(pady=20)
    _window2.mainloop()


def _window3():
    _window1.destroy()
    _window3 = tk.Tk()
    _window3.geometry("600x650")
    _window3.title("CHOOSE YOUR OWN ADVENTURE")
    _path3 = (
        "C:/Users/CALEB DICKINSON/Pictures/Saved Pictures/Paplau Road.png"
    )
    img3 = ImageTk.PhotoImage(Image.open(_path3))
    panel3 = tk.Label(_window3, image=img3)
    panel3.pack(side="bottom", fill="both", expand="yes")
    x_3 = tk.Label(
        _window3, text="You begin your journey down Paplau Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    x_3.pack()
    y_3 = tk.Frame(_window3)
    z1_3 = tk.Button(y_3, text="Walk")
    z2_3 = tk.Button(y_3, text="Bike")
    z3_3 = tk.Button(y_3, text="Drive")
    z1_3.grid(row=0, column=0, padx=20)
    z2_3.grid(row=0, column=1, padx=20)
    z3_3.grid(row=0, column=2, padx=20)
    y_3.pack(pady=20)
    _window3.mainloop()


def _window4():
    _window1.destroy()
    _window4 = tk.Tk()
    _window4.geometry("600x650")
    _window4.title("CHOOSE YOUR OWN ADVENTURE")
    _path4 = (
        "C:/Users/CALEB DICKINSON/Pictures/Saved Pictures/Vizinni Road.png"
    )
    img4 = ImageTk.PhotoImage(Image.open(_path4))
    panel4 = tk.Label(_window4, image=img4)
    panel4.pack(side="bottom", fill="both", expand="yes")
    x_4 = tk.Label(
        _window4, text="You begin your journey down Vizinni Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    x_4.pack()
    y_4 = tk.Frame(_window4)
    z1_4 = tk.Button(y_4, text="Walk")
    z2_4 = tk.Button(y_4, text="Bike")
    z3_4 = tk.Button(y_4, text="Drive")
    z1_4.grid(row=0, column=0, padx=20)
    z2_4.grid(row=0, column=1, padx=20)
    z3_4.grid(row=0, column=2, padx=20)
    y_4.pack(pady=20)
    _window4.mainloop()


def _window5():
    _window1.destroy()
    _window5 = tk.Tk()
    _window5.geometry("600x650")
    _window5.title("CHOOSE YOUR OWN ADVENTURE")
    _path5 = (
        "C:/Users/CALEB DICKINSON/Pictures/Saved Pictures/Burbon Road.png"
    )
    img5 = ImageTk.PhotoImage(Image.open(_path5))
    panel5 = tk.Label(_window5, image=img5)
    panel5.pack(side="bottom", fill="both", expand="yes")
    x_5 = tk.Label(
        _window5, text="You begin your journey down Burbon Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    x_5.pack()
    y_5 = tk.Frame(_window5)
    z1_5 = tk.Button(y_5, text="Walk")
    z2_5 = tk.Button(y_5, text="Bike")
    z3_5 = tk.Button(y_5, text="Drive")
    z1_5.grid(row=0, column=0, padx=20)
    z2_5.grid(row=0, column=1, padx=20)
    z3_5.grid(row=0, column=2, padx=20)
    y_5.pack(pady=20)
    _window5.mainloop()


def _window6():
    _window1.destroy()
    _window6 = tk.Tk()
    _window6.geometry("600x650")
    _window6.title("CHOOSE YOUR OWN ADVENTURE")
    _path6 = (
        "C:/Users/CALEB DICKINSON/Pictures/Saved Pictures/Icicle Road.png"
    )
    img6 = ImageTk.PhotoImage(Image.open(_path6))
    panel6 = tk.Label(_window6, image=img6)
    panel6.pack(side="bottom", fill="both", expand="yes")
    x_6 = tk.Label(
        _window6, text="You begin your journey down Icicle Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    x_6.pack()
    y_6 = tk.Frame(_window6)
    z1_6 = tk.Button(y_6, text="Walk")
    z2_6 = tk.Button(y_6, text="Bike")
    z3_6 = tk.Button(y_6, text="Drive")
    z1_6.grid(row=0, column=0, padx=20)
    z2_6.grid(row=0, column=1, padx=20)
    z3_6.grid(row=0, column=2, padx=20)
    y_6.pack(pady=20)
    _window6.mainloop()


x_1.pack()
y1 = tk.Frame(_window1)
z1_1 = tk.Button(y1, text="Chittyville Road", command=_window2)
z2_1 = tk.Button(y1, text="Paplau Road", command=_window3)
z3_1 = tk.Button(y1, text="Vizinni Road", command=_window4)
z4_1 = tk.Button(y1, text="Burbon Road", command=_window5)
z5_1 = tk.Button(y1, text="Icicle Road", command=_window6)
z1_1.grid(row=0, column=0, padx=10)
z2_1.grid(row=0, column=1, padx=10)
z3_1.grid(row=0, column=2, padx=10)
z4_1.grid(row=0, column=3, padx=10)
z5_1.grid(row=0, column=4, padx=10)
y1.pack(pady=20)
_window1.mainloop()
