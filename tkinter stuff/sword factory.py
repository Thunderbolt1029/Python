from tkinter import LEFT
import mouse, time
from PIL import ImageGrab

upgradePos = [
    (246, 429),
    (242, 493),
    (245, 551),
    (244, 614),
    (248, 678),
    (243, 743)
]

while True:
    for pos in upgradePos:
    #    color = ImageGrab.grab().getpixel(pos)
    #    (r, g, b) = color

        (x, y) = pos
        
        mouse.move(x, y, duration=0.1)
        time.sleep(0.2)
        mouse.press(button=LEFT)
        time.sleep(0.3)
        mouse.release(button=LEFT)
    
    time.sleep(5)