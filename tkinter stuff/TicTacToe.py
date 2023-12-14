import tkinter as tk
import time

window = tk.Tk()
window.title("Tic Tac Toe")
window.minsize(275,240)

CrossWins = NoughtWins = 0

class Outline(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.CrossWinTotal = tk.Label(text="Cross's Wins: " + str(CrossWins))
        self.NoughtWinTotal = tk.Label(text="Nought's Wins: " + str(NoughtWins))
        
        self.OutlineVertical_1 = tk.Label(text="|\n|")
        self.OutlineVertical_2 = tk.Label(text="|\n|")
        self.OutlineVertical_3 = tk.Label(text="|\n|")
        self.OutlineVertical_4 = tk.Label(text="|\n|")
        self.OutlineVertical_5 = tk.Label(text="|\n|")
        self.OutlineVertical_6 = tk.Label(text="|\n|")
        
        self.OutlineHorizontal_1 = tk.Label(text="-------")
        self.OutlineHorizontal_2 = tk.Label(text="-------")
        self.OutlineHorizontal_3 = tk.Label(text="-------")
        self.OutlineHorizontal_4 = tk.Label(text="-------")
        self.OutlineHorizontal_5 = tk.Label(text="-------")
        self.OutlineHorizontal_6 = tk.Label(text="-------")
        
        self.OutlineCross_1 = tk.Label(text="+")
        self.OutlineCross_2 = tk.Label(text="+")
        self.OutlineCross_3 = tk.Label(text="+")
        self.OutlineCross_4 = tk.Label(text="+")

        self.OutlineVertical_7 = tk.Label(text="|\n|")
        self.OutlineVertical_8 = tk.Label(text="|\n|")
        self.OutlineHorizontal_7 = tk.Label(text="-------")
        self.OutlineHorizontal_8 = tk.Label(text="-------")
        self.OutlineCorner_1 = tk.Label(text="/")
        self.OutlineCorner_2 = tk.Label(text="\\")
        self.OutlineCorner_3 = tk.Label(text="\\")
        self.OutlineCorner_4 = tk.Label(text="/")

        self.padder_1 = tk.Label(text="       ")
        self.padder_2 = tk.Label(text="    ")
        self.padder_3 = tk.Label(text=" ")

    def draw(self):
        self.CrossWinTotal.grid(column=3, row=10, columnspan=8)
        self.NoughtWinTotal.grid(column=3, row=11, columnspan=8)
        
        self.OutlineVertical_1.grid(column=2, row=3)
        self.OutlineVertical_2.grid(column=4, row=3)
        self.OutlineVertical_3.grid(column=2, row=5)
        self.OutlineVertical_4.grid(column=4, row=5)
        self.OutlineVertical_5.grid(column=2, row=7)
        self.OutlineVertical_6.grid(column=4, row=7)

        self.OutlineHorizontal_1.grid(column=1, row=4)
        self.OutlineHorizontal_2.grid(column=3, row=4)
        self.OutlineHorizontal_3.grid(column=5, row=4)
        self.OutlineHorizontal_4.grid(column=1, row=6)
        self.OutlineHorizontal_5.grid(column=3, row=6)
        self.OutlineHorizontal_6.grid(column=5, row=6)

        self.OutlineCross_1.grid(column=2, row=4)
        self.OutlineCross_2.grid(column=4, row=4)
        self.OutlineCross_3.grid(column=2, row=6)
        self.OutlineCross_4.grid(column=4, row=6)

        self.OutlineVertical_7.grid(column=11, row=5)
        self.OutlineVertical_8.grid(column=13, row=5)
        self.OutlineHorizontal_7.grid(column=12, row=6)
        self.OutlineHorizontal_8.grid(column=12, row=4)
        self.OutlineCorner_1.grid(column=11, row=4)
        self.OutlineCorner_2.grid(column=13, row=4)
        self.OutlineCorner_3.grid(column=11, row=6)
        self.OutlineCorner_4.grid(column=13, row=6)

        self.padder_1.grid(column=10, row=5)
        self.padder_2.grid(column=0, row=0)
        self.padder_3.grid(column=0, row=8)

    def Drop(self):
        self.CrossWinTotal.grid_remove()
        self.NoughtWinTotal.grid_remove()
        
        self.OutlineVertical_1.grid_remove()
        self.OutlineVertical_2.grid_remove()
        self.OutlineVertical_3.grid_remove()
        self.OutlineVertical_4.grid_remove()
        self.OutlineVertical_5.grid_remove()
        self.OutlineVertical_6.grid_remove()

        self.OutlineHorizontal_1.grid_remove()
        self.OutlineHorizontal_2.grid_remove()
        self.OutlineHorizontal_3.grid_remove()
        self.OutlineHorizontal_4.grid_remove()
        self.OutlineHorizontal_5.grid_remove()
        self.OutlineHorizontal_6.grid_remove()

        self.OutlineCross_1.grid_remove()
        self.OutlineCross_2.grid_remove()
        self.OutlineCross_3.grid_remove()
        self.OutlineCross_4.grid_remove()

        self.OutlineVertical_7.grid_remove()
        self.OutlineVertical_8.grid_remove()
        self.OutlineHorizontal_7.grid_remove()
        self.OutlineHorizontal_8.grid_remove()
        self.OutlineCorner_1.grid_remove()
        self.OutlineCorner_2.grid_remove()
        self.OutlineCorner_3.grid_remove()
        self.OutlineCorner_4.grid_remove()

        self.padder_1.grid_remove()
        self.padder_2.grid_remove()

class Piece(tk.Frame):
    def __init__(self, master):
        super().__init__(master)        
        self.Cross_TopLeft = tk.Label(text="X")
        self.Cross_Top = tk.Label(text="X")
        self.Cross_TopRight = tk.Label(text="X")
        self.Cross_Left = tk.Label(text="X")
        self.Cross_Middle = tk.Label(text="X")
        self.Cross_Right = tk.Label(text="X")
        self.Cross_BottomLeft = tk.Label(text="X")
        self.Cross_Bottom = tk.Label(text="X")
        self.Cross_BottomRight = tk.Label(text="X")
        self.Cross_Place = tk.Label(text="X")

        self.Nought_TopLeft = tk.Label(text="O")
        self.Nought_Top = tk.Label(text="O")
        self.Nought_TopRight = tk.Label(text="O")
        self.Nought_Left = tk.Label(text="O")
        self.Nought_Middle = tk.Label(text="O")
        self.Nought_Right = tk.Label(text="O")
        self.Nought_BottomLeft = tk.Label(text="O")
        self.Nought_Bottom = tk.Label(text="O")
        self.Nought_BottomRight = tk.Label(text="O")
        self.Nought_Place = tk.Label(text="O")

    def Cross(self, place=None):
        global TopLeftFilled, TopFilled, TopRightFilled, LeftFilled, MiddleFilled, RightFilled, BottomLeftFilled, BottomFilled, BottomRightFilled
        global TopLeftCross, TopCross, TopRightCross, LeftCross, MiddleCross, RightCross, BottomLeftCross, BottomCross, BottomRightCross
        if place=="TopLeft":
            self.Cross_TopLeft.grid(column=1, row=3)
            TopLeftFilled = TopLeftCross = True
        elif place=="Top":
            self.Cross_Top.grid(column=3, row=3)
            TopFilled = TopCross = True
        elif place=="TopRight":
            self.Cross_TopRight.grid(column=5, row=3)
            TopRightFilled = TopRightCross = True
        elif place=="Left":
            self.Cross_Left.grid(column=1, row=5)
            LeftFilled = LeftCross = True
        elif place=="Middle":
            self.Cross_Middle.grid(column=3, row=5)
            MiddleFilled = MiddleCross = True
        elif place=="Right":
            self.Cross_Right.grid(column=5, row=5)
            RightFilled = RightCross = True
        elif place=="BottomLeft":
            self.Cross_BottomLeft.grid(column=1, row=7)
            BottomLeftFilled = BottomLeftCross = True
        elif place=="Bottom":
            self.Cross_Bottom.grid(column=3, row=7)
            BottomFilled = BottomCross = True
        elif place=="BottomRight":
            self.Cross_BottomRight.grid(column=5, row=7)
            BottomRightFilled = BottomRightCross = True
        elif place=="Turn":
            self.Cross_Place.grid(column=12, row=5)
        else:
            raise Exception("You need to specify where to place the piece")

    def Nought(self, place=None):
        global TopLeftFilled, TopFilled, TopRightFilled, LeftFilled, MiddleFilled, RightFilled, BottomLeftFilled, BottomFilled, BottomRightFilled
        global TopLeftNought, TopNought, TopRightNought, LeftNought, MiddleNought, RightNought, BottomLeftNought, BottomNought, BottomRightNought
        if place=="TopLeft":
            self.Nought_TopLeft.grid(column=1, row=3)
            TopLeftFilled = TopLeftNought = True
        elif place=="Top":
            self.Nought_Top.grid(column=3, row=3)
            TopFilled = TopNought = True
        elif place=="TopRight":
            self.Nought_TopRight.grid(column=5, row=3)
            TopRightFilled = TopRightNought = True
        elif place=="Left":
            self.Nought_Left.grid(column=1, row=5)
            LeftFilled = LeftNought = True
        elif place=="Middle":
            self.Nought_Middle.grid(column=3, row=5)
            MiddleFilled = MiddleNought = True
        elif place=="Right":
            self.Nought_Right.grid(column=5, row=5)
            RightFilled = RightNought = True
        elif place=="BottomLeft":
            self.Nought_BottomLeft.grid(column=1, row=7)
            BottomLeftFilled = BottomLeftNought = True
        elif place=="Bottom":
            self.Nought_Bottom.grid(column=3, row=7)
            BottomFilled = BottomNought = True
        elif place=="BottomRight":
            self.Nought_BottomRight.grid(column=5, row=7)
            BottomRightFilled = BottomRightNought = True
        elif place=="Turn":
            self.Nought_Place.grid(column=12, row=5)
        else:
            raise Exception("You need to specify where to place the piece")

    def CrossDrop(self, place=None):
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
            
        elif place=="TopLeft":
            self.Cross_TopLeft.grid_remove()
        elif place=="Top":
            self.Cross_Top.grid_remove()
        elif place=="TopRight":
            self.Cross_TopRight.grid_remove()
        elif place=="Left":
            self.Cross_Left.grid_remove()
        elif place=="Middle":
            self.Cross_Middle.grid_remove()
        elif place=="Right":
            self.Cross_Right.grid_remove()
        elif place=="BottomLeft":
            self.Cross_BottomLeft.grid_remove()
        elif place=="Bottom":
            self.Cross_Bottom.grid_remove()
        elif place=="BottomRight":
            self.Cross_BottomRight.grid_remove()
        elif place=="Turn":
            self.Cross_Place.grid_remove()
        else:
            raise Exception("You need to specify which piece to drop")

    def NoughtDrop(self, place=None):
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
            
        elif place=="TopLeft":
            self.Nought_TopLeft.grid_remove()
        elif place=="Top":
            self.Nought_Top.grid_remove()
        elif place=="TopRight":
            self.Nought_TopRight.grid_remove()
        elif place=="Left":
            self.Nought_Left.grid_remove()
        elif place=="Middle":
            self.Nought_Middle.grid_remove()
        elif place=="Right":
            self.Nought_Right.grid_remove()
        elif place=="BottomLeft":
            self.Nought_BottomLeft.grid_remove()
        elif place=="Bottom":
            self.Nought_Bottom.grid_remove()
        elif place=="BottomRight":
            self.Nought_BottomRight.grid_remove()
        elif place=="Turn":
            self.Nought_Place.grid_remove()
        else:
            raise Exception("You need to specify which piece to drop")

def reset():
    global Turn
    global TopLeftFilled, TopFilled, TopRightFilled, LeftFilled, MiddleFilled, RightFilled, BottomLeftFilled, BottomFilled, BottomRightFilled
    global TopLeftCross, TopCross, TopRightCross, LeftCross, MiddleCross, RightCross, BottomLeftCross, BottomCross, BottomRightCross
    global TopLeftNought, TopNought, TopRightNought, LeftNought, MiddleNought, RightNought, BottomLeftNought, BottomNought, BottomRightNought
    TopLeftFilled = TopFilled = TopRightFilled =  LeftFilled = MiddleFilled = RightFilled = BottomLeftFilled = BottomFilled = BottomRightFilled = False
    TopLeftCross = TopCross = TopRightCross =  LeftCross = MiddleCross = RightCross = BottomLeftCross = BottomCross = BottomRightCross = False
    TopLeftNought = TopNought = TopRightNought =  LeftNought = MiddleNought = RightNought = BottomLeftNought = BottomNought = BottomRightNought = False
    Turn = "Cross"
    piece.CrossDrop("All")
    piece.NoughtDrop("All")
    outline.Drop()

    start()

def changeTurn(turn):
    global Turn
    if turn=="Cross":
        piece.CrossDrop("Turn")
        piece.Nought("Turn")
        Turn="Nought"
    elif turn=="Nought":
        piece.NoughtDrop("Turn")
        piece.Cross("Turn")
        Turn="Cross"

def key_pressed(event):
    clickTop = clickHorizontalMiddle = clickBottom = False
    clickLeft = clickVerticalMiddle = clickRight = False
    key = event.char
    x = event.x
    y = event.y
    
    if event.num==1:
        if 25<y and y<56:
            clickLeft=True
        elif 75<y and y<115:
            clickVerticalMiddle=True
        elif  130<y and y<170:
            clickRight=True
        
        if 25<x and x<56:
            clickTop=True
        elif 75<x and x<115:
            clickHorizontalMiddle=True
        elif  130<x and x<170:
            clickBottom=True
            
        if Turn=="Cross":
            if clickLeft==True:
                if clickTop==True:
                    piece.Cross("TopLeft")
                    changeTurn(Turn)
                elif clickHorizontalMiddle==True:
                    piece.Cross("Top")
                    changeTurn(Turn)
                elif clickBottom==True:
                    piece.Cross("TopRight")
                    changeTurn(Turn)
            elif clickVerticalMiddle==True:
                if clickTop==True:
                    piece.Cross("Left")
                    changeTurn(Turn)
                elif clickHorizontalMiddle==True:
                    piece.Cross("Middle")
                    changeTurn(Turn)
                elif clickBottom==True:
                    piece.Cross("Right")
                    changeTurn(Turn)
            elif clickRight==True:
                if clickTop==True:
                    piece.Cross("BottomLeft")
                    changeTurn(Turn)
                elif clickHorizontalMiddle==True:
                    piece.Cross("Bottom")
                    changeTurn(Turn)
                elif clickBottom==True:
                    piece.Cross("BottomRight")
                    changeTurn(Turn)
                    
        elif Turn=="Nought":
            if clickLeft==True:
                if clickTop==True:
                    piece.Nought("TopLeft")
                    changeTurn(Turn)
                elif clickHorizontalMiddle==True:
                    piece.Nought("Top")
                    changeTurn(Turn)
                elif clickBottom==True:
                    piece.Nought("TopRight")
                    changeTurn(Turn)
            elif clickVerticalMiddle==True:
                if clickTop==True:
                    piece.Nought("Left")
                    changeTurn(Turn)
                elif clickHorizontalMiddle==True:
                    piece.Nought("Middle")
                    changeTurn(Turn)
                elif clickBottom==True:
                    piece.Nought("Right")
                    changeTurn(Turn)
            elif clickRight==True:
                if clickTop==True:
                    piece.Nought("BottomLeft")
                    changeTurn(Turn)
                elif clickHorizontalMiddle==True:
                    piece.Nought("Bottom")
                    changeTurn(Turn)
                elif clickBottom==True:
                    piece.Nought("BottomRight")
                    changeTurn(Turn)        
        
    if key=="\r":
        reset()
    
    if key=="0":
        changeTurn(Turn)
        
    if Turn=="Cross":
        if key=="7" and TopLeftFilled==False:
            piece.Cross("TopLeft")
            changeTurn(Turn)
        elif key=="8" and TopFilled==False:
            piece.Cross("Top")
            changeTurn(Turn)
        elif key=="9" and TopRightFilled==False:
            piece.Cross("TopRight")
            changeTurn(Turn)
        elif key=="4" and LeftFilled==False:
            piece.Cross("Left")
            changeTurn(Turn)
        elif key=="5" and MiddleFilled==False:
            piece.Cross("Middle")
            changeTurn(Turn)
        elif key=="6" and RightFilled==False:
            piece.Cross("Right")
            changeTurn(Turn)
        elif key=="1" and BottomLeftFilled==False:
            piece.Cross("BottomLeft")
            changeTurn(Turn)
        elif key=="2" and BottomFilled==False:
            piece.Cross("Bottom")
            changeTurn(Turn)
        elif key=="3" and BottomRightFilled==False:
            piece.Cross("BottomRight")
            changeTurn(Turn)
    elif Turn=="Nought":
        if key=="7" and TopLeftFilled==False:
            piece.Nought("TopLeft")
            changeTurn(Turn)
        elif key=="8" and TopFilled==False:
            piece.Nought("Top")
            changeTurn(Turn)
        elif key=="9" and TopRightFilled==False:
            piece.Nought("TopRight")
            changeTurn(Turn)
        elif key=="4" and LeftFilled==False:
            piece.Nought("Left")
            changeTurn(Turn)
        elif key=="5" and MiddleFilled==False:
            piece.Nought("Middle")
            changeTurn(Turn)
        elif key=="6" and RightFilled==False:
            piece.Nought("Right")
            changeTurn(Turn)
        elif key=="1" and BottomLeftFilled==False:
            piece.Nought("BottomLeft")
            changeTurn(Turn)
        elif key=="2" and BottomFilled==False:
            piece.Nought("Bottom")
            changeTurn(Turn)
        elif key=="3" and BottomRightFilled==False:
            piece.Nought("BottomRight")
            changeTurn(Turn)
    checkForWin()

def checkForWin():
    if TopLeftCross==True and TopCross==True and TopRightCross==True:
        crossWin()
    elif LeftCross==True and MiddleCross==True and RightCross==True:
        crossWin()
    elif BottomLeftCross==True and BottomCross==True and BottomRightCross==True:
        crossWin()
    elif TopLeftCross==True and LeftCross==True and BottomLeftCross==True:
        crossWin()
    elif TopCross==True and MiddleCross==True and BottomCross==True:
        crossWin()
    elif TopRightCross==True and RightCross==True and BottomRightCross==True:
        crossWin()
    elif TopLeftCross==True and MiddleCross==True and BottomRightCross==True:
        crossWin()
    elif TopRightCross==True and MiddleCross==True and BottomLeftCross==True:
        crossWin()

    if TopLeftNought==True and TopNought==True and TopRightNought==True:
        noughtWin()
    elif LeftNought==True and MiddleNought==True and RightNought==True:
        noughtWin()
    elif BottomLeftNought==True and BottomNought==True and BottomRightNought==True:
        noughtWin()
    elif TopLeftNought==True and LeftNought==True and BottomLeftNought==True:
        noughtWin()
    elif TopNought==True and MiddleNought==True and BottomNought==True:
        noughtWin()
    elif TopRightNought==True and RightNought==True and BottomRightNought==True:
        noughtWin()
    elif TopLeftNought==True and MiddleNought==True and BottomRightNought==True:
        noughtWin()
    elif TopRightNought==True and MiddleNought==True and BottomLeftNought==True:
        noughtWin()
    

    elif TopLeftFilled==True and TopFilled==True and TopRightFilled==True and LeftFilled==True and MiddleFilled==True and RightFilled==True and BottomLeftFilled==True and BottomFilled==True and BottomRightFilled==True:
        draw()
    
def crossWin():
    global CrossWins
    CrossWins+=1
    window.after(1000,reset)

def noughtWin():
    global NoughtWins
    NoughtWins+=1
    window.after(1000,reset)

def draw():
    window.after(1000,reset)

def keyDetect():
    window.bind("<Key>", key_pressed)
    window.bind("<Button-1>", key_pressed)

def start():
    global outline, piece
    global Turn
    global TopLeftFilled, TopFilled, TopRightFilled, LeftFilled, MiddleFilled, RightFilled, BottomLeftFilled, BottomFilled, BottomRightFilled
    global TopLeftCross, TopCross, TopRightCross, LeftCross, MiddleCross, RightCross, BottomLeftCross, BottomCross, BottomRightCross
    global TopLeftNought, TopNought, TopRightNought, LeftNought, MiddleNought, RightNought, BottomLeftNought, BottomNought, BottomRightNought
    TopLeftFilled = TopFilled = TopRightFilled =  LeftFilled = MiddleFilled = RightFilled = BottomLeftFilled = BottomFilled = BottomRightFilled = False
    TopLeftCross = TopCross = TopRightCross =  LeftCross = MiddleCross = RightCross = BottomLeftCross = BottomCross = BottomRightCross = False
    TopLeftNought = TopNought = TopRightNought =  LeftNought = MiddleNought = RightNought = BottomLeftNought = BottomNought = BottomRightNought = False
    outline = Outline(window)
    piece = Piece(window)
    outline.draw()
    piece.Cross("Turn")
    Turn = "Cross"

    keyDetect()

start()
window.mainloop()
