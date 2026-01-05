import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13) # board.LED works?
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5) # change the time value
    led.value = False
    time.sleep(0.5) # change the time value
