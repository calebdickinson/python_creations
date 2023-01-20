"""
Does the same thing as python creation no 29 but uses winsound instead of
pygame.mixer because async is possible in winsound (also playsound) which
makes it possible to open a window while playing music.

Edit: doesn't work right because time.sleep() doesn't work with winsound
for some reason so there is no way to stop an infinite loop
"""
import winsound
winsound.PlaySound(
    "C:/Users/CALEB DICKINSON/Documents/Scores/"
    "Choose your own adventure music 1.wav",
    winsound.SND_FILENAME
)
