import threading, time
from tkinter import *

clicks = 0
testingClickSpeed = False

root = Tk()
root.title("Click Speed Test")

clickLabel = Label(text="Click to start")
clickLabel.grid(column=5, row=0)
clickCount = Label(text="You have clicked " + str(clicks) + " times!")
clickCount.grid(column=5, row=1)
timeRemaining = Label(text="Time left: Not started!")
timeRemaining.grid(column=5, row=2)

def start_test():
    global testingClickSpeed
    testingClickSpeed=True
    seconds=10+1
    for i in range(10+1):
        seconds-=1
        if seconds==1:
            timeRemaining["text"] = "Time left: 1 second"
        elif seconds==0:
            timeRemaining["text"] = "Time left: Test Finished!"
        else:
            timeRemaining["text"] = "Time left: " + str(seconds) + " seconds"
        if seconds!=0:
            time.sleep(1)

    finishedTest()

def finishedTest():
    global testingClickSpeed
    testingClickSpeed=False
    

def click(event):
    if testingClickSpeed==True:
        global clicks, clickCount, clickLabel
        clicks+=1
        clickCount["text"] = "You have clicked " + str(clicks) + " times!"
    else:
        reset()
        clickLabel["text"] = "Click as fast as you can!"
        threading.Thread(target=start_test).start()

def reset():
    global clicks, clickCount, testingClickSpeed
    clicks = 0
    clickCount["text"] = "You have clicked " + str(clicks) + " times!"
    clickLabel["text"] = "Click to start"
    testingClickSpeed = False


root.bind("<ButtonPress>", click)

root.mainloop()
