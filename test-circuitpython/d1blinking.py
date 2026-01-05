import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D1)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1) # change the time value
    led.value = False
    time.sleep(1) # change the time value
