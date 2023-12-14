import tkinter as tk
import time

window = tk.Tk()
window.title("Tic Tac Toe")
window.minsize(450,450)

CrossWins = NoughtWins = 0

trueCenter = {"column": 100,
              "row": 100}

class PropertyDefine(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.Buffer_1 = tk.Label(width=3)
        
        #------------------------------OUTLINE------------------------------
        
        #----------OUTER----------
        self.Outer_Horizontal_1 = tk.Label(text="------------", font=("Times", 20, "bold"))
        self.Outer_Horizontal_2 = tk.Label(text="------------", font=("Times", 20, "bold"))
        self.Outer_Horizontal_3 = tk.Label(text="------------", font=("Times", 20, "bold"))
        self.Outer_Horizontal_4 = tk.Label(text="------------", font=("Times", 20, "bold"))
        self.Outer_Horizontal_5 = tk.Label(text="------------", font=("Times", 20, "bold"))
        self.Outer_Horizontal_6 = tk.Label(text="------------", font=("Times", 20, "bold"))

        self.Outer_Vertical_1 = tk.Label(text="|\n|\n|\n|", font=("Times", 17, "bold"))
        self.Outer_Vertical_2 = tk.Label(text="|\n|\n|\n|", font=("Times", 17, "bold"))
        self.Outer_Vertical_3 = tk.Label(text="|\n|\n|\n|", font=("Times", 17, "bold"))
        self.Outer_Vertical_4 = tk.Label(text="|\n|\n|\n|", font=("Times", 17, "bold"))
        self.Outer_Vertical_5 = tk.Label(text="|\n|\n|\n|", font=("Times", 17, "bold"))
        self.Outer_Vertical_6 = tk.Label(text="|\n|\n|\n|", font=("Times", 17, "bold"))

        self.Outer_Cross_1 = tk.Label(text="+", font=("Times", 15, "bold"))
        self.Outer_Cross_2 = tk.Label(text="+", font=("Times", 15, "bold"))
        self.Outer_Cross_3 = tk.Label(text="+", font=("Times", 15, "bold"))
        self.Outer_Cross_4 = tk.Label(text="+", font=("Times", 15, "bold"))

        #----------TOP-LEFT----------
        self.TopLeft_Horizontal_1 = tk.Label(text="----")
        self.TopLeft_Horizontal_2 = tk.Label(text="----")
        self.TopLeft_Horizontal_3 = tk.Label(text="----")
        self.TopLeft_Horizontal_4 = tk.Label(text="----")
        self.TopLeft_Horizontal_5 = tk.Label(text="----")
        self.TopLeft_Horizontal_6 = tk.Label(text="----")

        self.TopLeft_Vertical_1 = tk.Label(text="|")
        self.TopLeft_Vertical_2 = tk.Label(text="|")
        self.TopLeft_Vertical_3 = tk.Label(text="|")
        self.TopLeft_Vertical_4 = tk.Label(text="|")
        self.TopLeft_Vertical_5 = tk.Label(text="|")
        self.TopLeft_Vertical_6 = tk.Label(text="|")

        self.TopLeft_Cross_1 = tk.Label(text="+")
        self.TopLeft_Cross_2 = tk.Label(text="+")
        self.TopLeft_Cross_3 = tk.Label(text="+")
        self.TopLeft_Cross_4 = tk.Label(text="+")

        #----------TOP----------
        self.Top_Horizontal_1 = tk.Label(text="----")
        self.Top_Horizontal_2 = tk.Label(text="----")
        self.Top_Horizontal_3 = tk.Label(text="----")
        self.Top_Horizontal_4 = tk.Label(text="----")
        self.Top_Horizontal_5 = tk.Label(text="----")
        self.Top_Horizontal_6 = tk.Label(text="----")

        self.Top_Vertical_1 = tk.Label(text="|")
        self.Top_Vertical_2 = tk.Label(text="|")
        self.Top_Vertical_3 = tk.Label(text="|")
        self.Top_Vertical_4 = tk.Label(text="|")
        self.Top_Vertical_5 = tk.Label(text="|")
        self.Top_Vertical_6 = tk.Label(text="|")

        self.Top_Cross_1 = tk.Label(text="+")
        self.Top_Cross_2 = tk.Label(text="+")
        self.Top_Cross_3 = tk.Label(text="+")
        self.Top_Cross_4 = tk.Label(text="+")
        
        #----------TOP-RIGHT----------
        self.TopRight_Horizontal_1 = tk.Label(text="----")
        self.TopRight_Horizontal_2 = tk.Label(text="----")
        self.TopRight_Horizontal_3 = tk.Label(text="----")
        self.TopRight_Horizontal_4 = tk.Label(text="----")
        self.TopRight_Horizontal_5 = tk.Label(text="----")
        self.TopRight_Horizontal_6 = tk.Label(text="----")

        self.TopRight_Vertical_1 = tk.Label(text="|")
        self.TopRight_Vertical_2 = tk.Label(text="|")
        self.TopRight_Vertical_3 = tk.Label(text="|")
        self.TopRight_Vertical_4 = tk.Label(text="|")
        self.TopRight_Vertical_5 = tk.Label(text="|")
        self.TopRight_Vertical_6 = tk.Label(text="|")

        self.TopRight_Cross_1 = tk.Label(text="+")
        self.TopRight_Cross_2 = tk.Label(text="+")
        self.TopRight_Cross_3 = tk.Label(text="+")
        self.TopRight_Cross_4 = tk.Label(text="+")

        #----------LEFT----------
        self.Left_Horizontal_1 = tk.Label(text="----")
        self.Left_Horizontal_2 = tk.Label(text="----")
        self.Left_Horizontal_3 = tk.Label(text="----")
        self.Left_Horizontal_4 = tk.Label(text="----")
        self.Left_Horizontal_5 = tk.Label(text="----")
        self.Left_Horizontal_6 = tk.Label(text="----")

        self.Left_Vertical_1 = tk.Label(text="|")
        self.Left_Vertical_2 = tk.Label(text="|")
        self.Left_Vertical_3 = tk.Label(text="|")
        self.Left_Vertical_4 = tk.Label(text="|")
        self.Left_Vertical_5 = tk.Label(text="|")
        self.Left_Vertical_6 = tk.Label(text="|")

        self.Left_Cross_1 = tk.Label(text="+")
        self.Left_Cross_2 = tk.Label(text="+")
        self.Left_Cross_3 = tk.Label(text="+")
        self.Left_Cross_4 = tk.Label(text="+")

        #----------MIDDLE----------
        self.Middle_Horizontal_1 = tk.Label(text="----")
        self.Middle_Horizontal_2 = tk.Label(text="----")
        self.Middle_Horizontal_3 = tk.Label(text="----")
        self.Middle_Horizontal_4 = tk.Label(text="----")
        self.Middle_Horizontal_5 = tk.Label(text="----")
        self.Middle_Horizontal_6 = tk.Label(text="----")

        self.Middle_Vertical_1 = tk.Label(text="|")
        self.Middle_Vertical_2 = tk.Label(text="|")
        self.Middle_Vertical_3 = tk.Label(text="|")
        self.Middle_Vertical_4 = tk.Label(text="|")
        self.Middle_Vertical_5 = tk.Label(text="|")
        self.Middle_Vertical_6 = tk.Label(text="|")

        self.Middle_Cross_1 = tk.Label(text="+")
        self.Middle_Cross_2 = tk.Label(text="+")
        self.Middle_Cross_3 = tk.Label(text="+")
        self.Middle_Cross_4 = tk.Label(text="+")

        #----------RIGHT----------
        self.Right_Horizontal_1 = tk.Label(text="----")
        self.Right_Horizontal_2 = tk.Label(text="----")
        self.Right_Horizontal_3 = tk.Label(text="----")
        self.Right_Horizontal_4 = tk.Label(text="----")
        self.Right_Horizontal_5 = tk.Label(text="----")
        self.Right_Horizontal_6 = tk.Label(text="----")

        self.Right_Vertical_1 = tk.Label(text="|")
        self.Right_Vertical_2 = tk.Label(text="|")
        self.Right_Vertical_3 = tk.Label(text="|")
        self.Right_Vertical_4 = tk.Label(text="|")
        self.Right_Vertical_5 = tk.Label(text="|")
        self.Right_Vertical_6 = tk.Label(text="|")

        self.Right_Cross_1 = tk.Label(text="+")
        self.Right_Cross_2 = tk.Label(text="+")
        self.Right_Cross_3 = tk.Label(text="+")
        self.Right_Cross_4 = tk.Label(text="+")

        #----------BOTTOM-LEFT----------
        self.BottomLeft_Horizontal_1 = tk.Label(text="----")
        self.BottomLeft_Horizontal_2 = tk.Label(text="----")
        self.BottomLeft_Horizontal_3 = tk.Label(text="----")
        self.BottomLeft_Horizontal_4 = tk.Label(text="----")
        self.BottomLeft_Horizontal_5 = tk.Label(text="----")
        self.BottomLeft_Horizontal_6 = tk.Label(text="----")

        self.BottomLeft_Vertical_1 = tk.Label(text="|")
        self.BottomLeft_Vertical_2 = tk.Label(text="|")
        self.BottomLeft_Vertical_3 = tk.Label(text="|")
        self.BottomLeft_Vertical_4 = tk.Label(text="|")
        self.BottomLeft_Vertical_5 = tk.Label(text="|")
        self.BottomLeft_Vertical_6 = tk.Label(text="|")

        self.BottomLeft_Cross_1 = tk.Label(text="+")
        self.BottomLeft_Cross_2 = tk.Label(text="+")
        self.BottomLeft_Cross_3 = tk.Label(text="+")
        self.BottomLeft_Cross_4 = tk.Label(text="+")

        #----------BOTTOM----------
        self.Bottom_Horizontal_1 = tk.Label(text="----")
        self.Bottom_Horizontal_2 = tk.Label(text="----")
        self.Bottom_Horizontal_3 = tk.Label(text="----")
        self.Bottom_Horizontal_4 = tk.Label(text="----")
        self.Bottom_Horizontal_5 = tk.Label(text="----")
        self.Bottom_Horizontal_6 = tk.Label(text="----")

        self.Bottom_Vertical_1 = tk.Label(text="|")
        self.Bottom_Vertical_2 = tk.Label(text="|")
        self.Bottom_Vertical_3 = tk.Label(text="|")
        self.Bottom_Vertical_4 = tk.Label(text="|")
        self.Bottom_Vertical_5 = tk.Label(text="|")
        self.Bottom_Vertical_6 = tk.Label(text="|")

        self.Bottom_Cross_1 = tk.Label(text="+")
        self.Bottom_Cross_2 = tk.Label(text="+")
        self.Bottom_Cross_3 = tk.Label(text="+")
        self.Bottom_Cross_4 = tk.Label(text="+")

        #----------BOTTOM-RIGHT----------
        self.BottomRight_Horizontal_1 = tk.Label(text="----")
        self.BottomRight_Horizontal_2 = tk.Label(text="----")
        self.BottomRight_Horizontal_3 = tk.Label(text="----")
        self.BottomRight_Horizontal_4 = tk.Label(text="----")
        self.BottomRight_Horizontal_5 = tk.Label(text="----")
        self.BottomRight_Horizontal_6 = tk.Label(text="----")

        self.BottomRight_Vertical_1 = tk.Label(text="|")
        self.BottomRight_Vertical_2 = tk.Label(text="|")
        self.BottomRight_Vertical_3 = tk.Label(text="|")
        self.BottomRight_Vertical_4 = tk.Label(text="|")
        self.BottomRight_Vertical_5 = tk.Label(text="|")
        self.BottomRight_Vertical_6 = tk.Label(text="|")

        self.BottomRight_Cross_1 = tk.Label(text="+")
        self.BottomRight_Cross_2 = tk.Label(text="+")
        self.BottomRight_Cross_3 = tk.Label(text="+")
        self.BottomRight_Cross_4 = tk.Label(text="+")

        #------------------------------PIECE------------------------------
        
        self.Cross_TopLeft = tk.Label(text="X")
        self.Cross_Top = tk.Label(text="X")
        self.Cross_TopRight = tk.Label(text="X")
        self.Cross_Left = tk.Label(text="X")
        self.Cross_Middle = tk.Label(text="X")
        self.Cross_Right = tk.Label(text="X")
        self.Cross_BottomLeft = tk.Label(text="X")
        self.Cross_Bottom = tk.Label(text="X")
        self.Cross_BottomRight = tk.Label(text="X")

        self.Nought_TopLeft = tk.Label(text="O")
        self.Nought_Top = tk.Label(text="O")
        self.Nought_TopRight = tk.Label(text="O")
        self.Nought_Left = tk.Label(text="O")
        self.Nought_Middle = tk.Label(text="O")
        self.Nought_Right = tk.Label(text="O")
        self.Nought_BottomLeft = tk.Label(text="O")
        self.Nought_Bottom = tk.Label(text="O")
        self.Nought_BottomRight = tk.Label(text="O")

class Frame(PropertyDefine):
    def DrawAll(self):
        frame.Outer()
        frame.TopLeft("Draw")
        frame.Top("Draw")
        frame.TopRight("Draw")
        frame.Left("Draw")
        frame.Middle("Draw")
        frame.Right("Draw")
        frame.BottomLeft("Draw")
        frame.Bottom("Draw")
        frame.BottomRight("Draw")

    def ForgetAll(self):
        frame.TopLeft("Drop")
        frame.Top("Drop")
        frame.TopRight("Drop")
        frame.Left("Drop")
        frame.Middle("Drop")
        frame.Right("Drop")
        frame.BottomLeft("Drop")
        frame.Bottom("Drop")
        frame.BottomRight("Drop")


        TopLeftBoard.Cross("All", "Drop")
        TopLeftBoard.Nought("All", "Drop")
        
##        TopBoard.Cross("All", "Drop")
##        TopBoard.Nought("All", "Drop")
##        
##        TopRightBoard.Cross("All", "Drop")
##        TopRightBoard.Nought("All", "Drop")
##        
##        LeftBoard.Cross("All", "Drop")
##        LeftBoard.Nought("All", "Drop")
##        
##        MiddleBoard.Cross("All", "Drop")
##        MiddleBoard.Nought("All", "Drop")
##        
##        RightBoard.Cross("All", "Drop")
##        RightBoard.Nought("All", "Drop")
##        
##        BottomLeftBoard.Cross("All", "Drop")
##        BottomLeftBoard.Nought("All", "Drop")
##        
##        BottomBoard.Cross("All", "Drop")
##        BottomBoard.Nought("All", "Drop")
##        
##        BottomRightBoard.Cross("All", "Drop")
##        BottomRightBoard.Nought("All", "Drop")
    
    def Outer(self):
        self.Buffer_1.grid(column=0, row=0)
        
        self.Outer_Horizontal_1.grid(column=trueCenter["column"]-11, row=trueCenter["row"]-4, columnspan=7)
        self.Outer_Horizontal_2.grid(column=trueCenter["column"]-3, row=trueCenter["row"]-4, columnspan=7)
        self.Outer_Horizontal_3.grid(column=trueCenter["column"]+5, row=trueCenter["row"]-4, columnspan=7)
        self.Outer_Horizontal_4.grid(column=trueCenter["column"]-11, row=trueCenter["row"]+4, columnspan=7)
        self.Outer_Horizontal_5.grid(column=trueCenter["column"]-3, row=trueCenter["row"]+4, columnspan=7)
        self.Outer_Horizontal_6.grid(column=trueCenter["column"]+5, row=trueCenter["row"]+4, columnspan=7)

        self.Outer_Vertical_1.grid(column=trueCenter["column"]-4, row=trueCenter["row"]-11, rowspan=7)
        self.Outer_Vertical_2.grid(column=trueCenter["column"]-4, row=trueCenter["row"]-3, rowspan=7)
        self.Outer_Vertical_3.grid(column=trueCenter["column"]-4, row=trueCenter["row"]+5, rowspan=7)
        self.Outer_Vertical_4.grid(column=trueCenter["column"]+4, row=trueCenter["row"]-11, rowspan=7)
        self.Outer_Vertical_5.grid(column=trueCenter["column"]+4, row=trueCenter["row"]-3, rowspan=7)
        self.Outer_Vertical_6.grid(column=trueCenter["column"]+4, row=trueCenter["row"]+5, rowspan=7)

        self.Outer_Cross_1.grid(column=trueCenter["column"]-4, row=trueCenter["row"]-4)
        self.Outer_Cross_2.grid(column=trueCenter["column"]+4, row=trueCenter["row"]-4)
        self.Outer_Cross_3.grid(column=trueCenter["column"]-4, row=trueCenter["row"]+4)
        self.Outer_Cross_4.grid(column=trueCenter["column"]+4, row=trueCenter["row"]+4)

    def TopLeft(self, state="Draw"):
        center = {"column": trueCenter["column"]-8,
                  "row": trueCenter["row"]-8}

        if state=="Draw":
            self.TopLeft_Horizontal_1.grid(column=center["column"]-2, row=center["row"]-1)
            self.TopLeft_Horizontal_2.grid(column=center["column"], row=center["row"]-1)
            self.TopLeft_Horizontal_3.grid(column=center["column"]+2, row=center["row"]-1)
            self.TopLeft_Horizontal_4.grid(column=center["column"]-2, row=center["row"]+1)
            self.TopLeft_Horizontal_5.grid(column=center["column"], row=center["row"]+1)
            self.TopLeft_Horizontal_6.grid(column=center["column"]+2, row=center["row"]+1)

            self.TopLeft_Vertical_1.grid(column=center["column"]-1, row=center["row"]-2)
            self.TopLeft_Vertical_2.grid(column=center["column"]-1, row=center["row"])
            self.TopLeft_Vertical_3.grid(column=center["column"]-1, row=center["row"]+2)
            self.TopLeft_Vertical_4.grid(column=center["column"]+1, row=center["row"]-2)
            self.TopLeft_Vertical_5.grid(column=center["column"]+1, row=center["row"])
            self.TopLeft_Vertical_6.grid(column=center["column"]+1, row=center["row"]+2)

            self.TopLeft_Cross_1.grid(column=center["column"]-1, row=center["row"]-1)
            self.TopLeft_Cross_2.grid(column=center["column"]+1, row=center["row"]-1)
            self.TopLeft_Cross_3.grid(column=center["column"]-1, row=center["row"]+1)
            self.TopLeft_Cross_4.grid(column=center["column"]+1, row=center["row"]+1)

        elif state=="Drop":
            self.TopLeft_Horizontal_1.grid_remove()
            self.TopLeft_Horizontal_2.grid_remove()
            self.TopLeft_Horizontal_3.grid_remove()
            self.TopLeft_Horizontal_4.grid_remove()
            self.TopLeft_Horizontal_5.grid_remove()
            self.TopLeft_Horizontal_6.grid_remove()

            self.TopLeft_Vertical_1.grid_remove()
            self.TopLeft_Vertical_2.grid_remove()
            self.TopLeft_Vertical_3.grid_remove()
            self.TopLeft_Vertical_4.grid_remove()
            self.TopLeft_Vertical_5.grid_remove()
            self.TopLeft_Vertical_6.grid_remove()

            self.TopLeft_Cross_1.grid_remove()
            self.TopLeft_Cross_2.grid_remove()
            self.TopLeft_Cross_3.grid_remove()
            self.TopLeft_Cross_4.grid_remove()

    def Top(self, state="Draw"):
        center = {"column": trueCenter["column"],
                  "row": trueCenter["row"]-8}

        if state=="Draw":
            self.Top_Horizontal_1.grid(column=center["column"]-2, row=center["row"]-1)
            self.Top_Horizontal_2.grid(column=center["column"], row=center["row"]-1)
            self.Top_Horizontal_3.grid(column=center["column"]+2, row=center["row"]-1)
            self.Top_Horizontal_4.grid(column=center["column"]-2, row=center["row"]+1)
            self.Top_Horizontal_5.grid(column=center["column"], row=center["row"]+1)
            self.Top_Horizontal_6.grid(column=center["column"]+2, row=center["row"]+1)

            self.Top_Vertical_1.grid(column=center["column"]-1, row=center["row"]-2)
            self.Top_Vertical_2.grid(column=center["column"]-1, row=center["row"])
            self.Top_Vertical_3.grid(column=center["column"]-1, row=center["row"]+2)
            self.Top_Vertical_4.grid(column=center["column"]+1, row=center["row"]-2)
            self.Top_Vertical_5.grid(column=center["column"]+1, row=center["row"])
            self.Top_Vertical_6.grid(column=center["column"]+1, row=center["row"]+2)

            self.Top_Cross_1.grid(column=center["column"]-1, row=center["row"]-1)
            self.Top_Cross_2.grid(column=center["column"]+1, row=center["row"]-1)
            self.Top_Cross_3.grid(column=center["column"]-1, row=center["row"]+1)
            self.Top_Cross_4.grid(column=center["column"]+1, row=center["row"]+1)

        elif state=="Drop":
            self.Top_Horizontal_1.grid_remove()
            self.Top_Horizontal_2.grid_remove()
            self.Top_Horizontal_3.grid_remove()
            self.Top_Horizontal_4.grid_remove()
            self.Top_Horizontal_5.grid_remove()
            self.Top_Horizontal_6.grid_remove()

            self.Top_Vertical_1.grid_remove()
            self.Top_Vertical_2.grid_remove()
            self.Top_Vertical_3.grid_remove()
            self.Top_Vertical_4.grid_remove()
            self.Top_Vertical_5.grid_remove()
            self.Top_Vertical_6.grid_remove()

            self.Top_Cross_1.grid_remove()
            self.Top_Cross_2.grid_remove()
            self.Top_Cross_3.grid_remove()
            self.Top_Cross_4.grid_remove()

    def TopRight(self, state="Draw"):
        center = {"column": trueCenter["column"]+8,
                  "row": trueCenter["row"]-8}

        if state=="Draw":
            self.TopRight_Horizontal_1.grid(column=center["column"]-2, row=center["row"]-1)
            self.TopRight_Horizontal_2.grid(column=center["column"], row=center["row"]-1)
            self.TopRight_Horizontal_3.grid(column=center["column"]+2, row=center["row"]-1)
            self.TopRight_Horizontal_4.grid(column=center["column"]-2, row=center["row"]+1)
            self.TopRight_Horizontal_5.grid(column=center["column"], row=center["row"]+1)
            self.TopRight_Horizontal_6.grid(column=center["column"]+2, row=center["row"]+1)

            self.TopRight_Vertical_1.grid(column=center["column"]-1, row=center["row"]-2)
            self.TopRight_Vertical_2.grid(column=center["column"]-1, row=center["row"])
            self.TopRight_Vertical_3.grid(column=center["column"]-1, row=center["row"]+2)
            self.TopRight_Vertical_4.grid(column=center["column"]+1, row=center["row"]-2)
            self.TopRight_Vertical_5.grid(column=center["column"]+1, row=center["row"])
            self.TopRight_Vertical_6.grid(column=center["column"]+1, row=center["row"]+2)

            self.TopRight_Cross_1.grid(column=center["column"]-1, row=center["row"]-1)
            self.TopRight_Cross_2.grid(column=center["column"]+1, row=center["row"]-1)
            self.TopRight_Cross_3.grid(column=center["column"]-1, row=center["row"]+1)
            self.TopRight_Cross_4.grid(column=center["column"]+1, row=center["row"]+1)

        elif state=="Drop":
            self.TopRight_Horizontal_1.grid_remove()
            self.TopRight_Horizontal_2.grid_remove()
            self.TopRight_Horizontal_3.grid_remove()
            self.TopRight_Horizontal_4.grid_remove()
            self.TopRight_Horizontal_5.grid_remove()
            self.TopRight_Horizontal_6.grid_remove()

            self.TopRight_Vertical_1.grid_remove()
            self.TopRight_Vertical_2.grid_remove()
            self.TopRight_Vertical_3.grid_remove()
            self.TopRight_Vertical_4.grid_remove()
            self.TopRight_Vertical_5.grid_remove()
            self.TopRight_Vertical_6.grid_remove()

            self.TopRight_Cross_1.grid_remove()
            self.TopRight_Cross_2.grid_remove()
            self.TopRight_Cross_3.grid_remove()
            self.TopRight_Cross_4.grid_remove()

    def Left(self, state="Draw"):
        center = {"column": trueCenter["column"]-8,
                  "row": trueCenter["row"]}

        if state=="Draw":
            self.Left_Horizontal_1.grid(column=center["column"]-2, row=center["row"]-1)
            self.Left_Horizontal_2.grid(column=center["column"], row=center["row"]-1)
            self.Left_Horizontal_3.grid(column=center["column"]+2, row=center["row"]-1)
            self.Left_Horizontal_4.grid(column=center["column"]-2, row=center["row"]+1)
            self.Left_Horizontal_5.grid(column=center["column"], row=center["row"]+1)
            self.Left_Horizontal_6.grid(column=center["column"]+2, row=center["row"]+1)

            self.Left_Vertical_1.grid(column=center["column"]-1, row=center["row"]-2)
            self.Left_Vertical_2.grid(column=center["column"]-1, row=center["row"])
            self.Left_Vertical_3.grid(column=center["column"]-1, row=center["row"]+2)
            self.Left_Vertical_4.grid(column=center["column"]+1, row=center["row"]-2)
            self.Left_Vertical_5.grid(column=center["column"]+1, row=center["row"])
            self.Left_Vertical_6.grid(column=center["column"]+1, row=center["row"]+2)

            self.Left_Cross_1.grid(column=center["column"]-1, row=center["row"]-1)
            self.Left_Cross_2.grid(column=center["column"]+1, row=center["row"]-1)
            self.Left_Cross_3.grid(column=center["column"]-1, row=center["row"]+1)
            self.Left_Cross_4.grid(column=center["column"]+1, row=center["row"]+1)

        elif state=="Drop":
            self.Left_Horizontal_1.grid_remove()
            self.Left_Horizontal_2.grid_remove()
            self.Left_Horizontal_3.grid_remove()
            self.Left_Horizontal_4.grid_remove()
            self.Left_Horizontal_5.grid_remove()
            self.Left_Horizontal_6.grid_remove()

            self.Left_Vertical_1.grid_remove()
            self.Left_Vertical_2.grid_remove()
            self.Left_Vertical_3.grid_remove()
            self.Left_Vertical_4.grid_remove()
            self.Left_Vertical_5.grid_remove()
            self.Left_Vertical_6.grid_remove()

            self.Left_Cross_1.grid_remove()
            self.Left_Cross_2.grid_remove()
            self.Left_Cross_3.grid_remove()
            self.Left_Cross_4.grid_remove()

    def Middle(self, state="Draw"):
        center = {"column": trueCenter["column"],
                  "row": trueCenter["row"]}

        if state=="Draw":
            self.Middle_Horizontal_1.grid(column=center["column"]-2, row=center["row"]-1)
            self.Middle_Horizontal_2.grid(column=center["column"], row=center["row"]-1)
            self.Middle_Horizontal_3.grid(column=center["column"]+2, row=center["row"]-1)
            self.Middle_Horizontal_4.grid(column=center["column"]-2, row=center["row"]+1)
            self.Middle_Horizontal_5.grid(column=center["column"], row=center["row"]+1)
            self.Middle_Horizontal_6.grid(column=center["column"]+2, row=center["row"]+1)

            self.Middle_Vertical_1.grid(column=center["column"]-1, row=center["row"]-2)
            self.Middle_Vertical_2.grid(column=center["column"]-1, row=center["row"])
            self.Middle_Vertical_3.grid(column=center["column"]-1, row=center["row"]+2)
            self.Middle_Vertical_4.grid(column=center["column"]+1, row=center["row"]-2)
            self.Middle_Vertical_5.grid(column=center["column"]+1, row=center["row"])
            self.Middle_Vertical_6.grid(column=center["column"]+1, row=center["row"]+2)

            self.Middle_Cross_1.grid(column=center["column"]-1, row=center["row"]-1)
            self.Middle_Cross_2.grid(column=center["column"]+1, row=center["row"]-1)
            self.Middle_Cross_3.grid(column=center["column"]-1, row=center["row"]+1)
            self.Middle_Cross_4.grid(column=center["column"]+1, row=center["row"]+1)

        elif state=="Drop":
            self.Middle_Horizontal_1.grid_remove()
            self.Middle_Horizontal_2.grid_remove()
            self.Middle_Horizontal_3.grid_remove()
            self.Middle_Horizontal_4.grid_remove()
            self.Middle_Horizontal_5.grid_remove()
            self.Middle_Horizontal_6.grid_remove()

            self.Middle_Vertical_1.grid_remove()
            self.Middle_Vertical_2.grid_remove()
            self.Middle_Vertical_3.grid_remove()
            self.Middle_Vertical_4.grid_remove()
            self.Middle_Vertical_5.grid_remove()
            self.Middle_Vertical_6.grid_remove()

            self.Middle_Cross_1.grid_remove()
            self.Middle_Cross_2.grid_remove()
            self.Middle_Cross_3.grid_remove()
            self.Middle_Cross_4.grid_remove()

    def Right(self, state="Draw"):
        center = {"column": trueCenter["column"]+8,
                  "row": trueCenter["row"]}

        if state=="Draw":
            self.Right_Horizontal_1.grid(column=center["column"]-2, row=center["row"]-1)
            self.Right_Horizontal_2.grid(column=center["column"], row=center["row"]-1)
            self.Right_Horizontal_3.grid(column=center["column"]+2, row=center["row"]-1)
            self.Right_Horizontal_4.grid(column=center["column"]-2, row=center["row"]+1)
            self.Right_Horizontal_5.grid(column=center["column"], row=center["row"]+1)
            self.Right_Horizontal_6.grid(column=center["column"]+2, row=center["row"]+1)

            self.Right_Vertical_1.grid(column=center["column"]-1, row=center["row"]-2)
            self.Right_Vertical_2.grid(column=center["column"]-1, row=center["row"])
            self.Right_Vertical_3.grid(column=center["column"]-1, row=center["row"]+2)
            self.Right_Vertical_4.grid(column=center["column"]+1, row=center["row"]-2)
            self.Right_Vertical_5.grid(column=center["column"]+1, row=center["row"])
            self.Right_Vertical_6.grid(column=center["column"]+1, row=center["row"]+2)

            self.Right_Cross_1.grid(column=center["column"]-1, row=center["row"]-1)
            self.Right_Cross_2.grid(column=center["column"]+1, row=center["row"]-1)
            self.Right_Cross_3.grid(column=center["column"]-1, row=center["row"]+1)
            self.Right_Cross_4.grid(column=center["column"]+1, row=center["row"]+1)

        elif state=="Drop":
            self.Right_Horizontal_1.grid_remove()
            self.Right_Horizontal_2.grid_remove()
            self.Right_Horizontal_3.grid_remove()
            self.Right_Horizontal_4.grid_remove()
            self.Right_Horizontal_5.grid_remove()
            self.Right_Horizontal_6.grid_remove()

            self.Right_Vertical_1.grid_remove()
            self.Right_Vertical_2.grid_remove()
            self.Right_Vertical_3.grid_remove()
            self.Right_Vertical_4.grid_remove()
            self.Right_Vertical_5.grid_remove()
            self.Right_Vertical_6.grid_remove()

            self.Right_Cross_1.grid_remove()
            self.Right_Cross_2.grid_remove()
            self.Right_Cross_3.grid_remove()
            self.Right_Cross_4.grid_remove()

    def BottomLeft(self, state="Draw"):
        center = {"column": trueCenter["column"]-8,
                  "row": trueCenter["row"]+8}

        if state=="Draw":
            self.BottomLeft_Horizontal_1.grid(column=center["column"]-2, row=center["row"]-1)
            self.BottomLeft_Horizontal_2.grid(column=center["column"], row=center["row"]-1)
            self.BottomLeft_Horizontal_3.grid(column=center["column"]+2, row=center["row"]-1)
            self.BottomLeft_Horizontal_4.grid(column=center["column"]-2, row=center["row"]+1)
            self.BottomLeft_Horizontal_5.grid(column=center["column"], row=center["row"]+1)
            self.BottomLeft_Horizontal_6.grid(column=center["column"]+2, row=center["row"]+1)

            self.BottomLeft_Vertical_1.grid(column=center["column"]-1, row=center["row"]-2)
            self.BottomLeft_Vertical_2.grid(column=center["column"]-1, row=center["row"])
            self.BottomLeft_Vertical_3.grid(column=center["column"]-1, row=center["row"]+2)
            self.BottomLeft_Vertical_4.grid(column=center["column"]+1, row=center["row"]-2)
            self.BottomLeft_Vertical_5.grid(column=center["column"]+1, row=center["row"])
            self.BottomLeft_Vertical_6.grid(column=center["column"]+1, row=center["row"]+2)

            self.BottomLeft_Cross_1.grid(column=center["column"]-1, row=center["row"]-1)
            self.BottomLeft_Cross_2.grid(column=center["column"]+1, row=center["row"]-1)
            self.BottomLeft_Cross_3.grid(column=center["column"]-1, row=center["row"]+1)
            self.BottomLeft_Cross_4.grid(column=center["column"]+1, row=center["row"]+1)

        elif state=="Drop":
            self.BottomLeft_Horizontal_1.grid_remove()
            self.BottomLeft_Horizontal_2.grid_remove()
            self.BottomLeft_Horizontal_3.grid_remove()
            self.BottomLeft_Horizontal_4.grid_remove()
            self.BottomLeft_Horizontal_5.grid_remove()
            self.BottomLeft_Horizontal_6.grid_remove()

            self.BottomLeft_Vertical_1.grid_remove()
            self.BottomLeft_Vertical_2.grid_remove()
            self.BottomLeft_Vertical_3.grid_remove()
            self.BottomLeft_Vertical_4.grid_remove()
            self.BottomLeft_Vertical_5.grid_remove()
            self.BottomLeft_Vertical_6.grid_remove()

            self.BottomLeft_Cross_1.grid_remove()
            self.BottomLeft_Cross_2.grid_remove()
            self.BottomLeft_Cross_3.grid_remove()
            self.BottomLeft_Cross_4.grid_remove()

    def Bottom(self, state="Draw"):
        center = {"column": trueCenter["column"],
                  "row": trueCenter["row"]+8}

        if state=="Draw":
            self.Bottom_Horizontal_1.grid(column=center["column"]-2, row=center["row"]-1)
            self.Bottom_Horizontal_2.grid(column=center["column"], row=center["row"]-1)
            self.Bottom_Horizontal_3.grid(column=center["column"]+2, row=center["row"]-1)
            self.Bottom_Horizontal_4.grid(column=center["column"]-2, row=center["row"]+1)
            self.Bottom_Horizontal_5.grid(column=center["column"], row=center["row"]+1)
            self.Bottom_Horizontal_6.grid(column=center["column"]+2, row=center["row"]+1)

            self.Bottom_Vertical_1.grid(column=center["column"]-1, row=center["row"]-2)
            self.Bottom_Vertical_2.grid(column=center["column"]-1, row=center["row"])
            self.Bottom_Vertical_3.grid(column=center["column"]-1, row=center["row"]+2)
            self.Bottom_Vertical_4.grid(column=center["column"]+1, row=center["row"]-2)
            self.Bottom_Vertical_5.grid(column=center["column"]+1, row=center["row"])
            self.Bottom_Vertical_6.grid(column=center["column"]+1, row=center["row"]+2)

            self.Bottom_Cross_1.grid(column=center["column"]-1, row=center["row"]-1)
            self.Bottom_Cross_2.grid(column=center["column"]+1, row=center["row"]-1)
            self.Bottom_Cross_3.grid(column=center["column"]-1, row=center["row"]+1)
            self.Bottom_Cross_4.grid(column=center["column"]+1, row=center["row"]+1)

        elif state=="Drop":
            self.Bottom_Horizontal_1.grid_remove()
            self.Bottom_Horizontal_2.grid_remove()
            self.Bottom_Horizontal_3.grid_remove()
            self.Bottom_Horizontal_4.grid_remove()
            self.Bottom_Horizontal_5.grid_remove()
            self.Bottom_Horizontal_6.grid_remove()

            self.Bottom_Vertical_1.grid_remove()
            self.Bottom_Vertical_2.grid_remove()
            self.Bottom_Vertical_3.grid_remove()
            self.Bottom_Vertical_4.grid_remove()
            self.Bottom_Vertical_5.grid_remove()
            self.Bottom_Vertical_6.grid_remove()

            self.Bottom_Cross_1.grid_remove()
            self.Bottom_Cross_2.grid_remove()
            self.Bottom_Cross_3.grid_remove()
            self.Bottom_Cross_4.grid_remove()

    def BottomRight(self, state="Draw"):
        center = {"column": trueCenter["column"]+8,
                  "row": trueCenter["row"]+8}

        if state=="Draw":
            self.BottomRight_Horizontal_1.grid(column=center["column"]-2, row=center["row"]-1)
            self.BottomRight_Horizontal_2.grid(column=center["column"], row=center["row"]-1)
            self.BottomRight_Horizontal_3.grid(column=center["column"]+2, row=center["row"]-1)
            self.BottomRight_Horizontal_4.grid(column=center["column"]-2, row=center["row"]+1)
            self.BottomRight_Horizontal_5.grid(column=center["column"], row=center["row"]+1)
            self.BottomRight_Horizontal_6.grid(column=center["column"]+2, row=center["row"]+1)

            self.BottomRight_Vertical_1.grid(column=center["column"]-1, row=center["row"]-2)
            self.BottomRight_Vertical_2.grid(column=center["column"]-1, row=center["row"])
            self.BottomRight_Vertical_3.grid(column=center["column"]-1, row=center["row"]+2)
            self.BottomRight_Vertical_4.grid(column=center["column"]+1, row=center["row"]-2)
            self.BottomRight_Vertical_5.grid(column=center["column"]+1, row=center["row"])
            self.BottomRight_Vertical_6.grid(column=center["column"]+1, row=center["row"]+2)

            self.BottomRight_Cross_1.grid(column=center["column"]-1, row=center["row"]-1)
            self.BottomRight_Cross_2.grid(column=center["column"]+1, row=center["row"]-1)
            self.BottomRight_Cross_3.grid(column=center["column"]-1, row=center["row"]+1)
            self.BottomRight_Cross_4.grid(column=center["column"]+1, row=center["row"]+1)

        elif state=="Drop":
            self.BottomRight_Horizontal_1.grid_remove()
            self.BottomRight_Horizontal_2.grid_remove()
            self.BottomRight_Horizontal_3.grid_remove()
            self.BottomRight_Horizontal_4.grid_remove()
            self.BottomRight_Horizontal_5.grid_remove()
            self.BottomRight_Horizontal_6.grid_remove()

            self.BottomRight_Vertical_1.grid_remove()
            self.BottomRight_Vertical_2.grid_remove()
            self.BottomRight_Vertical_3.grid_remove()
            self.BottomRight_Vertical_4.grid_remove()
            self.BottomRight_Vertical_5.grid_remove()
            self.BottomRight_Vertical_6.grid_remove()

            self.BottomRight_Cross_1.grid_remove()
            self.BottomRight_Cross_2.grid_remove()
            self.BottomRight_Cross_3.grid_remove()
            self.BottomRight_Cross_4.grid_remove()
        
class topleftboard(PropertyDefine):    
    def Cross(self, place=None, state="Draw"):
        center = {"column": trueCenter["column"]-8,
                  "row": trueCenter["row"]-8}
        
        global TopLeftBoard_TopLeftFilled, TopLeftBoard_TopFilled, TopLeftBoard_TopRightFilled, TopLeftBoard_LeftFilled, TopLeftBoard_MiddleFilled, TopLeftBoard_RightFilled, TopLeftBoard_BottomLeftFilled, TopLeftBoard_BottomFilled, TopLeftBoard_BottomRightFilled
        global TopLeftBoard_TopLeftCross, TopLeftBoard_TopCross, TopLeftBoard_TopRightCross, TopLeftBoard_LeftCross, TopLeftBoard_MiddleCross, TopLeftBoard_RightCross, TopLeftBoard_BottomLeftCross, TopLeftBoard_BottomCross, TopLeftBoard_BottomRightCross

        if state=="Draw":
            if place=="TopLeft":
                self.Cross_TopLeft.grid(column=(center["column"]-2), row=(center["row"]-2))
                TopLeftBoard_TopLeftFilled = TopLeftBoard_TopLeftCross = True
            elif place=="Top":
                self.Cross_Top.grid(column=center["column"], row=center["row"]-2)
                TopLeftBoard_TopFilled = TopLeftBoard_TopCross = True
            elif place=="TopRight":
                self.Cross_TopRight.grid(column=center["column"]+2, row=center["row"]-2)
                TopLeftBoard_TopRightFilled = TopLeftBoard_TopRightCross = True
            elif place=="Left":
                self.Cross_Left.grid(column=center["column"]-2, row=center["row"])
                TopLeftBoard_LeftFilled = TopLeftBoard_LeftCross = True
            elif place=="Middle":
                self.Cross_Middle.grid(column=center["column"], row=center["row"])
                TopLeftBoard_MiddleFilled = TopLeftBoard_MiddleCross = True
            elif place=="Right":
                self.Cross_Right.grid(column=center["column"]+2, row=center["row"])
                TopLeftBoard_RightFilled = TopLeftBoard_RightCross = True
            elif place=="BottomLeft":
                self.Cross_BottomLeft.grid(column=center["column"]-2, row=center["row"]+2)
                TopLeftBoard_BottomLeftFilled = TopLeftBoard_BottomLeftCross = True
            elif place=="Bottom":
                self.Cross_Bottom.grid(column=center["column"], row=center["row"]+2)
                TopLeftBoard_BottomFilled = TopLeftBoard_BottomCross = True
            elif place=="BottomRight":
                self.Cross_BottomRight.grid(column=center["column"]+2, row=center["row"]+2)
                TopLeftBoard_BottomRightFilled = TopLeftBoard_BottomRightCross = True
            else:
                raise Exception("You need to specify where to place the piece")

        elif state=="Drop":
            if place=="All":
                TopLeftBoard_TopLeftFilled = TopLeftBoard_TopFilled = TopLeftBoard_TopRightFilled = TopLeftBoard_LeftFilled = TopLeftBoard_MiddleFilled = TopLeftBoard_RightFilled = TopLeftBoard_BottomLeftFilled = TopLeftBoard_BottomFilled = TopLeftBoard_BottomRightFilled = False
                TopLeftBoard_TopLeftCross = TopLeftBoard_TopCross = TopLeftBoard_TopRightCross = TopLeftBoard_LeftCross = TopLeftBoard_MiddleCross = TopLeftBoard_RightCross = TopLeftBoard_BottomLeftCross = TopLeftBoard_BottomCross = TopLeftBoard_BottomRightCross = False

                self.Cross_TopLeft.grid_remove()
                self.Cross_Top.grid_remove()
                self.Cross_TopRight.grid_remove()
                self.Cross_Left.grid_remove()
                self.Cross_Middle.grid_remove()
                self.Cross_Right.grid_remove()
                self.Cross_BottomLeft.grid_remove()
                self.Cross_Bottom.grid_remove()
                self.Cross_BottomRight.grid_remove()
                
            elif place=="TopLeft":
                self.Cross_TopLeft.grid_remove()
                TopLeftBoard_TopLeftFilled = TopLeftBoard_TopLeftCross = False
            elif place=="Top":
                self.Cross_Top.grid_remove()
                TopLeftBoard_TopFilled = TopLeftBoard_TopCross = False
            elif place=="TopRight":
                self.Cross_TopRight.grid_remove()
                TopLeftBoard_TopRightFilled = TopLeftBoard_TopRightCross = False
            elif place=="Left":
                self.Cross_Left.grid_remove()
                TopLeftBoard_LeftFilled = TopLeftBoard_LeftCross = False
            elif place=="Middle":
                self.Cross_Middle.grid_remove()
                TopLeftBoard_MiddleFilled = TopLeftBoard_MiddleCross = False
            elif place=="Right":
                self.Cross_Right.grid_remove()
                TopLeftBoard_RightFilled = TopLeftBoard_RightCross = False
            elif place=="BottomLeft":
                self.Cross_BottomLeft.grid_remove()
                TopLeftBoard_BottomLeftFilled = TopLeftBoard_BottomLeftCross = False
            elif place=="Bottom":
                self.Cross_Bottom.grid_remove()
                TopLeftBoard_BottomFilled = TopLeftBoard_BottomCross = False
            elif place=="BottomRight":
                self.Cross_BottomRight.grid_remove()
                TopLeftBoard_BottomRightFilled = TopLeftBoard_BottomRightCross = False
            else:
                raise Exception("You need to specify which piece to drop")
            

    def Nought(self, place=None, state="Draw"):
        center = {"column": trueCenter["column"]-8,
                  "row": trueCenter["row"]-8}
        
        global TopLeftBoard_TopLeftFilled, TopLeftBoard_TopFilled, TopLeftBoard_TopRightFilled, TopLeftBoard_LeftFilled, TopLeftBoard_MiddleFilled, TopLeftBoard_RightFilled, TopLeftBoard_BottomLeftFilled, TopLeftBoard_BottomFilled, TopLeftBoard_BottomRightFilled
        global TopLeftBoard_TopLeftNought, TopLeftBoard_TopNought, TopLeftBoard_TopRightNought, TopLeftBoard_LeftNought, TopLeftBoard_MiddleNought, TopLeftBoard_RightNought, TopLeftBoard_BottomLeftNought, TopLeftBoard_BottomNought, TopLeftBoard_BottomRightNought

        if state=="Draw":
            if place=="TopLeft":
                self.Nought_TopLeft.grid(column=1, row=3)
                TopLeftBoard_TopLeftFilled = TopLeftBoard_TopLeftNought = True
            elif place=="Top":
                self.Nought_Top.grid(column=3, row=3)
                TopLeftBoard_TopFilled = TopLeftBoard_TopNought = True
            elif place=="TopRight":
                self.Nought_TopRight.grid(column=5, row=3)
                TopLeftBoard_TopRightFilled = TopLeftBoard_TopRightNought = True
            elif place=="Left":
                self.Nought_Left.grid(column=1, row=5)
                TopLeftBoard_LeftFilled = TopLeftBoard_LeftNought = True
            elif place=="Middle":
                self.Nought_Middle.grid(column=3, row=5)
                TopLeftBoard_MiddleFilled = TopLeftBoard_MiddleNought = True
            elif place=="Right":
                self.Nought_Right.grid(column=5, row=5)
                TopLeftBoard_RightFilled = TopLeftBoard_RightNought = True
            elif place=="BottomLeft":
                self.Nought_BottomLeft.grid(column=1, row=7)
                TopLeftBoard_BottomLeftFilled = TopLeftBoard_BottomLeftNought = True
            elif place=="Bottom":
                self.Nought_Bottom.grid(column=3, row=7)
                TopLeftBoard_BottomFilled = TopLeftBoard_BottomNought = True
            elif place=="BottomRight":
                self.Nought_BottomRight.grid(column=5, row=7)
                TopLeftBoard_BottomRightFilled = TopLeftBoard_BottomRightNought = True
            else:
                raise Exception("You need to specify where to place the piece")

        elif state=="Drop":
            if place=="All":
                TopLeftBoard_TopLeftFilled = TopLeftBoard_TopFilled = TopLeftBoard_TopRightFilled = TopLeftBoard_LeftFilled = TopLeftBoard_MiddleFilled = TopLeftBoard_RightFilled = TopLeftBoard_BottomLeftFilled = TopLeftBoard_BottomFilled = TopLeftBoard_BottomRightFilled = False
                TopLeftBoard_TopLeftNought = TopLeftBoard_TopNought = TopLeftBoard_TopRightNought = TopLeftBoard_LeftNought = TopLeftBoard_MiddleNought = TopLeftBoard_RightNought = TopLeftBoard_BottomLeftNought = TopLeftBoard_BottomNought = TopLeftBoard_BottomRightNought = False

                self.Nought_TopLeft.grid_remove()
                self.Nought_Top.grid_remove()
                self.Nought_TopRight.grid_remove()
                self.Nought_Left.grid_remove()
                self.Nought_Middle.grid_remove()
                self.Nought_Right.grid_remove()
                self.Nought_BottomLeft.grid_remove()
                self.Nought_Bottom.grid_remove()
                self.Nought_BottomRight.grid_remove()
                
            elif place=="TopLeft":
                self.Nought_TopLeft.grid_remove()
                TopLeftBoard_TopLeftFilled = TopLeftBoard_TopLeftNought = False
            elif place=="Top":
                self.Nought_Top.grid_remove()
                TopLeftBoard_TopFilled = TopLeftBoard_TopNought = False
            elif place=="TopRight":
                self.Nought_TopRight.grid_remove()
                TopLeftBoard_TopRightFilled = TopLeftBoard_TopRightNought = False
            elif place=="Left":
                self.Nought_Left.grid_remove()
                TopLeftBoard_LeftFilled = TopLeftBoard_LeftNought = False
            elif place=="Middle":
                self.Nought_Middle.grid_remove()
                TopLeftBoard_MiddleFilled = TopLeftBoard_MiddleNought = False
            elif place=="Right":
                self.Nought_Right.grid_remove()
                TopLeftBoard_RightFilled = TopLeftBoard_RightNought = False
            elif place=="BottomLeft":
                self.Nought_BottomLeft.grid_remove()
                TopLeftBoard_BottomLeftFilled = TopLeftBoard_BottomLeftNought = False
            elif place=="Bottom":
                self.Nought_Bottom.grid_remove()
                TopLeftBoard_BottomFilled = TopLeftBoard_BottomNought = False
            elif place=="BottomRight":
                self.Nought_BottomRight.grid_remove()
                TopLeftBoard_BottomRightFilled = TopLeftBoard_BottomRightNought = False
            else:
                raise Exception("You need to specify which piece to drop")

def reset():
    #-----TOP-LEFT-BOARD-----
    global TopLeftBoard_TopLeftFilled, TopLeftBoard_TopFilled, TopLeftBoard_TopRightFilled, TopLeftBoard_LeftFilled, TopLeftBoard_MiddleFilled, TopLeftBoard_RightFilled, TopLeftBoard_BottomLeftFilled, TopLeftBoard_BottomFilled, TopLeftBoard_BottomRightFilled
    global TopLeftBoard_TopLeftCross, TopLeftBoard_TopCross, TopLeftBoard_TopRightCross, TopLeftBoard_LeftCross, TopLeftBoard_MiddleCross, TopLeftBoard_RightCross, TopLeftBoard_BottomLeftCross, TopLeftBoard_BottomCross, TopLeftBoard_BottomRightCross
    global TopLeftBoard_TopLeftNought, TopLeftBoard_TopNought, TopLeftBoard_TopRightNought, TopLeftBoard_LeftNought, TopLeftBoard_MiddleNought, TopLeftBoard_RightNought, TopLeftBoard_BottomLeftNought, TopLeftBoard_BottomNought, TopLeftBoard_BottomRightNought

    TopLeftBoard_TopLeftFilled = TopLeftBoard_TopFilled = TopLeftBoard_TopRightFilled = TopLeftBoard_LeftFilled = TopLeftBoard_MiddleFilled = TopLeftBoard_RightFilled = TopLeftBoard_BottomLeftFilled = TopLeftBoard_BottomFilled = TopLeftBoard_BottomRightFilled = False
    TopLeftBoard_TopLeftCross = TopLeftBoard_TopCross = TopLeftBoard_TopRightCross = TopLeftBoard_LeftCross = TopLeftBoard_MiddleCross = TopLeftBoard_RightCross = TopLeftBoard_BottomLeftCross = TopLeftBoard_BottomCross = TopLeftBoard_BottomRightCross = False
    TopLeftBoard_TopLeftNought = TopLeftBoard_TopNought = TopLeftBoard_TopRightNought = TopLeftBoard_LeftNought = TopLeftBoard_MiddleNought = TopLeftBoard_RightNought = TopLeftBoard_BottomLeftNought = TopLeftBoard_BottomNought = TopLeftBoard_BottomRightNought = False

    #-----TOP-BOARD-----
    global TopBoard_TopLeftFilled, TopBoard_TopFilled, TopBoard_TopRightFilled, TopBoard_LeftFilled, TopBoard_MiddleFilled, TopBoard_RightFilled, TopBoard_BottomLeftFilled, TopBoard_BottomFilled, TopBoard_BottomRightFilled
    global TopBoard_TopLeftCross, TopBoard_TopCross, TopBoard_TopRightCross, TopBoard_LeftCross, TopBoard_MiddleCross, TopBoard_RightCross, TopBoard_BottomLeftCross, TopBoard_BottomCross, TopBoard_BottomRightCross
    global TopBoard_TopLeftNought, TopBoard_TopNought, TopBoard_TopRightNought, TopBoard_LeftNought, TopBoard_MiddleNought, TopBoard_RightNought, TopBoard_BottomLeftNought, TopBoard_BottomNought, TopBoard_BottomRightNought

    TopBoard_TopLeftFilled = TopBoard_TopFilled = TopBoard_TopRightFilled = TopBoard_LeftFilled = TopBoard_MiddleFilled = TopBoard_RightFilled = TopBoard_BottomLeftFilled = TopBoard_BottomFilled = TopBoard_BottomRightFilled = False
    TopBoard_TopLeftCross = TopBoard_TopCross = TopBoard_TopRightCross = TopBoard_LeftCross = TopBoard_MiddleCross = TopBoard_RightCross = TopBoard_BottomLeftCross = TopBoard_BottomCross = TopBoard_BottomRightCross = False
    TopBoard_TopLeftNought = TopBoard_TopNought = TopBoard_TopRightNought = TopBoard_LeftNought = TopBoard_MiddleNought = TopBoard_RightNought = TopBoard_BottomLeftNought = TopBoard_BottomNought = TopBoard_BottomRightNought = False
    
    #-----TOP-RIGHT-BOARD-----
    global TopRightBoard_TopLeftFilled, TopRightBoard_TopFilled, TopRightBoard_TopRightFilled, TopRightBoard_LeftFilled, TopRightBoard_MiddleFilled, TopRightBoard_RightFilled, TopRightBoard_BottomLeftFilled, TopRightBoard_BottomFilled, TopRightBoard_BottomRightFilled
    global TopRightBoard_TopLeftCross, TopRightBoard_TopCross, TopRightBoard_TopRightCross, TopRightBoard_LeftCross, TopRightBoard_MiddleCross, TopRightBoard_RightCross, TopRightBoard_BottomLeftCross, TopRightBoard_BottomCross, TopRightBoard_BottomRightCross
    global TopRightBoard_TopLeftNought, TopRightBoard_TopNought, TopRightBoard_TopRightNought, TopRightBoard_LeftNought, TopRightBoard_MiddleNought, TopRightBoard_RightNought, TopRightBoard_BottomLeftNought, TopRightBoard_BottomNought, TopRightBoard_BottomRightNought

    TopRightBoard_TopLeftFilled = TopRightBoard_TopFilled = TopRightBoard_TopRightFilled = TopRightBoard_LeftFilled = TopRightBoard_MiddleFilled = TopRightBoard_RightFilled = TopRightBoard_BottomLeftFilled = TopRightBoard_BottomFilled = TopRightBoard_BottomRightFilled = False
    TopRightBoard_TopLeftCross = TopRightBoard_TopCross = TopRightBoard_TopRightCross = TopRightBoard_LeftCross = TopRightBoard_MiddleCross = TopRightBoard_RightCross = TopRightBoard_BottomLeftCross = TopRightBoard_BottomCross = TopRightBoard_BottomRightCross = False
    TopRightBoard_TopLeftNought = TopRightBoard_TopNought = TopRightBoard_TopRightNought = TopRightBoard_LeftNought = TopRightBoard_MiddleNought = TopRightBoard_RightNought = TopRightBoard_BottomLeftNought = TopRightBoard_BottomNought = TopRightBoard_BottomRightNought = False
    
    #-----LEFT-BOARD-----
    global LeftBoard_TopLeftFilled, LeftBoard_TopFilled, LeftBoard_TopRightFilled, LeftBoard_LeftFilled, LeftBoard_MiddleFilled, LeftBoard_RightFilled, LeftBoard_BottomLeftFilled, LeftBoard_BottomFilled, LeftBoard_BottomRightFilled
    global LeftBoard_TopLeftCross, LeftBoard_TopCross, LeftBoard_TopRightCross, LeftBoard_LeftCross, LeftBoard_MiddleCross, LeftBoard_RightCross, LeftBoard_BottomLeftCross, LeftBoard_BottomCross, LeftBoard_BottomRightCross
    global LeftBoard_TopLeftNought, LeftBoard_TopNought, LeftBoard_TopRightNought, LeftBoard_LeftNought, LeftBoard_MiddleNought, LeftBoard_RightNought, LeftBoard_BottomLeftNought, LeftBoard_BottomNought, LeftBoard_BottomRightNought

    LeftBoard_TopLeftFilled = LeftBoard_TopFilled = LeftBoard_TopRightFilled = LeftBoard_LeftFilled = LeftBoard_MiddleFilled = LeftBoard_RightFilled = LeftBoard_BottomLeftFilled = LeftBoard_BottomFilled = LeftBoard_BottomRightFilled = False
    LeftBoard_TopLeftCross = LeftBoard_TopCross = LeftBoard_TopRightCross = LeftBoard_LeftCross = LeftBoard_MiddleCross = LeftBoard_RightCross = LeftBoard_BottomLeftCross = LeftBoard_BottomCross = LeftBoard_BottomRightCross = False
    LeftBoard_TopLeftNought = LeftBoard_TopNought = LeftBoard_TopRightNought = LeftBoard_LeftNought = LeftBoard_MiddleNought = LeftBoard_RightNought = LeftBoard_BottomLeftNought = LeftBoard_BottomNought = LeftBoard_BottomRightNought = False
    
    #-----MIDDLE-BOARD-----
    global MiddleBoard_TopLeftFilled, MiddleBoard_TopFilled, MiddleBoard_TopRightFilled, MiddleBoard_LeftFilled, MiddleBoard_MiddleFilled, MiddleBoard_RightFilled, MiddleBoard_BottomLeftFilled, MiddleBoard_BottomFilled, MiddleBoard_BottomRightFilled
    global MiddleBoard_TopLeftCross, MiddleBoard_TopCross, MiddleBoard_TopRightCross, MiddleBoard_LeftCross, MiddleBoard_MiddleCross, MiddleBoard_RightCross, MiddleBoard_BottomLeftCross, MiddleBoard_BottomCross, MiddleBoard_BottomRightCross
    global MiddleBoard_TopLeftNought, MiddleBoard_TopNought, MiddleBoard_TopRightNought, MiddleBoard_LeftNought, MiddleBoard_MiddleNought, MiddleBoard_RightNought, MiddleBoard_BottomLeftNought, MiddleBoard_BottomNought, MiddleBoard_BottomRightNought

    MiddleBoard_TopLeftFilled = MiddleBoard_TopFilled = MiddleBoard_TopRightFilled = MiddleBoard_LeftFilled = MiddleBoard_MiddleFilled = MiddleBoard_RightFilled = MiddleBoard_BottomLeftFilled = MiddleBoard_BottomFilled = MiddleBoard_BottomRightFilled = False
    MiddleBoard_TopLeftCross = MiddleBoard_TopCross = MiddleBoard_TopRightCross = MiddleBoard_LeftCross = MiddleBoard_MiddleCross = MiddleBoard_RightCross = MiddleBoard_BottomLeftCross = MiddleBoard_BottomCross = MiddleBoard_BottomRightCross = False
    MiddleBoard_TopLeftNought = MiddleBoard_TopNought = MiddleBoard_TopRightNought = MiddleBoard_LeftNought = MiddleBoard_MiddleNought = MiddleBoard_RightNought = MiddleBoard_BottomLeftNought = MiddleBoard_BottomNought = MiddleBoard_BottomRightNought = False
    
    #-----RIGHT-BOARD-----
    global RightBoard_TopLeftFilled, RightBoard_TopFilled, RightBoard_TopRightFilled, RightBoard_LeftFilled, RightBoard_MiddleFilled, RightBoard_RightFilled, RightBoard_BottomLeftFilled, RightBoard_BottomFilled, RightBoard_BottomRightFilled
    global RightBoard_TopLeftCross, RightBoard_TopCross, RightBoard_TopRightCross, RightBoard_LeftCross, RightBoard_MiddleCross, RightBoard_RightCross, RightBoard_BottomLeftCross, RightBoard_BottomCross, RightBoard_BottomRightCross
    global RightBoard_TopLeftNought, RightBoard_TopNought, RightBoard_TopRightNought, RightBoard_LeftNought, RightBoard_MiddleNought, RightBoard_RightNought, RightBoard_BottomLeftNought, RightBoard_BottomNought, RightBoard_BottomRightNought

    RightBoard_TopLeftFilled = RightBoard_TopFilled = RightBoard_TopRightFilled = RightBoard_LeftFilled = RightBoard_MiddleFilled = RightBoard_RightFilled = RightBoard_BottomLeftFilled = RightBoard_BottomFilled = RightBoard_BottomRightFilled = False
    RightBoard_TopLeftCross = RightBoard_TopCross = RightBoard_TopRightCross = RightBoard_LeftCross = RightBoard_MiddleCross = RightBoard_RightCross = RightBoard_BottomLeftCross = RightBoard_BottomCross = RightBoard_BottomRightCross = False
    RightBoard_TopLeftNought = RightBoard_TopNought = RightBoard_TopRightNought = RightBoard_LeftNought = RightBoard_MiddleNought = RightBoard_RightNought = RightBoard_BottomLeftNought = RightBoard_BottomNought = RightBoard_BottomRightNought = False
    
    #-----BOTTOM-LEFT-BOARD-----
    global BottomLeftBoard_TopLeftFilled, BottomLeftBoard_TopFilled, BottomLeftBoard_TopRightFilled, BottomLeftBoard_LeftFilled, BottomLeftBoard_MiddleFilled, BottomLeftBoard_RightFilled, BottomLeftBoard_BottomLeftFilled, BottomLeftBoard_BottomFilled, BottomLeftBoard_BottomRightFilled
    global BottomLeftBoard_TopLeftCross, BottomLeftBoard_TopCross, BottomLeftBoard_TopRightCross, BottomLeftBoard_LeftCross, BottomLeftBoard_MiddleCross, BottomLeftBoard_RightCross, BottomLeftBoard_BottomLeftCross, BottomLeftBoard_BottomCross, BottomLeftBoard_BottomRightCross
    global BottomLeftBoard_TopLeftNought, BottomLeftBoard_TopNought, BottomLeftBoard_TopRightNought, BottomLeftBoard_LeftNought, BottomLeftBoard_MiddleNought, BottomLeftBoard_RightNought, BottomLeftBoard_BottomLeftNought, BottomLeftBoard_BottomNought, BottomLeftBoard_BottomRightNought

    BottomLeftBoard_TopLeftFilled = BottomLeftBoard_TopFilled = BottomLeftBoard_TopRightFilled = BottomLeftBoard_LeftFilled = BottomLeftBoard_MiddleFilled = BottomLeftBoard_RightFilled = BottomLeftBoard_BottomLeftFilled = BottomLeftBoard_BottomFilled = BottomLeftBoard_BottomRightFilled = False
    BottomLeftBoard_TopLeftCross = BottomLeftBoard_TopCross = BottomLeftBoard_TopRightCross = BottomLeftBoard_LeftCross = BottomLeftBoard_MiddleCross = BottomLeftBoard_RightCross = BottomLeftBoard_BottomLeftCross = BottomLeftBoard_BottomCross = BottomLeftBoard_BottomRightCross = False
    BottomLeftBoard_TopLeftNought = BottomLeftBoard_TopNought = BottomLeftBoard_TopRightNought = BottomLeftBoard_LeftNought = BottomLeftBoard_MiddleNought = BottomLeftBoard_RightNought = BottomLeftBoard_BottomLeftNought = BottomLeftBoard_BottomNought = BottomLeftBoard_BottomRightNought = False
    
    #-----BOTTOM-BOARD-----
    global BottomBoard_TopLeftFilled, BottomBoard_TopFilled, BottomBoard_TopRightFilled, BottomBoard_LeftFilled, BottomBoard_MiddleFilled, BottomBoard_RightFilled, BottomBoard_BottomLeftFilled, BottomBoard_BottomFilled, BottomBoard_BottomRightFilled
    global BottomBoard_TopLeftCross, BottomBoard_TopCross, BottomBoard_TopRightCross, BottomBoard_LeftCross, BottomBoard_MiddleCross, BottomBoard_RightCross, BottomBoard_BottomLeftCross, BottomBoard_BottomCross, BottomBoard_BottomRightCross
    global BottomBoard_TopLeftNought, BottomBoard_TopNought, BottomBoard_TopRightNought, BottomBoard_LeftNought, BottomBoard_MiddleNought, BottomBoard_RightNought, BottomBoard_BottomLeftNought, BottomBoard_BottomNought, BottomBoard_BottomRightNought

    BottomBoard_TopLeftFilled = BottomBoard_TopFilled = BottomBoard_TopRightFilled = BottomBoard_LeftFilled = BottomBoard_MiddleFilled = BottomBoard_RightFilled = BottomBoard_BottomLeftFilled = BottomBoard_BottomFilled = BottomBoard_BottomRightFilled = False
    BottomBoard_TopLeftCross = BottomBoard_TopCross = BottomBoard_TopRightCross = BottomBoard_LeftCross = BottomBoard_MiddleCross = BottomBoard_RightCross = BottomBoard_BottomLeftCross = BottomBoard_BottomCross = BottomBoard_BottomRightCross = False
    BottomBoard_TopLeftNought = BottomBoard_TopNought = BottomBoard_TopRightNought = BottomBoard_LeftNought = BottomBoard_MiddleNought = BottomBoard_RightNought = BottomBoard_BottomLeftNought = BottomBoard_BottomNought = BottomBoard_BottomRightNought = False
    
    #-----BOTTOM-RIGHT-BOARD-----
    global BottomRightBoard_TopLeftFilled, BottomRightBoard_TopFilled, BottomRightBoard_TopRightFilled, BottomRightBoard_LeftFilled, BottomRightBoard_MiddleFilled, BottomRightBoard_RightFilled, BottomRightBoard_BottomLeftFilled, BottomRightBoard_BottomFilled, BottomRightBoard_BottomRightFilled
    global BottomRightBoard_TopLeftCross, BottomRightBoard_TopCross, BottomRightBoard_TopRightCross, BottomRightBoard_LeftCross, BottomRightBoard_MiddleCross, BottomRightBoard_RightCross, BottomRightBoard_BottomLeftCross, BottomRightBoard_BottomCross, BottomRightBoard_BottomRightCross
    global BottomRightBoard_TopLeftNought, BottomRightBoard_TopNought, BottomRightBoard_TopRightNought, BottomRightBoard_LeftNought, BottomRightBoard_MiddleNought, BottomRightBoard_RightNought, BottomRightBoard_BottomLeftNought, BottomRightBoard_BottomNought, BottomRightBoard_BottomRightNought

    BottomRightBoard_TopLeftFilled = BottomRightBoard_TopFilled = BottomRightBoard_TopRightFilled = BottomRightBoard_LeftFilled = BottomRightBoard_MiddleFilled = BottomRightBoard_RightFilled = BottomRightBoard_BottomLeftFilled = BottomRightBoard_BottomFilled = BottomRightBoard_BottomRightFilled = False
    BottomRightBoard_TopLeftCross = BottomRightBoard_TopCross = BottomRightBoard_TopRightCross = BottomRightBoard_LeftCross = BottomRightBoard_MiddleCross = BottomRightBoard_RightCross = BottomRightBoard_BottomLeftCross = BottomRightBoard_BottomCross = BottomRightBoard_BottomRightCross = False
    BottomRightBoard_TopLeftNought = BottomRightBoard_TopNought = BottomRightBoard_TopRightNought = BottomRightBoard_LeftNought = BottomRightBoard_MiddleNought = BottomRightBoard_RightNought = BottomRightBoard_BottomLeftNought = BottomRightBoard_BottomNought = BottomRightBoard_BottomRightNought = False
    

    global frame, TopLeftBoard, TopBoard, TopRightBoard, LeftBoard, MiddleBoard, RightBoard, BottomLeftBoard, BottomBoard, BottomRightBoard
    
    frame = Frame(window)

    TopLeftBoard = topleftboard(window)
    ##TopBoard = topboard(window)
    ##TopRightBoard = toprightboard(window)
    ##LeftBoard = leftboard(window)
    ##MiddleBoard = middleboard(window)
    ##RightBoard = rightboard(window)
    ##BottomLeftBoard = bottomleftboard(window)
    ##BottomBoard = bottomboard(window)
    ##BottomRightBoard = bottomrightboard(window)

    frame.ForgetAll()    
    frame.DrawAll()

    window.bind("<Key>", key_detect)    

def changeTurn(): # <------------------
    pass

def key_detect(event):
    key = event.char
    
    if key=="\r":
        reset()
    
    if key=="0":
        changeTurn()
    
    if key=="7":
        TopLeftBoard.Cross("TopLeft")
        changeTurn()
    elif key=="8":
        TopLeftBoard.Cross("Top")
        changeTurn()
    elif key=="9":
        TopLeftBoard.Cross("TopRight")
        changeTurn()
    elif key=="4":
        TopLeftBoard.Cross("Left")
        changeTurn()
    elif key=="5":
        TopLeftBoard.Cross("Middle")
        changeTurn()
    elif key=="6":
        TopLeftBoard.Cross("Right")
        changeTurn()
    elif key=="1":
        TopLeftBoard.Cross("BottomLeft")
        changeTurn()
    elif key=="2":
        TopLeftBoard.Cross("Bottom")
        changeTurn()
    elif key=="3":
        TopLeftBoard.Cross("BottomRight")
        changeTurn()
    

reset()
window.mainloop()
