"""
Randomly prints from a list of 3 strings with a probability of:
1/2 for "I am a scary computer"
1/3 for "I am not a scary computer"
1/6 for "HA!HA!HA!HA!HA! -cue evil laughter- "
"""
import random
import tkinter as tk
_x = random.randint(1, 200)


def button_pressed():
    """
    if _x/2 has remainder of 0
    print "I am a scary computer"
    else if 2*_x/2 has a remainder of 0
    print "I am not a scary computer"
    else if 2*_x/2 does not have a remainder of 0
    print "HA!HA!HA!HA!HA! -cue evil laughter- "
    """
    _x = random.randint(1, 200)
    if _x % 2 == 0:
        print("I am a scary computer")
    elif _x % 3 == 0:
        print("HA!HA!HA!HA!HA! -cue evil laughter- ")
    elif _x % 1 == 0:
        print("I am not a scary computer")


window = tk.Tk()
border_effects = {
    "raised": tk.RAISED,
}
button = tk.Button(
    text="Click me!",
    relief=border_effects["raised"],
    borderwidth=8,
    width=15,
    height=5,
    command=button_pressed,
    bg="white",
    fg="black",)
button.pack()
greeting = tk.Label(text="Hello, Tkinter")
window.mainloop()
