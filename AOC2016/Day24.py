import os, time
from itertools import permutations
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC24_1.txt", "r").read().splitlines()

coords = []
goals = {}
start = []

for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] != "#":
            coords.append([x,y])
            if input[y][x] != ".":
                goals[input[y][x]] = [x,y]
                if input[y][x] == "0": start = [x,y]

#for i in nodes:
#    print(i)

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

def Part1():
    now = time.time()
    best = 10000000
    distances = {}
    for l in goals.keys():
        for m in goals.keys():
            if l != m: distances[(l,m)] = bfsDist(goals[l],goals[m],coords)
    del goals["0"]
    combs = permutations(goals.keys(), len(goals.keys()))
    for i in combs:
        count = 0
        for j in range(len(i)):
            if j == 0: count += distances[("0",i[j])]
            else: count += distances[(i[j-1],i[j])]
        if count < best: best = count
    print("Part 1:", best)
    print("Time taken: " + str(time.time() - now))

def Part2():
    now = time.time()
    best = 10000000
    distances = {}
    for l in goals.keys():
        for m in goals.keys():
            if l != m: distances[(l,m)] = bfsDist(goals[l],goals[m],coords)
    del goals["0"]
    combs = permutations(goals.keys(), len(goals.keys()))

    for i in combs:
        count = 0
        for j in range(len(i)):
            if j == 0: count += distances[("0",i[j])]
            else: count += distances[(i[j-1],i[j])]
            if j == len(i) - 1: count += distances[(i[j],"0")]
        if count < best: best = count
    print("Part 2:", best)
    print("Time taken: " + str(time.time() - now))

Part1()
Part2()