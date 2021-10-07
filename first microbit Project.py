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
        sleep(500)
        
        display.show(Image("0000:"
             "99099:"
             "99099:"
             "90009:"
             "99999:"))
        sleep(500)
#Hold B Button for KAT animation

display.clear()