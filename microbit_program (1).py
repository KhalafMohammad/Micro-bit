# Add your Python code here. E.g.
from microbit import *
import music

while True:
    journey = ["G2:4", "A2:4", "A#:8", "F2:4", "G2:4", "A2:8", "F2:4", "G2:4", "A2:8",
    "G2:8","G2:4", "A2:4", "A#:8", "F2:4", "G2:4", "A2:8", "F2:4", "G2:4", "A2:8",
    "D#:4", "A#:8", "F2:4", "A2:8", "G2:4", "A2:4", "A#:8", "A2:4", "G2:4", "F2:4",
    "G2:4", "A2:8", "F2:4", "G2:4", "A2:8", "G2:4", "F2:4", "G2:8", "G2:4", "A2:4",
    "A#:8", "C3:4", "D3:4", "D#:4", "G2:4", "A2:8", "F2:4", "G2:4", "A2:8", "A#:4",
    "C3:4", "D#:4", "A2:4", "C3:4", "A#:4", "A2:4", "A#:4"]
    if button_a.is_pressed():
        music.play(journey)
    elif button_b.is_pressed():
        display.scroll("Journey from Destiny 2")