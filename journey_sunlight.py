from microbit import *
import music
import speech

journey = ["G2:4", "A2:4", "A#:8", "F2:4", "G2:4", "A2:8", "F2:4", "G2:4", "A2:8",
    "G2:8","G2:4", "A2:4", "A#:8", "F2:4", "G2:4", "A2:8", "F2:4", "G2:4", "A2:8",
    "D#:4", "A#:8", "F2:4", "A2:8", "G2:4", "A2:4", "A#:8", "A2:4", "G2:4", "F2:4",
    "G2:4", "A2:8", "F2:4", "G2:4", "A2:8", "G2:4", "F2:4", "G2:8", "G2:4", "A2:4",
    "A#:8", "C3:4", "D3:4", "D#:4", "G2:4", "A2:8", "F2:4", "G2:4", "A2:8", "A#:4",
    "C3:4", "D#:4", "A2:4", "C3:4", "A#:4", "A2:4", "A#:4"]

while True:
    
    if display.read_light_level() > 100: ##licht met je telefoon dan spelt het JOURNEY en image van de zon.
        display.show(Image(
        "90909:"
        "09990:"
        "99999:"
        "09990:"
        "90909"))
        sleep(500)
        music.play(journey)
        if button_a.is_pressed():
            ## press en hold b (zeg bye bye en break)
            music.stop()
            speech.say("Bye Bye")
            break
        
    elif button_a.is_pressed(): ## press a om en animatie van de zon de verschijnen.
        while True:
            display.show(Image(
            "00000:"
            "00900:"
            "09990:"
            "00900:"
            "00000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "09990:"
                "09990:"
                "09990:"
                "00000"))
            sleep(500)
            display.show(Image(
            "90909:"
            "09990:"
            "99999:"
            "09990:"
            "90909"))
            sleep(500)
            if button_b.is_pressed(): ## press en hold b (zeg bye bye en break de loop)
                speech.say("Bye Bye")
                break
          
        
    else:
        display.clear()