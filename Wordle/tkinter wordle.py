from mttkinter import mtTkinter as tk
import random

root = tk.Tk()
root.title("Zacatron")

root.geometry("250x120")


class Window(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.entryFrame = tk.LabelFrame(master)
        self.entry = tk.Entry(self.entryFrame)
        self.entry.pack()

        self.guessesFrame = tk.LabelFrame(master)

    def start(self):
        pass # <------------------------------------------------------------------

    def getGuess(self):
        self.guess = self.entry.get()
        return self.guess

    def draw(self):
        self.entryFrame.pack(side=tk.BOTTOM)
        self.guessesFrame.pack(side=tk.TOP)

    def delete(self):
        self.entryFrame.forget()
        self.guessesFrame.forget()

    def reset(self):
        self.delete()
        self.draw()
        self.start()

    def addGuess(self, guess):
        self.newGuess = self.guessLabel(guess)
        self.newGuess.pack()

    def guessLabel(self, text):
        label = tk.Label(self.guessesFrame, text=text)
        return label

       

window = Window(root)


window.start()