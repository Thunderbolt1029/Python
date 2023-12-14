import turtle as tl

class turtle():
    def __init__(self):
        tl.speed(100000000000000000000000000000)
        tl.home()

    def start(self):
        tl.mainloop()

    def right(self, degrees):
        tl.right(degrees)

    def circle(self, scale_factor=1):
        for i in range(360):
            tl.forward(scale_factor)
            tl.right(1)

    def square(self, side_length=1):
        for i in range(4):
            tl.forward(side_length)
            tl.right(90)
    
