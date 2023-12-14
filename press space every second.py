import keyboard
from time import sleep

while True:
    keyboard.press("Space")
    sleep(0.5)
    keyboard.release("Space")
    sleep(1)
