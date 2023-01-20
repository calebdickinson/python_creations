"""
Basic code for generating a randomly sampled string(x) from a list and
printing x instead of ["x"]
"""

from random import sample

Z = [
    "a",
    "b"
]
X = sample(Z, 1)
SEPARATOR = ", "
Y = (SEPARATOR.join(X))
print(f"{Y} c")
