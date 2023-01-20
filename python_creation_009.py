"""
Basic code for part of Python_Creation_No.10
"""

from random import sample

list1 = [
    "Panda",
    "Alien",
    "Evil Monster",
    "Dragon",
    "Slithy Toves",
    "Borogoves",
    "Jubjub Bird",
    "Tumtum Tree",
    "Jabberwock",
    "Bandersnatch"
]
X = sample(list1, 1)
SEPARATOR = ", "
Y = (SEPARATOR.join(X))
print(f"{Y} decides to eat cheese.")
