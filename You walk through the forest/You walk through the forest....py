#-------------------MODULE IMPORT, WINDOW DECLORATION AND VARIABLE DECLORATION-------------------

import time, random, tkinter
from tkinter import *


root = Tk()
root.geometry("250x150")
root.title("You walk through the forest...")

#-----------------------------------------FRAME CONTROL------------------------------------------

#--------------------CHOOSING YOUR CLASS--------------------

def chooseClass(): #Start screen - choosing class
    warriorConformationLabel.forget() #When this "frame" is switched to it hides all other frames
    warriorConformationFrame.forget()

    rogueConformationLabel.forget()
    rogueConformationFrame.forget()

    warlockConformationLabel.forget()
    warlockConformationFrame.forget()

    
    classChooseLabel.pack()

    classSelectWarriorButton.pack(side=LEFT)
    classSelectRogueButton.pack(side=LEFT)
    classSelectWarlockButton.pack(side=LEFT)
    
    classSelectFrame.pack()

def chooseWarriorConformation(): #Confirming the Warrior Class
    classSelectFrame.forget() #When this "frame" is switched to it hides all other frames
    classChooseLabel.forget()
    
    warriorConformationLabel.pack()
    warriorConformationButtonYes.pack(side=LEFT)
    warriorConformationButtonNo.pack(side=LEFT)
    warriorConformationFrame.pack()

def chooseRogueConformation(): #Confirming the Rogue Class
    classSelectFrame.forget() #When this "frame" is switched to it hides all other frames
    classChooseLabel.forget()

    rogueConformationLabel.pack()
    rogueConformationButtonYes.pack(side=LEFT)
    rogueConformationButtonNo.pack(side=LEFT)
    rogueConformationFrame.pack()
    
def chooseWarlockConformation(): #Confirming the Warlock Class
    classSelectFrame.forget() #When this "frame" is switched to it hides all other frames
    classChooseLabel.forget()
    
    warlockConformationLabel.pack()
    warlockConformationButtonYes.pack(side=LEFT)
    warlockConformationButtonNo.pack(side=LEFT)
    warlockConformationFrame.pack()

#-------------------FOREST LOADING SCREEN-------------------

def enteringTheForest(): #Usless loading screen to give it a bit of depth
    warriorConformationLabel.forget() #When this "frame" is switched to it hides all other frames
    warriorConformationFrame.forget()

    rogueConformationLabel.forget()
    rogueConformationFrame.forget()

    warlockConformationLabel.forget()
    warlockConformationFrame.forget()
    
    loadingTheForestLabel.pack()
    loadingTheForestFrame.pack()
    
    root.after(1500, enteringElipsisEffect1)

def enteringElipsisEffect1(): #Adds 1st fullstop
    enteringElipsisEffectLabel1.pack(side=LEFT)
    root.after(500, enteringElipsisEffect2)

def enteringElipsisEffect2(): #Adds 2nd fullstop
    enteringElipsisEffectLabel2.pack(side=LEFT)
    root.after(500, enteringElipsisEffect3)

def enteringElipsisEffect3(): #Adds 3rd fullstop
    enteringElipsisEffectLabel3.pack(side=LEFT)
    root.after(750, theWindingPath)

#---------------------THE WINDING PATH----------------------

def theWindingPath():
    loadingTheForestLabel.forget()
    loadingTheForestFrame.forget()

    windingPathChallenge1Label.pack()

#------------------------------LABEL, BUTTON AND FRAME DECLORATION-------------------------------

classSelectFrame = Frame(root, width=250, height=150)

warriorConformationFrame = Frame(root,width=250, height=150)
rogueConformationFrame = Frame(root,width=250, height=150)
warlockConformationFrame = Frame(root,width=250, height=150)

loadingTheForestFrame = Frame(root, width=250, height=150)


classChooseLabel = Label(root, text="\nChoose your class\n")

warriorConformationLabel = Label(root, text="\nAre You Sure You Want to Enter The Forest\nas a Warrior?\n")
rogueConformationLabel = Label(root, text="\nAre You Sure You Want to Enter The Forest\nas a Rogue?\n")
warlockConformationLabel = Label(root, text="\nAre You Sure You Want to Enter The Forest\nas a Warlock?\n")

loadingTheForestLabel = Label(root, text="\nNow Entering The Forest\n")

windingPathChallenge1Label = Label(root, text="\nYou Walk Down a Winding Path...\n")


enteringElipsisEffectLabel1 = Label(loadingTheForestFrame, text=".")
enteringElipsisEffectLabel2 = Label(loadingTheForestFrame, text=".")
enteringElipsisEffectLabel3 = Label(loadingTheForestFrame, text=".")


classSelectWarriorButton = Button(classSelectFrame, text="Warrior", command=chooseWarriorConformation)
classSelectRogueButton = Button(classSelectFrame, text="Rogue", command=chooseRogueConformation)
classSelectWarlockButton = Button(classSelectFrame, text="Warlock", command=chooseWarlockConformation)

warriorConformationButtonYes = Button(warriorConformationFrame, text="Yes", command=enteringTheForest)
warriorConformationButtonNo = Button(warriorConformationFrame, text="No", command=chooseClass)
rogueConformationButtonYes = Button(rogueConformationFrame, text="Yes", command=enteringTheForest)
rogueConformationButtonNo = Button(rogueConformationFrame, text="No", command=chooseClass)
warlockConformationButtonYes = Button(warlockConformationFrame, text="Yes", command=enteringTheForest)
warlockConformationButtonNo = Button(warlockConformationFrame, text="No", command=chooseClass)

#-------------------------------------------GAME START-------------------------------------------

chooseClass()

root.mainloop()
