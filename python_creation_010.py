"""
Writes a very short story by randomly selecting from list(x)
x = 1&6(nouns), 2(adverbs), 3&4(verbs), 5(adjectives) 6(endings of story)
"""

from random import sample

list1 = [
    "panda ",
    "weird alien ",
    "super evil monster ",
    "dragon ",
    "slithy tove ",
    "borogove ",
    "jubjub bird ",
    "tumtum tree ",
    "jabberwock ",
    "bandersnatch "
]
list2 = [
    "happily ",
    "sadly ",
    "angerly ",
    "enthusiastically ",
    "instinctively ",
    "gladly ",
    "cheerfully ",
    "immunoelectrophoretically ",
    "uffishly ",
    "whifflingly ",
    "",
    "",
    "",
    ""
]
list3 = [
    "gimbled ",
    "sought ",
    "journeyed ",
    "traveled ",
    "navigated ",
    "ambulated "
]
list4 = [
    "behold ",
    "arrive at ",
    "consult ",
    "see ",
    "discern ",
    "survey ",
    "observe "
]
list5 = [
    " strange ",
    " blue ",
    " green ",
    " purple ",
    " bizarre ",
    " peculiar ",
    "n uncommon ",
    "n antidisestablishmentarian ",
    " floccinaucinihilipilificatave ",
    " turgiversative ",
    " brobdingnagian ",
    "n incomprehensible ",
    "n eellogofusciouhipoppokunurious "
]
list6 = [
    "mountain",
    "ocean",
    "rock",
    "spaceship",
    "forest",
    "microscope",
    "telescope",
    "helicopter",
    "snowflake"
]
list7 = [
    "were lixivated.",
    "decided to live on Mars.",
    "were eaten by the Jabberwock",
    "went galumphing back.",
    "moved to the north pole and became better known as Santa Claus.",
    "transformed into a christmas tree.",
    "died."
]
WORD_1 = sample(list1, 1)
SEPARATOR = ", "
Z = (SEPARATOR.join(WORD_1))

WORD_2 = sample(list2, 1)
SEPARATOR = ", "
Y = (SEPARATOR.join(WORD_2))

WORD_3 = sample(list3, 1)
SEPARATOR = ", "
X = (SEPARATOR.join(WORD_3))

WORD_4 = sample(list4, 1)
SEPARATOR = ", "
W = (SEPARATOR.join(WORD_4))

WORD_5 = sample(list5, 1)
SEPARATOR = ", "
V = (SEPARATOR.join(WORD_5))

WORD_6 = sample(list6, 1)
SEPARATOR = ", "
U = (SEPARATOR.join(WORD_6))

WORD_7 = sample(list7, 1)
SEPARATOR = ", "
T = (SEPARATOR.join(WORD_7))

WORD_8 = sample(list2, 1)
SEPARATOR = ", "
S = (SEPARATOR.join(WORD_8))

print(f"Once upon a time, a {Z}{Y}{X}in order to {W}a{V}{U}.")
print(
    f"The {Z}moved into the {U} and lived there {S}ever after, until they {T}"
)
print("The End.")
