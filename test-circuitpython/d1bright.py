import board
import pwmio

led = pwmio.PWMOut(board.D1)

# change the number to adjust the brightness
led.duty_cycle = 65535  # max

# e.g. medium: 30000, dark: 5000
