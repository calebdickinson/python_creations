"""
Code written for hackerrank first problem
"""

import random
n = random.randint(1, 100)
print(n)
if n % 2 != 0:
    print("Weird")
elif 1 < n < 6:
    print("Not Weird")
elif n < 21:
    print("Weird")
else:
    print("Not Weird")
