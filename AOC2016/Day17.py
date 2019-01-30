from hashlib import md5

cells = [(0,0),(1,0),(2,0),(3,0),
         (0,1),(1,1),(2,1),(3,1),
         (0,2),(1,2),(2,2),(3,2),
         (0,3),(1,3),(2,3),(3,3)]

valid = ["b", "c", "d", "e", "f"]

code = "pvhmgsws"
#code = "ihgpwlah"

bestPath = ""
bestLength = 1000000

def recurseRun(x, y, path, count, P2):
    global bestPath, bestLength
    if not P2:
        if count > bestLength: return
    if x == 3 and y == 3:
        if P2:
            if count > bestLength:
                bestPath = path
                bestLength = count
        else:
            bestPath = path
            bestLength = count
        return
    count +=1
    md = md5((code+path).encode()).hexdigest()
    #print(x, y, path, count,md)
    if md[0] in valid and (x,y-1) in cells: recurseRun(x, y-1, path + "U",count, P2)
    if md[1] in valid and (x,y+1) in cells: recurseRun(x, y+1, path + "D",count, P2)
    if md[2] in valid and (x-1,y) in cells: recurseRun(x-1, y, path + "L",count, P2)
    if md[3] in valid and (x+1,y) in cells: recurseRun(x+1, y, path + "R",count, P2)

def Part1():
    recurseRun(0,0,"",0, False)
    print("Part 1:", bestPath)

def Part2():
    global bestLength
    bestLength = 0
    recurseRun(0,0,"",0, True)
    print("Part 2:", len(bestPath))

Part1()
Part2()