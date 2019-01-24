import os
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC03_1.txt", "r").read().splitlines()

def Part1():
    tri = []
    for i in input:
        t = list(map(int,i.split()))
        t.sort(reverse = True)
        tri.append(t)

    count = 0
    for t in tri:
        #print(t)
        if t[1] + t[2] > t[0]:
            count += 1
    print("Part 1:", count)

def Part2():
    tri = []
    for i in range(0,len(input),3):
        i1 = list(map(int,input[i].split()))
        i2 = list(map(int,input[i+1].split()))
        i3 = list(map(int,input[i+2].split()))
        for j in range(3):
            t = [i1[j],i2[j],i3[j]]
            t.sort(reverse = True)
            tri.append(t)

    count = 0
    for t in tri:
        print(t)
        if t[1] + t[2] > t[0]:
            count += 1
    print("Part 2:", count)

Part1()
Part2()