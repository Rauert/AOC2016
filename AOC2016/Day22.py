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

#Determines distance to c2 from c1
def bfsDist(c1, c2, coords):
    def neighbours(cc):
        candidates = [[cc[0] - 1, cc[1]], [cc[0] + 1, cc[1]], [cc[0], cc[1] - 1], [cc[0], cc[1] + 1]]
        return [c for c in candidates if c in coords]
    bool = False
    seen = []
    seenDist = []
    frontier = [c1]
    frontierDist = [0]
    #print(c1,c2)
    #print(coords)
    while not len(frontier) == 0 and bool == False:
        element = frontier.pop(0)
        dist = frontierDist.pop(0)
        seen.append(element)
        seenDist.append(dist)
        if c2 in seen:
            bool = True
        nextCoords = [n for n in neighbours(element) if not n in seen if not n in frontier]
        for i in nextCoords:
            frontierDist.append(dist + 1)
        frontier.extend(nextCoords)
        #print(nextCoords)
        #print(frontier)
        #print(frontierDist)
    return seenDist[seen.index(c2)]

def Part2():
    #maxU, maxT, minU, minT = 0, 0, 100, 100
    coords = []
    start = []
    maxX = 0
    for y in range(25):
        for i in range(0,len(nodes),25):
            if nodes[i+y][3] < 100 and nodes[i+y][2] < 100: #All nodes with size < 100 are compatible with one another.
                coords.append([nodes[i+y][0], nodes[i+y][1]])
                if nodes[i+y][3] == 0: start = [nodes[i+y][0], nodes[i+y][1]]
                if nodes[i+y][0] > maxX: maxX = nodes[i+y][0]
                #if nodes[i+y][2] > maxT: maxT = nodes[i+y][2]
                #if nodes[i+y][3] > maxU: maxU = nodes[i+y][3]
                #if nodes[i+y][2] < minT: minT = nodes[i+y][2]
                #if nodes[i+y][3] < minU: minU = nodes[i+y][3]
                print(nodes[i+y][3], "/", nodes[i+y][2] ,end="\t")
            else:
                print("#", end="\t\t")
            #print(nodes[i+y][0], "/", nodes[i+y][1] ,end="\t")
        print()
    #Find shortest path from 0 to data
    #print(maxU, "/", minT)
    #print(minU, "/", maxT)
    #print(maxX, start)
    count = bfsDist(start, [maxX-1,0],coords) #Distance from blank drive to position left of goal
    count += ((maxX-1) * 5) + 1 #1 step to goal and 4 to move to new position on left of goal
    print("Part 2:", count)

Part1()
Part2()