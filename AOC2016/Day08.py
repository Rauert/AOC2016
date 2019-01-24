import os, re
from string import ascii_lowercase
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC08_1.txt", "r").read().splitlines()

inst = []

for i in input:
    s = re.split("\s|=",i)
    if len(s) == 2:
        t = s[1].split("x")
        inst.append([s[0],int(t[0]),int(t[1])])
    else:
        inst.append([s[1],int(s[3]),int(s[5])])

def printScr(screen):
    for i in screen:
        print("".join(map(str,i)))

def Part12():
    screen = [[0 for a in range(50)] for b in range(6)]
    #printScr(screen)
    for i in inst:
        if i[0] == "rect":
            for y in range(i[2]):
                for x in range(i[1]):
                    screen[y][x] = 1
        elif i[0] == "row":
            old = screen[i[1]]
            new = []
            for j in range(50):
                new.append(old[(j-i[2]) % 50])
            screen[i[1]] = new
        elif i[0] == "column":
            old = []
            for j in range(6):
                old.append(screen[j][i[1]])
            new  = []
            for j in range(6):
                new.append(old[j-(i[2]) % 6])
            for j in range(6):
                screen[j][i[1]] = new[j]
        #printScr(screen)
    count = 0
    for k in screen:
        count += sum(k)
    print("Part 1:", count)

    print("Part 2:")
    for s in screen:
        out = "".join(map(str,s))
        out = out.replace("0"," ")
        out = out.replace("1","#")
        print(out)

Part12()