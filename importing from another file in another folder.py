import time
import Import.test as test

tl = test.turtle()

for i in range(1000):
    tl.square(i)
    tl.right(17)

tl.start()
