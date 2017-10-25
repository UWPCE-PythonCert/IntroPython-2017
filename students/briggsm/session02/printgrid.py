'''Print a grid'''

def element (char1, char2, mmm):
    seq = "{}{}{}{}{}".format(char1, char2, char2, char2, char2)
    madeline= ""
    for l in range(mmm):
        madeline = madeline + seq
    madeline = madeline + char1
    return madeline

def printGrid(n):
    
    lineA = element("+", " - ", n)
    lineB = element("|", "   ", n)
    grid = ""

    for sections in range(n):
        grid = grid + lineA + "\n"
        for sec in range(4):
            grid = grid + lineB + "\n"
    grid = grid + lineA + "\n"

    print (grid)

printGrid(2)