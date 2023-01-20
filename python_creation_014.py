"""
Choose Your Own Adventure Story Window 1#
"""
import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.geometry("600x650")
window.title("CHOOSE YOUR OWN ADVENTURE")
PATH = "C:/Users/CALEB DICKINSON/Downloads/Choose your own adventure.png"
img = ImageTk.PhotoImage(Image.open(PATH))
panel = tk.Label(window, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
x = tk.Label(
    window, text="You are off to seek your fortune.\n"
    "There are five roads that lead away from the town where you live.\n"
    "Which road do you choose to travel?"
)
x.pack()
y = tk.Frame(window)
z1 = tk.Button(y, text="Chittyville Road")
z2 = tk.Button(y, text="Paplau Road")
z3 = tk.Button(y, text="Vizinni Road")
z4 = tk.Button(y, text="Burbon Road")
z5 = tk.Button(y, text="Icicle Road")
z1.grid(row=0, column=0, padx=10)
z2.grid(row=0, column=1, padx=10)
z3.grid(row=0, column=2, padx=10)
z4.grid(row=0, column=3, padx=10)
z5.grid(row=0, column=4, padx=10)
y.pack(pady=20)
window.mainloop()
