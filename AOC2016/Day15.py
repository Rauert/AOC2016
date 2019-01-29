
def run():
    d = [17,3,19,13,7,5]
    p = [15,2,4,2,2,0]
    goal = [17,2,17,10,3,0]
    i = 0
    while p != goal:
        #print(p)
        i+=1
        for j in range(6):
            p[j] = (p[j]+1) % (d[j]+1)
    
    print("Part 1:",i)

run()
