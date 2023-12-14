import keyboard, time

time.sleep(5)

while True:
    keyboard.press("a")
    time.sleep(0.5)
    keyboard.release("a")
    
    time.sleep(0.5)

    keyboard.press("d")
    time.sleep(0.5)
    keyboard.release("d")

    time.sleep(10)