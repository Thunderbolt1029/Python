from mttkinter import mtTkinter as tk
import time

root = tk.Tk()
root.title("Ultimate Tic Tac Toe")
root.resizable(0,0)
root.configure(bg="black")

turn = "Cross"

topLeftFull = False
topFull = False
topRightFull = False
leftFull = False
middleFull = False
rightFull = False
bottomLeftFull = False
bottomFull = False
bottomRightFull = False

class outerBoard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        global outerFrame
        outerFrame = tk.LabelFrame(master, relief="flat", bg="black")

        
        self.Outer_Horizontal_1 = tk.Label(outerFrame, text="---------------------", font=("Times", 20, "bold"), bg="black", fg="white")
        self.Outer_Horizontal_2 = tk.Label(outerFrame, text="---------------------", font=("Times", 20, "bold"), bg="black", fg="white")
        self.Outer_Horizontal_3 = tk.Label(outerFrame, text="---------------------", font=("Times", 20, "bold"), bg="black", fg="white")
        self.Outer_Horizontal_4 = tk.Label(outerFrame, text="---------------------", font=("Times", 20, "bold"), bg="black", fg="white")
        self.Outer_Horizontal_5 = tk.Label(outerFrame, text="---------------------", font=("Times", 20, "bold"), bg="black", fg="white")
        self.Outer_Horizontal_6 = tk.Label(outerFrame, text="---------------------", font=("Times", 20, "bold"), bg="black", fg="white")

        self.Outer_Vertical_1 = tk.Label(outerFrame, text="|\n|\n|\n|\n|\n|\n|\n|", font=("Times", 17, "bold"), bg="black", fg="white")
        self.Outer_Vertical_2 = tk.Label(outerFrame, text="|\n|\n|\n|\n|\n|\n|\n|", font=("Times", 17, "bold"), bg="black", fg="white")
        self.Outer_Vertical_3 = tk.Label(outerFrame, text="|\n|\n|\n|\n|\n|\n|\n|", font=("Times", 17, "bold"), bg="black", fg="white")
        self.Outer_Vertical_4 = tk.Label(outerFrame, text="|\n|\n|\n|\n|\n|\n|\n|", font=("Times", 17, "bold"), bg="black", fg="white")
        self.Outer_Vertical_5 = tk.Label(outerFrame, text="|\n|\n|\n|\n|\n|\n|\n|", font=("Times", 17, "bold"), bg="black", fg="white")
        self.Outer_Vertical_6 = tk.Label(outerFrame, text="|\n|\n|\n|\n|\n|\n|\n|", font=("Times", 17, "bold"), bg="black", fg="white")

        self.Outer_Cross_1 = tk.Label(outerFrame, text="+", font=("Times", 15, "bold"), bg="black", fg="white")
        self.Outer_Cross_2 = tk.Label(outerFrame, text="+", font=("Times", 15, "bold"), bg="black", fg="white")
        self.Outer_Cross_3 = tk.Label(outerFrame, text="+", font=("Times", 15, "bold"), bg="black", fg="white")
        self.Outer_Cross_4 = tk.Label(outerFrame, text="+", font=("Times", 15, "bold"), bg="black", fg="white")



        self.Outer_Horizontal_1.grid(column=0, row=1, columnspan=2, sticky="W")
        self.Outer_Horizontal_2.grid(column=2, row=1, columnspan=2, sticky="W")
        self.Outer_Horizontal_3.grid(column=4, row=1, columnspan=2, sticky="W")
        self.Outer_Horizontal_4.grid(column=0, row=3, columnspan=2, sticky="W")
        self.Outer_Horizontal_5.grid(column=2, row=3, columnspan=2, sticky="W")
        self.Outer_Horizontal_6.grid(column=4, row=3, columnspan=2, sticky="W")

        self.Outer_Vertical_1.grid(column=1, row=0, rowspan=2, sticky="N")
        self.Outer_Vertical_2.grid(column=1, row=2, rowspan=2, sticky="N")
        self.Outer_Vertical_3.grid(column=1, row=4, rowspan=2, sticky="N")
        self.Outer_Vertical_4.grid(column=3, row=0, rowspan=2, sticky="N")
        self.Outer_Vertical_5.grid(column=3, row=2, rowspan=2, sticky="N")
        self.Outer_Vertical_6.grid(column=3, row=4, rowspan=2, sticky="N")

        self.Outer_Cross_1.grid(column=1, row=1, sticky="SW")
        self.Outer_Cross_2.grid(column=3, row=1, sticky="SW")
        self.Outer_Cross_3.grid(column=1, row=3, sticky="SW")
        self.Outer_Cross_4.grid(column=3, row=3, sticky="SW")


    def draw(self):
        global outerFrame
        outerFrame.grid(column=0,row=0, rowspan=4, padx=10, pady=5)
        

class smallBoard(tk.Frame):
    def __init__(self, master, column, row):
        super().__init__(master)
        self.Won = False
        self.Selected = False
        self.TopLeftFilled = "Empty"
        self.TopFilled = "Empty"
        self.TopRightFilled = "Empty"
        self.LeftFilled = "Empty"
        self.MiddleFilled = "Empty"
        self.RightFilled = "Empty"
        self.BottomLeftFilled = "Empty"
        self.BottomFilled = "Empty"
        self.BottomRightFilled = "Empty"
        
        (self.column, self.row) = (column, row)


        self.gridContainer = tk.LabelFrame(master, relief="flat", bg="black")

        self.OutlineVertical_1 = tk.Label(self.gridContainer, text="|\n|", bg="black", fg="white")
        self.OutlineVertical_2 = tk.Label(self.gridContainer, text="|\n|", bg="black", fg="white")
        self.OutlineVertical_3 = tk.Label(self.gridContainer, text="|\n|", bg="black", fg="white")
        self.OutlineVertical_4 = tk.Label(self.gridContainer, text="|\n|", bg="black", fg="white")
        self.OutlineVertical_5 = tk.Label(self.gridContainer, text="|\n|", bg="black", fg="white")
        self.OutlineVertical_6 = tk.Label(self.gridContainer, text="|\n|", bg="black", fg="white")
        
        self.OutlineHorizontal_1 = tk.Label(self.gridContainer, text="-------", bg="black", fg="white")
        self.OutlineHorizontal_2 = tk.Label(self.gridContainer, text="-------", bg="black", fg="white")
        self.OutlineHorizontal_3 = tk.Label(self.gridContainer, text="-------", bg="black", fg="white")
        self.OutlineHorizontal_4 = tk.Label(self.gridContainer, text="-------", bg="black", fg="white")
        self.OutlineHorizontal_5 = tk.Label(self.gridContainer, text="-------", bg="black", fg="white")
        self.OutlineHorizontal_6 = tk.Label(self.gridContainer, text="-------", bg="black", fg="white")
        
        self.OutlineCross_1 = tk.Label(self.gridContainer, text="+", bg="black", fg="white")
        self.OutlineCross_2 = tk.Label(self.gridContainer, text="+", bg="black", fg="white")
        self.OutlineCross_3 = tk.Label(self.gridContainer, text="+", bg="black", fg="white")
        self.OutlineCross_4 = tk.Label(self.gridContainer, text="+", bg="black", fg="white")


        self.OutlineVertical_1.grid(column=2, row=1)
        self.OutlineVertical_2.grid(column=4, row=1)
        self.OutlineVertical_3.grid(column=2, row=3)
        self.OutlineVertical_4.grid(column=4, row=3)
        self.OutlineVertical_5.grid(column=2, row=5)
        self.OutlineVertical_6.grid(column=4, row=5)

        self.OutlineHorizontal_1.grid(column=1, row=2)
        self.OutlineHorizontal_2.grid(column=3, row=2)
        self.OutlineHorizontal_3.grid(column=5, row=2)
        self.OutlineHorizontal_4.grid(column=1, row=4)
        self.OutlineHorizontal_5.grid(column=3, row=4)
        self.OutlineHorizontal_6.grid(column=5, row=4)

        self.OutlineCross_1.grid(column=2, row=2)
        self.OutlineCross_2.grid(column=4, row=2)
        self.OutlineCross_3.grid(column=2, row=4)
        self.OutlineCross_4.grid(column=4, row=4)
        


        self.SelectorHorizontal_1 = tk.Label(self.gridContainer, text="-----------------------------", bg="black", fg="black")
        self.SelectorHorizontal_2 = tk.Label(self.gridContainer, text="-----------------------------", bg="black", fg="black")
        self.SelectorVertical_1 = tk.Label(self.gridContainer, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|", bg="black", fg="black")
        self.SelectorVertical_2 = tk.Label(self.gridContainer, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|", bg="black", fg="black")
        self.SelectorCorner_1 = tk.Label(self.gridContainer, text="/", bg="black", fg="black")
        self.SelectorCorner_2 = tk.Label(self.gridContainer, text="\\", bg="black", fg="black")
        self.SelectorCorner_3 = tk.Label(self.gridContainer, text="\\", bg="black", fg="black")
        self.SelectorCorner_4 = tk.Label(self.gridContainer, text="/", bg="black", fg="black")

        self.SelectorHorizontal_1.grid(column=1, row=0, columnspan=5, sticky="NW")
        self.SelectorHorizontal_2.grid(column=1, row=6, columnspan=5, sticky="SW")
        self.SelectorVertical_1.grid(column=0, row=1, rowspan=5, sticky="NW")
        self.SelectorVertical_2.grid(column=6, row=1, rowspan=5, sticky="NE")
        self.SelectorCorner_1.grid(column=0, row=0)
        self.SelectorCorner_2.grid(column=6, row=0)
        self.SelectorCorner_3.grid(column=0, row=6)
        self.SelectorCorner_4.grid(column=6, row=6)
        
        

        self.Cross_TopLeft = tk.Label(self.gridContainer, text="X", bg="black", fg="white")
        self.Cross_Top = tk.Label(self.gridContainer, text="X", bg="black", fg="white")
        self.Cross_TopRight = tk.Label(self.gridContainer, text="X", bg="black", fg="white")
        self.Cross_Left = tk.Label(self.gridContainer, text="X", bg="black", fg="white")
        self.Cross_Middle = tk.Label(self.gridContainer, text="X", bg="black", fg="white")
        self.Cross_Right = tk.Label(self.gridContainer, text="X", bg="black", fg="white")
        self.Cross_BottomLeft = tk.Label(self.gridContainer, text="X", bg="black", fg="white")
        self.Cross_Bottom = tk.Label(self.gridContainer, text="X", bg="black", fg="white")
        self.Cross_BottomRight = tk.Label(self.gridContainer, text="X", bg="black", fg="white")
        self.Cross_Place = tk.Label(self.gridContainer, text="X", bg="black", fg="white")

        self.Nought_TopLeft = tk.Label(self.gridContainer, text="O", bg="black", fg="white")
        self.Nought_Top = tk.Label(self.gridContainer, text="O", bg="black", fg="white")
        self.Nought_TopRight = tk.Label(self.gridContainer, text="O", bg="black", fg="white")
        self.Nought_Left = tk.Label(self.gridContainer, text="O", bg="black", fg="white")
        self.Nought_Middle = tk.Label(self.gridContainer, text="O", bg="black", fg="white")
        self.Nought_Right = tk.Label(self.gridContainer, text="O", bg="black", fg="white")
        self.Nought_BottomLeft = tk.Label(self.gridContainer, text="O", bg="black", fg="white")
        self.Nought_Bottom = tk.Label(self.gridContainer, text="O", bg="black", fg="white")
        self.Nought_BottomRight = tk.Label(self.gridContainer, text="O", bg="black", fg="white")
        self.Nought_Place = tk.Label(self.gridContainer, text="O", bg="black", fg="white")

        

        self.bigCross = tk.Label(master, text="X", bg="black", fg="white", font=("Calibri", 127))
        self.bigNought = tk.Label(master, text="O", bg="black", fg="white", font=("Calibri", 127))

    def drawFrame(self):
        self.gridContainer.grid(column=self.column, row=self.row, padx=10, pady=5)

    def dropFrame(self):
        self.gridContainer.grid_remove()

    def win(self, piece=None, drop=False):
        if drop:
            self.bigCross.grid_remove()
            self.bigNought.grid_remove()
            self.Won = False
        else:
            if piece=="Cross":
                self.bigCross.grid(column=self.column, row=self.row)
            elif piece=="Nought":
                self.bigNought.grid(column=self.column, row=self.row)
            self.Won = True

    def select(self):
        self.Selected = True
        
        self.SelectorHorizontal_1["fg"] = "white"
        self.SelectorHorizontal_2["fg"] = "white"
        self.SelectorVertical_1["fg"] = "white"
        self.SelectorVertical_2["fg"] = "white"
        self.SelectorCorner_1["fg"] = "white"
        self.SelectorCorner_2["fg"] = "white"
        self.SelectorCorner_3["fg"] = "white"
        self.SelectorCorner_4["fg"] = "white"

    def deselect(self):
        self.Selected = False
        
        self.SelectorHorizontal_1["fg"] = "black"
        self.SelectorHorizontal_2["fg"] = "black"
        self.SelectorVertical_1["fg"] = "black"
        self.SelectorVertical_2["fg"] = "black"
        self.SelectorCorner_1["fg"] = "black"
        self.SelectorCorner_2["fg"] = "black"
        self.SelectorCorner_3["fg"] = "black"
        self.SelectorCorner_4["fg"] = "black"

    def Cross(self, place=None, drop=False):
        if drop==False:
            if place=="TopLeft":
                self.Cross_TopLeft.grid(column=1, row=1)
                self.TopLeftFilled = "Cross"
            elif place=="Top":
                self.Cross_Top.grid(column=3, row=1)
                self.TopFilled = "Cross"
            elif place=="TopRight":
                self.Cross_TopRight.grid(column=5, row=1)
                self.TopRightFilled = "Cross"
            elif place=="Left":
                self.Cross_Left.grid(column=1, row=3)
                self.LeftFilled = "Cross"
            elif place=="Middle":
                self.Cross_Middle.grid(column=3, row=3)
                self.MiddleFilled = "Cross"
            elif place=="Right":
                self.Cross_Right.grid(column=5, row=3)
                self.RightFilled = "Cross"
            elif place=="BottomLeft":
                self.Cross_BottomLeft.grid(column=1, row=5)
                self.BottomLeftFilled = "Cross"
            elif place=="Bottom":
                self.Cross_Bottom.grid(column=3, row=5)
                self.BottomFilled = "Cross"
            elif place=="BottomRight":
                self.Cross_BottomRight.grid(column=5, row=5)
                self.BottomRightFilled = "Cross"
            else:
                raise Exception("You need to specify where to place the piece")

        else:
            if place=="All":
                self.Cross_TopLeft.grid_remove()
                self.Cross_Top.grid_remove()
                self.Cross_TopRight.grid_remove()
                self.Cross_Left.grid_remove()
                self.Cross_Middle.grid_remove()
                self.Cross_Right.grid_remove()
                self.Cross_BottomLeft.grid_remove()
                self.Cross_Bottom.grid_remove()
                self.Cross_BottomRight.grid_remove()
                self.Cross_Place.grid_remove()

                self.TopLeftFilled = "Empty"
                self.TopFilled = "Empty"
                self.TopRightFilled = "Empty"
                self.LeftFilled = "Empty"
                self.MiddleFilled = "Empty"
                self.RightFilled = "Empty"
                self.BottomLeftFilled = "Empty"
                self.BottomFilled = "Empty"
                self.BottomRightFilled = "Empty"
                
            elif place=="TopLeft":
                self.Cross_TopLeft.grid_remove()
                self.TopLeftFilled = "Empty"
            elif place=="Top":
                self.Cross_Top.grid_remove()
                self.TopFilled = "Empty"
            elif place=="TopRight":
                self.Cross_TopRight.grid_remove()
                self.TopRightFilled = "Empty"
            elif place=="Left":
                self.Cross_Left.grid_remove()
                self.LeftFilled = "Empty"
            elif place=="Middle":
                self.Cross_Middle.grid_remove()
                self.MiddleFilled = "Empty"
            elif place=="Right":
                self.Cross_Right.grid_remove()
                self.RightFilled = "Empty"
            elif place=="BottomLeft":
                self.Cross_BottomLeft.grid_remove()
                self.BottomLeftFilled = "Empty"
            elif place=="Bottom":
                self.Cross_Bottom.grid_remove()
                self.BottomFilled = "Empty"
            elif place=="BottomRight":
                self.Cross_BottomRight.grid_remove()
                self.BottomRightFilled = "Empty"
            else:
                raise Exception("You need to specify which piece to drop")

    def Nought(self, place=None, drop=False):
        if drop==False:
            if place=="TopLeft":
                self.Nought_TopLeft.grid(column=1, row=1)
                self.TopLeftFilled = "Nought"
            elif place=="Top":
                self.Nought_Top.grid(column=3, row=1)
                self.TopFilled = "Nought"
            elif place=="TopRight":
                self.Nought_TopRight.grid(column=5, row=1)
                self.TopRightFilled = "Nought"
            elif place=="Left":
                self.Nought_Left.grid(column=1, row=3)
                self.LeftFilled = "Nought"
            elif place=="Middle":
                self.Nought_Middle.grid(column=3, row=3)
                self.MiddleFilled = "Nought"
            elif place=="Right":
                self.Nought_Right.grid(column=5, row=3)
                self.RightFilled = "Nought"
            elif place=="BottomLeft":
                self.Nought_BottomLeft.grid(column=1, row=5)
                self.BottomLeftFilled = "Nought"
            elif place=="Bottom":
                self.Nought_Bottom.grid(column=3, row=5)
                self.BottomFilled = "Nought"
            elif place=="BottomRight":
                self.Nought_BottomRight.grid(column=5, row=5)
                self.BottomRightFilled = "Nought"
            else:
                raise Exception("You need to specify where to place the piece")

        else:
            if place=="All":
                self.Nought_TopLeft.grid_remove()
                self.Nought_Top.grid_remove()
                self.Nought_TopRight.grid_remove()
                self.Nought_Left.grid_remove()
                self.Nought_Middle.grid_remove()
                self.Nought_Right.grid_remove()
                self.Nought_BottomLeft.grid_remove()
                self.Nought_Bottom.grid_remove()
                self.Nought_BottomRight.grid_remove()
                self.Nought_Place.grid_remove()

                self.TopLeftFilled = "Empty"
                self.TopFilled = "Empty"
                self.TopRightFilled = "Empty"
                self.LeftFilled = "Empty"
                self.MiddleFilled = "Empty"
                self.RightFilled = "Empty"
                self.BottomLeftFilled = "Empty"
                self.BottomFilled = "Empty"
                self.BottomRightFilled = "Empty"
                
            elif place=="TopLeft":
                self.Nought_TopLeft.grid_remove()
                self.TopLeftFilled = "Empty"
            elif place=="Top":
                self.Nought_Top.grid_remove()
                self.TopFilled = "Empty"
            elif place=="TopRight":
                self.Nought_TopRight.grid_remove()
                self.TopRightFilled = "Empty"
            elif place=="Left":
                self.Nought_Left.grid_remove()
                self.LeftFilled = "Empty"
            elif place=="Middle":
                self.Nought_Middle.grid_remove()
                self.MiddleFilled = "Empty"
            elif place=="Right":
                self.Nought_Right.grid_remove()
                self.RightFilled = "Empty"
            elif place=="BottomLeft":
                self.Nought_BottomLeft.grid_remove()
                self.BottomLeftFilled = "Empty"
            elif place=="Bottom":
                self.Nought_Bottom.grid_remove()
                self.BottomFilled = "Empty"
            elif place=="BottomRight":
                self.Nought_BottomRight.grid_remove()
                self.BottomRightFilled = "Empty"
            else:
                raise Exception("You need to specify which piece to drop")

    def winCheck(self):
        if self.TopLeftFilled==self.TopFilled==self.TopRightFilled and self.TopLeftFilled!="Empty":
            return self.TopLeftFilled

        elif self.LeftFilled==self.MiddleFilled==self.RightFilled and self.LeftFilled!="Empty":
            return self.LeftFilled

        elif self.BottomLeftFilled==self.BottomFilled==self.BottomRightFilled and self.BottomLeftFilled!="Empty":
            return self.BottomLeftFilled

        if self.TopLeftFilled==self.LeftFilled==self.BottomLeftFilled and self.TopLeftFilled!="Empty":
            return self.TopLeftFilled

        elif self.TopFilled==self.MiddleFilled==self.BottomFilled and self.TopFilled!="Empty":
            return self.TopFilled

        elif self.TopRightFilled==self.RightFilled==self.BottomRightFilled and self.TopRightFilled!="Empty":
            return self.TopRightFilled

        elif self.TopLeftFilled==self.MiddleFilled==self.BottomRightFilled and self.TopLeftFilled!="Empty":
            return self.TopLeftFilled

        elif self.TopRightFilled==self.MiddleFilled==self.BottomLeftFilled and self.TopRightFilled!="Empty":
            return self.TopRightFilled

        else:
            return "No Win"
        
        


class turnBoard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.TurnFrame = tk.LabelFrame(master, relief="flat", bg="black")

        self.Horizontal_1 = tk.Label(self.TurnFrame, text="------------------------", bg="black", fg="white")
        self.Horizontal_2 = tk.Label(self.TurnFrame, text="------------------------", bg="black", fg="white")
        self.Vertical_1 = tk.Label(self.TurnFrame, text="|\n|\n|\n|\n|\n|\n|\n|", bg="black", fg="white")
        self.Vertical_2 = tk.Label(self.TurnFrame, text="|\n|\n|\n|\n|\n|\n|\n|", bg="black", fg="white")
        self.Corner_1 = tk.Label(self.TurnFrame, text="/", bg="black", fg="white")
        self.Corner_2 = tk.Label(self.TurnFrame, text="\\", bg="black", fg="white")
        self.Corner_3 = tk.Label(self.TurnFrame, text="\\", bg="black", fg="white")
        self.Corner_4 = tk.Label(self.TurnFrame, text="/", bg="black", fg="white")

        self.Horizontal_1.grid(column=1, row=0)
        self.Horizontal_2.grid(column=1, row=2)
        self.Vertical_1.grid(column=0, row=1)
        self.Vertical_2.grid(column=2, row=1)
        self.Corner_1.grid(column=0, row=0)
        self.Corner_2.grid(column=0, row=2)
        self.Corner_3.grid(column=2, row=0)
        self.Corner_4.grid(column=2, row=2)


        self.Cross = tk.Label(self.TurnFrame, text="X", bg="black", fg="white", font=("Calibri", 60))
        self.Nought = tk.Label(self.TurnFrame, text="O", bg="black", fg="white", font=("Calibri", 60))

    def draw(self):
        self.TurnFrame.grid(column=1, row=1, padx=10, sticky="S")

    def drop(self):
        self.TurnFrame.grid_remove()

    def cross(self):
        self.Nought.grid_remove()
        self.Cross.grid(column=1, row=1)

    def nought(self):
        self.Cross.grid_remove()
        self.Nought.grid(column=1, row=1)

class winTotal(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.winTotalFrame = tk.LabelFrame(master, relief="flat", bg="black", fg="white")

        self.CrossTotal = 0
        self.NoughtTotal = 0

        self.CrossTotalVar = tk.StringVar(self.winTotalFrame)
        self.CrossTotalVar.set(self.CrossTotal)
        self.NoughtTotalVar = tk.StringVar(self.winTotalFrame)
        self.NoughtTotalVar.set(self.NoughtTotal)


        self.CrossTotalLabel = tk.Label(self.winTotalFrame, text="Cross Wins:", bg="black", fg="white", font=("Calibri", 15))
        self.CrossTotalVarLabel = tk.Label(self.winTotalFrame, textvar=self.CrossTotalVar, bg="black", fg="white", font=("Calibri", 15))
        self.NoughtTotalLabel = tk.Label(self.winTotalFrame, text="Nought Wins:", bg="black", fg="white", font=("Calibri", 15))
        self.NoughtTotalVarLabel = tk.Label(self.winTotalFrame, textvar=self.NoughtTotalVar, bg="black", fg="white", font=("Calibri", 15))

        self.CrossTotalLabel.grid(column=0,row=0, sticky="E")
        self.CrossTotalVarLabel.grid(column=1,row=0, sticky="W")
        self.NoughtTotalLabel.grid(column=0,row=1, sticky="E")
        self.NoughtTotalVarLabel.grid(column=1,row=1, sticky="W")

    def draw(self):
        self.winTotalFrame.grid(column=1,row=2, sticky="N")

    def CrossWin(self, reset=False):
        if reset==True:
            self.CrossTotal = 0
            self.CrossTotalVar.set(self.CrossTotal)
        else:
            self.CrossTotal+=1
            self.CrossTotalVar.set(self.CrossTotal)

    def NoughtWin(self, reset=False):
        if reset==True:
            self.NoughtTotal = 0
            self.NoughtTotalVar.set(self.NoughtTotal)
        else:
            self.NoughtTotal+=1
            self.NoughtTotalVar.set(self.NoughtTotal)
            
outerBoard = outerBoard(root)
topLeft = smallBoard(outerFrame, 0, 0)
top = smallBoard(outerFrame, 2, 0)
topRight = smallBoard(outerFrame, 4, 0)
left = smallBoard(outerFrame, 0, 2)
middle = smallBoard(outerFrame, 2, 2)
right = smallBoard(outerFrame, 4, 2)
bottomLeft = smallBoard(outerFrame, 0, 4)
bottom = smallBoard(outerFrame, 2, 4)
bottomRight = smallBoard(outerFrame, 4, 4)
turnBoard = turnBoard(root)
winTotal = winTotal(root)

outerBoard.draw()
topLeft.drawFrame()
top.drawFrame()
topRight.drawFrame()
left.drawFrame()
middle.drawFrame()
right.drawFrame()
bottomLeft.drawFrame()
bottom.drawFrame()
bottomRight.drawFrame()
turnBoard.draw()
turnBoard.cross()
winTotal.draw()

def select_all():
    topLeft.select()
    top.select()
    topRight.select()
    left.select()
    middle.select()
    right.select()
    bottomLeft.select()
    bottom.select()
    bottomRight.select()

def deselect_all():
    topLeft.deselect()
    top.deselect()
    topRight.deselect()
    left.deselect()
    middle.deselect()
    right.deselect()
    bottomLeft.deselect()
    bottom.deselect()
    bottomRight.deselect()

def reset():
    deselect_all()

    topLeft.Cross("All", True)
    topLeft.Nought("All", True)
    top.Cross("All", True)
    top.Nought("All", True)
    topRight.Cross("All", True)
    topRight.Nought("All", True)
    left.Cross("All", True)
    left.Nought("All", True)
    middle.Cross("All", True)
    middle.Nought("All", True)
    right.Cross("All", True)
    right.Nought("All", True)
    bottomLeft.Cross("All", True)
    bottomLeft.Nought("All", True)
    bottom.Cross("All", True)
    bottom.Nought("All", True)
    bottomRight.Cross("All", True)
    bottomRight.Nought("All", True)

    global turn
    turn = "Cross"
    turnBoard.cross()
    
    global topLeftFull, FalsetopFull, FalsetopRightFull, FalseleftFull, FalsemiddleFull, FalserightFull, FalsebottomLeftFull, FalsebottomFull, FalsebottomRightFull
    topLeftFull = False
    topFull = False
    topRightFull = False
    leftFull = False
    middleFull = False
    rightFull = False
    bottomLeftFull = False
    bottomFull = False
    bottomRightFull = False

    topLeft.win(drop=True)
    topLeft.drawFrame()
    top.win(drop=True)
    top.drawFrame()
    topRight.win(drop=True)
    topRight.drawFrame()
    left.win(drop=True)
    left.drawFrame()
    middle.win(drop=True)
    middle.drawFrame()
    right.win(drop=True)
    right.drawFrame()
    bottomLeft.win(drop=True)
    bottomLeft.drawFrame()
    bottom.win(drop=True)
    bottom.drawFrame()
    bottomRight.win(drop=True)
    bottomRight.drawFrame()

def changeTurn():
    global turn
    
    if turn=="Cross":
        turn = "Nought"
        turnBoard.nought()
    elif turn=="Nought":
        turn = "Cross"
        turnBoard.cross()

def key_detect(event):
    key = event.char
    
    if key=="\r":
        reset()

    if key=="\t":
        reset()
        winTotal.CrossWin(True)
        winTotal.NoughtWin(True)
    
    if key=="0":
        changeTurn()
    
    if key=="7":
        if topLeft.Selected==False and top.Selected==False and topRight.Selected==False and left.Selected==False and middle.Selected==False and right.Selected==False and bottomLeft.Selected==False and bottom.Selected==False and bottomRight.Selected==False:
            deselect_all()
            topLeft.select()
        
        elif topLeft.Selected and topLeft.TopLeftFilled=="Empty":
            if turn=="Cross":
                topLeft.Cross("TopLeft")
            elif turn=="Nought":
                topLeft.Nought("TopLeft")
            changeTurn()
            deselect_all()
            topLeft.select()
            
        elif top.Selected and top.TopLeftFilled=="Empty":
            if turn=="Cross":
                top.Cross("TopLeft")
            elif turn=="Nought":
                top.Nought("TopLeft")
            changeTurn()
            deselect_all()
            topLeft.select()
            
        elif topRight.Selected and topRight.TopLeftFilled=="Empty":
            if turn=="Cross":
                topRight.Cross("TopLeft")
            elif turn=="Nought":
                topRight.Nought("TopLeft")
            changeTurn()
            deselect_all()
            topLeft.select()
            
        elif left.Selected and left.TopLeftFilled=="Empty":
            if turn=="Cross":
                left.Cross("TopLeft")
            elif turn=="Nought":
                left.Nought("TopLeft")
            changeTurn()
            deselect_all()
            topLeft.select()
            
        elif middle.Selected and middle.TopLeftFilled=="Empty":
            if turn=="Cross":
                middle.Cross("TopLeft")
            elif turn=="Nought":
                middle.Nought("TopLeft")
            changeTurn()
            deselect_all()
            topLeft.select()
            
        elif right.Selected and right.TopLeftFilled=="Empty":
            if turn=="Cross":
                right.Cross("TopLeft")
            elif turn=="Nought":
                right.Nought("TopLeft")
            changeTurn()
            deselect_all()
            topLeft.select()
            
        elif bottomLeft.Selected and bottomLeft.TopLeftFilled=="Empty":
            if turn=="Cross":
                bottomLeft.Cross("TopLeft")
            elif turn=="Nought":
                bottomLeft.Nought("TopLeft")
            changeTurn()
            deselect_all()
            topLeft.select()
            
        elif bottom.Selected and bottom.TopLeftFilled=="Empty":
            if turn=="Cross":
                bottom.Cross("TopLeft")
            elif turn=="Nought":
                bottom.Nought("TopLeft")
            changeTurn()
            deselect_all()
            topLeft.select()
            
        elif bottomRight.Selected and bottomRight.TopLeftFilled=="Empty":
            if turn=="Cross":
                bottomRight.Cross("TopLeft")
            elif turn=="Nought":
                bottomRight.Nought("TopLeft")
            changeTurn()
            deselect_all()
            topLeft.select()

            
    elif key=="8":
        if topLeft.Selected==False and top.Selected==False and topRight.Selected==False and left.Selected==False and middle.Selected==False and right.Selected==False and bottomLeft.Selected==False and bottom.Selected==False and bottomRight.Selected==False:
            deselect_all()
            top.select()
        
        elif topLeft.Selected and topLeft.TopFilled=="Empty":
            if turn=="Cross":
                topLeft.Cross("Top")
            elif turn=="Nought":
                topLeft.Nought("Top")
            changeTurn()
            deselect_all()
            top.select()
            
        elif top.Selected and top.TopFilled=="Empty":
            if turn=="Cross":
                top.Cross("Top")
            elif turn=="Nought":
                top.Nought("Top")
            changeTurn()
            deselect_all()
            top.select()
            
        elif topRight.Selected and topRight.TopFilled=="Empty":
            if turn=="Cross":
                topRight.Cross("Top")
            elif turn=="Nought":
                topRight.Nought("Top")
            changeTurn()
            deselect_all()
            top.select()
            
        elif left.Selected and left.TopFilled=="Empty":
            if turn=="Cross":
                left.Cross("Top")
            elif turn=="Nought":
                left.Nought("Top")
            changeTurn()
            deselect_all()
            top.select()
            
        elif middle.Selected and middle.TopFilled=="Empty":
            if turn=="Cross":
                middle.Cross("Top")
            elif turn=="Nought":
                middle.Nought("Top")
            changeTurn()
            deselect_all()
            top.select()
            
        elif right.Selected and right.TopFilled=="Empty":
            if turn=="Cross":
                right.Cross("Top")
            elif turn=="Nought":
                right.Nought("Top")
            changeTurn()
            deselect_all()
            top.select()
            
        elif bottomLeft.Selected and bottomLeft.TopFilled=="Empty":
            if turn=="Cross":
                bottomLeft.Cross("Top")
            elif turn=="Nought":
                bottomLeft.Nought("Top")
            changeTurn()
            deselect_all()
            top.select()
            
        elif bottom.Selected and bottom.TopFilled=="Empty":
            if turn=="Cross":
                bottom.Cross("Top")
            elif turn=="Nought":
                bottom.Nought("Top")
            changeTurn()
            deselect_all()
            top.select()
            
        elif bottomRight.Selected and bottomRight.TopFilled=="Empty":
            if turn=="Cross":
                bottomRight.Cross("Top")
            elif turn=="Nought":
                bottomRight.Nought("Top")
            changeTurn()
            deselect_all()
            top.select()
            
    elif key=="9":
        if topLeft.Selected==False and top.Selected==False and topRight.Selected==False and left.Selected==False and middle.Selected==False and right.Selected==False and bottomLeft.Selected==False and bottom.Selected==False and bottomRight.Selected==False:
            deselect_all()
            topRight.select()
        
        elif topLeft.Selected and topLeft.TopRightFilled=="Empty":
            if turn=="Cross":
                topLeft.Cross("TopRight")
            elif turn=="Nought":
                topLeft.Nought("TopRight")
            changeTurn()
            deselect_all()
            topRight.select()
            
        elif top.Selected and top.TopRightFilled=="Empty":
            if turn=="Cross":
                top.Cross("TopRight")
            elif turn=="Nought":
                top.Nought("TopRight")
            changeTurn()
            deselect_all()
            topRight.select()
            
        elif topRight.Selected and topRight.TopRightFilled=="Empty":
            if turn=="Cross":
                topRight.Cross("TopRight")
            elif turn=="Nought":
                topRight.Nought("TopRight")
            changeTurn()
            deselect_all()
            topRight.select()
            
        elif left.Selected and left.TopRightFilled=="Empty":
            if turn=="Cross":
                left.Cross("TopRight")
            elif turn=="Nought":
                left.Nought("TopRight")
            changeTurn()
            deselect_all()
            topRight.select()
            
        elif middle.Selected and middle.TopRightFilled=="Empty":
            if turn=="Cross":
                middle.Cross("TopRight")
            elif turn=="Nought":
                middle.Nought("TopRight")
            changeTurn()
            deselect_all()
            topRight.select()
            
        elif right.Selected and right.TopRightFilled=="Empty":
            if turn=="Cross":
                right.Cross("TopRight")
            elif turn=="Nought":
                right.Nought("TopRight")
            changeTurn()
            deselect_all()
            topRight.select()
            
        elif bottomLeft.Selected and bottomLeft.TopRightFilled=="Empty":
            if turn=="Cross":
                bottomLeft.Cross("TopRight")
            elif turn=="Nought":
                bottomLeft.Nought("TopRight")
            changeTurn()
            deselect_all()
            topRight.select()
            
        elif bottom.Selected and bottom.TopRightFilled=="Empty":
            if turn=="Cross":
                bottom.Cross("TopRight")
            elif turn=="Nought":
                bottom.Nought("TopRight")
            changeTurn()
            deselect_all()
            topRight.select()
            
        elif bottomRight.Selected and bottomRight.TopRightFilled=="Empty":
            if turn=="Cross":
                bottomRight.Cross("TopRight")
            elif turn=="Nought":
                bottomRight.Nought("TopRight")
            changeTurn()
            deselect_all()
            topRight.select()
            
    elif key=="4":
        if topLeft.Selected==False and top.Selected==False and topRight.Selected==False and left.Selected==False and middle.Selected==False and right.Selected==False and bottomLeft.Selected==False and bottom.Selected==False and bottomRight.Selected==False:
            deselect_all()
            left.select()
        
        elif topLeft.Selected and topLeft.LeftFilled=="Empty":
            if turn=="Cross":
                topLeft.Cross("Left")
            elif turn=="Nought":
                topLeft.Nought("Left")
            changeTurn()
            deselect_all()
            left.select()
            
        elif top.Selected and top.LeftFilled=="Empty":
            if turn=="Cross":
                top.Cross("Left")
            elif turn=="Nought":
                top.Nought("Left")
            changeTurn()
            deselect_all()
            left.select()
            
        elif topRight.Selected and topRight.LeftFilled=="Empty":
            if turn=="Cross":
                topRight.Cross("Left")
            elif turn=="Nought":
                topRight.Nought("Left")
            changeTurn()
            deselect_all()
            left.select()
            
        elif left.Selected and left.LeftFilled=="Empty":
            if turn=="Cross":
                left.Cross("Left")
            elif turn=="Nought":
                left.Nought("Left")
            changeTurn()
            deselect_all()
            left.select()
            
        elif middle.Selected and middle.LeftFilled=="Empty":
            if turn=="Cross":
                middle.Cross("Left")
            elif turn=="Nought":
                middle.Nought("Left")
            changeTurn()
            deselect_all()
            left.select()
            
        elif right.Selected and right.LeftFilled=="Empty":
            if turn=="Cross":
                right.Cross("Left")
            elif turn=="Nought":
                right.Nought("Left")
            changeTurn()
            deselect_all()
            left.select()
            
        elif bottomLeft.Selected and bottomLeft.LeftFilled=="Empty":
            if turn=="Cross":
                bottomLeft.Cross("Left")
            elif turn=="Nought":
                bottomLeft.Nought("Left")
            changeTurn()
            deselect_all()
            left.select()
            
        elif bottom.Selected and bottom.LeftFilled=="Empty":
            if turn=="Cross":
                bottom.Cross("Left")
            elif turn=="Nought":
                bottom.Nought("Left")
            changeTurn()
            deselect_all()
            left.select()
            
        elif bottomRight.Selected and bottomRight.LeftFilled=="Empty":
            if turn=="Cross":
                bottomRight.Cross("Left")
            elif turn=="Nought":
                bottomRight.Nought("Left")
            changeTurn()
            deselect_all()
            left.select()
        
    elif key=="5":
        if topLeft.Selected==False and top.Selected==False and topRight.Selected==False and left.Selected==False and middle.Selected==False and right.Selected==False and bottomLeft.Selected==False and bottom.Selected==False and bottomRight.Selected==False:
            deselect_all()
            middle.select()
        
        elif topLeft.Selected and topLeft.MiddleFilled=="Empty":
            if turn=="Cross":
                topLeft.Cross("Middle")
            elif turn=="Nought":
                topLeft.Nought("Middle")
            changeTurn()
            deselect_all()
            middle.select()
            
        elif top.Selected and top.MiddleFilled=="Empty":
            if turn=="Cross":
                top.Cross("Middle")
            elif turn=="Nought":
                top.Nought("Middle")
            changeTurn()
            deselect_all()
            middle.select()
            
        elif topRight.Selected and topRight.MiddleFilled=="Empty":
            if turn=="Cross":
                topRight.Cross("Middle")
            elif turn=="Nought":
                topRight.Nought("Middle")
            changeTurn()
            deselect_all()
            middle.select()
            
        elif left.Selected and left.MiddleFilled=="Empty":
            if turn=="Cross":
                left.Cross("Middle")
            elif turn=="Nought":
                left.Nought("Middle")
            changeTurn()
            deselect_all()
            middle.select()
            
        elif middle.Selected and middle.MiddleFilled=="Empty":
            if turn=="Cross":
                middle.Cross("Middle")
            elif turn=="Nought":
                middle.Nought("Middle")
            changeTurn()
            deselect_all()
            middle.select()
            
        elif right.Selected and right.MiddleFilled=="Empty":
            if turn=="Cross":
                right.Cross("Middle")
            elif turn=="Nought":
                right.Nought("Middle")
            changeTurn()
            deselect_all()
            middle.select()
            
        elif bottomLeft.Selected and bottomLeft.MiddleFilled=="Empty":
            if turn=="Cross":
                bottomLeft.Cross("Middle")
            elif turn=="Nought":
                bottomLeft.Nought("Middle")
            changeTurn()
            deselect_all()
            middle.select()
            
        elif bottom.Selected and bottom.MiddleFilled=="Empty":
            if turn=="Cross":
                bottom.Cross("Middle")
            elif turn=="Nought":
                bottom.Nought("Middle")
            changeTurn()
            deselect_all()
            middle.select()
            
        elif bottomRight.Selected and bottomRight.MiddleFilled=="Empty":
            if turn=="Cross":
                bottomRight.Cross("Middle")
            elif turn=="Nought":
                bottomRight.Nought("Middle")
            changeTurn()
            deselect_all()
            middle.select()
        
    elif key=="6":
        if topLeft.Selected==False and top.Selected==False and topRight.Selected==False and left.Selected==False and middle.Selected==False and right.Selected==False and bottomLeft.Selected==False and bottom.Selected==False and bottomRight.Selected==False:
            deselect_all()
            right.select()
        
        elif topLeft.Selected and topLeft.RightFilled=="Empty":
            if turn=="Cross":
                topLeft.Cross("Right")
            elif turn=="Nought":
                topLeft.Nought("Right")
            changeTurn()
            deselect_all()
            right.select()
            
        elif top.Selected and top.RightFilled=="Empty":
            if turn=="Cross":
                top.Cross("Right")
            elif turn=="Nought":
                top.Nought("Right")
            changeTurn()
            deselect_all()
            right.select()
            
        elif topRight.Selected and topRight.RightFilled=="Empty":
            if turn=="Cross":
                topRight.Cross("Right")
            elif turn=="Nought":
                topRight.Nought("Right")
            changeTurn()
            deselect_all()
            right.select()
            
        elif left.Selected and left.RightFilled=="Empty":
            if turn=="Cross":
                left.Cross("Right")
            elif turn=="Nought":
                left.Nought("Right")
            changeTurn()
            deselect_all()
            right.select()
            
        elif middle.Selected and middle.RightFilled=="Empty":
            if turn=="Cross":
                middle.Cross("Right")
            elif turn=="Nought":
                middle.Nought("Right")
            changeTurn()
            deselect_all()
            right.select()
            
        elif right.Selected and right.RightFilled=="Empty":
            if turn=="Cross":
                right.Cross("Right")
            elif turn=="Nought":
                right.Nought("Right")
            changeTurn()
            deselect_all()
            right.select()
            
        elif bottomLeft.Selected and bottomLeft.RightFilled=="Empty":
            if turn=="Cross":
                bottomLeft.Cross("Right")
            elif turn=="Nought":
                bottomLeft.Nought("Right")
            changeTurn()
            deselect_all()
            right.select()
            
        elif bottom.Selected and bottom.RightFilled=="Empty":
            if turn=="Cross":
                bottom.Cross("Right")
            elif turn=="Nought":
                bottom.Nought("Right")
            changeTurn()
            deselect_all()
            right.select()
            
        elif bottomRight.Selected and bottomRight.RightFilled=="Empty":
            if turn=="Cross":
                bottomRight.Cross("Right")
            elif turn=="Nought":
                bottomRight.Nought("Right")
            changeTurn()
            deselect_all()
            right.select()
        
    elif key=="1":
        if topLeft.Selected==False and top.Selected==False and topRight.Selected==False and left.Selected==False and middle.Selected==False and right.Selected==False and bottomLeft.Selected==False and bottom.Selected==False and bottomRight.Selected==False:
            deselect_all()
            bottomLeft.select()
        
        elif topLeft.Selected and topLeft.BottomLeftFilled=="Empty":
            if turn=="Cross":
                topLeft.Cross("BottomLeft")
            elif turn=="Nought":
                topLeft.Nought("BottomLeft")
            changeTurn()
            deselect_all()
            bottomLeft.select()
            
        elif top.Selected and top.BottomLeftFilled=="Empty":
            if turn=="Cross":
                top.Cross("BottomLeft")
            elif turn=="Nought":
                top.Nought("BottomLeft")
            changeTurn()
            deselect_all()
            bottomLeft.select()
            
        elif topRight.Selected and topRight.BottomLeftFilled=="Empty":
            if turn=="Cross":
                topRight.Cross("BottomLeft")
            elif turn=="Nought":
                topRight.Nought("BottomLeft")
            changeTurn()
            deselect_all()
            bottomLeft.select()
            
        elif left.Selected and left.BottomLeftFilled=="Empty":
            if turn=="Cross":
                left.Cross("BottomLeft")
            elif turn=="Nought":
                left.Nought("BottomLeft")
            changeTurn()
            deselect_all()
            bottomLeft.select()
            
        elif middle.Selected and middle.BottomLeftFilled=="Empty":
            if turn=="Cross":
                middle.Cross("BottomLeft")
            elif turn=="Nought":
                middle.Nought("BottomLeft")
            changeTurn()
            deselect_all()
            bottomLeft.select()
            
        elif right.Selected and right.BottomLeftFilled=="Empty":
            if turn=="Cross":
                right.Cross("BottomLeft")
            elif turn=="Nought":
                right.Nought("BottomLeft")
            changeTurn()
            deselect_all()
            bottomLeft.select()
            
        elif bottomLeft.Selected and bottomLeft.BottomLeftFilled=="Empty":
            if turn=="Cross":
                bottomLeft.Cross("BottomLeft")
            elif turn=="Nought":
                bottomLeft.Nought("BottomLeft")
            changeTurn()
            deselect_all()
            bottomLeft.select()
            
        elif bottom.Selected and bottom.BottomLeftFilled=="Empty":
            if turn=="Cross":
                bottom.Cross("BottomLeft")
            elif turn=="Nought":
                bottom.Nought("BottomLeft")
            changeTurn()
            deselect_all()
            bottomLeft.select()
            
        elif bottomRight.Selected and bottomRight.BottomLeftFilled=="Empty":
            if turn=="Cross":
                bottomRight.Cross("BottomLeft")
            elif turn=="Nought":
                bottomRight.Nought("BottomLeft")
            changeTurn()
            deselect_all()
            bottomLeft.select()
        
    elif key=="2":
        if topLeft.Selected==False and top.Selected==False and topRight.Selected==False and left.Selected==False and middle.Selected==False and right.Selected==False and bottomLeft.Selected==False and bottom.Selected==False and bottomRight.Selected==False:
            deselect_all()
            bottom.select()
        
        elif topLeft.Selected and topLeft.BottomFilled=="Empty":
            if turn=="Cross":
                topLeft.Cross("Bottom")
            elif turn=="Nought":
                topLeft.Nought("Bottom")
            changeTurn()
            deselect_all()
            bottom.select()
            
        elif top.Selected and top.BottomFilled=="Empty":
            if turn=="Cross":
                top.Cross("Bottom")
            elif turn=="Nought":
                top.Nought("Bottom")
            changeTurn()
            deselect_all()
            bottom.select()
            
        elif topRight.Selected and topRight.BottomFilled=="Empty":
            if turn=="Cross":
                topRight.Cross("Bottom")
            elif turn=="Nought":
                topRight.Nought("Bottom")
            changeTurn()
            deselect_all()
            bottom.select()
            
        elif left.Selected and left.BottomFilled=="Empty":
            if turn=="Cross":
                left.Cross("Bottom")
            elif turn=="Nought":
                left.Nought("Bottom")
            changeTurn()
            deselect_all()
            bottom.select()
            
        elif middle.Selected and middle.BottomFilled=="Empty":
            if turn=="Cross":
                middle.Cross("Bottom")
            elif turn=="Nought":
                middle.Nought("Bottom")
            changeTurn()
            deselect_all()
            bottom.select()
            
        elif right.Selected and right.BottomFilled=="Empty":
            if turn=="Cross":
                right.Cross("Bottom")
            elif turn=="Nought":
                right.Nought("Bottom")
            changeTurn()
            deselect_all()
            bottom.select()
            
        elif bottomLeft.Selected and bottomLeft.BottomFilled=="Empty":
            if turn=="Cross":
                bottomLeft.Cross("Bottom")
            elif turn=="Nought":
                bottomLeft.Nought("Bottom")
            changeTurn()
            deselect_all()
            bottom.select()
            
        elif bottom.Selected and bottom.BottomFilled=="Empty":
            if turn=="Cross":
                bottom.Cross("Bottom")
            elif turn=="Nought":
                bottom.Nought("Bottom")
            changeTurn()
            deselect_all()
            bottom.select()
            
        elif bottomRight.Selected and bottomRight.BottomFilled=="Empty":
            if turn=="Cross":
                bottomRight.Cross("Bottom")
            elif turn=="Nought":
                bottomRight.Nought("Bottom")
            changeTurn()
            deselect_all()
            bottom.select()
        
    elif key=="3":
        if topLeft.Selected==False and top.Selected==False and topRight.Selected==False and left.Selected==False and middle.Selected==False and right.Selected==False and bottomLeft.Selected==False and bottom.Selected==False and bottomRight.Selected==False:
            deselect_all()
            bottomRight.select()
        
        elif topLeft.Selected and topLeft.BottomRightFilled=="Empty":
            if turn=="Cross":
                topLeft.Cross("BottomRight")
            elif turn=="Nought":
                topLeft.Nought("BottomRight")
            changeTurn()
            deselect_all()
            bottomRight.select()
            
        elif top.Selected and top.BottomRightFilled=="Empty":
            if turn=="Cross":
                top.Cross("BottomRight")
            elif turn=="Nought":
                top.Nought("BottomRight")
            changeTurn()
            deselect_all()
            bottomRight.select()
            
        elif topRight.Selected and topRight.BottomRightFilled=="Empty":
            if turn=="Cross":
                topRight.Cross("BottomRight")
            elif turn=="Nought":
                topRight.Nought("BottomRight")
            changeTurn()
            deselect_all()
            bottomRight.select()
            
        elif left.Selected and left.BottomRightFilled=="Empty":
            if turn=="Cross":
                left.Cross("BottomRight")
            elif turn=="Nought":
                left.Nought("BottomRight")
            changeTurn()
            deselect_all()
            bottomRight.select()
            
        elif middle.Selected and middle.BottomRightFilled=="Empty":
            if turn=="Cross":
                middle.Cross("BottomRight")
            elif turn=="Nought":
                middle.Nought("BottomRight")
            changeTurn()
            deselect_all()
            bottomRight.select()
            
        elif right.Selected and right.BottomRightFilled=="Empty":
            if turn=="Cross":
                right.Cross("BottomRight")
            elif turn=="Nought":
                right.Nought("BottomRight")
            changeTurn()
            deselect_all()
            bottomRight.select()
            
        elif bottomLeft.Selected and bottomLeft.BottomRightFilled=="Empty":
            if turn=="Cross":
                bottomLeft.Cross("BottomRight")
            elif turn=="Nought":
                bottomLeft.Nought("BottomRight")
            changeTurn()
            deselect_all()
            bottomRight.select()
            
        elif bottom.Selected and bottom.BottomRightFilled=="Empty":
            if turn=="Cross":
                bottom.Cross("BottomRight")
            elif turn=="Nought":
                bottom.Nought("BottomRight")
            changeTurn()
            deselect_all()
            bottomRight.select()
            
        elif bottomRight.Selected and bottomRight.BottomRightFilled=="Empty":
            if turn=="Cross":
                bottomRight.Cross("BottomRight")
            elif turn=="Nought":
                bottomRight.Nought("BottomRight")
            changeTurn()
            deselect_all()
            bottomRight.select()
            

    if topLeft.Selected and topLeft.TopLeftFilled!="Empty" and topLeft.TopFilled!="Empty" and topLeft.TopRightFilled!="Empty" and topLeft.LeftFilled!="Empty" and topLeft.MiddleFilled!="Empty" and topLeft.RightFilled!="Empty" and topLeft.BottomLeftFilled!="Empty" and topLeft.BottomFilled!="Empty" and topLeft.BottomRightFilled!="Empty":
        global topLeftFull
        topLeftFull = True
        deselect_all()
        
    elif top.Selected and top.TopLeftFilled!="Empty" and top.TopFilled!="Empty" and top.TopRightFilled!="Empty" and top.LeftFilled!="Empty" and top.MiddleFilled!="Empty" and top.RightFilled!="Empty" and top.BottomLeftFilled!="Empty" and top.BottomFilled!="Empty" and top.BottomRightFilled!="Empty":
        global topFull
        topFull = True
        deselect_all()
        
    elif topRight.Selected and topRight.TopLeftFilled!="Empty" and topRight.TopFilled!="Empty" and topRight.TopRightFilled!="Empty" and topRight.LeftFilled!="Empty" and topRight.MiddleFilled!="Empty" and topRight.RightFilled!="Empty" and topRight.BottomLeftFilled!="Empty" and topRight.BottomFilled!="Empty" and topRight.BottomRightFilled!="Empty":
        global topRightFull
        topRightFull = True
        deselect_all()
        
    elif left.Selected and left.TopLeftFilled!="Empty" and left.TopFilled!="Empty" and left.TopRightFilled!="Empty" and left.LeftFilled!="Empty" and left.MiddleFilled!="Empty" and left.RightFilled!="Empty" and left.BottomLeftFilled!="Empty" and left.BottomFilled!="Empty" and left.BottomRightFilled!="Empty":
        global leftFull
        leftFull = True
        deselect_all()
        
    elif middle.Selected and middle.TopLeftFilled!="Empty" and middle.TopFilled!="Empty" and middle.TopRightFilled!="Empty" and middle.LeftFilled!="Empty" and middle.MiddleFilled!="Empty" and middle.RightFilled!="Empty" and middle.BottomLeftFilled!="Empty" and middle.BottomFilled!="Empty" and middle.BottomRightFilled!="Empty":
        global middleFull
        middleFull = True
        deselect_all()
        
    elif right.Selected and right.TopLeftFilled!="Empty" and right.TopFilled!="Empty" and right.TopRightFilled!="Empty" and right.LeftFilled!="Empty" and right.MiddleFilled!="Empty" and right.RightFilled!="Empty" and right.BottomLeftFilled!="Empty" and right.BottomFilled!="Empty" and right.BottomRightFilled!="Empty":
        global rightFull
        rightFull = True
        deselect_all()
        
    elif bottomLeft.Selected and bottomLeft.TopLeftFilled!="Empty" and bottomLeft.TopFilled!="Empty" and bottomLeft.TopRightFilled!="Empty" and bottomLeft.LeftFilled!="Empty" and bottomLeft.MiddleFilled!="Empty" and bottomLeft.RightFilled!="Empty" and bottomLeft.BottomLeftFilled!="Empty" and bottomLeft.BottomFilled!="Empty" and bottomLeft.BottomRightFilled!="Empty":
        global bottomLeftFull
        bottomLeftFull = True
        deselect_all()
        
    elif bottom.Selected and bottom.TopLeftFilled!="Empty" and bottom.TopFilled!="Empty" and bottom.TopRightFilled!="Empty" and bottom.LeftFilled!="Empty" and bottom.MiddleFilled!="Empty" and bottom.RightFilled!="Empty" and bottom.BottomLeftFilled!="Empty" and bottom.BottomFilled!="Empty" and bottom.BottomRightFilled!="Empty":
        global bottomFull
        bottomFull = True
        deselect_all()
        
    elif bottomRight.Selected and bottomRight.TopLeftFilled!="Empty" and bottomRight.TopFilled!="Empty" and bottomRight.TopRightFilled!="Empty" and bottomRight.LeftFilled!="Empty" and bottomRight.MiddleFilled!="Empty" and bottomRight.RightFilled!="Empty" and bottomRight.BottomLeftFilled!="Empty" and bottomRight.BottomFilled!="Empty" and bottomRight.BottomRightFilled!="Empty":
        global bottomRightFull
        bottomRightFull = True
        deselect_all()


    if topLeft.Selected and topLeft.Won==True:
        deselect_all()
    elif top.Selected and top.Won==True:
        deselect_all()
    elif topRight.Selected and topRight.Won==True:
        deselect_all()
    elif left.Selected and left.Won==True:
        deselect_all()
    elif middle.Selected and middle.Won==True:
        deselect_all()
    elif right.Selected and right.Won==True:
        deselect_all()
    elif bottomLeft.Selected and bottomLeft.Won==True:
        deselect_all()
    elif bottom.Selected and bottom.Won==True:
        deselect_all()
    elif bottomRight.Selected and bottomRight.Won==True:
        deselect_all()


    if topLeft.winCheck()=="Cross":
        topLeft.dropFrame()
        topLeft.win("Cross")
    elif topLeft.winCheck()=="Nought":
        topLeft.dropFrame()
        topLeft.win("Nought")

    if top.winCheck()=="Cross":
        top.dropFrame()
        top.win("Cross")
    elif top.winCheck()=="Nought":
        top.dropFrame()
        top.win("Nought")
    
    if topRight.winCheck()=="Cross":
        topRight.dropFrame()
        topRight.win("Cross")
    elif topRight.winCheck()=="Nought":
        topRight.dropFrame()
        topRight.win("Nought")

    if left.winCheck()=="Cross":
        left.dropFrame()
        left.win("Cross")
    elif left.winCheck()=="Nought":
        left.dropFrame()
        left.win("Nought")

    if middle.winCheck()=="Cross":
        middle.dropFrame()
        middle.win("Cross")
    elif middle.winCheck()=="Nought":
        middle.dropFrame()
        middle.win("Nought")
    
    if right.winCheck()=="Cross":
        right.dropFrame()
        right.win("Cross")
    elif right.winCheck()=="Nought":
        right.dropFrame()
        right.win("Nought")

    if bottomLeft.winCheck()=="Cross":
        bottomLeft.dropFrame()
        bottomLeft.win("Cross")
    elif bottomLeft.winCheck()=="Nought":
        bottomLeft.dropFrame()
        bottomLeft.win("Nought")

    if bottom.winCheck()=="Cross":
        bottom.dropFrame()
        bottom.win("Cross")
    elif bottom.winCheck()=="Nought":
        bottom.dropFrame()
        bottom.win("Nought")
    
    if bottomRight.winCheck()=="Cross":
        bottomRight.dropFrame()
        bottomRight.win("Cross")
    elif bottomRight.winCheck()=="Nought":
        bottomRight.dropFrame()
        bottomRight.win("Nought")


    if topLeft.winCheck()==top.winCheck()==topRight.winCheck()=="Cross":
        winTotal.CrossWin()
        root.after(3000, reset)
    elif topLeft.winCheck()==top.winCheck()==topRight.winCheck()=="Nought":
        winTotal.NoughtWin()
        root.after(3000, reset)
        
    elif left.winCheck()==middle.winCheck()==right.winCheck()=="Cross":
        winTotal.CrossWin()
        root.after(3000, reset)
    elif left.winCheck()==middle.winCheck()==right.winCheck()=="Nought":
        winTotal.NoughtWin()
        root.after(3000, reset)
        
    elif bottomLeft.winCheck()==bottom.winCheck()==bottomRight.winCheck()=="Cross":
        winTotal.CrossWin()
        root.after(3000, reset)
    elif bottomLeft.winCheck()==bottom.winCheck()==bottomRight.winCheck()=="Nought":
        winTotal.NoughtWin()
        root.after(3000, reset)
    
    elif topLeft.winCheck()==left.winCheck()==bottomLeft.winCheck()=="Cross":
        winTotal.CrossWin()
        root.after(3000, reset)
    elif topLeft.winCheck()==left.winCheck()==bottomLeft.winCheck()=="Nought":
        winTotal.NoughtWin()
        root.after(3000, reset)
        
    elif top.winCheck()==middle.winCheck()==bottom.winCheck()=="Cross":
        winTotal.CrossWin()
        root.after(3000, reset)
    elif top.winCheck()==middle.winCheck()==bottom.winCheck()=="Nought":
        winTotal.NoughtWin()
        root.after(3000, reset)
        
    elif topRight.winCheck()==right.winCheck()==bottomRight.winCheck()=="Cross":
        winTotal.CrossWin()
        root.after(3000, reset)
    elif topRight.winCheck()==right.winCheck()==bottomRight.winCheck()=="Nought":
        winTotal.NoughtWin()
        root.after(3000, reset)

    elif topLeft.winCheck()==middle.winCheck()==bottomRight.winCheck()=="Cross":
        winTotal.CrossWin()
        root.after(3000, reset)
    elif topLeft.winCheck()==middle.winCheck()==bottomRight.winCheck()=="Nought":
        winTotal.NoughtWin()
        root.after(3000, reset)
        
    elif topRight.winCheck()==middle.winCheck()==bottomLeft.winCheck()=="Cross":
        winTotal.CrossWin()
        root.after(3000, reset)
    elif topRight.winCheck()==middle.winCheck()==bottomLeft.winCheck()=="Nought":
        winTotal.NoughtWin()
        root.after(3000, reset)
        

root.bind("<Key>", key_detect)
root.mainloop()
