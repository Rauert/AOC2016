office = []

fn = 10
goal = [7,4]
fn = 1350
goal = [31,39]


for y in range(50):
    for x in range(50):
        if (str(format((x*x) + (3*x) + (2*x*y) + y + (y*y) + fn, "08b")).count("1")) % 2 == 0:
            office.append([x,y])
            #print(".",end="")
        #else:
            #print("#",end="")
    #print()


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
        if bool == True:
            return seenDist[seen.index(c2)]
        else: #Not connected
            return 100

#Slow
def Part2():
    count = 0
    for c in office:
        if bfsDist([1,1],c,office) <= 50: count += 1
    print("Part 2:", count)

def bfsMaxDist(c1, maxDist, coords):
        def neighbours(cc):
            candidates = [[cc[0] - 1, cc[1]], [cc[0] + 1, cc[1]], [cc[0], cc[1] - 1], [cc[0], cc[1] + 1]]
            return [c for c in candidates if c in coords]
        bool = False
        seen = []
        seenDist = []
        frontier = [c1]
        frontierDist = [0]
        count = 0
        while not len(frontier) == 0 and bool == False:
            element = frontier.pop(0)
            dist = frontierDist.pop(0)
            seen.append(element)
            seenDist.append(dist)
            if dist <= maxDist:
                count+=1
            else:
                bool = True
            nextCoords = [n for n in neighbours(element) if not n in seen if not n in frontier]
            for i in nextCoords:
                frontierDist.append(dist + 1)
            frontier.extend(nextCoords)
        return count

print("Part 1:", bfsDist([1,1],goal,office))
print("Part 2:", bfsMaxDist([1,1],50,office))
#Part2()