from tkinter import *

root = Tk()
root.title("Tk dropdown example")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()
