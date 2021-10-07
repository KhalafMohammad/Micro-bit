
from microbit import *
display.scroll("Hello, you!")

while True:
    if button_a.is_pressed():
        display.scroll("Mohammad, Khalaf!")
    elif button_b.is_pressed():
        display.show(Image("09090:"
             "90909:"
             "99099:"
             "90009:"
             "99999"))
    

display.clear()