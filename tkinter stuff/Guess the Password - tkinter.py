from tkinter import *
import random

root = Tk()
root.title("Guess the Password")

def password_length():
    password_length_label = Label(root, text="How long should the password be?").grid(row=1, column=1, padx=5, pady=5)
    password_length_entry = Entry(root, width=35).grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    password_length_enterButton = Button(root, text="Enter").grid(row=0, column=2, padx=5, pady=5, command=Lambda(password_length_enter()))

password_length()

root.mainloop()
