"""
code solution for problem in python creation 21
"""
import tkinter as tk
_window1 = tk.Tk()
_window1.title("CHOOSE YOUR OWN ADVENTURE")
_window1.geometry("600x650")


def _window2():
    """
    ends window and opens another one
    """
    _window1.destroy()
    _window2 = tk.Tk()
    tk.Label(_window2, text="New Window").pack()
    _window2.mainloop()


button = tk.Button(text="Click Me!", command=_window2)
button.pack()
_window1.mainloop()
