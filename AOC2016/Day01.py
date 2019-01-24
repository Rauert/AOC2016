import os
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC01_1.txt", "r").read()

input = input.replace(",","")
input = input.split()
#input = ["R5", "L5", "R5", "R3"]
#input = ["R8", "R4", "R4", "R8"]
#input = ["R2", "R2", "R2"]
#input =["R2", "L3"]
dirs = ["W","N","E","S"]

def Part1():
    dir = "N"
    x,y = 0,0
    #print(input)
    for i in input:
        turn = i[0:1]
        dist = int(i[1:])
        #print(dir, i)
        if turn == "R":
            dir = dirs[(dirs.index(dir)+1) % 4]
        else:
            dir = dirs[(dirs.index(dir)-1) % 4]
        if dir == "N":
            y += dist
        elif dir == "S":
            y -= dist
        elif dir == "E":
            x += dist
        elif dir == "W":
            x -= dist
        #print(x,y)
    print("Part 1:", abs(x) + abs(y))



def Part2():
    dir = "N"
    x,y = 0,0
    print(input)
    seen = []
    for i in input:
        turn = i[0:1]
        dist = int(i[1:])
        #print(dir, i)
        if turn == "R":
            dir = dirs[(dirs.index(dir)+1) % 4]
        else:
            dir = dirs[(dirs.index(dir)-1) % 4]
        if dir == "N":
            for yd in range(y,y+dist):
                if [x,yd] in seen:
                    print("Part 2:", abs(x) + abs(yd))
                    return
                #print(x,yd)
                seen.append([x,yd])
            y += dist
        elif dir == "S":
            for yd in range(y,y-dist,-1):
                if [x,yd] in seen:
                    print("Part 2:", abs(x) + abs(yd))
                    return
                #print(x,yd)
                seen.append([x,yd])
            y -= dist
        elif dir == "E":
            for xd in range(x,x+dist):
                if [xd,y] in seen:
                    print("Part 2:", abs(xd) + abs(y))
                    return
                #print(xd,y)
                seen.append([xd,y])
            x += dist
        elif dir == "W":
            for xd in range(x,x-dist,-1):
                if [xd,y] in seen:
                    print("Part 2:", abs(xd) + abs(y))
                    return
                #print(xd,y)
                seen.append([xd,y])
            x -= dist
        #print("FIN",x,y)

Part1()
Part2()