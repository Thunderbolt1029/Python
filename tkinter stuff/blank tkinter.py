from tkinter import *
import random

root = Tk()
root.title("Zacatron")

root.geometry("250x120")

label = Label(text="Destroy me")
label.grid(column=0, row=0)

def key_pressed(event):
    print(event)
    label.grid_remove()

root.bind("<ButtonPress>", key_pressed)

root.mainloop()
