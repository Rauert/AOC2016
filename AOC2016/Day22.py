import os, re
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC22_1.txt", "r").read().splitlines()

nodes = []

for i in range(len(input)):
    if i > 1:
        s = re.split("\s+|-",input[i])
        nodes.append([int(s[1][1:]), int(s[2][1:]), int(s[3][0:len(s[3])-1]), int(s[4][0:len(s[4])-1]), int(s[5][0:len(s[5])-1]), int(s[6][0:len(s[6])-1])])

#for i in nodes:
#    print(i)

def Part1():
    count = 0
    for i in nodes:
        for j in nodes:
            if i != j and i[3] > 0 and j[4] >= i[3]:
                count +=1
    print("Part 1:", count)

def Part2():
    for y in range(25):
        for i in range(0,len(nodes),25):
            print(nodes[i+y][3], "/", nodes[i+y][2] ,end="\t")
            #print(nodes[i+y][0], "/", nodes[i+y][1] ,end="\t")
        print()
    print("Part 2:")

Part1()
Part2()