import time
import board
import adafruit_dotstar

dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

while True:
    dot[0] = (255, 0, 0)  # red
    time.sleep(0.5)
    dot[0] = (0, 0, 0)    # off
    time.sleep(0.5)
