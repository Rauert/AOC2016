import itertools, copy

best = 32
goal = 10
#seen = []

def canMove(c,fl):
    #fl = floor.copy()
    fl.extend(list(c))
    #if len(c) == 2:
    #    if c[0][1] != c[1][1] and c[0][0] != c[1][0]: #Will destroy MC in elevator. ????? I think
    #        rtn = False
    count = 0
    for f in fl:
        if f[1] == "G": count += 1
    if count == 0: return True #No generators
    for f in fl:
        if f[1] == "M":
            gen = f[0] + "G"
            safe = False
            for i in fl:
                if i == gen: #M is Safe
                    safe = True
                    break
            if safe == False:
                return False
    return True

def runNew(c,e,newF,count, dir):
    #global seen
    #newF = floors.copy()
    en = e-1
    if dir == "up": en = e+1
    for i in c:
        #print(dir,e,i,newF)
        newF[e].remove(i)
        newF[en].append(i)
    #print((e,newF) not in seen)
    #if (e,newF) not in seen:
    recurseRun(count, en, newF)


def recurseRun(count, e, f):
    global best, fin, seen
    #seen.append((e,copy.deepcopy(f)))
    if count > best: return
    if len(f[4]) == goal:
        best = count
        return
    count +=1
    #Test every item and every combination for above floor
    combs = list(itertools.combinations(f[e],2))
    for j in f[e]: combs.append((j,))
    #print(combs)
    if e < 4:
        for c in combs:
            #print("up",c,f)
            if canMove(c,copy.deepcopy(f[e+1])):
                runNew(c,e,copy.deepcopy(f),count,"up")
                #newF = f.copy()
                #for i in c:
                #    print("up",e,i,newF)
                #    newF[e].remove(i)
                #    newF[e+1].append(i)
                #recurseRun(count, e+1, newF)

    ##Test every item and every combination for below floor
    if e > 1:
        for c in combs:
            #print("dw",c,f)
            if canMove(c,copy.deepcopy(f[e-1])):
                runNew(c,e,copy.deepcopy(f),count,"dw")
                #newF = f.copy()
                #for i in c:
                #    print("dw",e,i,newF)
                #    newF[e].remove(i)
                #    newF[e-1].append(i)
                #recurseRun(count, e-1, newF)

def Part1():
    global goal
    f = {4:[],
         3:["OG","OM","RG","RM"],
         2:["PM","SM"],
         1:["TG","TM","PG","SG"]}
    goal = 10

    #f = {4:[],
    #     3:["LG"],
    #     2:["HG"],
    #     1:["HM","LM"]}
    #goal = 4

    e = 1
    count = 0
    recurseRun(count,e,f)

    print("Part 1:", best)

Part1()


#From https://www.reddit.com/r/adventofcode/comments/5hoia9/2016_day_11_solutions/
def get_moves(items):
    """
    Through playing around with bolts and nuts,
    I came across the optimal strategy, move things up a floor at a time

    I also discovered to move n items up 1 floor,
        it requires 2 * (n - 1) - 1 moves

    So assuming a "good" start state, it doesn't matter what is on what floor
    Just the number of things per floor
    """
    moves = 0
    while items[-1] != sum(items):
        # print moves, items
        lowest_floor = 0
        while items[lowest_floor] == 0:
            lowest_floor += 1
        moves += 2 * (items[lowest_floor] - 1) - 1
        items[lowest_floor + 1] += items[lowest_floor]
        items[lowest_floor] = 0
    return moves


print("Part One", get_moves([4, 2, 4, 0]))
print("Part Two", get_moves([8, 2, 4, 0]))