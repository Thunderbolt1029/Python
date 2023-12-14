import keyboard, time, random

time.sleep(5)

while True:
    keyboard.send("a")
    time.sleep(random.randint(1,5))
    keyboard.send("d")
    time.sleep(random.randint(1,5))
