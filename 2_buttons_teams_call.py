"""
Author: Elouan Cottenot
Project : Dual button for teams
URl : https://www.elouan.fr
Version : 0.0.1
Description : Box with big button to answer or hang up on call team. Enable to answer without having to search for shortcut or mouse while putting headphone.
System : Circuit python 7.3.3
Board : Raspberry pi pico 2020
"""

import usb_hid
import board
import digitalio
import time

""" 
Library to add in pico root folder
URI to download: https://github.com/adafruit/Adafruit_CircuitPython_HID
Copy adafruit_hid folder
"""
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

"""
Microswitch with led attached, green for the answering
Button and led have separated power connection
"""
# Answer button
greenButton = digitalio.DigitalInOut(board.GP16)
greenButton.switch_to_input(pull=digitalio.Pull.UP)

#Answer led 
greenLed = digitalio.DigitalInOut(board.GP17)
greenLed.direction = digitalio.Direction.OUTPUT


"""
Microswitch with led attached, red form hanging up
Button and led have separated power connection
"""
# Hanging up button
redButton = digitalio.DigitalInOut(board.GP15)
redButton.switch_to_input(pull=digitalio.Pull.UP)

#Answer led 
redLed = digitalio.DigitalInOut(board.GP20)
redLed.direction = digitalio.Direction.OUTPUT

# Devices definition for keyboard
keyboard = Keyboard(usb_hid.devices)


while True:
    if(greenButton.value) :
        # Shut off the led for visual confirmation
        greenLed.value = False
    else :
        # Light led for visual confirmation
        greenLed.value = True
        # Shortcut Teams : Answer an audio call Ctrl + Maj + S
        keyboard.send(Keycode.CONTROL,Keycode.MAJ, Keycode.S)
        time.sleep(0.50)
        keyboard.release_all()
    
    if(redButton.value) :
        # Shut off the led for visual confirmation
        redLed.value = False
    else :
        # Light led for visual confirmation
        redLed.value = True
        # Shortcut Teams : Hang up an audi call Ctrl+Maj+H
        keyboard.send(Keycode.CONTROL,Keycode.S)
        time.sleep(0.50)
        keyboard.release_all()


