def Part1():
    d = [17,3,19,13,7,5]
    p = [15,2,4,2,2,0]
    goal = [16,1,16,9,2,4]
    i = 0
    while p != goal:
        #if p[0] == 16 and p[1] == 1: print(p)
        i+=1
        for j in range(6):
            p[j] = (p[j]+1) % d[j]
    
    print("Part 1:", i)

def Part2():
    d = [17,3,19,13,7,5,11]
    p = [15,2,4,2,2,0,0]
    goal = [16,1,16,9,2,4,4]
    i = 0
    while p != goal:
        #print(p)
        i+=1
        for j in range(7):
            p[j] = (p[j]+1) % d[j]
    
    print("Part 2:", i)

Part1()
Part2()
