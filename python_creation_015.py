"""
Choose Your Own Adventure Story Window 2#
"""
import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.geometry("600x650")
window.title("CHOOSE YOUR OWN ADVENTURE")
PATH = "C:/Users/CALEB DICKINSON/Pictures/Saved Pictures/Chittyville Road.png"
img = ImageTk.PhotoImage(Image.open(PATH))
panel = tk.Label(window, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
x = tk.Label(
    window, text="You begin your journey down Chittyville Road. "
    "Do you choose to walk, bike, or drive?"
    )
x.pack()
y = tk.Frame(window)
x1 = tk.Button(y, text="Walk")
x2 = tk.Button(y, text="Bike")
x3 = tk.Button(y, text="Drive")
x1.grid(row=0, column=0, padx=30)
x2.grid(row=0, column=1, padx=30)
x3.grid(row=0, column=2, padx=30)
y.pack(pady=30)
window.mainloop()
