import board
import digitalio

led = digitalio.DigitalInOut(board.D1)
led.direction = digitalio.Direction.OUTPUT

led.value = True   # turn on and off
