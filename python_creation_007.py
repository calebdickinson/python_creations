"""
Prints random strings and ints
"""
import random
_y = random.randint(1, 3)
if _y == 1:
    _x = random.randint(1, 3)
    if _x == 1:
        print("1 giraffe")
    if _x != 1:
        status = f"{_x} giraffes"
        print(status)
if _y == 2:
    _x = random.randint(1, 3)
    if _x == 1:
        print("1 tiger")
    if _x != 1:
        status = f"{_x} tigers"
        print(status)
if _y == 3:
    _x = random.randint(1, 3)
    if _x == 1:
        print("1 elephant")
    if _x != 1:
        status = f"{_x} elephants"
        print(status)
