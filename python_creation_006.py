"""
Prints "x elephants" where x is a randint. If x == 1 prints "1 elephant".
"""

import random
_x = random.randint(1, 3)
if _x == 1:
    print("1 elephant")
if _x != 1:
    print(f"{_x} elephants")
