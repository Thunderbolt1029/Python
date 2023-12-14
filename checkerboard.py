board = [{"x":0, "y":0}]*64

i=0
for y in range(8):
    for x in range(8):
        board[i] = {"x": x, "y": y}
        i+=1

for square in board:
    if (square["x"]+square["y"])%2==0:
        if square["x"]%8!=7: 
            print("o", end="")
        else: 
            print("o")
    else:
        if square["x"]%8!=7: 
            print("x", end="")
        else: 
            print("x")
