import itertools

best = 100000000
fin = []
goal = 4

def recurseRun(count, e, f):
    if count > best: return
    if len(f[4]) == goal:
        fin.append(count)
        return
    count +=1
    #Test every item and every combination for above floor
    combs = list(itertools.combinations(f[e],2))
    for j in f[e]: combs.append((j,))
    print(combs)
    #if e < 4:
    #    for c in combs:
    #        if canMove(c,f[e+1]):

    ##Test every item and every combination for below floor
    #if e > 1:
    #    for c in combs:
    #        if canMove(c,f[e+1]):

def Part1():
    f = {4:[],
         3:["OG","OM","RG","RM"],
         2:["PM","SM"],
         1:["TG","TM","PG","SG"]}

    f = {4:[],
         3:["LG"],
         2:["HG"],
         1:["HM","LM"]}
    e = 1
    count = 0
    recurseRun(count,e,f)

    print("Part 1:", min(fin))

Part1()