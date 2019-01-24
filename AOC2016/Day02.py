import os
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC02_1.txt", "r").read().splitlines()

#input = ["ULL","RRDDD","LURDL","UUUUD"]

def Part1():
    numPad = [["1","2","3"],
              ["4","5","6"],
              ["7","8","9"]]
    code = ""
    x = 1
    y = 1
    min, max = 0, 2
    for line in input:
        for i in line:
            if i == "U":
                if y > min: y -= 1
            elif i == "D":
                if y < max: y += 1
            elif i == "L":
                if x > min: x -= 1
            elif i == "R":
                if x < max: x += 1
        code += numPad[y][x]
    print("Part 1:", code)



def Part2():
    numPad = [[" "," ","1"," "," "],
              [" ","2","3","4"," "],
              ["5","6","7","9","9"],
              [" ","A","B","C"," "],
              [" "," ","D"," "," "]]
    code = ""
    x = 0
    y = 2
    min, max = 0, 4
    for line in input:
        for i in line:
            if i == "U":
                if y > min and numPad[y-1][x] != " ": y -= 1
            elif i == "D":
                if y < max and numPad[y+1][x] != " ": y += 1
            elif i == "L":
                if x > min and numPad[y][x-1] != " ": x -= 1
            elif i == "R":
                if x < max and numPad[y][x+1] != " ": x += 1
        code += numPad[y][x]
    print("Part 2:", code)

Part1()
Part2()