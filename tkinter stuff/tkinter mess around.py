#"""
import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.title("Try code")

entry = tkinter.Entry(root)
entry.pack()

def on_button():
    if entry.get().strip().lower() == ("screen"):
        slabel = tkinter.Label(root, text="Screen was entered")
        slabel.pack()
    else:
       tlabel = tkinter.Label(root, text="yup")
       tlabel.pack()

button = tkinter.Button(root, text="Enter", command=on_button)
button.pack()

root.mainloop()
#"""
"""
from tkinter import *
m=Tk()
m.title("NUMBER GUESSING GAME")
lable=Label(m,text="CodeSpeedy")
lable.pack()
frame=Frame(m,width=300,height=300)
button1=Button(frame,text="enter")
button2=Button(frame,text="number 1")
button3=Button(frame,text="number 2")
button4=Button(frame,text="number 3")
button4.pack(side=LEFT)
button3.pack(side=LEFT)
button2.pack(side=LEFT)
button1.pack(side=LEFT)
frame.pack()
bottomframe=Frame(m,width=300,height=300)
lable2=Label(bottomframe,text="JITENDRA KUMAR")
button5=Button(bottomframe,text="Exit")
button5.pack(side=RIGHT)
bottomframe.pack(side=BOTTOM)
mainloop()
"""
