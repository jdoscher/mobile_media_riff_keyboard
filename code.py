# For testing with an on screen keyboard try adding "sudo apt-get install matchbox-keyboard"  
# and rebooting via https://raspberrypi.stackexchange.com/questions/41150/virtual-keyboard-activation

#Key mapping using Chromium shortcuts from here: https://www.chromium.org/user-experience/keyboard-access
# CircuitPython code reference for keyboard emulation here: https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode
# Usage Examples: https://github.com/adafruit/Adafruit_CircuitPython_HID
# Digital IO: https://learn.adafruit.com/arduino-to-circuitpython/digital-in-out
# CircuitPython HID Keyboard and Mouse: https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-hid-keyboard-and-mouse
# Rotary encoder: https://learn.adafruit.com/rotary-encoder/circuitpython

# Parts:
# Raspberry Pi 3B+ (Pi 4 is too hot for this project): https://amzn.to/2LahBnC
# Adafruit Feather M4 Express: https://amzn.to/2ZEUB4c
# Official Raspberry Pi Touchscreen: https://amzn.to/2MPiZht
# Cherry MX Brown Keys: https://amzn.to/2NSaBxN
# Adafruit Rotary Encoder: https://amzn.to/2HCB5iD
# Hatchbox Grey PLA (Probably need a little more than 1 spool): https://amzn.to/2NHTD55
# 
import digitalio
import board
import time 
import rotaryio

#from adafruit_hid.keycode import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard

# For Feather M0 Express, Metro M0 Express, Metro M4 Express, and Circuit Playground Express
import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

m = Mouse()
kbd = Keyboard()

#red wire, (Alt-F4 button)
button1 = digitalio.DigitalInOut(board.D9)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP
button1_state = None

#grey wire, Twitter button
button2 = digitalio.DigitalInOut(board.D6)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP
button2_state = None

#blue wire, (Instagram button)
button3 = digitalio.DigitalInOut(board.D12)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP
button3_state = None

#yellow wire, (Reddit button)
button4 = digitalio.DigitalInOut(board.D10)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP
button4_state = None

#Encoder push switch, white wire (Refresh/F5 function)
button5 = digitalio.DigitalInOut(board.D4)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP
button5_state = None


encoder = rotaryio.IncrementalEncoder(board.D11, board.D5)
last_position = encoder.position

print("Waiting for button presses")

while True:
    # rotary reference for CP here: https://learn.adafruit.com/rotary-encoder/circuitpython
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            m.move(0, 0, 1)
        print(current_position)
    elif position_change < 0:
        for _ in range(-position_change):
            m.move(0, 0, -1)
        print(current_position)
    last_position = current_position
    # Refresh (F5)
    if button5.value and button5_state is None:
        button5_state = "pressed"
    if not button5.value and button5_state == "pressed":
        print("Refresh #5 button pressed.")
        kbd.send(Keycode.F5)
        button5_state = None
    
    #Twitter
    if not button2.value and button2_state is None:
        button2_state = "pressed"
    if button2.value and button2_state == "pressed":
        print("Twitter button #2 pressed.")
        # 63 is F6, focus on the toolbar
        #kbd.press(Keycode.F6)
        # Type out Twitter
        #kbd.press(Keycode.T)
        #time.sleep(.1)
        #kbd.press(Keycode.W)
        #time.sleep(.1)
        #kbd.press(Keycode.I)
        #time.sleep(.1)
        #kbd.press(Keycode.T)
        #time.sleep(.1)
        #kbd.press(Keycode.T)
        #time.sleep(.1)
        #kbd.press(Keycode.E)
        #time.sleep(.1)
        #kbd.press(Keycode.R)
        #kbd.press(Keycode.KEYPAD_PERIOD)
        #kbd.press(Keycode.C)
        #kbd.press(Keycode.O)
        #kbd.press(Keycode.M)
        #kbd.press(Keycode.FORWARD_SLASH)
        #kbd.press(Keycode.B)
        #kbd.press(Keycode.A)
        #kbd.press(Keycode.C)
        #kbd.press(Keycode.K)
        #kbd.press(Keycode.SEVEN)
        #kbd.press(Keycode.C)
        #kbd.press(Keycode.O)
        #kbd.release_all()
        button2_state = None
    # Instagram
    if not button3.value and button3_state is None:
        button3_state = "pressed"
    if button3.value and button3_state == "pressed":
        print("Instagram button #3 pressed.")
        # 63 is F6, focus on the toolbar
        #kbd.press(Keycode.F6)
        # Type out Instagram
        #kbd.press(Keycode.i)
        #kbd.press(Keycode.n)
        #kbd.press(Keycode.s)
        #kbd.press(Keycode.t)
        #kbd.press(Keycode.a)
        #kbd.press(Keycode.g)
        #kbd.press(Keycode.r)
        #kbd.press(Keycode.a)
        #kbd.press(Keycode.m)
        #kbd.press(Keycode.KEYPAD_PERIOD)
        #kbd.press(Keycode.c)
        #kbd.press(Keycode.o)
        #kbd.press(Keycode.m)
        #kbd.press(Keycode.FORWARD_SLASH)
        #kbd.press(Keycode.b)
        #kbd.press(Keycode.a)
        #kbd.press(Keycode.c)
        #kbd.press(Keycode.k)
        #kbd.press(Keycode.SEVEN)
        #kbd.press(Keycode.KEYPAD_PERIOD)
        #kbd.press(Keycode.c)
        #kbd.press(Keycode.o)
        button3_state = None

    #Reddit
    if not button4.value and button4_state is None:
        button4_state = "pressed"
    if button4.value and button4_state == "pressed":
        print("Reddit #4 Button pressed.")
        # 63 is F6, focus on the toolbar
        #kbd.press(Keycode.F6)
        # Type out Instagram
        #kbd.press(Keycode.r)
        #kbd.press(Keycode.e)
        #kbd.press(Keycode.d)
        #kbd.press(Keycode.d)
        #kbd.press(Keycode.i)
        #kbd.press(Keycode.t)
        #kbd.press(Keycode.KEYPAD_PERIOD)
        #kbd.press(Keycode.c)
        #kbd.press(Keycode.o)
        #kbd.press(Keycode.m)
        #kbd.press(Keycode.FORWARD_SLASH)
        #kbd.press(Keycode.r)
        #kbd.press(Keycode.FORWARD_SLASH)
        #kbd.press(Keycode.THREE)
        #kbd.press(Keycode.d)
        #kbd.press(Keycode.p)
        #kbd.press(Keycode.r)
        #kbd.press(Keycode.i)
        #kbd.press(Keycode.n)
        #kbd.press(Keycode.t)
        #kbd.press(Keycode.i)
        #kbd.press(Keycode.n)
        #kbd.press(Keycode.g)
        button4_state = None

    #Close (ALT-F4)
    if not button1.value and button1_state is None:
        button1_state = "pressed"
    if button1.value and button1_state == "pressed":
        print("Alt-F4 button pressed.")
        #kbd.press(Keycode.ALT, Keycode.F4)
        button1_state = None

# helpful demo from LadyAda here: https://www.youtube.com/watch?v=tzDGTYDR_M4
