"""
Generates paragraphs made up of 600 concatenated strings
Each of the 600 strings has the below probability of being:
1/70 for B, J, K, Q, V, W, X, Z,
     for _FROM_, _A_, _IS_, _THAT_, _FOR_, _THIS_, _NOT_, _WILL_, _BUT_, _IN_,
     for _THEY_, _THERE_, _WOULD_, _WHO_, _SO_, _NO_,
1/45 for A, C, D, F, G, H, L, M, N, O, P, R, T, U, Y,
     for _THE_, _OF_, _AND_
3/70 for S,
2/45 for E or I
"""

import random

x = random.randint(1, 70)

Y = ""
Z = ""
for _ in range(600):
    Y = random.randint(1, 70)
    if Y == 1:
        Z = Z + "A"
    if Y == 2:
        Z = Z + "B"
    if Y == 3:
        Z = Z + "C"
    if Y == 4:
        Z = Z + "D"
    if Y == 5:
        Z = Z + "E"
    if Y == 6:
        Z = Z + "F"
    if Y == 7:
        Z = Z + "G"
    if Y == 8:
        Z = Z + "H"
    if Y == 9:
        Z = Z + "I"
    if Y == 10:
        Z = Z + "J"
    if Y == 11:
        Z = Z + "K"
    if Y == 12:
        Z = Z + "L"
    if Y == 13:
        Z = Z + "M"
    if Y == 14:
        Z = Z + "N"
    if Y == 15:
        Z = Z + "O"
    if Y == 16:
        Z = Z + "P"
    if Y == 17:
        Z = Z + "Q"
    if Y == 18:
        Z = Z + "R"
    if Y == 19:
        Z = Z + "S"
    if Y == 20:
        Z = Z + "T"
    if Y == 21:
        Z = Z + "U"
    if Y == 22:
        Z = Z + "V"
    if Y == 23:
        Z = Z + "W"
    if Y == 24:
        Z = Z + "X"
    if Y == 25:
        Z = Z + "Y"
    if Y == 26:
        Z = Z + "Z"
    if Y == 27:
        Z = Z + "A"
    if Y == 28:
        Z = Z + "E"
    if Y == 29:
        Z = Z + "E"
    if Y == 30:
        Z = Z + "I"
    if Y == 31:
        Z = Z + "I"
    if Y == 32:
        Z = Z + "O"
    if Y == 33:
        Z = Z + "U"
    if Y == 34:
        Z = Z + "Y"
    if Y == 35:
        Z = Z + "T"
    if Y == 36:
        Z = Z + " THE "
    if Y == 37:
        Z = Z + " THE "
    if Y == 38:
        Z = Z + " FROM "
    if Y == 39:
        Z = Z + " OF "
    if Y == 40:
        Z = Z + " OF "
    if Y == 41:
        Z = Z + " AND "
    if Y == 42:
        Z = Z + " AND "
    if Y == 43:
        Z = Z + " A "
    if Y == 44:
        Z = Z + " IS "
    if Y == 45:
        Z = Z + " THAT "
    if Y == 46:
        Z = Z + " FOR "
    if Y == 47:
        Z = Z + " THIS "
    if Y == 48:
        Z = Z + " NOT "
    if Y == 49:
        Z = Z + " WILL "
    if Y == 50:
        Z = Z + " BUT "
    if Y == 51:
        Z = Z + " IN "
    if Y == 52:
        Z = Z + " THEY "
    if Y == 53:
        Z = Z + "N"
    if Y == 54:
        Z = Z + "S"
    if Y == 55:
        Z = Z + "R"
    if Y == 56:
        Z = Z + "H"
    if Y == 57:
        Z = Z + "L"
    if Y == 58:
        Z = Z + "D"
    if Y == 59:
        Z = Z + "C"
    if Y == 60:
        Z = Z + "M"
    if Y == 61:
        Z = Z + "F"
    if Y == 62:
        Z = Z + "P"
    if Y == 63:
        Z = Z + "G"
    if Y == 64:
        Z = Z + "I"
    if Y == 65:
        Z = Z + "E"
    if Y == 66:
        Z = Z + " THERE "
    if Y == 67:
        Z = Z + " WOULD "
    if Y == 68:
        Z = Z + " WHO "
    if Y == 69:
        Z = Z + " SO "
    if Y == 70:
        Z = Z + " NO "

print(Z)
