import time, mouse, sys, threading

while True:
    mouse.move(3100, 200)
    mouse.click(button="left")
    time.sleep(0.1)

    mouse.move(3100, 250)
    mouse.click(button="left")
    time.sleep(0.1)

    mouse.move(3100, 350)
    mouse.click(button="left")
    time.sleep(0.1)
    
    for i in range(10):
        if mouse.is_pressed(button='right'):
            sys.exit()
        time.sleep(0.1)
