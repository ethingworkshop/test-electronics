import board
import pwmio
import time

led = pwmio.PWMOut(board.D1)

while True:
    for brightness in range(0, 65535, 5000): # adjust brightness. value will be increasing by 5000
        led.duty_cycle = brightness
        time.sleep(0.05)
    for brightness in range(65535, 0, -5000): # value will be decreasing by 5000
        led.duty_cycle = brightness
        time.sleep(0.05)
